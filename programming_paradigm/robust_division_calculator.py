def safe_divide(numerator, denominator):
    "Safe division while handling errors"
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"

        # catch ZeroDivisionError.
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

        # catch ValueError
    except ValueError:
        return f"Error: Please enter numeric values only."

