clear; close all; clc;

global sensor_pos
sensor_pos = [12 22 32 52 91];

cur_gauss = [0, 30];
% bel = Gaussian(cur_gauss(1), cur_gauss(2));
bel = normpdf(1:1:100,cur_gauss(1),cur_gauss(2));
bel = bel/sum(bel);

fig1 = figure;
fig1.Position = [500 50 1000 800];

cur_x = 0;
xs = [];
% ks = [];
sigmas = [];
real_ys = [];
kalman_ys = [];

count = 0;
while true
    rand_x = ceil(rand()*3);
    cur_x = cur_x + rand_x;
    xs = [xs count];
    % if find(sensor_pos == cur_x)
    [new_mean, new_variance] = Kalman(cur_gauss(1), cur_gauss(2), 2, cur_x);
    sigmas = [sigmas new_variance];
    real_ys = [real_ys cur_x];
    kalman_ys = [kalman_ys round(new_mean)];
    % ks = [ks kr];

    cur_gauss = [new_mean, new_variance];
    bel = normpdf(1:1:100,cur_gauss(1),cur_gauss(2));

    subplot(3,3,[4,5,6])
    cla
    plot(1:100, bel)
    xlim([0,100]);
    ylim([0,1]);
    title('Bel')
    % end
    
    if cur_x > 100
        break
    end

    subplot(3,3,[1,2,3])
    cla
    plot(sensor_pos, 0, "o", "Color", "r")
    hold on
    plot(cur_x, 0, "o", "Color","k")
    xlim([0,100]);
    ylim([-0.1,0.1]);
    title(['Real: ' num2str(cur_x)])

    subplot(3,3,[7,8])
    cla
    plot(xs,real_ys,"-", "Color", "b")
    hold on
    plot(xs,kalman_ys,"-", "Color", "r")
    legend({'Real', 'Kalman'}, 'Location','northwest')
    xlim([0,60]);
    ylim([0,100]);

    subplot(3,3,9)
    plot(xs,sigmas,"-", "Color", "g")
    xlim([0,60]);
    ylim([0,50]);
    title('sigma square')

    % subplot(3,3,9)
    % plot(xs,ks,"-", "Color", "b")
    % title('kalman gain')
    % xlim([0,60]);
    % ylim([0,1]);

    drawnow
    pause(0.1)
    count = count + 1;
end

%% Kalman filter
function [mean, variance] = Kalman(x, P, u, z)
    global sensor_pos
    
    A = 1;
    B = 1;
    C = 1;
    % C = Gaussian(0, 2);
     
    R = 2;
    Q = 1;
    
    xp = A*x + B*u;
    Pp = A*P*A' + R;

    if find(sensor_pos == z | sensor_pos == z+1 | sensor_pos == z-1)
        K = Pp*C'/(C*Pp*C' + Q);
        x = xp + K*(z-C*xp);
        P = Pp - K*C*Pp;
    else
        % K = K + 0.01;
        x = xp;
        P = Pp;
    end

    mean = x;
    variance = P;
    % re_k = K;
end

%% Gaussian distribution
% function re = Gaussian(mean, sigma) % sigma = 표준편차
%     size = 100;
%     tmp = zeros(1, size);
%     for i=1:size
%         tmp(i) = 1/(sqrt(2*pi)*sigma^2) * exp((-1*(i-1)*(i-1))/(2*sigma*sigma));
%     end
% 
%     tmp = [0 flip(tmp(2:99)) tmp];
%     tmp = circshift(tmp, ceil(mean-100));
%     tmp  = tmp(1:100);
%     tmp = tmp/sum(tmp);
% 
%     re = tmp;
% end