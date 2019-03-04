within ;
model zigzag
  Modelica.Blocks.Math.Product product
    annotation (Placement(transformation(extent={{-60,-10},{-40,10}})));
  Modelica.Blocks.Logical.Switch switch1
    annotation (Placement(transformation(extent={{60,-10},{80,10}})));
  Modelica.Blocks.Logical.Hysteresis hysteresis(uLow=-1, uHigh=1)
    annotation (Placement(transformation(extent={{20,-10},{40,10}})));
  Modelica.Blocks.Sources.Constant const(k=-1)
    annotation (Placement(transformation(extent={{30,20},{50,40}})));
  Modelica.Blocks.Sources.Constant const1(k=1)
    annotation (Placement(transformation(extent={{30,-40},{50,-20}})));
  Modelica.Blocks.Continuous.Integrator integrator
    annotation (Placement(transformation(extent={{-20,-10},{0,10}})));
  Modelica.Blocks.Interfaces.RealInput k
    annotation (Placement(transformation(extent={{-140,-20},{-100,20}})));
  Modelica.Blocks.Interfaces.RealOutput x
    annotation (Placement(transformation(extent={{100,50},{120,70}})));
  Modelica.Blocks.Interfaces.RealOutput derx
    annotation (Placement(transformation(extent={{100,-70},{120,-50}})));
equation
  connect(switch1.u2, hysteresis.y)
    annotation (Line(points={{58,0},{41,0}}, color={255,0,255}));
  connect(switch1.u3, const1.y) annotation (Line(points={{58,-8},{54,-8},{54,
          -30},{51,-30}}, color={0,0,127}));
  connect(switch1.u1, const.y)
    annotation (Line(points={{58,8},{54,8},{54,30},{51,30}}, color={0,0,127}));
  connect(hysteresis.u, integrator.y)
    annotation (Line(points={{18,0},{1,0}}, color={0,0,127}));
  connect(product.y, integrator.u)
    annotation (Line(points={{-39,0},{-22,0}}, color={0,0,127}));
  connect(switch1.y, product.u2) annotation (Line(points={{81,0},{90,0},{90,-50},
          {-70,-50},{-70,-6},{-62,-6}}, color={0,0,127}));
  connect(k, product.u1) annotation (Line(points={{-120,0},{-70,0},{-70,6},{-62,
          6}}, color={0,0,127}));
  connect(derx, integrator.u) annotation (Line(points={{110,-60},{-30,-60},{-30,
          0},{-22,0}}, color={0,0,127}));
  connect(x, integrator.y)
    annotation (Line(points={{110,60},{10,60},{10,0},{1,0}}, color={0,0,127}));
  annotation (uses(Modelica(version="3.2.2")), Icon(graphics={
        Rectangle(
          extent={{-100,100},{100,-100}},
          lineColor={0,0,0},
          fillColor={255,255,255},
          fillPattern=FillPattern.Solid),
        Line(points={{-80,70},{80,70}}, color={215,215,215}),
        Line(points={{-80,-70},{80,-70}}, color={215,215,215}),
        Line(points={{-70,-70},{-50,70},{-30,-70},{-10,70},{10,-70},{30,70},{50,
              -70},{70,70}}, color={0,0,0})}));
end zigzag;
