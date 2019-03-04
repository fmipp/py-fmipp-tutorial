# Tutorial: The FMI++ Python Interface

## Running the demos / exercises in this tutorial

Demos are provided as **Jupyter notebooks**
 * subfolder *demos*: contains the notebooks
 * also online: [Code Ocean compute capsule](https://doi.org/10.24433/CO.9880202.v2)

All **supporting material** for demos and exercises in this tutorial are available in the following subfolders:
 * subfolder *demos*:
   * subfolder *demos/scripts*: notebooks as standard Python scripts (in case you don’t want to install jupyter)
   * subfolder *demos/modelica*: Modelica models used in the demos
   * subfolder *demos/data*: FMU for model zigzag (Linux 64-bit, Windows 32-bit, Windows 64-bit)
 * subfolder *exercises*:
   * subfolder *exercises/import*: import Modelica plant model in Python
   * subfolder *exercise/export*: export Python controller and use it from Modelica


## Requirements for running the demos / exercises

General requirements:
 * up-to-date version of *Python* installed (version 2.7 or 3.6 and higher)
 * know how to install Python packages via *pip*

Required Python packages for running **demos**:
 * *fmipp*: see tutorial slides for details
 * *jupyter*: `pip install jupyter`
 * *matplotlib*: `pip install matplotlib`

Requirements for running the **exercises**:
 * *Modelica compiler* that allows to *export FMUs for Model Exchange* (FMI 1.0 or 2.0)
 * *Modelica compiler* that allows to *import FMUs for Co-Simulation* (FMI 2.0)
 * Modelica compiler and Python version have to be either both 32-bit or 64-bit
 * tested with Dymola 2018, but should also work with JModelica, OpenModelica, etc.

### Alternative to Jupyter notebooks

Run standard Python scripts in subfolder *demos/scripts*.
