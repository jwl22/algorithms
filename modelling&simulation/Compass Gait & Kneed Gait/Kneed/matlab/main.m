clear; clc; close all
%% Initialization
global mST mT mS mH rFT g IS IT IK theta tspan
mS=0.05; mT=0.5; mH=0.5; mST = mS+mT;
IS = 0; IT = 0; IK = 0; g = 9.81;
rFT = [0, 0, 0]';

global a1 b1 a2 b2 ls lt L
a1=0.375; b1=0.125; a2=0.175; b2=0.325;
ls = a1+b1; lt = a2+b2; L = ls+lt;
tspan = 0:0.01:1;

% Plane Angle and Initial q
theta = 4*pi/180;

% q0 = [qST qTW qSW dqST dqTW dqSW]'
q0 = [0.1967 -0.3363 -0.3363 -1.1498 0.3010 0.3010]';                         % 4도(Success)
% q0 = [0.20112    -0.37482    -0.37482     -1.1605     0.61428     0.61428]';  % 5도(Success)
% q0 = [0.2028 -0.4123 -0.4123 -1.1606 0.9230 0.9230]';                         % 6도(Success)
% q0 = [.2032   -0.4475   -0.4475   -1.1583    1.2050    1.2050]';              % 7도(Success)
% q0 = [0.2028   -0.4820   -0.4820   -1.1630    1.4575    1.4575]';             % 8도(Success)

% If you want to find initial point
%[q0, Jac, err] = find_limit_cycle(q0)
%q0'
%% Simulation
X_cfg = [];
X_wrk = [];
epoch = 100;

for i = 1:epoch
    %% Phase1 : Unlocked Knee Model
    % input : q0 = [qST qTW qSW dqST dqTW dqSW]'
    % output : q = [qST qTW qSW dqST dqTW dqSW]'

    % Fill Your Code
    options=odeset('events',@Event_Kneestrike);
    [t,q] = ode15s(@Dyn_Unlocked_Swing, tspan, q0, options);
    % Finish

    % kinematics
    % output : x = [rFT rST rKT rTT rH rTW rKW rSW rFW]
    X = [];
    for j = 1:length(q(:,1))
        X(j, :,:) = Kinematics([q(j,1), q(j,1), q(j,2), q(j,3)]);
    end
    X_wrk = [X_wrk; X];
    X_cfg = [X_cfg; q(:,[1, 3, 4, 6])];

    %% Phase2 : Knee Strike
    % input : q0 = [qST qTW qSW dqST dqTW dqSW]'
    % output q_ = [dqST dqSW]'

    % Fill Your Code
    q0 = q(end, :);
    q_ = Dyn_Knee_Strike(q0);
    % Finish

    %% Phase3 : Locked Knee Model
    % input : q0 = [qST qSW dqST dqSW]'
    % output : q = [qST qSW dqST dqSW]'

    % Fill Your Code
    q0 = [q(end,1), q(end,3), q_(1), q_(2)]';
    options=odeset('events',@Event_Heelstrike);
    [t,q] = ode15s(@Dyn_Locked_Swing, tspan, q0, options);
    % Finish

    % kinematics
    % output : x = [rFT rST rKT rTT rH rTW rKW rSW rFW]
    X = [];
    for j = 1:length(q(:,1))
        
        X(j, :,:) = Kinematics([q(j,1), q(j,1), q(j,2), q(j,2)]);
    end
    X_wrk = [X_wrk; X];
    X_cfg = [X_cfg; q];

    %% Phase4 : Heel Strike
    % input : q0 = [qST qSW dqST dqSW]'
    % output : dq_plus = [dqST dqSW vFTx vFTy]'

    % Fill Your Code
    q0 = q(end, :);
    dq_plus = Dyn_Heel_Strike(q0);
    % Finish

    
    %% Swap Leg
    % input : q(end,:) = [qST qSW dqST dqSW]'
    % input : dq_ext = [dqST dqSW vCx vCy]'
    % output : q0 = [qSW qST qST dqSW dqST dqST]'

    % Fill Your Code
    q0 = [q(end,2), q(end,1), q(end,1), dq_plus(2), dq_plus(1), dq_plus(1)];
    % Finish

    % x = [rFT rST rKT rTT rH rTW rKW rSW rFW]
    rFT = squeeze(X_wrk(end, end, :));

end

%% Animation
figure();
set(gcf, 'position', [825 41 1093 945]);

subplot(2, 2, 1);
handle_S1 = line(0,0,'Color', [1 0.5 0.5], 'linewidth', 6); hold on;
handle_T1 = line(0,0,'Color', [1 0.5 0.5], 'linewidth', 6);
handle_S2 = line(0,0,'Color', [1 0.5 0.5], 'linewidth', 6);
handle_T2 = line(0,0,'Color', [1 0.5 0.5], 'linewidth', 6);
plane = [cos(theta), -sin(theta); sin(theta), cos(theta)] * [1000, -1000; 0, 0];
handle_plane = line(plane(1,:), -plane(2,:), 'Color', 'k', 'linewidth', 3);
axis([-5 5 -5 5])
xlabel('$X[m]$', 'interpreter','latex')
ylabel('$Y[m]$', 'interpreter','latex')
title('Kneed Walker', 'fontsize', 20, 'interpreter','latex')
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
axis([-1.5 1.5 -2.5 0.5])
xlabel('$\theta_{ST}[rad]$', 'interpreter','latex')
ylabel('$\dot\theta_{ST}[rad/sec]$', 'interpreter','latex')
title('Phase Portrait of $\theta_{ST}$', 'fontsize', 20, 'interpreter','latex')
set(gca, 'fontsize' , 17, 'TickLabelInterpreter','latex')

subplot(2, 2, 4);
handle_line_qSWdqSW = plot(0,0,'Color', [0.4 0.8 0.8], 'linewidth', 2); hold on;
handle_dot_qSWdqSW = plot(0,0,'Color', [0 0.5 0.5], 'linewidth', 2, 'Marker', 'o', 'MarkerFaceColor', [0 0.5 0.5]);
axis([-8 8 -6 12])
xlabel('$\theta_{SW}[rad]$', 'interpreter','latex')
ylabel('$\dot\theta_{SW}[rad/sec]$', 'interpreter','latex')
title('Phase Portrait of $\theta_{SW}$', 'fontsize', 20, 'interpreter','latex')
set(gca, 'fontsize' , 17, 'TickLabelInterpreter','latex')

pause()
t = 0:0.01:length(X_wrk)/100;
for i = 1:length(X_wrk)
    % x = [rFT rST rKT rTT rH rTW rKW rSW rFW]
    x = X_wrk(i,:,:);
    rFT = squeeze(x(1,1,:)); rKT = squeeze(x(1,3,:)); rH = squeeze(x(1,5,:)); rKW = squeeze(x(1,7,:)); rFW = squeeze(x(1,9,:));
    
    % Robot
    subplot(2, 2, 1);
    axis([rH(1)-1 rH(1)+1 rH(2)-1.2 rH(2)+0.8])
    
    % line S1
    x = [rFT(1), rKT(1)]; y = [rFT(2), rKT(2)]; z = [rFT(3), rKT(3)];
    set(handle_S1, 'xdata', x, 'ydata', y, 'zdata', z);
    
    % line T1
    x = [rKT(1), rH(1)]; y = [rKT(2), rH(2)]; z = [rKT(3), rH(3)];
    set(handle_T1, 'xdata', x, 'ydata', y, 'zdata', z);
    
    % line S2
    x = [rH(1), rKW(1)]; y = [rH(2), rKW(2)]; z = [rH(3), rKW(3)];
    set(handle_S2, 'xdata', x, 'ydata', y, 'zdata', z);
    
    % line T1
    x = [rKW(1), rFW(1)]; y = [rKW(2), rFW(2)]; z = [rKW(3), rFW(3)];
    set(handle_T2, 'xdata', x, 'ydata', y, 'zdata', z);
    
    % Phase Portrait
    % X_cfg(i,:) = [qST qSW dqST dqSW]
    subplot(2, 2, 2);
    set(handle_line_dqST, 'xdata', t(1:i),'ydata', X_cfg(1:i,3))
    set(handle_dot_dqST, 'xdata', t(i),'ydata', X_cfg(i,3))
    set(handle_line_dqSW, 'xdata', t(1:i),'ydata', X_cfg(1:i,4))
    set(handle_dot_dqSW, 'xdata', t(i),'ydata', X_cfg(i,4))
    axis([t(i)-1.5 t(i)+1.5 -12 12])
    
    set(handle_line_qSTdqST, 'xdata', X_cfg(1:i,1), 'ydata', X_cfg(1:i,3))
    set(handle_dot_qSTdqST,'xdata', X_cfg(i,1), 'ydata', X_cfg(i,3))
    
    set(handle_line_qSWdqSW, 'xdata', X_cfg(1:i,2), 'ydata', X_cfg(1:i,4))
    set(handle_dot_qSWdqSW,'xdata', X_cfg(i,2), 'ydata', X_cfg(i,4))
    
    pause(0.01);
end