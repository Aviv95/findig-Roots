import sympy
import math

def max_steps(start_point, end_point, epsilon):
    """Calculate the maximum number of steps for the bisection method."""
    return math.ceil(math.log2((end_point - start_point) / epsilon))

def bisection_method(f, start_point, end_point, epsilon=1e-6):
    """
    Find the root of a  function using the bisection method.

    :param f:The function
    :param start_point: Start of the interval
    :param end_point: End of the interval
    :param epsilon: Convergence tolerance
    :return: root, iterations - The root of the function and the number of iterations
    """
    a, b = start_point, end_point
    iterations = 0

    if sympy.sign(f(a)) == sympy.sign(f(b)):
        raise Exception("The scalars start_point and end_point do not bound a root")

    steps = max_steps(a, b, epsilon)

    # Print header for the iteration table
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))

    while abs(b - a) > epsilon and iterations < steps:
        c = (a + b) / 2
        fc = f(c)

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(
            iterations, a, b, f(a), f(b), c, fc))

        if abs(fc) < epsilon:
            return c, iterations

        if sympy.sign(f(a)) != sympy.sign(fc):
            b = c
        else:
            a = c

        iterations += 1


    root = (a + b) / 2
    return root, iterations
