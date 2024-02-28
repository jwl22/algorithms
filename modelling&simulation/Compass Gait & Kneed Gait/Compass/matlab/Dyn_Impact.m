function dx_plus = Dyn_Impact(x)
% input : x = [qST qSW dqST dqSW]'  T회전각, W회전각, T회전각속도, W회전각속도
% output : dx_plus = [dqST, dqSW, vCx vCy]' 
global a b mH mS IST ISW g
qST = x(1); qSW = x(2); dqST = x(3); dqSW = x(4);

%%%%%% Fill Your Code
M = [IST+(a+b).^2.*mH+(2.*a.^2+2.*a.*b+b.^2).*mS,(-1).*b.*(a+b).*mS.* ...
  cos(qST+(-1).*qSW),(-1).*(b.*(mH+mS)+a.*(mH+2.*mS)).*sin( ...
  qST),(b.*(mH+mS)+a.*(mH+2.*mS)).*cos(qST);(-1).*b.*(a+b).* ...
  mS.*cos(qST+(-1).*qSW),ISW+b.^2.*mS,b.*mS.*sin(qSW),(-1) ...
  .*b.*mS.*cos(qSW);(-1).*(b.*(mH+mS)+a.*(mH+2.*mS)).*sin(qST) ...
  ,b.*mS.*sin(qSW),mH+2.*mS,0;(b.*(mH+mS)+a.*(mH+2.*mS)).*cos( ...
  qST),(-1).*b.*mS.*cos(qSW),0,mH+2.*mS];

% Jv = [(-1).*(a+b).*sin(qST),(a+b).*cos(qST);
%     (a+b).*sin(qSW),(-1).*(a+b).*cos(qSW);
%     1,0;
%     0,1];

J = [(-1).*(a+b).*sin(qST),(a+b).*sin(qSW),1,0;(a+b).*cos(qST ...
  ),(-1).*(a+b).*cos(qSW),0,1];

dx_minus = [dqST dqSW 0 0];
A = [M -transpose(J);
    J zeros(2,2)];
B = [M*dx_minus';
    zeros(2,1)];
dx_plus_and_F = A\B;
%%%%%% Finish     

dx_plus = dx_plus_and_F(1:4);
end