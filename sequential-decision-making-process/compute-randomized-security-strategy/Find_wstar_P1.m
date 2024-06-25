close all; clc; clear

cost_matrix = [3 0; -1 1];

syms w1 z1 z2
w = [w1 1-w1];
wA = w*cost_matrix;
z = [z1 z2];
L_dagger = wA .* z;

z1L = subs(L_dagger(1),z1,1);
z2L = subs(L_dagger(2),z2,1);
w1 = double(solve(z1L==z2L, w1));
w2 = double(1-w1);

disp("w*1= "+w1)
disp("w*2= "+w2)
disp("L*="+double(subs(z1L, w1)))
