def Newton_Raphson(f_derivative, f_derivative_2nd, start_point, end_point, epsilon=1e-5, max_iterations=10000):
    """
    Find the root of a function using the Newton-Raphson method.
    :param f_derivative:The derivative of the function
    :param f_derivative_2nd:The second derivative of the function
    :param start_point:The start of the interval
    :param end_point:The end of the interval
    :param epsilon:Ancillary value for convergence
    :param max_iterations:The maximum number of iterations
    :return:None, iterations - The root of the function and the number of iterations

    """
    x_current = (start_point + end_point) / 2  # Start from the middle of the interval
    iterations = 0

    while iterations < max_iterations:
        f_prime = f_derivative(x_current)
        f_double_prime = f_derivative_2nd(x_current)

        if f_double_prime == 0:
            print("Second derivative is zero. No valid root found using Newton-Raphson method.")
            return None, iterations

        # Newton-Raphson update
        x_next = x_current - f_prime / f_double_prime

        # Clamp the result to the interval
        x_next = max(min(x_next, end_point), start_point)

        # Check convergence based on epsilon
        if abs(f_prime) <= epsilon or abs(x_next - x_current) <= epsilon:
            return x_next, iterations + 1

        # Update x_current and increment iterations
        x_current = x_next
        iterations += 1

    # If max iterations reached
    print("Maximum iterations reached, no convergence.")
    return None, iterations