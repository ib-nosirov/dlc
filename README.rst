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
