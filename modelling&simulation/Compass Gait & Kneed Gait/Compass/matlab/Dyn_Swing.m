function dx = Dyn_Swing(t, x)
% x
% qST qSW qST' qSW'
global a b mH mS g IST ISW
dx=zeros(4,1);
qST = x(1); qSW = x(2); dqST = x(3); dqSW = x(4);

% IST zero version
%%%%%% Fill Your Code
M = [IST+(a+b).^2.*mH+(2.*a.^2+2.*a.*b+b.^2).*mS, (-1).*b.*(a+b).*mS.*cos(qST+(-1).*qSW);
    (-1).*b.*(a+b).*mS.*cos(qST+(-1).*qSW), ISW+b.^2.*mS];

C = [0,(-1).*b.*(a+b).*mS.*sin(qST+(-1).*qSW).*dqSW;
    b.*(a+b).*mS.*sin(qST+(-1).*qSW).*dqST,0];
 
G = [(-1).*g.*(b.*(mH+mS)+a.*(mH+2.*mS)).*sin(qST);
    b.*g.*mS.*sin(qSW)];

tau = [0; 0];
qdd = M\(tau-C*[dqST; dqSW]-G);
%%%%%% Finish                

dx(1) = x(3);
dx(2) = x(4);
dx(3) = qdd(1);
dx(4) = qdd(2);
end