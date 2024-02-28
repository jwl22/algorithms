clear; close all; clc
addpath('Myfunc\')

t0= 0; tf= 50;
tspan = [t0 tf];
x0= [.1 0 0 0 0 0]';
[t,x]= ode23('robctl_classical',tspan,x0);
% figure(1)
% plot(t,x)
[qd,e]= robout(t,x);
figure(2)
plot(t,e)
legend('theta1','theta2')
title('error')
xlabel('Time (sec)');
grid on;

fig = figure(1);
grid on;
title('simulation')
axis([-3, 3, -3, 3])
pbaspect([1 1 1])
A = line(inf,inf);
rA = line(inf,inf);
set(A, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 8);
set(A, 'xdata', 0, 'ydata', 0);
set(rA, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 8);
set(rA, 'xdata', 0, 'ydata', 0);
B = line(inf,inf);
rB = line(inf,inf);
set(B, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 8); 
set(rB, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 8); 
C = line(inf,inf);
rC = line(inf,inf);
set(C, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 8); 
set(rC, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 8); 
AB = line(inf,inf);
rAB = line(inf,inf);
set(AB, 'linestyle', '-', 'marker', 'none'); 
set(rAB, 'linestyle', '-', 'marker', 'none', 'Color', 'r'); 
BC = line(inf,inf);
rBC = line(inf,inf);
set(BC, 'linestyle', '-', 'marker', 'none');
set(rBC, 'linestyle', '-', 'marker', 'none', 'Color', 'r');

legend([AB rAB], {'approximation', 'reference'})

waitforbuttonpress;
for i=1:length(t)
    set(B, 'xdata', cos(x(i,1)), 'ydata', sin(x(i,1)));
    set(C, 'xdata', cos(x(i,1))+cos(x(i,2)), 'ydata', sin(x(i,1))+sin(x(i,2)));
    set(rB, 'xdata', cos(qd(i,1)), 'ydata', sin(qd(i,1)));
    set(rC, 'xdata', cos(qd(i,1))+cos(qd(i,2)), 'ydata', sin(qd(i,1))+sin(qd(i,2)));
    set(AB, 'xdata', linspace(0,cos(x(i,1)),20), 'ydata', linspace(0,sin(x(i,1)),20));
    set(BC, 'xdata', linspace(cos(x(i,1)),cos(x(i,1))+cos(x(i,2)),20), 'ydata', linspace(sin(x(i,1)),sin(x(i,1))+sin(x(i,2)),20));
    set(rAB, 'xdata', linspace(0,cos(qd(i,1)),20), 'ydata', linspace(0,sin(qd(i,1)),20));
    set(rBC, 'xdata', linspace(cos(qd(i,1)),cos(qd(i,1))+cos(qd(i,2)),20), 'ydata', linspace(sin(qd(i,1)),sin(qd(i,1))+sin(qd(i,2)),20));

    pause(0.01)
end