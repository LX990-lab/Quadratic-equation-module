import cmath

def solvequadratic(a:float,b:float,c:float):
    if a == 0:
        raise ValueError(" 'a' cannot be zero ")
    x = (-b + cmath.sqrt(b*b-4*a*c))/(2*a)
    y = (-b - cmath.sqrt(b*b-4*a*c))/(2*a)
    return x,y

def solvedelta(a:float,b:float,c:float):
    x = b*b-4*a*c
    return x

def rootnature(delta:float):
    if delta == 0:
        x = "Real,Equal,One root"
        return x
    elif delta > 0:
        x = "Real,Distinct,unequal root"
        return x
    elif delta < 0:
        x = "complex,imaginary,conjugate root"

def rootrelation(a:float,b:float,c:float):
    if a == 0:
        raise ValueError(" 'a' cannot be zero ")
    rootsum = -b/a
    rootproduct = c/a
    return rootsum,rootproduct

def findvertex(a:float,b:float,c:float):
    if a == 0:
        raise ValueError(" 'a' cannot be zero ")
    delta = solvedelta(a,b,c)
    x =  -b/(2*a)
    y = -delta/(4*a)
    return x,y