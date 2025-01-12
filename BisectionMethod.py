def bisection_method(f_derivative, start_point, end_point, epsilon=1e-5):
    """
    Find the root of a function using the bisection method.
    :param f_derivative: The derivative of the function
    :param start_point: The start of the interval
    :param end_point: The end of the interval
    :param epsilon: Epsilon value for convergence
    :return: root, iterations - The root of the function and the number of iterations
    """
    a, b ,f= start_point, end_point, f_derivative
    iterations = 0


    if f(a) * f(b) >= 0:
        print("---no root found in---")
        print(f" [{a:.2f}, {b:.2f}]")

        return None, iterations

    while (b - a) / 2 > epsilon:
        iterations += 1
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < epsilon:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    root = (a + b) / 2
    return root, iterations