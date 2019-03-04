#!/usr/bin/env python
# coding: utf-8

# # Debugging code before exporting it as FMU
# 
# File *FMUExportTest.py* defines class **FMUExportTest**, which derives from class **FMIAdapterV2**. Import the class, in order to debug it.

from TestClassFMUExport import FMUExportTestClass


# Create an instance of class **FMUExportTest** to debug its functionality.

test = FMUExportTestClass()


# Initialize the new instance (at time *t=0*). When executing this function, a runtime warning will be displayed, saying that the "FMI++ export interface is not active". When debugging a class, this warning can be ignored.

test.init( 0. )


# Use functions *debugSetX* to set values for parameters and input variables.

test.debugSetRealParameterValues( { 'pr_y' : 2.2, 'pr_x' : 1.1 } )
test.debugSetRealInputValues( { 'ir_y' : 2., 'ir_x' : 1. } )

test.debugSetIntegerParameterValues( { 'pi_y' : 3, 'pi_x' : 6 } )
test.debugSetIntegerInputValues( { 'ii_y' : 4, 'ii_x' : 5 } )

test.debugSetBooleanParameterValues( { 'pb_y' : True, 'pb_x' : True } )
test.debugSetBooleanInputValues( { 'ib_y' : False, 'ib_x' : True } )

test.debugSetStringParameterValues( { 'ps_y' : 'abc', 'ps_x' : 'def' } )
test.debugSetStringInputValues( { 'is_y' : 'ghi', 'is_x' : 'jkl' } )


# Call the *doStep* function. Again, runtime warnings regarding the FMI++ export interface can be ignored.

test.doStep(0., 1.)


# After calling the *doStep* function, use functions *debugGetX* to retrieve and check the values of outputs.

out_real = test.debugGetRealOutputValues()
assert 1.1 == out_real[ 'or_x' ]
assert 4.4 == out_real[ 'or_y' ]

out_integer = test.debugGetIntegerOutputValues()
assert 30 == out_integer[ 'oi_x' ]
assert 12 == out_integer[ 'oi_y' ]

out_boolean = test.debugGetBooleanOutputValues()
assert True == out_boolean[ 'ob_x' ]
assert False == out_boolean[ 'ob_y' ]

out_strings = test.debugGetStringOutputValues()
assert 'jkldef' == out_strings[ 'os_x' ]
assert 'ghiabc' == out_strings[ 'os_y' ]


# Done.
