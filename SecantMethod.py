def secant_method(f_derivative, start_point, end_point, epsilon=1e-5):
    """
    Find the root of a function using the secant method.
    :param f_derivative: The derivative of the function
    :param start_point: The start of the interval
    :param end_point: The end of the interval
    :param epsilon: The epsilon value for convergence
    :return: b, iterations - The root of the function and the number of iterations
    """
    f = f_derivative
    a = start_point
    b = end_point
    iterations = 0

    while abs(f(b)) > epsilon:
        if abs(f(b) - f(a)) < epsilon:  # Check if the difference is too small
            print("Secant method fails to converge, small difference between f(a) and f(b) please change the epsilon value to be higher : [1e-5]-->[1e-4].")
            return None, iterations

        c = b - f(b) * (b - a) / (f(b) - f(a))  # Secant formula


        a, b = b, c  # Update for next iteration
        iterations += 1

    # Clamp the result to the interval
    b = max(min(b, end_point), start_point)

    return b, iterations