% input : q = [qST qTT qTW qSW]
% output : x = [rFT rST rKT rTT rH rTW rKW rSW rFW]
function x = Kinematics(q)
global a1 b1 a2 b2 rFT

% configuration
qST = q(1);
qTT = q(2);
qTW = q(3);
qSW = q(4);

% rotation matrix
R_qST = Rotation_z(qST);
R_qTW = Rotation_z(qTW);
R_qSW = Rotation_z(qSW);

% chage of basis 
R_basis = Rotation_z(pi/2);

% position
rFT = rFT;
rST = rFT + R_basis*R_qST*[a1, 0, 0]';
rKT = rFT + R_basis*R_qST*[a1+b1, 0, 0]';
rTT = rFT + R_basis*R_qST*[a1+b1+a2, 0, 0]';
rH = rFT + R_basis*R_qST*[a1+b1+a2+b2, 0, 0]';
rTW = rH - R_basis*R_qTW*[b2, 0, 0]';
rKW = rH - R_basis*R_qTW*[a2+b2, 0, 0]';
rSW = rKW - R_basis*R_qSW*[b1, 0, 0]';
rFW = rKW - R_basis*R_qSW*[a1+b1, 0, 0]';

% Kinematics
x = [rFT rST rKT rTT rH rTW rKW rSW rFW]';
end

function R = Rotation_z(theta_z)
R = [cos(theta_z), -sin(theta_z), 0;
     sin(theta_z), cos(theta_z),  0;
     0,            0,             1];
end



