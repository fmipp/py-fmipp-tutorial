within ;
model Radiator
  Modelica.Thermal.HeatTransfer.Components.HeatCapacitor
                                        heatCapacitor(C=500000, T(start=358.15,
        fixed=true))
    annotation (Placement(transformation(extent={{-10,-40},{10,-60}},
          rotation=0)));
  Modelica.Thermal.HeatTransfer.Celsius.TemperatureSensor
                                         temperatureSensor  annotation (Placement(
        transformation(
        origin={0,0},
        extent={{-10,10},{10,-10}},
        rotation=90)));
  Modelica.Thermal.HeatTransfer.Sources.PrescribedHeatFlow prescribedHeatFlow
    annotation (Placement(transformation(extent={{-60,-30},{-40,-10}})));
  Modelica.Thermal.HeatTransfer.Sources.FixedHeatFlow fixedHeatFlow(Q_flow=-400)
    annotation (Placement(transformation(extent={{60,-30},{40,-10}})));
  Modelica.Blocks.Interfaces.RealInput Pheat
    annotation (Placement(transformation(extent={{-140,-40},{-100,0}})));
  Modelica.Blocks.Interfaces.RealOutput T
    annotation (Placement(transformation(extent={{100,10},{120,30}})));
  Modelica.Blocks.Logical.LessEqualThreshold lessEqualThreshold(threshold=90)
    annotation (Placement(transformation(extent={{20,70},{40,90}})));
  Modelica.Blocks.Logical.GreaterEqualThreshold greaterEqualThreshold(threshold
      =70) annotation (Placement(transformation(extent={{20,30},{40,50}})));
  Modelica.Blocks.Logical.And and1
    annotation (Placement(transformation(extent={{60,50},{80,70}})));
  Modelica.Blocks.Interfaces.BooleanOutput ok
    annotation (Placement(transformation(extent={{100,50},{120,70}})));
equation
  connect(prescribedHeatFlow.port, temperatureSensor.port) annotation (Line(
        points={{-40,-20},{0,-20},{0,-10}},             color={191,0,0}));
  connect(fixedHeatFlow.port, temperatureSensor.port)
    annotation (Line(points={{40,-20},{0,-20},{0,-10}},   color={191,0,0}));
  connect(heatCapacitor.port, temperatureSensor.port)
    annotation (Line(points={{0,-40},{0,-10}},            color={191,0,0}));
  connect(prescribedHeatFlow.Q_flow, Pheat)
    annotation (Line(points={{-60,-20},{-120,-20}},color={0,0,127}));
  connect(temperatureSensor.T, T)
    annotation (Line(points={{0,10},{0,20},{110,20}},
                                                    color={0,0,127}));
  connect(T, T) annotation (Line(points={{110,20},{110,20}}, color={0,0,127}));
  connect(greaterEqualThreshold.u, temperatureSensor.T)
    annotation (Line(points={{18,40},{0,40},{0,10}}, color={0,0,127}));
  connect(lessEqualThreshold.u, temperatureSensor.T) annotation (Line(points={{
          18,80},{0,80},{0,10},{6.10623e-16,10}}, color={0,0,127}));
  connect(lessEqualThreshold.y, and1.u1) annotation (Line(points={{41,80},{50,
          80},{50,60},{58,60}}, color={255,0,255}));
  connect(greaterEqualThreshold.y, and1.u2) annotation (Line(points={{41,40},{
          50,40},{50,52},{58,52}}, color={255,0,255}));
  connect(and1.y, ok)
    annotation (Line(points={{81,60},{110,60}}, color={255,0,255}));
  annotation (
    uses(Modelica(version="3.2.2")),
    Diagram(coordinateSystem(preserveAspectRatio=false, extent={{-100,-100},{
            100,100}})),
    experiment(StopTime=43200));
end Radiator;
