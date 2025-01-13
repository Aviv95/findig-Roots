def Newton_Raphson(f, f_derivative, start_point, end_point, epsilon=1e-5, max_iterations=10000):
    """
    Find the root of a function using the Newton-Raphson method.
    
    :param f_derivative:The function
    :param f_derivative:The derivative of the function
    :param start_point:The start of the interval
    :param end_point:The end of the interval
    :param epsilon:Ancillary value for convergence
    :param max_iterations:The maximum number of iterations
    :return:None, iterations - The root of the function and the number of iterations

    """
    x_current = (start_point + end_point) / 2  # Start from the middle of the interval
    iterations = 0

    # Print header for the iteration table
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Iteration", "a", "b", "x_current", "f(x)", "f'(x)", "c"
    ))

    while iterations < max_iterations:
        f_prime = f(x_current)
        f_double_prime = f_derivative(x_current)

        if f_double_prime == 0:
            print("Second derivative is zero. No valid root found using Newton-Raphson method.")
            return None, iterations

        # Newton-Raphson update
        c = x_current - f_prime / f_double_prime

        # Clamp the result to the interval
        c = max(min(c, end_point), start_point)

        # Print current iteration details
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(
            iterations, start_point, end_point, x_current, f_prime, f_double_prime, c
        ))


        # Check convergence based on epsilon
        if abs(f_prime) <= epsilon or abs(c - x_current) <= epsilon:
            return c, iterations + 1

        # Update x_current and increment iterations
        x_current = c
        iterations += 1

    # If max iterations reached
    print("Maximum iterations reached, no convergence.")
    return None, iterations
