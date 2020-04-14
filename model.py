from math import log

def f (rating) :
    return log(rating, 5)

def C_D() :
    return 1

def Q2 (Q1, p1, p2, c_d) :
    return float(2*Q1)/((p1/p2)*c_d*(p1-p2)/(p1+p2) + 1) - Q1

def attract (k) :
    q2 = Q2(k['Quantity'], k['Regular Price'], k['Price'], C_D() )
    return (q2/k['Quantity']) * f(k['Rating'])