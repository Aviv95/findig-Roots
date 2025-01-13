import sympy
from BisectionMethod import bisection_method
from NewtonRaphson import Newton_Raphson
from SecantMethod import secant_method


def find_extreme_segments(f, start, end, step):
    """
    Find segments where the derivative changes sign, indicating an extreme point.
    :param f: The function
    :param start: The start of the interval
    :param end: The end of the interval
    :param step: Resolution of the interval
    :return: segments, no_extreme_segments - Segments with extreme points and without extreme points
    """
    segments = []
    a = start
    while a < end:
        b = a + step
        try:
            # If sign change occurs, it's an extreme point
            if f(a) * f(b) <= 0 and a+step<end:
                segments.append((a, b))

        except ValueError:
            pass  # Skip points where the function is not defined
        a = b

    return segments
def main():
    """
    Main function to find extreme points of a polynomial using various methods.
    :return: None
    """
    x = sympy.Symbol('x')

    # Define your polynomial
    polynomial = ((3*x**7)+(5*x**5)-(8*x**3)-(x*6)-20)
    print("Polynomial:", polynomial)

    # Lambdify the polynomial (no numpy)
    f = sympy.utilities.lambdify(x, polynomial, modules=['math'])
    print("f(0) =", f(0))

    # Create the derivative of the polynomial
    derivative = sympy.diff(polynomial, x)
    f_derivative = sympy.utilities.lambdify(x, derivative, modules=['math'])
    print("Derivative:", derivative)
    print("f'(0) =", f_derivative(0))

    # Define range and segment size
    range_start = -100
    range_end = 100
    step_size = 0.001  # Reduced step size for more accurate root finding



    extreme_segments = find_extreme_segments(f, range_start, range_end, step_size)
    # Print extreme segments
    if extreme_segments:
        print(f"Extreme segments found: {', '.join([f'[{round(a, 3)}, {round(b, 3)}]' for a, b in extreme_segments])}")
    else:
        print("No extreme segments found.")



    while True:
        print("\nChoose a method to find extreme points:")
        print("1. Bisection Method")
        print("2. Newton Raphson Method")
        print("3. Secant Method")
        print("4. Exit")

        try:
            method = int(input("Enter your choice (1/2/3/4): "))
            if method == 4:
                print("Exiting the program. Goodbye!")
                break

            if method not in [1, 2, 3]:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                continue

            print("\nExtreme Points and Iterations:")
            for a, b in extreme_segments:
                try:

                    if method == 1:
                        root, iterations = bisection_method(f, a, b)
                    elif method == 2:
                        root, iterations = Newton_Raphson(f,f_derivative, a,b)
                    elif method == 3:
                        root, iterations = secant_method(f, a, b)

                    if root is not None:
                        print ("---Root found in---")
                        print(f" [{a:.4f}, {b:.4f}]")
                        print(f"Extreme point: {float(root):.6f}, Iterations: {iterations}")
                except Exception as e:
                    print(f"Failed to find extreme point in segment [{a:.4f}, {b:.4f}]: {e}")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
