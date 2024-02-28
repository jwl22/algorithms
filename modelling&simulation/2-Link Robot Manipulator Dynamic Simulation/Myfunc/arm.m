function [M,N]=arm(m1,m2,a1,a2,g,x)
    M11=(m1+m2)*a1^2+m2*a2^2+2*m2*a1*a2*cos(x(2));
    M12=m2*a2^2+m2*a1*a2*cos(x(2));
    M22=m2*a2^2;
    N1=-m2*a1*a2*(2*x(3)*x(4)+x(4)^2)*sin(x(2));
    N1=N1+(m1+m2)*g*a1*cos(x(1))+m2*g*a2*cos(x(1)+x(2));
    N2=m2*a1*a2*x(3)^2*sin(x(2))+m2*g*a2*cos(x(1)+x(2));
    M=[M11 M12;M12 M22];
    N=[N1 N2]';