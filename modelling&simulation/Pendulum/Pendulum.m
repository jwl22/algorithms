clear; close all; clc
% 실행 후 아무 키 입력 시 동작합니다

%% Problem 1. Pendulum in a box.
fig = figure(1);
fig.Position = [500 500 1000 400];
title('Pendulum in a box')
axis([-5, 55, -15, 5])
box = rectangle('position',[0 -10 20 10]);

O = [0 0];
xi = 12;
l = 5;
a0 = 1;
v = 0;
g = 9.8;
m = 1;

wire = line(inf,inf);
pendulum = line(inf,inf);

theta = -pi/5;
dtheta = 0;

set(wire, 'linestyle', '-', 'xdata', linspace(O(1)+xi, O(1)+xi+l*sin(pi+theta), 50), 'ydata', linspace(O(2), l*cos(pi+theta), 50));
set(pendulum, 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 10, 'xdata', O(1)+xi+l*sin(pi+theta), 'ydata', l*cos(pi+theta));

% r = [O(1)+xi+l*sin(pi+theta), l*cos(pi+theta)];
dt = 0.0003;
a0 = a0*dt;
g = g*dt;
waitforbuttonpress;
for i=1:1000
    ddtheta = (a0*cos(theta) - m*g*sin(theta))/(l*cos(2*theta));
    dtheta = dtheta + ddtheta;
    theta = theta + dtheta;

    % ddr = a0+l*ddtheta*(cos(theta)-sin(theta))-l*d
    
    v = v + a0;
    O(1) = O(1) + v;

    set(wire, 'xdata', linspace(O(1)+xi, O(1)+xi+l*sin(pi+theta), 50), 'ydata', linspace(O(2), l*cos(pi+theta), 50));
    set(pendulum, 'xdata', O(1)+xi+l*sin(pi+theta), 'ydata', l*cos(pi+theta))
    box.Position = [0+O(1) -10+O(2) 20 10];

    pause(0.005);
    % drawnow;
end