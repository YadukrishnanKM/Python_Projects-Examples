'''Maths'''
from sympy.vector import gradient, dot, cross, Del, curl
from sympy import symbols, pprint, laplace_transform, inverse_laplace_transform, lambdify, diff, init_printing


def gradt(Equation):
    delop = Del()
    pprint(delop(Equation))
    gradA = gradient(Equation)
    print(f"The gradient of {Equation} is")
    print(gradA)


def Cur_l(Equation):
    delop = Del()
    # pprint(delop(Equation))
    curlA = delop.cross(Equation)
    print(f"The curl of {Equation} is")
    print(curlA)


def diver(Equation):
    delop = Del()
    pprint(delop(Equation))
    divA = delop.dot(Equation)
    print(f"The divergence of {Equation} is")
    pprint(Equation)
    pprint(divA)


def Laplace_Transforming(function_LpT):
    t, s = symbols('t,s')
    pprint(laplace_transform(function_LpT, t, s, noconds=True))


def inverse_Laplace_Transforming(function_inv_LpT):
    t, s = symbols('t,s')
    pprint(inverse_laplace_transform(function_inv_LpT, s, t, noconds=True))


def RegulA_fAlsi(Expres, sym, a_value, b_value, num_iterations):
    f = lambdify(sym, Expres)
    for i in range(1, num_iterations+1):
        c = (a_value*f(b_value)-b_value*f(a_value))/(f(b_value)-f(a_value))
        if ((f(a_value) * f(c) < 0)):
            b_value = c
        else:
            a_value = c
        print('Iteration %d \t the root %0.3f \t function value %0.3f \n' %
              (i, c, f(c)))


def Newton_Raphson(Expres, sym, inetial_approa, num_iteration):
    f = lambdify(sym, Expres)
    dg = diff(Expres)
    df = lambdify(sym, dg)
    for i in range(1, num_iteration+1):
        x1 = (inetial_approa - (f(inetial_approa)/df(inetial_approa)))
        print('itration %d \t the root %0.3f \t function value %0.3f \n' %
              (i, x1, f(x1)))
        inetial_approa = x1


'''
a, t, s, x = symbols('a,t,s,x')
A = sin(a*t)
B = 1/(s**4)
Laplace_Transforming(A)
inverse_Laplace_Transforming(B)
print("\n-------------------------")
d = (x**3)-(2*x)-5
RegulA_fAlsi(d, x, 2, 3, 5)
Newton_Raphson(d, x, 1, 5)'''
