clear; clc; close all
%% Initialization
global a b mS mH IST ISW g theta rC
global tall xall plotx ploty p0
a=0.6; b=0.3; mS=10; mH=30; g = 9.81;
IST = 0; ISW = 0;
theta = 4*pi/180;
tall = []; xall = []; plotx = []; ploty = []; p0 = [0; 0; 0];

q0=[0.2286;-0.3682;-1.2286;0.4063];
rC = [0, 0, 0]';

%% Simulation
X_cfg = [];
X_wrk = [];
epoch = 30;

for i = 1:epoch
    % Phase1
    % x = [qST qSW dqST dqSW]
    tspan=[0:0.01:5]';
    options=odeset('events',@heelcontact);
    [t,q] = ode15s(@Dyn_Swing, tspan, q0, options);
    X_cfg = [X_cfg; q];

    % Phase2
    % dx_plus = [dqST, dqSW, vCx vCy]'
    dq_plus = Dyn_Impact(q(end, :));
    X_wrk = [X_wrk; Kinematics(q)];
    rC = squeeze(X_wrk(end, 3, :));

    % Swap Leg
    % x = [qST qSW dqST dqSW]'
    % dx_plus = [dqST, dqSW, vCx vCy]'
    % x0 = [qSW qST dqSW dqST]'
    q0 = [q(end,2), q(end,1), dq_plus(2), dq_plus(1)]';

end

%% Animation
figure();
set(gcf, 'position', [825 41 1093 945]);

subplot(2, 2, 1);
handle_leg1 = line(0,0,'Color', [1 0.5 0.5], 'linewidth', 6); hold on;
handle_leg2 = line(0,0,'Color', [1 0.5 0.5], 'linewidth', 6);
plane = [cos(theta), -sin(theta); sin(theta), cos(theta)] * [1000, -1000; 0, 0];
handle_plane = line(plane(1,:), -plane(2,:), 'Color', 'k', 'linewidth', 3);
axis([-5, 5, -5, 5])
xlabel('$X[m]$', 'interpreter','latex')
ylabel('$Y[m]$', 'interpreter','latex')
title('Compass Gait', 'fontsize', 20, 'interpreter','latex')
set(gca, 'fontsize' , 17, 'TickLabelInterpreter','latex')

subplot(2, 2, 2);
handle_dot_dqST = plot(0,0,'Color', 'r', 'linewidth', 2, 'Marker', 'o', 'MarkerFaceColor', 'r'); hold on;
handle_dot_dqSW = plot(0,0,'Color', 'b', 'linewidth', 2, 'Marker', 'o', 'MarkerFaceColor', 'b');
handle_line_dqST = plot(0,0,'Color', [1 0.7 0.7], 'linewidth', 2); 
handle_line_dqSW = plot(0,0,'Color', [0.7 0.7 1], 'linewidth', 2);
axis([-3 3 -3 3])
xlabel('$Time[sec]$', 'interpreter','latex')
ylabel('$\dot\theta[rad/sec]$', 'interpreter','latex')
legend('$\dot\theta_{ST}$', '$\dot\theta_{SW}$', 'fontsize', 17, 'interpreter','latex')
title('Angular Velocities', 'fontsize', 20, 'interpreter','latex')
set(gca, 'fontsize' , 17, 'TickLabelInterpreter','latex')

subplot(2, 2, 3);
handle_line_qSTdqST = plot(0,0,'Color', [0.7 1 0.7], 'linewidth', 2); hold on;
handle_dot_qSTdqST= plot(0,0,'Color', [0 0.6 0], 'linewidth', 2, 'Marker', 'o', 'MarkerFaceColor', [0 0.6 0]);
axis([-0.75 0.75 -2 -0.5])
xlabel('$\theta_{ST}[rad]$', 'interpreter','latex')
ylabel('$\dot\theta_{ST}[rad/sec]$', 'interpreter','latex')
title('Phase Portrait of $\theta_{ST}$', 'fontsize', 20, 'interpreter','latex')
set(gca, 'fontsize' , 17, 'TickLabelInterpreter','latex')

subplot(2, 2, 4);
handle_line_qSWdqSW = plot(0,0,'Color', [0.4 0.8 0.8], 'linewidth', 2); hold on;
handle_dot_qSWdqSW = plot(0,0,'Color', [0 0.5 0.5], 'linewidth', 2, 'Marker', 'o', 'MarkerFaceColor', [0 0.5 0.5]);
axis([-3 3 -3 3])
xlabel('$\theta_{SW}[rad]$', 'interpreter','latex')
ylabel('$\dot\theta_{SW}[rad/sec]$', 'interpreter','latex')
title('Phase Portrait of $\theta_{SW}$', 'fontsize', 20, 'interpreter','latex')
set(gca, 'fontsize' , 17, 'TickLabelInterpreter','latex')

pause()
t = [0:0.01:length(X_wrk)/100];
for i = 1:length(X_wrk)
    % x = [rC rH rE]
    x = X_wrk(i,:,:);
    rC = squeeze(x(1,1,:)); rH = squeeze(x(1,2,:)); rE = squeeze(x(1,3,:));
    
    % Robot
    subplot(2, 2, 1);
    axis([rH(1)-1 rH(1)+1 rH(2)-1.2 rH(2)+0.8])
    
    % line CH
    x = [rC(1), rH(1)];
    y = [rC(2), rH(2)];
    z = [rC(3), rH(3)];
    set(handle_leg1, 'xdata', x, 'ydata', y, 'zdata', z);
    
    % line HE
    x = [rE(1), rH(1)];
    y = [rE(2), rH(2)];
    z = [rE(3), rH(3)];
    set(handle_leg2, 'xdata', x, 'ydata', y, 'zdata', z);
    
    % Phase Portrait
    % X_cfg(i,:) = [qST qSW dqST dqSW]
    subplot(2, 2, 2);
    set(handle_line_dqST, 'xdata', t(1:i),'ydata', X_cfg(1:i,3))
    set(handle_dot_dqST, 'xdata', t(i),'ydata', X_cfg(i,3))
    set(handle_line_dqSW, 'xdata', t(1:i),'ydata', X_cfg(1:i,4))
    set(handle_dot_dqSW, 'xdata', t(i),'ydata', X_cfg(i,4))
    axis([t(i)-1.5 t(i)+1.5 -5 5])
    
    set(handle_line_qSTdqST, 'xdata', X_cfg(1:i,1), 'ydata', X_cfg(1:i,3))
    set(handle_dot_qSTdqST,'xdata', X_cfg(i,1), 'ydata', X_cfg(i,3))
    
    set(handle_line_qSWdqSW, 'xdata', X_cfg(1:i,2), 'ydata', X_cfg(1:i,4))
    set(handle_dot_qSWdqSW,'xdata', X_cfg(i,2), 'ydata', X_cfg(i,4))
    
    pause(0.01);
end

%% 
function [value,isterm,direct]=heelcontact(t,x)
global a b theta
R01=[cos(-theta),-sin(-theta),0;sin(-theta),cos(-theta),0;0,0,1];
p0=(a+b)*[cos(x(1))-cos(x(2));sin(x(1))-sin(x(2));0];
p1=R01'*p0;
value=1;
if x(2)>x(1)
    value = p1(1)
end
isterm=1;
direct=0;

end