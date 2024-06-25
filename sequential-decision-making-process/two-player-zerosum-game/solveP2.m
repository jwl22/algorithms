close all; clc; clear

cost_matrix = [1 3 3 2; 0 -1 2 1; -2 2 0 1]';

v = [min(cost_matrix(1,:)) min(cost_matrix(2,:)) min(cost_matrix(3,:)) min(cost_matrix(4,:))];
v_star = max(v);
v_idx = find(v==v_star);

fprintf("v*:")
disp("v"+v_idx)
disp("lower_L*:"+v_star)