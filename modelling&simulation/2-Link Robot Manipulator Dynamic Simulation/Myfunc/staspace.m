function xdot=staspace(t,x)
    global t1 t2
    param;
    [M,N]=arm(m1,m2,a1,a2,g,x);
    MI=inv(M);
    xdot(1)=x(3);
    xdot(2)=x(4);
    xdot(3)=MI(1,1)*(-N(1)+t1)+MI(1,2)*(-N(2)+t2);
    xdot(4)=MI(1,2)*(-N(1)+t1)+MI(2,2)*(-N(2)+t2);
    
    xdot = xdot';