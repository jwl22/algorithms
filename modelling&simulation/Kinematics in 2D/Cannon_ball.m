% 실행 후 아무 키 입력 시 동작합니다

clear vars; close all; clc

g = 9.8;
v0 = [20, 20];
r0 = [20, 10];
i = [1,0];
j = [0,1];

fig = figure(1);
grid on;
axis([5, 100, -50, 50])
ball = line(inf,inf);
set(ball, 'linestyle', 'none', 'marker', 'o', 'markeredgecolor', 'k',...
    'markerfacecolor', 'k',    'markersize', 10); 
waitforbuttonpress;
theta = pi/4;
for t=0:0.01:10
    v = v0.*cos(theta).*i + (v0.*sin(theta)-g.*t).*j;
    r = r0 + v0.*t.*cos(theta).*i + (v0.*t.*sin(theta)-1/2.*g.*t.^2).*j
    % v0 = v;
    
    set(ball, 'xdata', r(1), 'ydata', r(2));
    pause(0.003);
    drawnow;
end