#!/usr/bin/env python
# coding: utf-8

# # Exporting Python scripts as FMU for Co-Simulation
# 
# The functionality of Python can be made available as FMU for Co-Simulation (version 1.0 or 2.0) with the help of class **FMIAdapterV1** or **FMIAdapterV2**, respectively. These class define two abstract methods that have to be implemented by the user:
# 
#  * Method *init( self, currentCommunicationPoint )* is intended to initialize input/output variables and parameters needed for co-simulation. Optionally, a fixed simulation time step can be specified.
#  * Method *doStep( self, currentCommunicationPoint, communicationStepSize )* is called at every simulation step (as requested by the master algorithm).
# 
# By deriving a new class from class **FMIAdapterV1** or **FMIAdapterV2** and implementing these two methods, virtually all functionality of Python can be made available via an FMU for Co-Simulation. When using such an FMU, Python is started in the background and synchronized to the master algorithm.
# 
# ## Creating an FMU
# 
# Import the requried functionality from the FMI++ library.

from fmipp.export.createFMU import createFMU


# File *FMUExportTest.py* defines class **FMUExportTest**, which derives from class **FMIAdapterV2**. Import the class, in order to export it.

from TestClassFMUExport import FMUExportTestClass


# Specify the model name of the FMU.

model_name = 'FMUExportTestCS'


# Define start values for the variables defined in class **FMUExportTest** (see method *init*).

start_values = {
   'pr_y' : 2.2, 'pr_x' : 1.1,
   'ir_y' : 2., 'ir_x' : 1.,
   'pi_y' : 3, 'pi_x' : 6,
   'ii_y' : 4, 'ii_x' : 5,
   'pb_y' : True, 'pb_x' : True,
   'ib_y' : False, 'ib_x' : True,
   'ps_y' : 'abc', 'ps_x' : 'def',
   'is_y' : 'ghi', 'is_x' : 'jkl'
}


# Declare additional files, that will be added to the *resources* directory of the FMU.

import os.path
optional_files = [ os.path.join( 'data', 'extra.dat' ) ]


# Use function *createFMU* to create the FMU.

createFMU(
   FMUExportTestClass, model_name, fmi_version = '2',
   verbose = False, start_values = start_values, optional_files = optional_files )

# ## Testing the FMU
# 
# Specify the absolute path to the newly created FMU. In this example, the FMU was created in the same directory as this notebook.

import os
work_dir = os.getcwd() # define working directory
path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU

print( 'The path to the FMU is: {}'.format( path_to_fmu ) )


# Extract the FMU to the current work directory. The return value is the URI to the folder containing the unzipped FMU.

import fmipp
uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir )

print( 'The URI of the extracted FMU is: {}'.format( uri_to_extracted_fmu ) )


# Load the FMU.

logging_on = False
time_diff_resolution = 1e-9

fmu = fmipp.FMUCoSimulationV2(
   uri_to_extracted_fmu, model_name,
   logging_on, time_diff_resolution
   )


# Instantiate and initialize the FMU, then call *doStep*, *getRealValue*, etc.

start_time = 0.
stop_time = 10.

instance_name = "test1"
visible = False
interactive = False
status = fmu.instantiate( instance_name, start_time, visible, interactive )
assert status == fmipp.fmiOK

stop_time_defined = True
status = fmu.initialize( start_time, stop_time_defined, stop_time )
assert status == fmipp.fmiOK

time = 0.
step_size = 1.

new_step = True
status = fmu.doStep( time, step_size, new_step )
assert status == fmipp.fmiOK


# Check if the outputs are as expected.

or_x = fmu.getRealValue( 'or_x' )
status = fmu.getLastStatus()
assert 1.1 == or_x
assert status == fmipp.fmiOK
print( 'Test for real output variable "or_x" successfull!' )

or_y = fmu.getRealValue( 'or_y' )
status = fmu.getLastStatus()
assert 4.4 == or_y
assert status == fmipp.fmiOK
print( 'Test for real output variable "or_y" successfull!' )

oi_x = fmu.getIntegerValue( 'oi_x' )
status = fmu.getLastStatus()
assert 30 == oi_x
assert status == fmipp.fmiOK
print( 'Test for integer output variable "oi_x" successfull!' )

oi_y = fmu.getIntegerValue( 'oi_y' )
status = fmu.getLastStatus()
assert 12 == oi_y
assert status == fmipp.fmiOK
print( 'Test for integer output variable "oi_y" successfull!' )

ob_x = fmu.getBooleanValue( 'ob_x' )
status = fmu.getLastStatus()
assert True == ob_x
assert status == fmipp.fmiOK
print( 'Test for boolean output variable "ob_x" successfull!' )

ob_y = fmu.getBooleanValue( 'ob_y' )
status = fmu.getLastStatus()
assert False == ob_y
assert status == fmipp.fmiOK
print( 'Test for boolean output variable "ob_y" successfull!' )

os_x = fmu.getStringValue( 'os_x' )
status = fmu.getLastStatus()
assert 'jkldef' == os_x
assert status == fmipp.fmiOK
print( 'Test for string output variable "os_x" successfull!' )

os_y = fmu.getStringValue( 'os_y' )
status = fmu.getLastStatus()
assert 'ghiabc' == os_y
assert status == fmipp.fmiOK
print( 'Test for string output variable "os_y" successfull!' )


# Done.
