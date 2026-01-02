import numpy as np
import sympy as sp
x= sp.symbols('x')
Up= True
epsilon = 1e-9
Down = False
turning_point_x =[]
turning_point_y = []
turning_points = []
def g(x):
    f = (3*x**2 -10*x+8)
    return f
f=g(x)
f_derivative= sp.diff(f,x)
f_derivative =sp.simplify(f_derivative)
turning_point_x=sp.solve(f_derivative,x)    
def TPconverter(turning_point_x):
    for i in range(0,len(turning_point_x)):
        y=g(turning_point_x[i])
        turning_point_y.append(y)
roots=sp.solve(f,x)
TPconverter(turning_point_x)
f_second_derivative = sp.diff(f_derivative,x)
f_second_derivative = sp.simplify(f_second_derivative)
if turning_point_x:
    print("Turning points:")
    for x_val, y_val in zip(turning_point_x, turning_point_y):
        print(f"x = {x_val}, y = {y_val}")
        second_deriv_value = f_second_derivative.subs(x,x_val)
        if second_deriv_value>0:
            print("max point")
        if second_deriv_value<0:
            print("min point")
else:
    print("No turning points")
if roots:
    print("\nRoots:")
    for r in roots:
        print(f"x = {r}")
else:
    print("No roots")