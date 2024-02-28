function X = Kinematics(q)
    global a b rC
    
    qST_list = q(:,1); qSW_list = q(:,2); dqST_list = q(:,3); dqSW_list = q(:,4);
    
    X = zeros(length(qST_list) ,3, 3);
    for i = 1:length(qST_list)
        % q
        % qST qSW dqST dqSW
        qST = qST_list(i);
        qSW = qSW_list(i);
        dqST = dqST_list(i);
        dqSW = dqSW_list(i);
        
        % rotation matrix
        R_qST = Rotation_z(qST);
        R_qSW = Rotation_z(qSW);
        
        % chage of basis 
        R_basis = Rotation_z(pi/2);
        
        % position
        rT = rC + R_basis*R_qST*[a, 0, 0]';
        rH = rC + R_basis*R_qST*[a+b, 0, 0]';
        rE = rH - R_basis*R_qSW*[a+b, 0, 0]';
        rW = rH - R_basis*R_qSW*[b, 0, 0]';
        
        % velocity
        vC = [0, 0, 0]';
        vT = vC + cross([0, 0, dqST], rT)';
        vH = vC + cross([0, 0, dqST], rH)';
        vW = vH + cross([0, 0, dqSW], rW - rH)';
        vE = vH + cross([0, 0, dqSW], rE - rH)';
        
        % x = [rH rE vH vE]'
        x = zeros(3, 3);
        x(1, :) = rC;
        x(2, :) = rH;
        x(3, :) = rE;
        
        X(i,:,:) = x;
    end

end

function R = Rotation_z(theta_z)
R = [cos(theta_z), -sin(theta_z), 0;
     sin(theta_z), cos(theta_z),  0;
     0,            0,             1];
end


