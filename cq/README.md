# Install Conda

https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg

## Setup a CQ environment (M1 Mac)

```sh
CONDA_SUBDIR=osx-arm64 conda create -n cq python=3.10
conda activate cq
conda config --add channels conda-forge

conda install cadquery

pip install ocp_vscode watch_import
```

## Setup a CQ environment (x86-64 version)
```sh
CONDA_SUBDIR=osx-64 conda create -n cq python=3.10
conda activate cq
conda config --env --set subdir osx-64

pip install cadquery ocp_vscode watch_import
```

# Install OCP CAD Viewer
https://marketplace.visualstudio.com/items?itemName=bernhard-42.ocp-cad-viewer

# Select python interpreter in VS Code
Select Conda 'cq'

# Auto reload folder
run `watch_import PATH_TO_CQ_FILES` and viewer will reload on save

# Auto reload from script
```python
import cadquery as cq
from ocp_vscode import show
from watch_import import watch_me

body = cq.Workplane("XY").box(5, 10, 15)
show(body)

watch_me()
```
