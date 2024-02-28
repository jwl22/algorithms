close; clear all; clc

particleCount = 2000;

%% Initial space
fig1 = figure;
fig1.Position = [850 100 700 600];

robot = [50 50];
xlim([1,100]);
ylim([1,100]);
hold on

landmarks = [20 10; 25 80; 10 90; 30 60; 40 30; 50 90; 57 70; 69 54; 60 80; 84 90; 91 80; 92 89; 95 57; 80 30; 60 10].';
% landmarks = randi([1,100],2,20);
plot(landmarks(1,:), landmarks(2,:), '.', 'MarkerSize', 20, 'Color','b');

particles = randn(2,particleCount) * sqrt(300) + 50;
particles(particles>100) = 100;
particles(particles<1) = 1;
plot(particles(1,:), particles(2,:), '.', 'Color', 'r')
plot(robot(1), robot(2), '.', 'Color','g','MarkerSize',20);

%% Sensor Gaussian
sensorPosModel = zeros(100,100);
Sigma = [10 0; 0 10];
x1 = 1:100;
x2 = 1:100;
[X1,X2] = meshgrid(x1,x2);
X = [X1(:) X2(:)];
for i=landmarks
    mu = [i(1) i(2)];
    y = mvnpdf(X,mu,Sigma);
    y = reshape(y,100,100);
    sensorPosModel = sensorPosModel + y;
end
weights = zeros(1, particleCount);
for i=1:particleCount
    weights(i) = sensorPosModel(round(particles(2,i)),round(particles(1,i)));
end
weights = weights/sum(weights,'all');

%% Move
isXPositive = 1;
isYPositive = 1;
while true
    randomX = rand()*0.1 * isXPositive;
    randomY = rand()*0.2 * isYPositive;
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
    for i=1:2000
        mvrange = randn(1,1)+1;
        mvrange(mvrange>2) = 2;
        mvrange(mvrange<0) = 0;
        particles(1,i) = particles(1,i) + randomX * mvrange;
        mvrange = randn(1,1)+1;
        mvrange(mvrange>2) = 2;
        mvrange(mvrange<0) = 0;
        particles(2,i) = particles(2,i) + randomY * mvrange;
    end
    particles(particles>100) = 100;
    particles(particles<1) = 1;
    weights = zeros(1, particleCount);
    for i=1:particleCount
        weights(i) = sensorPosModel(round(particles(2,i)),round(particles(1,i)));
    end
    weights = weights/sum(weights,'all');

    flag = 0;
    for i=landmarks
        if norm(i.'-robot) < 5
            flag = 1;
            break
        end
    end
    if flag == 1
        newParticles = [];
        [M,I] = max(weights);
        tmp = 0;
        count = 1;
        while true
            I = I + 1;
            if I > particleCount
                I = 1;
            end
            tmp = tmp + weights(I);
            if tmp > M
                newParticles = [newParticles [particles(1,I), particles(2,I)]'];
                count = count + 1;
                if count > particleCount
                    particles = newParticles;
                    break
                end
                tmp = 0;
            end
        end
    end

    cla
    plot(landmarks(1,:), landmarks(2,:), '.', 'MarkerSize', 20, 'Color','b');
    hold on
    plot(particles(1,:), particles(2,:), '.', 'Color', 'r')
    plot(robot(1), robot(2), '.', 'Color','g','MarkerSize',30);

    drawnow
end
