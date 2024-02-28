function [qd,e]= robout(t,x)
    % compute desired trajectory
    period= 2 ; amp1= 0.1 ; amp2= 0.1 ;
    fact= 2*pi/period ;
    sinf= sin(fact*t) ;
    cosf= cos(fact*t) ;
    qd= [amp1*sinf amp2*cosf] ;
    % tracking errors
    e= qd - x(:,1:2) ;