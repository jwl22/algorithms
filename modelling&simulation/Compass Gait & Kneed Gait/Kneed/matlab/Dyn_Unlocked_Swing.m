% input : q = [qST qTW qSW dqST dqTW dqSW]
% output : dq = [dqST dqTW dqSW ddqST ddqTW ddqSW]
function dq = Dyn_Unlocked_Swing(t, q)
global a1 b1 a2 b2 mH mS mT g IK lt ls L IS IT
dq=zeros(6,1);
% state
qST=q(1); qTW=q(2); qSW=q(3); dqST=q(4); dqTW=q(5); dqSW=q(6);

% Fill Your Code
% M C G matrix
M = [IK+a1.^2.*mS+(a2+ls).^2.*mT+L.^2.*(mH+mS+mT),(-1).*L.*(lt.*mS+ ...
  b2.*mT).*cos(qST+(-1).*qTW),(-1).*b1.*L.*mS.*cos(qST+(-1) ...
  .*qSW);(-1).*L.*(lt.*mS+b2.*mT).*cos(qST+(-1).*qTW),IT+ ...
  lt.^2.*mS+b2.^2.*mT,b1.*lt.*mS.*cos(qSW+(-1).*qTW);(-1).* ...
  b1.*L.*mS.*cos(qST+(-1).*qSW),b1.*lt.*mS.*cos(qSW+(-1).* ...
  qTW),IS+b1.^2.*mS];

C = [0,(-1).*L.*(lt.*mS+b2.*mT).*sin(qST+(-1).*qTW).*dqTW,(-1).*b1.*L.*mS.*sin(qST+(-1).*qSW).*dqSW;
    L.*(lt.*mS+b2.*mT).*sin(qST+(-1).*qTW).*dqST,0,(-1).*b1.*lt.*mS.*sin(qSW+(-1).*qTW).*dqSW;
    b1.*L.*mS.*sin(qST+(-1).*qSW).*dqST,b1.*lt.*mS.*sin(qSW+(-1).*qTW).*dqTW,0];

G =[(-1).*g.*(a1.*mS+(a2+ls).*mT+L.*(mH+mS+mT)).*sin(qST);
    g.*(lt.*mS+b2.*mT).*sin(qTW);
    b1.*g.*mS.*sin(qSW)];

qdd = M\(-C*[dqST; dqTW; dqSW]-G);
% Finish

dq(1)=q(4);
dq(2)=q(5);
dq(3)=q(6);
dq(4) = qdd(1);
dq(5) = qdd(2);
dq(6) = qdd(3);
end