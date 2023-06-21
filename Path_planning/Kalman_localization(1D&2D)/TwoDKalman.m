clear vars; close all; clc;

global sensor_pos_x sensor_pos_y
sensor_pos_x = [8 5 6 10 12 13 15 20 23 27];
sensor_pos_y = [4 5 11 9 14 10 20 19 21 28];

cur_gauss = [[0, 0], 15];
mu = [0 0];
Sigma = [15 0; 0 15];
x1 = 1:30;
x2 = 1:30;
[X1,X2] = meshgrid(x1,x2);
X = [X1(:) X2(:)];
bel = mvnpdf(X,mu,Sigma);
bel = reshape(bel,length(x2),length(x1));
bel = bel/sum(bel,'all');

fig1 = figure;
fig1.Position = [500 50 1000 650];

cur_x = 0;
cur_y = 0;
xs = [];
ys = [];
% ks = [];
sigmas = [];
kalman_xs = [];
kalman_ys = [];

count = 0;
while true
    rand_x = round(rand());
    rand_y = round(rand());
    while rand_x == 0 && rand_y == 0
        rand_x = round(rand());
        rand_y = round(rand());
    end
    cur_x = cur_x + rand_x;
    cur_y = cur_y + rand_y;
    if cur_x > 30 || cur_y > 30
        break
    end
    xs = [xs cur_x];
    ys = [ys cur_y];
    
    [new_mean, new_variance] = Kalman(cur_gauss(1:2), cur_gauss(3), [1 1], [cur_x cur_y]);
    sigmas = [sigmas new_variance];
    kalman_xs = [kalman_xs round(new_mean(1))];
    kalman_ys = [kalman_ys round(new_mean(2))];
    % ks = [ks kr];

    cur_gauss = [new_mean, new_variance];
    mu = [new_mean(1), new_mean(2)];
    Sigma = [new_variance 0; 0 new_variance];
    X = [X1(:) X2(:)];
    bel = mvnpdf(X,mu,Sigma);
    bel = reshape(bel,length(x2),length(x1));
    bel = bel/sum(bel,'all');

    %%plot
    subplot(2,3,2)
    surf(x1,x2,bel)
    axis([1 30 1 30 0 1])
    title('Bel')

    subplot(2,3,5)
    surf(x1,x2,bel)
    axis([1 30 1 30 0 1])
    view(2)
    title('Bel')
    
    subplot(2,3,1)
    axis square
    grid on
    cla
    plot(cur_x, cur_y, "o", "Color", "k", "LineWidth",3)
    hold on
    for i=1:length(sensor_pos_x)
        plot(sensor_pos_x(i), sensor_pos_y(i), "o", "Color","r","LineWidth",1)
    end
    xlim([0,30]);
    ylim([0,30]);
    title('Real')

    subplot(2,3,4)
    plot(xs,ys,"-", "Color", "b","LineWidth",1)
    hold on
    plot(kalman_xs,kalman_ys,"-", "Color", "r","LineWidth",1)
    legend({'Real', 'Kalman'}, 'Location','northwest')
    xlim([0,30]);
    ylim([0,30]);

    subplot(2,3,[3,6])
    axis square
    hold on
    plot(xs,sigmas,"-", "Color", "g")
    xlim([0,40]);
    ylim([0,50]);
    title('sigma square')
    
    drawnow
    pause(0.1)
    count = count + 1;
end

%% Kalman filter
function [mean, variance] = Kalman(x, P, u, z)
    global sensor_pos_x sensor_pos_y
    
    A = 1;
    B = 1;
    C = 1;
    % C = Gaussian(0, 2);
     
    R = 2;
    Q = 1;
    
    xp = A*x + B*u;
    Pp = A*P*A' + R;

    if find(((sensor_pos_x == z(1) & (sensor_pos_y == z(2)) |  sensor_pos_y == z(2)-1)) | (sensor_pos_x == z(1)-1 & (sensor_pos_y == z(2) | sensor_pos_y == z(2)-1)))
        K = Pp*C'/(C*Pp*C' + Q);
        x = xp + K*(z-C*xp);
        P = Pp - K*C*Pp;
    else
        x = xp;
        P = Pp;
    end

    mean = x;
    variance = P;
    % re_k = K;
end