#!/usr/bin/env python
# coding: utf-8

# # Importing and using an FMU for Model Exchange in Python
# 
# The most obvious obstacle for using a bare FMU for ModelExchange is its lack of an integrator. For this reason, classes **FMUModelExchangeV1** and **FMUModelExchangeV2** provide generic methods for the integration of FMUs for ModelExchange for FMI Version 1.0 and 2.0, respectively. Instances of these classes own the actual FMU instance and are able to advance the current state up to a specified point in time, including the proper handling of FMU-internal events. The classes also provide functionality for convenient input and output handling.
# 
# The following example demonstrates the basic usage of class **FMUModelExchangeV2** (usage of class FMUModelExchangeV1 is analogous).
# 
# ## Loading the library and extracting an FMU
# 
# Load the FMI++ library into Python.

import fmipp


# Specify the FMU's model name.

model_name = 'Radiator'


# Specify the absolute path of the FMU. In this example, the FMU is supposed to be in the same directory as this notebook.

import os
work_dir = os.getcwd() # get current working directory (contains 'zigzag.fmu')
path_to_fmu = os.path.join( work_dir, 'win', model_name + '.fmu' ) # path to FMU


# Extract the FMU to the current work directory. The return value is the URI to the folder containing the unzipped FMU.

uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir )
print( 'URI of extracted FMU: {}'.format( uri_to_extracted_fmu ) )


# ## Loading, instantiating and initialising the FMU
# 
# Specify the FMU's configuration parameters.

logging_on = False              # turn logging on/off
stop_before_event = False       # halt integration immediately before an event?
event_search_precision = 1e-2   # set precision for event detection
integrator_type = fmipp.bdf     # use Backward Differentiation Formula from CVODE
#integrator_type = fmipp.rk     # alternatively, use Runge-Kutta for integration


# Load the FMU with the help of class **FMUModelExchangeV2**.

fmu = fmipp.FMUModelExchangeV2(
   uri_to_extracted_fmu, model_name,
   logging_on, stop_before_event, event_search_precision, integrator_type
   )


# Instantiate the FMU and check the status.

status = fmu.instantiate( 'radiator_1' ) # instantiate model
assert status == fmipp.fmiOK # check status


# Initialize the FMU and check the status.

status = fmu.initialize() # initialize model
assert status == fmipp.fmiOK # check status


# ## Run a simulation with the FMU
# 
# Specify default step size of one simulation step (communication step size).
stepsize = 3600;
integrator_stepsize = stepsize/10;

# Specify the simulation time and simulation stop time.
t = 0
tstop = 24 * 60 * 60

# Specify upper and lower threshold of hysteresis controller.
Tlow = 70
Thigh = 90

# For storing results.
t_sim = []
T_sim = []

# Simulation loop.
while t < tstop:
    # Integrate the model.
    t = fmu.integrate( t + stepsize, integrator_stepsize )

    # Retrieve value for output variable T.
    T = fmu.getRealValue( 'T' )

    # Hysteresis controller.
    if ( T >= Thigh ):
        fmu.setRealValue( 'Pheat', 0.0 ) # turn off heating
    elif ( T <= Tlow ):
        fmu.setRealValue( 'Pheat', 1e3 ) # turn on heating

    t_sim.append( t/3600 )
    T_sim.append( T )

import matplotlib.pyplot as plotter

plotter.plot( t_sim, T_sim, 'ro' ) # plot simulated results

plotter.xlabel( 'simulation time' )
plotter.ylabel( 'T' )
plotter.draw()


# Done.
