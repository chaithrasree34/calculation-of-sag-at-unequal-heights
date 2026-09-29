# calculation-of-sag-at-unequal-heights
# Calculation of sag of a conductor between supports at unequal heights

L = float(input("Enter span length L (m): "))
h = float(input("Enter difference in support heights h (m): "))
w = float(input("Enter conductor weight w (N/m): "))
T = float(input("Enter horizontal tension T (N): "))

# Distance of lowest point from lower support
x0 = (L / 2) - (T * h) / (w * L)

print("\nDistance of lowest point from lower support =", x0, "m")

# Check whether lowest point lies between the supports
if 0 <= x0 <= L:

    # Sag below the level of the lower support
    sag_lower = (w * x0**2) / (2 * T)

    # Sag below the level of the higher support
    sag_higher = (w * (L - x0)**2) / (2 * T)

    print("Sag below lower support level =", sag_lower, "m")
    print("Sag below higher support level =", sag_higher, "m")

else:
    print("Lowest point lies outside the span.")

# Sag at any specified point
x = float(input("\nEnter distance x from lower support (m): "))

y = (w * (x - x0)**2) / (2 * T)

print("Sag at x =", x, "m is", y, "m")
