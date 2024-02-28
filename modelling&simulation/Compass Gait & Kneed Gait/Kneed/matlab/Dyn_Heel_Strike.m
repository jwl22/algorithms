function dq_plus = Dyn_Heel_Strike(q)
% input : x = [qST qSW dqST dqSW]'
% output : dx_plus = [dqST, dqSW, vCx vCy]'
global mH mS mT mST IK L IS IT g ls lt a1 b1 a2 b2 L
% state
qST = q(1); qSW = q(2); dqST = q(3); dqSW = q(4);

% Fill Your Code
M = [IK+a1.^2.*mS+(a2+ls).^2.*mT+L.^2.*(mH+mS+mT),(-1).*L.*((b1+lt).* ...
  mS+b2.*mT).*cos(qST+(-1).*qSW),(-1).*(a1.*mS+(a2+ls).*mT+L.* ...
  (mH+mS+mT)).*sin(qST),(a1.*mS+(a2+ls).*mT+L.*(mH+mS+mT)).*cos( ...
  qST);(-1).*L.*((b1+lt).*mS+b2.*mT).*cos(qST+(-1).*qSW), ...
  IK+(b1+lt).^2.*mS+b2.^2.*mT,((b1+lt).*mS+b2.*mT).*sin(qSW),(-1) ...
  .*((b1+lt).*mS+b2.*mT).*cos(qSW);(-1).*(a1.*mS+(a2+ls).*mT+L.*( ...
  mH+mS+mT)).*sin(qST),((b1+lt).*mS+b2.*mT).*sin(qSW),mH+2.*( ...
  mS+mT),0;(a1.*mS+(a2+ls).*mT+L.*(mH+mS+mT)).*cos(qST),(-1).*(( ...
  b1+lt).*mS+b2.*mT).*cos(qSW),0,mH+2.*(mS+mT)];

Jv = [(-1).*L.*sin(qST),L.*cos(qST);(ls+lt).*sin(qSW),(-1).* ...
  (ls+lt).*cos(qSW);1,0;0,1]';

dx_minus = [dqST dqSW 0 0];

A = [M -transpose(Jv);
    Jv zeros(2,2)];

B = [M*dx_minus';
    zeros(2,1)];

% Finish
dx_plus_and_F = A\B;
dq_plus = dx_plus_and_F(1:4);
end
