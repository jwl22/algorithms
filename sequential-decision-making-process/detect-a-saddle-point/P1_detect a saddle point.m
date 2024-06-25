close all; clc; clear

cost_matrix = [3 3 5; 1 -1 7; 0 -2 4];

u = [max(cost_matrix(1,:)) max(cost_matrix(2,:)) max(cost_matrix(3,:))];
u_star = min(u);
u_star_idx = find(u==u_star);

cost_matrix_v = cost_matrix';
v = [min(cost_matrix_v(1,:)) min(cost_matrix_v(2,:)) min(cost_matrix_v(3,:))];
v_star = max(v);
v_star_idx = find(v==v_star);

disp("Ex 9.14")
if u_star == v_star
    disp("(u"+u_star_idx+",v"+v_star_idx+") is saddle point")
else
    disp("(u"+u_star_idx+",v"+v_star_idx+") is not saddle point")
end

cost_matrix = [4 3 5 1 2; -1 0 -2 0 -1; -4 1 4 3 5; -3 0 -1 0 -2; 3 2 -7 3 8];

u = [max(cost_matrix(1,:)) max(cost_matrix(2,:)) max(cost_matrix(3,:)) max(cost_matrix(4,:)) max(cost_matrix(5,:))];
u_star = min(u);
u_star_idx = find(u==u_star);

cost_matrix_v = cost_matrix';
v = [min(cost_matrix_v(1,:)) min(cost_matrix_v(2,:)) min(cost_matrix_v(3,:)) min(cost_matrix_v(4,:)) min(cost_matrix_v(5,:))];
v_star = max(v);
v_star_idx = find(v==v_star);

disp("Ex 9.15")
for i=u_star_idx
    for j=v_star_idx
        if u_star == v_star
            disp("(u"+i+",v"+j+") is saddle point")
        else
            disp("(u"+i+",v"+j+") is not saddle point")
        end
    end
end