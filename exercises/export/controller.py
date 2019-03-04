# -*- coding: utf-8 -*-
from fmipp.export.FMIAdapterV2 import FMIAdapterV2
import warnings

class Controller( FMIAdapterV2 ):

    Thigh_ = 90
    Tlow_ = 70
    Pheat_ = 0

    def init( self, currentCommunicationPoint ):
        """
        Initialize the FMU (definition of input/output variables and parameters, enforce step size).
        """
        self.defineRealInputs( 'T' )
        self.defineRealOutputs( 'Pheat' )


    def doStep( self, currentCommunicationPoint, communicationStepSize ):
        """
        Make a simulation step.
        """

        syncTime = currentCommunicationPoint + communicationStepSize;

        # Read current input values.
        realInputs = self.getRealInputValues()
        T = realInputs['T']

        # Calculate output values.
        if ( T >= self.Thigh_ ):
            self.Pheat_ = 0. # turn off heating
            print( 'turn heating OFF at t = {}'.format( syncTime ) )
        elif ( T <= self.Tlow_ ):
            self.Pheat_ = 1e3 # turn on heating
            print( 'turn heating ON at t = {}'.format( syncTime ) )

        # Write current output values.
        realOutputs = { 'Pheat' : self.Pheat_ }
        self.setRealOutputValues( realOutputs )
