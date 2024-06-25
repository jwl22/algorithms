close all; clc; clear

cost_matrix = [1 -1 0; -1 2 -2; 2 -1 1];
nature_prob = [1/5 1/5 3/5];

[~, P_i] = min(cost_matrix*nature_prob');

disp("Probabilistic Nature Model: u"+P_i)