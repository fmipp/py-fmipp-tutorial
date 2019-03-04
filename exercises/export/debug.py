
from controller import Controller

test = Controller()

test.init( 0. )

test.debugSetRealParameterValues( { 'T' : 80. } )

test.doStep(0., 300.)
out_real = test.debugGetRealOutputValues()

assert 1e3 == out_real[ 'Pheat' ]
