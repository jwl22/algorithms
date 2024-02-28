function [t1,t2]=control(kv,kp,t,xx)

    param;
    [qd,qdp,qdpp]=sysinp(g1,g2,T,t);
    e=qd-[xx(1) xx(2)]';
    ep=qdp-[xx(3) xx(4)]';

    [M,N]=arm(m1,m2,a1,a2,g,xx);
    s1=qdpp(1)+kv*ep(1)+kp*e(1);
    s2=qdpp(2)+kv*ep(2)+kp*e(2);
    t1=M(1,1)*s1+M(1,2)*s2+N(1);
    t2=M(1,2)*s1+M(2,2)*s2+N(2);