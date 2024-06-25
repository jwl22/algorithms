close all; clc; clear

cost_matrix = [1 -1 0; -1 2 -2; 2 -1 1];
nature_prob = [1/5 1/5 3/5];

[~, ND_i] = min([max(cost_matrix(1,:)) max(cost_matrix(2,:)) max(cost_matrix(3,:))]);

disp("Non-Deterministic Nature Model: u"+ND_i)