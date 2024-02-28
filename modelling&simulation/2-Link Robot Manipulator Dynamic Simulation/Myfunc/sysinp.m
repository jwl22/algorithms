function [qd,qdp,qdpp]=sysinp(g1,g2,T,t)
    fact=2*pi/2;
    sinf=sin(fact*t);
    cosf=cos(fact*t);
    qd=[g1*sinf g2*cosf]';
    qdp=fact*[g1*cosf -g2*sinf]';
    qdpp=-fact^2*qd;