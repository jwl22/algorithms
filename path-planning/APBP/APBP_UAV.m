clear vars; close all; clc;

start_points = [4,2,-5 ; 1, 3,-5; 1, 1, -5];
end_points = [11,11,3; 8, 12, 3; 8, 10, 3];
obstacles = [5,6,0; 5,7,0; 5,8,0];

k_att = 1;
k_rep = 20;
pot_field = 3;
roll = 0; pitch=0; yaw=0;

p1 = start_points(1,:);
p2 = start_points(2,:);
p3 = start_points(3,:);
ps = [p1; p2; p3];
cur_pos = mean(start_points);
end_pos = mean(end_points);

f1 = figure;
camera1 = [-45,0,90,0];
camera2 = [30,0,0,90];
while 1
    %% plot
    for i=1:4
        subplot(2,2,i)
        view(camera1(i), camera2(i))
        xlim([0,12]);
        ylim([0,12]);
        zlim([-6,6]);
        xlabel('X');
        ylabel('Y');
        zlabel('Z');
        cla;
        hold on
        grid on;
        plot3(obstacles(:,1), obstacles(:,2),obstacles(:,3), 'mo', 'MarkerSize', 5, 'LineWidth', 1);
        fill3(ps(:,1).', ps(:,2).',ps(:,3).', 'r');
        fill3(end_points(:,1).', end_points(:,2).',end_points(:,3).', 'b');
    end
    %% func
    obs_grad = [0;0;0];

    for i = 1:size(obstacles,1)
        obs_pos = obstacles(i,:);
        r1 = (p1 - obs_pos).';
        r2 = (p2 - obs_pos).';
        r3 = (p3 - obs_pos).';
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

    syms x y z theta1 theta2 theta3
    H01 = [
    [cos(theta1)*cos(theta2), cos(theta1)*sin(theta2)*sin(theta3) - cos(theta3)*sin(theta1), sin(theta1)*sin(theta3) + cos(theta1)*cos(theta3)*sin(theta2), x]
    [cos(theta2)*sin(theta1), cos(theta1)*cos(theta3) + sin(theta1)*sin(theta2)*sin(theta3), cos(theta3)*sin(theta1)*sin(theta2) - cos(theta1)*sin(theta3), y]
    [           -sin(theta2),                                       cos(theta2)*sin(theta3),                                       cos(theta2)*cos(theta3), z]
    [                      0,                                                             0,                                                             0, 1]
    ];
    P1 = [p1.'-cur_pos.' p2.'-cur_pos.' p3.'-cur_pos.';
        [1 1 1]];
%     P1 = H01(:,4);
    P0 = H01 * P1;
    P0 = P0(1:3).';
    P0jacobi = jacobian(P0, [x,y,z,theta1,theta2,theta3]);

    p0jacobi = double(subs(P0jacobi, [x,y,z,theta1,theta2,theta3], [cur_pos(1),cur_pos(2),cur_pos(3),roll,pitch,yaw])).';
%     p0grad = (obs_grad + k_att * [end_pos(1)-cur_pos(1); end_pos(2)-cur_pos(2); end_pos(3)-cur_pos(3)]) * 0.01;
    
    p1jacobi = double(subs(P0jacobi, [x,y,z,theta1,theta2,theta3], [p1(1),p1(2),p1(3),roll,pitch,yaw])).';
    p1grad = (obs_grad  + k_att * [end_points(1,1)-p1(1); end_points(1,2)-p1(2); end_points(1,3)-p1(3)]) * 0.01;
    p2jacobi = double(subs(P0jacobi, [x,y,z,theta1,theta2,theta3], [p2(1),p2(2),p2(3),roll,pitch,yaw])).';
    p2grad = (obs_grad  + k_att * [end_points(2,1)-p2(1); end_points(2,2)-p2(2); end_points(2,3)-p2(3)]) * 0.01;
    p3jacobi = double(subs(P0jacobi, [x,y,z,theta1,theta2,theta3], [p3(1),p3(2),p3(3),roll,pitch,yaw])).';
    p3grad = (obs_grad  + k_att * [end_points(3,1)-p3(1); end_points(3,2)-p3(2); end_points(3,3)-p3(3)]) * 0.01;
    
    f = (p1jacobi*p1grad + p2jacobi*p2grad + p3jacobi*p3grad);
%     f = p0jacobi * (p1grad + p2grad + p3grad);
%     f0 = p0jacobi*p0grad;
%     f1 = p1jacobi*p1grad;
%     f2 = p2jacobi*p2grad;
%     f3 = p3jacobi*p3grad;
    cur_pos = cur_pos + f(1:3).';
    rd = f(4);
    pd = f(5);
    yd = f(6);
    roll = roll + rd;
    pitch = pitch + pd;
    yaw = yaw + yd;

    ps_center = ps - mean(ps);
    Rx = [1 0 0; 0 cos(rd) -sin(rd); 0 sin(rd) cos(rd)];
    Ry = [cos(pd) 0 sin(pd); 0 1 0; -sin(pd) 0 cos(pd)];
    Rz = [cos(yd) -sin(yd) 0; sin(yd) cos(yd) 0; 0 0 1];
    R = Rz * Ry * Rx;
    ps = (R * ps_center.').';
    ps = ps + cur_pos;
    p1 = ps(1,:);
    p2 = ps(2,:);
    p3 = ps(3,:);

    if norm(end_points(1,:)-p1) < 0.3 && norm(end_points(2,:)-p2) < 0.3 && norm(end_points(3,:)-p3) < 0.3
        break;
    end
    
    drawnow;
end

