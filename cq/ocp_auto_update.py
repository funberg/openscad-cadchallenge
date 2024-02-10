import os
import sys
import asyncio
import importlib
import importlib.abc
import traceback
from watchfiles import awatch, PythonFilter

import importlib.util
import sys

modules = {}
specs = {}

class myfinder(importlib.abc.MetaPathFinder):
    def __init__(self):
        pass
    
    def find_spec(self, full, path, target=None):
        if full in specs:
            return specs[full]
        return None

async def main(pwd):
    print(f"Watching {pwd} for changes")
    async for changes in awatch(pwd, watch_filter=PythonFilter()):
        for c in changes:
            fn = c[1]
            rfn = os.path.relpath(fn, pwd)
            name, ext = os.path.splitext(rfn)

            print(f"Reloading: {name}")
            if name in modules:
                importlib.reload(modules[name])
            else:
                spec = importlib.util.spec_from_file_location(name, fn)
                mod = importlib.util.module_from_spec(spec)
                specs[name] = spec
                spec.loader.exec_module(mod)
                sys.modules[name] = mod
                modules[name] = mod
                # OG import lib
                #modules[name] = importlib.import_module(name, package=name)

if __name__ == "__main__":
    sys.meta_path.append(myfinder())
    try:
        pwd = os.path.abspath(sys.argv[1])
    except IndexError:
        pwd = os.getcwd()


    while True:
        try:
            asyncio.run(main(pwd))
        except KeyboardInterrupt:
            print("Exiting")
            exit(0)
        except Exception as e:
            print(traceback.format_exc())
            print("*"*80)
            print("Something went horribly wrong!, trace above, quick summary:")
            print(e)
