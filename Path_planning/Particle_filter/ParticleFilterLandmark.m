close; clear all; clc

particleCount = 1000;
landmarks_count = 7;

%% Initial space
fig1 = figure;
fig1.Position = [850 100 700 600];

robot = [50 50];
xlim([1,100]);
ylim([1,100]);
hold on

landmarks = [10 90; 20 20; 80 85; 90 10; 60 70; 30 50; 60 30];
% landmarks = randi([1,100],2,20);
plot(landmarks(1,:), landmarks(2,:), '.', 'MarkerSize', 20, 'Color','k');

particles = rand(landmarks_count*2,particleCount)*99+1;
for i=1:2:landmarks_count*2
    plot(particles(i,:), particles(i+1,:), '.', 'Color', 'r')
end
tmp = mean(particles,2);
estimates = [];
for i=1:landmarks_count
    estimates = [estimates ; tmp(i) tmp(i+1)];
end
estimates = estimates.';
plot(estimates(1,:), estimates(2,:),'O', 'Color','g','MarkerSize',20, 'LineWidth',3)
plot(robot(1), robot(2), '.', 'Color','b','MarkerSize',30);

%% Move
isXPositive = 1;
isYPositive = 1;
while true
    randomX = rand()*0.3 * isXPositive;
    randomY = rand()*0.6 * isYPositive;
    while randomX == 0 && randomY == 0
        randomX = rand()*0.1 * isXPositive;
        randomY = rand()*0.2 * isYPositive;
    end
    robot(1) = robot(1) + randomX;
    robot(2) = robot(2) + randomY;
    if robot(1) > 100
        robot(1) = 100;
        isXPositive = -1;
    elseif robot(1) < 1
        robot(1) = 1;
        isXPositive = 1;
    end
    if robot(2) > 100
        robot(2) = 100;
        isYPositive = -1;
    elseif robot(2) < 1
        robot(2) = 1;
        isYPositive = 1;
    end

    weights = zeros(landmarks_count, particleCount);
    for i=1:landmarks_count
        if norm(robot-landmarks(i,:)) < 20
            gauss = normpdf(0:0.1:2*norm(robot-landmarks(i,:)),norm(robot-landmarks(i,:)),norm(robot-landmarks(i,:))/20);
            for j=1:particleCount
                % if norm(robot-landmarks(i,:)) < norm([particles(2*i-1,j) particles(2*i,j)] - robot)
                %     weights(i,j) = (norm(robot-landmarks(i,:)) / norm([particles(2*i-1,j) particles(2*i,j)] - robot))^3;
                % else
                %     weights(i,j) = (norm([particles(2*i-1,j) particles(2*i,j)] - robot) / norm(robot-landmarks(i,:)))^3;
                % end
                if norm([particles(2*i-1,j) particles(2*i,j)] - robot) > 2*norm(robot-landmarks(i,:))
                    weights(i,j) = 0.00000000000001;
                else
                    tmp = round(norm([particles(2*i-1,j) particles(2*i,j)] - robot),1)*10;
                    if tmp == 0
                        weights(i,j) = gauss(1);
                    else
                        weights(i,j) = gauss(round(norm([particles(2*i-1,j) particles(2*i,j)] - robot),1) * 10);
                    end
                end
            end
            weights(i,:) = weights(i,:)/sum(weights(i,:),"all");

            newParticles1 = [];
            newParticles2 = [];
            [M,I] = max(weights(i,:));
            count = 0;
            tmp = 0;
            while true
                I = I+1;
                if I > particleCount
                    I = 1;
                end
                tmp = tmp + weights(i,I);
                if tmp > M
                    newParticles1 = [newParticles1 particles(2*i-1,I)+randn(1,1)*0.3];
                    newParticles2 = [newParticles2 particles(2*i,I)+randn(1,1)*0.3];
                    count = count + 1;
                    if count >= particleCount
                        particles(2*i-1,:) = newParticles1;
                        particles(2*i,:) = newParticles2;
                        break
                    end
                    tmp = 0;
                end
            end
        end
    end
    particles(particles>100) = 100;
    particles(particles<1) = 1;
    

    %% plot
    cla
    for i=1:2:landmarks_count*2
        plot(particles(i,:), particles(i+1,:), '.', 'Color', 'r')
    end
    landmarkst = landmarks.';
    tmp = mean(particles,2);
    estimates = [];
    for i=1:2:landmarks_count*2
        estimates = [estimates ; tmp(i) tmp(i+1)];
    end
    estimates = estimates.';
    plot(estimates(1,:), estimates(2,:),'O', 'Color','g','MarkerSize',20, 'LineWidth',3)
    plot(landmarkst(1,:), landmarkst(2,:), '.', 'MarkerSize', 20, 'Color','k');
    plot(robot(1), robot(2), '.', 'Color','b','MarkerSize',30);

    drawnow
end
