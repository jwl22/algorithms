clear; close all; clc;

%% Bayes Filter
sensor_pos_x = [1];
sensor_pos_y = [1];
sensor_model = zeros(20,20,20,20);
bel = zeros(20);
% bel = bel/sum(bel,'all');
bel(1,1) = 1;
state = zeros(20,20,20,20); % (x, y) 좌표 , (현재x, 현재y)에서의 2x2행렬
for i=1:20
    for j=1:20
        if i+2 <= 20 && j+1 <= 20
            state(j+1,i+2,j,i) = 1;
        end
        if j+2 <= 20 && i+1 <= 20
            state(j+2,i+1,j,i) = 1;
        end
        if i+2 <= 20 && j+2 <= 20
            state(j+2,i+2,j,i) = 1;
        end
        if j+1 <= 20
            state(j+1,i,j,i) = 1;
        end
        if i+1 <= 20
            state(j,i+1,j,i) = 1;
        end
        state(j,i,j,i) = 1;
        if i+2 <= 20
            state(j,i+2,j,i) = 1;
        end
        if j+2 <= 0
            state(j+2,i,j,i) = 1;
        end
    end
end

sensor_pos_model = zeros(20);

fig1 = figure;
fig1.Position = [300 70 1000 900];
waitforbuttonpress
% subplot(2,3,2)
Sigma = [1 0; 0 1];
x1 = 1:20;
x2 = 1:20;
[X1,X2] = meshgrid(x1,x2);
X = [X1(:) X2(:)];
for i = 1:length(sensor_pos_x)
    mu = [sensor_pos_x(i) sensor_pos_y(i)];
    y = mvnpdf(X,mu,Sigma);
    y = reshape(y,length(x2),length(x1));
    % y = y/length(sensor_pos_x);
    sensor_pos_model = sensor_pos_model + y;
end
sensor_pos_model = sensor_pos_model/(sum(sensor_pos_model,'all')*2);
% surf(x1,x2,sensor_pos_model)
% axis([1 20 1 20 0 0.1])
% title('p(z|x)')

% subplot(2,3,5)
% surf(x1,x2,sensor_pos_model)
% axis([1 20 1 20 0 0.1])
% title('p(z|x) - vertical')
% view(2)

for i=1:20
    i_y = find(sensor_pos_y == i);
    for j=1:20
        i_x = find(sensor_pos_x == j);
        if i_y == i_x
            sensor_model(:,:,1,i) = sensor_pos_model;
            sensor_model(:,:,j,1) = sensor_pos_model;
            sensor_model(:,:,1,1) = sensor_pos_model;
            sensor_model(:,:,j,i) = sensor_pos_model;
            % sensor_model(:,:,j+1,i) = sensor_pos_model;
            % sensor_model(:,:,j,i+1) = sensor_pos_model;
            % sensor_model(:,:,j+1,i+1) = sensor_pos_model;
        else
            sensor_model(:,:,j,i) = 1/(20*20);
        end
    end
    
end
bel_list = zeros(20,20,20,20); % 현재 x확률, y확률, 현재 위치x, 위치y
% x_list = zeros(1,100);

% for i=1:20
%     tmp = bel;
%     for j=1:20
%         bel_list(:,:,j,i) = bel;
%         bel(j,:) = state(:,:,j,i) * bel(j,:)';
%         % bel(j,:) = sensor_model(:,i,j,i)' .* bel(j,:);
%         bel = sensor_model(:,:,j,i) .* bel;
%         bel = bel / sum(bel, 'all');
%     end
%     bel = tmp;
%     bel_list(:,:,1,i) = bel;
%     bel(:,i) = state(:,:,1,i) * bel(:,i);
%     % bel(:,i) = sensor_model(1,:,1,i)' .* bel(:,i);
%     bel = sensor_model(:,:,1,i) .* bel;
%     bel = bel / sum(bel, 'all');
% end

%% plot
cur_x = 1;
cur_y = 1;
real_xs = [];
real_ys = [];
bayes_xs = [];
bayes_ys = [];
while true
    if cur_x > 20
        cur_x = 20;
    end
    if cur_y > 20
        cur_y = 20;
    end
    % randx = round(rand);
    % randy = round(rand);
    randx = 1;
    randy = 1;
    % while randx == 0 && randy == 0
    %     randx = round(rand);
    %     randy = round(rand);
    % end
    % [v1,mi1] = max(bel_list(:,:,cur_x,cur_y));
    [v1,mi1] = max(bel);
    [v2,mi2] = max(v1);
    real_xs = [real_xs cur_x];
    real_ys = [real_ys cur_y];
    bayes_xs = [bayes_xs mi1(mi2)];
    bayes_ys = [bayes_ys mi2];
    subplot(2,2,1)
    % pos1 = [0.05 0.35 0.3 0.3];
    % subplot('Position',pos1)
    axis square
    grid on
    cla
    plot(cur_x, cur_y, "o", "Color", "k", "LineWidth",3)
    hold on
    % for i=1:length(sensor_pos_x)
    %     plot(sensor_pos_x(i), sensor_pos_y(i), "o", "Color","r","LineWidth",1)
    % end
    xlim([0,20]);
    ylim([0,20]);
    title('Real')

    subplot(2,2,2)
    x = 1:20;
    y = bel';
    surf(x1,x2,y)
    axis([1 20 1 20 0 2])
    title('Bel')

    subplot(2,2,4)
    x = 1:20;
    y = bel';
    surf(x1,x2,y)
    axis([1 20 1 20 0 1])
    title('Bel - vertical')
    view(2)

    % subplot(2,3,4)
    % plot(real_xs,real_ys,"-", "Color", "b","LineWidth",1)
    % hold on
    % plot(bayes_xs,bayes_ys,"-", "Color", "r","LineWidth",1)
    % legend({'Real', 'Bayes'}, 'Location','northwest')
    % xlim([0,20]);
    % ylim([0,20]);
    drawnow
    
    % bel(cur_x,:) = state(:,:,cur_x,cur_y) * bel(cur_x,:)';
    % bel(:,cur_y) = state(:,:,cur_x,cur_y) * bel(:,cur_y);

    % for i=1:20
    %     for j=1:20
    %         bel(cur_x,:) = state(:,:,i,j) * bel(cur_x,:)';
    %         bel(:,cur_y) = state(:,:,i,j) * bel(:,cur_y);
    %     end
    % end
    tmp = zeros(20,20);
    % if randx == 1 && randy == 1
    %     tmp(2:end,2:end) = bel(1:end-1,1:end-1);
    % elseif randx == 1
    %     tmp(2:end,1:end) = bel(1:end-1,1:end);
    % elseif randy == 1
    %     tmp(1:end,2:end) = bel(1:end,1:end-1);
    % end
    for i=1:20
        for j=1:20
            if bel(i,j) ~= 0
                if j+1 <= 20
                    tmp(i,j+1) = 1;
                end
                if  i+1 <= 20
                    tmp(i+1,j) = 1;
                end
                tmp(i,j) = 1;
                if i+2 <= 20
                    tmp(i+2,j) = 1;
                end
                if j+2 <= 20
                    tmp(i,j+2) = 1;
                end
                if i+2 <= 20 && j+2 <= 20
                    tmp(i+2,j+2) = 1;
                end
                if i+2 <= 20 && j+1 <= 20
                    tmp(i+2,j+1) = 1;
                end
                if j+2 <= 20 && i+1 <= 20
                    tmp(i+1,j+2) = 1;
                end
            end
            % if i+1 <= 20 && j+1 <= 20
            %     tmp(i+1,j+1) = tmp(i+1,j+1) + bel(i,j) * 1/3;
            % end
            % if i+1 <= 20
            %     tmp(i+1,j) = tmp(i+1,j) + bel(i,j) * 1/3;
            % end
            % if j+1 <= 20
            %     tmp(i,j+1) = tmp(i,j+1) + bel(i,j) * 1/3;
            % end
        end
    end
    % tmp = tmp/sum(tmp,'all');
    bel = tmp;

    % bel = sensor_model(:,:,cur_x,cur_y)' .* bel;
    % bel = bel / sum(bel, 'all');
    % for i=1:20
    %     for j=1:20
    %         bel_list(:,:,j,i) = bel;
    %         bel(j,:) = state(:,:,j,i) * bel(j,:)';
    %         % bel(j,:) = sensor_model(:,i,j,i)' .* bel(j,:);
    %         bel = sensor_model(:,:,j,i) .* bel;
    %         bel = bel / sum(bel, 'all');
    %     end
    %     bel_list(:,:,1,i) = bel;
    %     bel(:,i) = state(:,:,1,i) * bel(:,i);
    %     % bel(:,i) = sensor_model(1,:,1,i)' .* bel(:,i);
    %     bel = sensor_model(:,:,1,i) .* bel;
    %     bel = bel / sum(bel, 'all');
    % end

    pause(0.1)
    if cur_x == 20 || cur_y == 20
        break
    end

    cur_x = cur_x + randx;
    cur_y = cur_y + randy;
end