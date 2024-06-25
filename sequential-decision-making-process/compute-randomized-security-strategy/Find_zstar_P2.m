close all; clc; clear

cost_matrix = [3 0; -1 1];

syms z1 w1 w2
z = [z1 1-z1];
wA = z*cost_matrix';
z = [w1 w2];
L_dagger = wA .* z;

z1L = subs(L_dagger(1),w1,1);
z2L = subs(L_dagger(2),w2,1);
z1 = double(solve(z1L==z2L, z1));
z2 = double(1-z1);

disp("z*1= "+z1)
disp("z*2= "+z2)
disp("L*="+double(subs(z1L, z1)))
