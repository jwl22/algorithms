clear; close all; clc
addpath('Myfunc\')

global t1 t2

param; % Setting all the parameters
t0=0; % Initial Simulation Time (Sec)
tf=50; % Final Simulation Time (Sec)

x0=[0.1 0 0 0]'; % Initial Conditions
xx=x0;
tt=0:T:tf; % generating the discrete steps between t0 and tf    
for i=1:length(tt)-1
    t1=0;
    t2=0;
    [t1,t2]=control(kv,kp,tt(i),xx);
    clear t
    clear y
    tspan = [tt(i) tt(i+1)];
    [t,y]=ode23('staspace',tspan,x0);
    x0=y(length(t),:)';
    xx=x0;
    k111(i)=t1;
    k112(i)=t2;
    yyy(i,:)=x0';
end

for i=1:length(tt)-1
    ttt(i)=tt(i);
end

% stairs(ttt,yyy(:,1));
% hold on
% stairs(ttt,yyy(:,2));
% hold off
% title('Joint Angles theta1(t) and theta2(t) in rad (T=100 msec)');
% xlabel('Time (sec)');
% figure;
% 
% stairs(ttt,k111);
% hold on
% stairs(ttt,k112);
% hold off
% title('Input Torque Tao1(t) and Tao2(t) (T=100 msec)');
% xlabel('Time (sec)');

for i=1:length(ttt)
    [qd,qdp,qdpp]=sysinp(g1,g2,T,ttt(i));
    e(:,i)=qd-[yyy(i,1) yyy(i,2)]';
end
figure;
stairs(ttt,e(1,:));
hold on
stairs(ttt,e(2,:));
hold off
grid on
legend('theta1','theta2')
title('error')
% title('Tracking Error for Theta1(t) and Theta2(t) (T=100 msec)');
xlabel('Time (sec)');

fig = figure(2);
grid on
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
for i=1:length(ttt)
    [qd,qdp,qdpp]=sysinp(g1,g2,T,ttt(i));

    set(B, 'xdata', cos(yyy(i,1)), 'ydata', sin(yyy(i,1)));
    set(C, 'xdata', cos(yyy(i,1))+cos(yyy(i,2)), 'ydata', sin(yyy(i,1))+sin(yyy(i,2)));
    set(rB, 'xdata', cos(qd(1)), 'ydata', sin(qd(1)));
    set(rC, 'xdata', cos(qd(1))+cos(qd(2)), 'ydata', sin(qd(1))+sin(qd(2)));
    set(AB, 'xdata', linspace(0,cos(yyy(i,1)),20), 'ydata', linspace(0,sin(yyy(i,1)),20));
    set(BC, 'xdata', linspace(cos(yyy(i,1)),cos(yyy(i,1))+cos(yyy(i,2)),20), 'ydata', linspace(sin(yyy(i,1)),sin(yyy(i,1))+sin(yyy(i,2)),20));
    set(rAB, 'xdata', linspace(0,cos(qd(1)),20), 'ydata', linspace(0,sin(qd(1)),20));
    set(rBC, 'xdata', linspace(cos(qd(1)),cos(qd(1))+cos(qd(2)),20), 'ydata', linspace(sin(qd(1)),sin(qd(1))+sin(qd(2)),20));

    pause(0.01)
end