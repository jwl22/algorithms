% input : q = [qST qSW dqST dqSW]
% output : [value,isterm,direct]
function [value,isterm,direct]=Event_Heelstrike(t,q)
global a1 b1 a2 b2 theta
% state
qST=q(1); qSW=q(2); dqST=q(3); dqSW=q(4);

R01=[cos(-theta),-sin(-theta),0;
    sin(-theta),cos(-theta),0;
    0,0,1];

p0=(a1+b1+a2+b2)*[cos(q(1))-cos(q(2));sin(q(1))-sin(q(2));0];
p1=R01'*p0;
value=1;

if q(2)>q(1)
    value = p1(1);
end
isterm=1;
direct=0;

end