clear; close all; clc
% 실행 후 아무 키 입력 시 동작합니다

%% local(A) 좌표계 기준
% A와 B가 연결되어 회전하면서 A가 B에게 공을 던지는 상황
% 회전하고 있는 좌표계에서 공의 움직임을 표현한다.

fig = figure(1);
title('local coordinate') 
% grid on;
axis([-10, 10, -5, 15])
pbaspect([1 1 1])
A = line(inf,inf);
set(A, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 10);
set(A, 'xdata', 0, 'ydata', 0);
B = line(inf,inf);
set(B, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k', 'markerfacecolor', 'k', 'markersize', 10); 
set(B, 'xdata', 0, 'ydata', 10);
AB = line(inf,inf);
set(AB, 'linestyle', '--', 'marker', 'none', 'xdata', 0*ones(1,21), 'ydata', 0:20); 
ball = line(inf,inf);
set(ball, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'b', 'markerfacecolor', 'b', 'markersize', 10);
theta = 0:0.01:2*pi;
set(line, 'linestyle', '--', 'xdata', 5*cos(theta), 'ydata',5+5*sin(theta));

s = [0 0 0];
w = [0 0 pi/16];
v = [0 5 0]; % 처음 가해진 속도

% theta = pi/2;
% r = 5;
% a = [0 0 0];

dt = 0.01;
v = v*dt;
w = w*dt;
waitforbuttonpress;
for t=0:1000
    % theta = theta + w(3)*dt;
    coriolis = -2*(cross(w,v)); % coriolis 힘

    v = v + coriolis;
    s = s + v;
    set(ball, 'xdata', s(1), 'ydata', s(2));

    % set(A, 'xdata', r*cos(theta), 'ydata', 5+r*sin(theta));
    % set(B, 'xdata', r*cos(theta+pi), 'ydata', 5+r*sin(theta+pi));

    pause(0.002);
end