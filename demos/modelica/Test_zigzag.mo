within ;
model Test_zigzag
  zigzag zigzag1
    annotation (Placement(transformation(extent={{30,-10},{50,10}})));
  Modelica.Blocks.Sources.Pulse pulse(
    offset=2,
    width=50,
    amplitude=1,
    period=4.567)
    annotation (Placement(transformation(extent={{-50,10},{-30,30}})));
  Modelica.Blocks.Math.Add add
    annotation (Placement(transformation(extent={{-10,-10},{10,10}})));
  Modelica.Blocks.Sources.Pulse pulse1(
    amplitude=2,
    offset=2,
    width=50,
    period=1.654)
    annotation (Placement(transformation(extent={{-50,-30},{-30,-10}})));
equation
  connect(pulse.y, add.u1) annotation (Line(points={{-29,20},{-20,20},{-20,6},{
          -12,6}}, color={0,0,127}));
  connect(zigzag1.k, add.y)
    annotation (Line(points={{28,0},{11,0}}, color={0,0,127}));
  connect(add.u2, pulse1.y) annotation (Line(points={{-12,-6},{-20,-6},{-20,-20},
          {-29,-20}}, color={0,0,127}));
  annotation (
    Icon(coordinateSystem(preserveAspectRatio=false)),
    Diagram(coordinateSystem(preserveAspectRatio=false)),
    uses(Modelica(version="3.2.2")));
end Test_zigzag;
