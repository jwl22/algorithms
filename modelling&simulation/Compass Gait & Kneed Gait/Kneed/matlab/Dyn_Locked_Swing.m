% input : q = [qST qSW dqST dqSW]
% output : dq = [dqST dqSW ddqST ddqSW]
function dq = Dyn_Locked_Swing(t, q)
global a1 b1 a2 b2 mH mS mT g IK ls lt L IS
dq=zeros(4,1);
% state
qST=q(1); qSW=q(2); dqST=q(3); dqSW=q(4);

% Fill Your Code
% M C G matrix
M = [IK+a1.^2.*mS+(a2+ls).^2.*mT+L.^2.*(mH+mS+mT),(-1).*L.*((b1+lt).* ...
  mS+b2.*mT).*cos(qST+(-1).*qSW);(-1).*L.*((b1+lt).*mS+b2.*mT) ...
  .*cos(qST+(-1).*qSW),IK+(b1+lt).^2.*mS+b2.^2.*mT];

C = [0,(-1).*L.*((b1+lt).*mS+b2.*mT).*sin(qST+(-1).*qSW).* ...
  dqSW;L.*((b1+lt).*mS+b2.*mT).*sin(qST+(-1).* ...
  qSW).*dqST,0];

G = [(-1).*g.*(a1.*mS+(a2+ls).*mT+L.*(mH+mS+mT)).*sin(qST); g.*((b1+ ...
  lt).*mS+b2.*mT).*sin(qSW)];

qdd = M\(-C*[dqST; dqSW]-G);
% Finish

dq(1)=q(3);
dq(2)=q(4);
dq(3) = qdd(1);
dq(4) = qdd(2);
end