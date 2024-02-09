# Install Conda

https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg

# Setup a CQ environment
CONDA_SUBDIR=osx-64 conda create -n cq python=3.10
conda activate cq
conda config --env --set subdir osx-64

pip install cadquery
pip install ocp_vscode

## Optional
pip install build123d
pip install cadquery-server

# Install OCP CAD Viewer
https://marketplace.visualstudio.com/items?itemName=bernhard-42.ocp-cad-viewer

# Select python interpreter in VS Code

Select Conda 'cq'


```
from ocp_vscode import show, set_port
```
