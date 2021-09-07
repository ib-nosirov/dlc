====================================
Ibrohim's Fork of DeepLabCut v2.1.10
====================================

This fork is meant to help install DeepLabCut on a local machine.
It version-matches with the current version of DeepLabCut installed on TACC resources.

--------------------------
Install DLC on Mac (Intel)
--------------------------
``/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)``
  Install the Homebrew package manager.


``brew install python@3.7``
  Install Python version 3.7; one of the other package dependencies, wxPython, is specifically compatible with this version.

``/usr/local/opt/python@3.7/bin/python3 -m pip install --upgrade pip wxpython``
  Install wxPython; it is needed for GUI support.

``/usr/local/opt/python@3.7/bin/python3 -m venv --system-site-packages [name]``
  Create a virtual environment containing wxPython; pass in a ``[name]`` of choice (without square brackets).

``source [name]/bin/activate``
  Activate the virtual environment.

``pip install tensorflow==1.15 pytest``
  Install and test TensorFlow version 1.15.

``git clone https://github.com/ib-nosirov/dlc.git dlc``

``cd dlc``

``pip install -e .``
  Install DeepLabCut v2.1.10.

-----
Usage
-----

DeepLabCut documentation is the perfect place to start learning how to use DLC.
  https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide.html

I have also included some helpful template files in the `Templates` folder.
The files contain basic files for creating a DLC project and runnings `sbatch` scripts on a TACC resource. You can even try running `python create_project.py` from inside a virtual environment to test how a DLC project is made, though make sure the file path dates in the python file are set to your current date.

One very important command for transporting a created project to and from a TACC resource is the `rsync` command.
  Move to the directory immediately above your DLC project directory.
  Now pass the command
  `rsync -avz [project name] [username]@maverick2.tacc.utexas.edu:/work2/[your allocation number]/[username]/maverick2/[project name]`.
  (Tip: everything after the ':' is found by passing the `pwd` command while you are in your TACC workspace.)

More information can be found about TACC resources, and Maverick2 specifically, in the Maverick2 User Guide.
  https://portal.tacc.utexas.edu/user-guides/maverick2
