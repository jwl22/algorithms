clear vars; close all; clc

fig = figure(1);
grid on;
axis([-50, 50, -50, 50])
ball = line(inf,inf);
set(ball, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 10); 
waitforbuttonpress;

for t=0:0.01:100
    r = 20 + 15*cos(pi*t);
    x = [r*cos(pi*t) r*sin(pi*t)];

    set(ball, 'xdata', x(1), 'ydata', x(2));
    pause(0.005);
    drawnow;
end