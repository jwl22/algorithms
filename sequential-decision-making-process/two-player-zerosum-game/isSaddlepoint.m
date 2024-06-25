close all; clc; clear

cost_matrix = [1 3 3 2; 0 -1 2 1; -2 2 0 1];

u = [max(cost_matrix(1,:)) max(cost_matrix(2,:)) max(cost_matrix(3,:))];
u_star = min(u);
u_idx = find(u==u_star);

cost_matrix = [1 3 3 2; 0 -1 2 1; -2 2 0 1]';

v = [min(cost_matrix(1,:)) min(cost_matrix(2,:)) min(cost_matrix(3,:)) min(cost_matrix(4,:))];
v_star = max(v);
v_idx = find(v==v_star);

cost_matrix = [1 3 3 2; 0 -1 2 1; -2 2 0 1];

issatisfied = 1;
for i=u_idx
    for j=v_idx
        if cost_matrix(i,j) < v_star || cost_matrix(i,j) > u_star
            issatisfied = 0;
        end
    end
end

if issatisfied
    disp("satisfied")
else
    disp("unsatisfied")
end