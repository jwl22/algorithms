close all; clc; clear

disp("Ex 9.14")
cost_matrix = [3 3 5; 1 -1 7; 0 -2 4];

saddle_x = [];
saddle_y = [];
for i=1:length(cost_matrix(:,1)) % row
    for j=1:length(cost_matrix(1,:)) % col
        if max(cost_matrix(i,:)) == cost_matrix(i,j) && min(cost_matrix(:,j)) == cost_matrix(i,j)
            saddle_x = [saddle_x i];
            saddle_y = [saddle_y j];
        end
    end
end
if saddle_x
    for i=1:length(saddle_x)
        disp("(u"+saddle_x(i)+",v"+saddle_y(i)+") is saddle point")
    end
end

disp("Ex 9.15")
cost_matrix = [4 3 5 1 2; -1 0 -2 0 -1; -4 1 4 3 5; -3 0 -1 0 -2; 3 2 -7 3 8];

saddle_x = [];
saddle_y = [];
for i=1:length(cost_matrix(:,1)) % row
    for j=1:length(cost_matrix(1,:)) % col
        if max(cost_matrix(i,:)) == cost_matrix(i,j) && min(cost_matrix(:,j)) == cost_matrix(i,j)
            saddle_x = [saddle_x i];
            saddle_y = [saddle_y j];
        end
    end
end
if saddle_x
    for i=1:length(saddle_x)
        disp("(u"+saddle_x(i)+",v"+saddle_y(i)+") is saddle point")
    end
end