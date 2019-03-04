from fmipp.export.createFMU import createFMU

from controller import Controller


# Specify the model name of the FMU.

model_name = 'Controller'

createFMU( Controller, model_name, fmi_version = '2', verbose = True )