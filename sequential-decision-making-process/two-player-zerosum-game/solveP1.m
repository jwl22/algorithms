close all; clc; clear

cost_matrix = [1 3 3 2; 0 -1 2 1; -2 2 0 1];

u = [max(cost_matrix(1,:)) max(cost_matrix(2,:)) max(cost_matrix(3,:))];
u_star = min(u);
u_idx = find(u==u_star);

fprintf("u*:")
disp("u"+u_idx)
disp("upper_L*:"+u_star)