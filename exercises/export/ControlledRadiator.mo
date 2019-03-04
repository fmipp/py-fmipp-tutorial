within ;
model ControlledRadiator
  Modelica.Thermal.HeatTransfer.Components.HeatCapacitor
                                        heatCapacitor(C=500000, T(start=358.15,
        fixed=true))
    annotation (Placement(transformation(extent={{-16,-28},{4,-48}},
          rotation=0)));
  Modelica.Thermal.HeatTransfer.Celsius.TemperatureSensor
                                         temperatureSensor  annotation (Placement(
        transformation(
        origin={-6,-6},
        extent={{-10,10},{10,-10}},
        rotation=90)));
  Modelica.Thermal.HeatTransfer.Sources.PrescribedHeatFlow prescribedHeatFlow
    annotation (Placement(transformation(extent={{-44,-32},{-24,-12}})));
  Modelica.Thermal.HeatTransfer.Sources.FixedHeatFlow fixedHeatFlow(Q_flow=-400)
    annotation (Placement(transformation(extent={{32,-32},{12,-12}})));
  Controller_fmu controller_fmu(fmi_CommunicationStepSize=300,
    fmi_StopTime=43200,
    fmi_NumberOfSteps=144)
    annotation (Placement(transformation(extent={{-32,20},{-52,40}})));
equation
  connect(prescribedHeatFlow.port, temperatureSensor.port) annotation (Line(
        points={{-24,-22},{-24,-22},{-6,-22},{-6,-16}}, color={191,0,0}));
  connect(fixedHeatFlow.port, temperatureSensor.port)
    annotation (Line(points={{12,-22},{-6,-22},{-6,-16}}, color={191,0,0}));
  connect(heatCapacitor.port, temperatureSensor.port)
    annotation (Line(points={{-6,-28},{-6,-28},{-6,-16}}, color={191,0,0}));
  connect(temperatureSensor.T, controller_fmu.T)
    annotation (Line(points={{-6,4},{-6,30},{-31.6,30}}, color={0,0,127}));
  connect(controller_fmu.Pheat, prescribedHeatFlow.Q_flow) annotation (Line(
        points={{-54,30},{-76,30},{-76,-22},{-44,-22}}, color={0,0,127}));
  annotation (
    uses(Modelica(version="3.2.2")),
    Diagram(coordinateSystem(preserveAspectRatio=false, extent={{-100,-100},{
            100,100}})),
    experiment(StopTime=43200));
end ControlledRadiator;
