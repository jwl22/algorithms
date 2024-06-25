close all; clc; clear

cost_matrix = [1 -1 0; -1 2 -2; 2 -1 1];
nature_prob = [1/5 1/5 3/5];

T = zeros(3,3);
for j=1:3
    for i=1:3
        T(i,j) = max(cost_matrix(i,j)-cost_matrix(:,j));
    end
end

[~, ND_i] = min([max(T(1,:)) max(T(2,:)) max(T(3,:))]);

disp("Non-Deterministic Nature Model(regret): u"+ND_i)