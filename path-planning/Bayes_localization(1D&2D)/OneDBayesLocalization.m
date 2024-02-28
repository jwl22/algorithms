clear vars; close all; clc;

%% Bayes Filter
sensor_pos = [12 22 32 52 91];
sensor_model = zeros(100);
bel = ones(100,1);
bel = bel/sum(bel);
state = zeros(100);
for i=1:100
    if i+1 <= 100
        state(i+1,i) = 1/3;
    end
    if i+2 <= 100
        state(i+2,i) = 1/3;
    end
    if i+3 <= 100
        state(i+3,i) = 1/3;
    end
end

sensor_pos_model = zeros(1,100);
sensor_model_tmp = Gaussian(1.5);
for i = sensor_pos
    l = i - fix(length(sensor_model_tmp) / 2);
    r = i + fix(length(sensor_model_tmp) / 2);
    idx = 1;
    for j = l:r
        if sensor_pos_model(j) < sensor_model_tmp(idx)
            sensor_pos_model(j) = sensor_model_tmp(idx);
        end
        idx = idx + 1;
    end
end

for i=1:100
    if find(sensor_pos == i)
        sensor_model(i-1,:) = sensor_pos_model;
        sensor_model(i,:) = sensor_pos_model;
        sensor_model(i+1,:) = sensor_pos_model;
    else
        sensor_model(i,:) = 1/length(sensor_model);
    end
end
bel_list = zeros(100);
% x_list = zeros(1,100);
% idx = 1;
for i=1:100
    % x_list(i) = idx;
    bel_list(i,:) = bel';

    if rem(i,2) == 1
        bel = state * bel;
    end
    bel = sensor_model(i,:)' .* bel;
    bel = bel / sum(bel);
    % idx = idx + 2;
    % if idx == 101
    %     break
    % end
end

%% plot
fig1 = figure;
fig1.Position = [1000 50 800 1000];
subplot(3,3,[7,8,9])
x = 1:100;
y = sensor_pos_model(x);
plot(x, y)
xlim([0,100]);
ylim([0,1]);
title('p(z|x)')

cur_x = 1;
count = 0;
xs = [];
real_ys = [];
bayes_ys = [];
while true
    count = count + 1;
    xs = [xs count];
    cur_x = cur_x + ceil(rand*3);
    if cur_x > 100
        cur_x = 100;
    end
    [~,mi] = max(bel_list(cur_x,:));
    real_ys = [real_ys cur_x];
    bayes_ys = [bayes_ys mi];
    subplot(3,3,[1,2])
    cla
    plot(sensor_pos, 0, "o", "Color", "r")
    hold on
    plot(cur_x, 0, "o", "Color","k")
    xlim([0,100]);
    ylim([-0.1,0.1]);
    title(['Real: ' num2str(cur_x)])

    subplot(3,3,3)
    cla
    plot(xs,real_ys,"-", "Color", "b")
    hold on
    plot(xs,bayes_ys,"-", "Color", "r")
    legend({'Real', 'Bayes'}, 'Location','northwest')
    xlim([0,60]);
    ylim([0,100]);

    subplot(3,3,[4,5,6])
    x = 1:100;
    y = bel_list(cur_x,:)';
    plot(x,y)
    xlim([0,100]);
    ylim([0,1]);
    title('Bel')

    pause(0.1)
    if cur_x == 100
        break
    end
end

%% Gaussian distribution
function re = Gaussian(sigma) % sigma = 표준편차
    tmp = zeros(1, 5);
    for i=1:5
        tmp(i) = 1/(sqrt(2*pi)*sigma^2) * exp((-1*(i-1)*(i-1))/(2*sigma*sigma));
    end
    
    tmp = [0 flip(tmp(2:5)) tmp 0];
    re = tmp;
end