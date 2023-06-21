clear vars; close all; clc;

start_points = [0, 0; 2, 0; 2, 1];
end_points = [9, 8; 9, 10; 8, 10];
obstacles = [4,6; 6,6; 4,8];

k_att = 1;
k_rep = 1;
pot_field = 2;

f1 = figure;
hold on;
axis equal;
xlim([0,11]);
ylim([0,13]);
grid on;

L1 = 2; L2 = 1;
theta1=0; theta2=pi/2;
p1 = start_points(1,:);
p2 = start_points(2,:);
p3 = start_points(3,:);
while 1
    cla;
    plot(start_points(:,1), start_points(:,2), 'ro', 'MarkerSize', 5, 'LineWidth', 1);
    plot(end_points(:,1), end_points(:,2), 'bo', 'MarkerSize', 5, 'LineWidth', 1);
    plot(obstacles(:,1), obstacles(:,2), 'mo', 'MarkerSize', 5, 'LineWidth', 1);

%     syms x y theta theta2
%     p1jacobi = jacobian([x,y],[x;y;theta])'
    p1jacobi = [[1, 0]
    [0, 1]
    [0, 0]];
%     p2jacobi = jacobian([x+L1*cos(theta) , y+L1*sin(theta)],[x;y;theta]).'
    p2jacobi = [[            1,            0]
    [            0,            1]
    [-2*sin(theta1), 2*cos(theta1)]];
%     p3jacobi = jacobian([x+L1*cos(theta) + L2*cos(theta+theta2), y+L1*sin(theta) + L2*sin(theta+theta2)],[x;y;theta]).'
    p3jacobi = [[                                 1,                                0]
    [                                 0,                                1]
    [- 2*sin(theta1) - sin(theta1 + pi/2), 2*cos(theta1) + cos(theta1 + pi/2)]];

    p1grad = [0;0];
    p2grad = [0;0];
    p3grad = [0;0];
    obs_grad = [0;0];

    for i = 1:size(obstacles,1)
        obs_pos = obstacles(i,:);
        r1 = (p1 - obs_pos)';
        r2 = (p2 - obs_pos)';
        r3 = (p3 - obs_pos)';
        d1 = norm(r1);
        d2 = norm(r2);
        d3 = norm(r3);
        if d1 < pot_field
            obs_grad = obs_grad + k_rep * (1/d1 - 1/pot_field) * (1/d1^2) * r1;
        end
        if d2 < pot_field
            obs_grad = obs_grad + k_rep * (1/d2 - 1/pot_field) * (1/d2^2) * r2;
        end
        if d3 < pot_field
            obs_grad = obs_grad + k_rep * (1/d3 - 1/pot_field) * (1/d3^2) * r3;
        end
    end

    p1grad = obs_grad  + k_att * ([end_points(1,1)-p1(1); end_points(1,2)-p1(2)]) * 0.005;
    p2grad = obs_grad  + k_att * ([end_points(2,1)-p2(1); end_points(2,2)-p2(2)]) * 0.005;
    p3grad = obs_grad  + k_att * ([end_points(3,1)-p3(1); end_points(3,2)-p3(2)]) * 0.005;

    f = p1jacobi*p1grad + p2jacobi*p2grad + p3jacobi*p3grad;
    p1 = p1 + f(1:2)';
    theta1 = theta1 + f(3);
    p2 = [p1(1)+L1*cos(theta1) , p1(2)+L1*sin(theta1)];
    p3 = [p2(1)+L2*cos(theta1+theta2), p2(2)+L2*sin(theta1+theta2)];
    cur_points = [p1;p2;p3];
    plot(cur_points(:,1),cur_points(:,2), 'ko', 'MarkerSize', 5, 'LineWidth', 1);
   
    if norm(end_points(1,:)-p1) < 0.1 && norm(end_points(2,:)-p2) < 0.1 && norm(end_points(3,:)-p3) < 0.1
        break;
    end

    drawnow;
end
