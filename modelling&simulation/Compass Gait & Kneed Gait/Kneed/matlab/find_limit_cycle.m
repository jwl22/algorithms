function [x0,Jac,err]=find_limit_cycle(x0) 
% study Poincare map right after impact
% [t,x,qd_e,x0]=perform_onestep(x0);
err=ones(size(x0));
one_step(x0);
options=optimset('LargeScale','on','Display','off', 'MaxFunEvals', 500, 'MaxIter', 100);
lr = 1;
while norm(err)>0.0001
    Jac=jacobianest(@one_step,x0);
    dx= - inv(Jac - eye(6))*(one_step(x0) - x0);

    % Learning Rate Update
    [lr, err] = fmincon(@(lr) CostFun(lr, x0, dx), lr, [], [], [], [], 1e-9, 10, @NONLCON, options);
    %[lr, err] = fmincon(@(lr) CostFun(lr, x0, dx), 0.01, [], [], [], [], 1e-9, 1, @NONLCON);

    % Update
    x0 = x0 + lr*dx;
    disp(['Error : ', num2str(err), ' // Learning Rate : ', num2str(lr), ' // x0 : [', num2str(x0'), ']'])
end
end

function err = CostFun(lr, x0, dx)
    x0 = x0 + lr*dx;
    Jac = jacobianest(@one_step,x0);
    err = norm(- inv(Jac - eye(6))*(one_step(x0) - x0));
end

function [g,h]=NONLCON(W,~,~)
% inequality constraints
g=[];
% equality constraints
h=[];
end