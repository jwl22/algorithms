clear all; close all; clc

x = 5;
y = 10/x;
% pos = [x y];
dt = 0.005;
et = [5/sqrt(29) -2/sqrt(29)];
en = [2/sqrt(29) 5/sqrt(29)];
v = 5 * et;
% a = -0.5 * et;

% [et, en]

% pre_s = 0;

fig = figure(1);
grid on;
axis([0, 50, 0, 10])
box = line(inf,inf);
set(box, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 10); 

set(box, 'xdata', x, 'ydata', y);
drawnow;
waitforbuttonpress;
while true
    et = [x^2/sqrt(10^2+(x^2)^2) -10/sqrt(10^2+(x^2)^2)];
    en = [10/sqrt(10^2+(x^2)^2) x^2/sqrt(10^2+(x^2)^2)];

    ro_t = abs(20./x.^3) / (1+(-10./x.^2).^2).^(3/2);

    spd = sqrt(v(1)^2 + v(2)^2);
    a = -0.5*et + spd^2*ro_t*en;
    v = v + a*dt;
    if v(1)<0
        break
    end

    % spd = sqrt(v(1)^2 + v(2)^2);
    % a = sqrt(a(1)^2+a(2)^2)*et + spd^2*ro_t*en;
    % v = spd*et;
    % pos = pos + v*dt;
    x = x + v(1)*dt;
    y = y + v(2)*dt;
    % pos = [x y];

    set(box, 'xdata', x, 'ydata', y);
    % pause(0.01);
    drawnow;

    % pre_s = cur_s;
end