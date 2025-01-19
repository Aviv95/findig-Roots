def secant_method(f, start_point, end_point, epsilon=1e-5):
    """
    Find the root of a function using the secant method with detailed iteration output.

    :param f: The function
    :param start_point: The start of the interval
    :param end_point: The end of the interval
    :param epsilon: The epsilon value for convergence
    :return: b, iterations - The root of the function and the number of iterations
    """
    a = start_point
    b = end_point
    iterations = 0

    # Print header for the iteration table
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Iteration", "a", "b", "f(a)", "f(b)", "c"
    ))

    while abs(f(b)) > epsilon:
        # Check if the difference is too small
        if abs(f(b) - f(a)) < epsilon:
            print("Secant method fails to converge, small difference between f(a) and f(b) please change the epsilon value to be higher : [1e-5]-->[1e-4].")
            return None, iterations

        # Secant formula
        c = b - f(b) * (b - a) / (f(b) - f(a))

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(
            iterations, a, b, f(a), f(b), c
        ))

        # Update for next iteration
        a, b = b, c
        iterations += 1

    # Clamp the result to the interval
    b = max(min(b, end_point), start_point)

    return b, iterations
