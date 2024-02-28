% input : q = [qST qTW qSW dqST dqTW dqSW]
% output : [value,isterm,direct]
function [value,isterm,direct]=Event_Kneestrike(t,q)
global a1 b1 a2 b2 mH mS mT g IK IS IT
% conf. state
qST=q(1); qTW=q(2); qSW=q(3);

value = qTW - qSW;
isterm=1;
direct=-1;
end
