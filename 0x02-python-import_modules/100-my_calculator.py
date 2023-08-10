#!/usr/bin/python3
# my own calculator!
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    strcont = len(sys.argv) - 1
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
        sys.exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        op = sys.argv[2]
        a = int(a)
        b = int(b)
    if op == "+":
        x = add(a, b)
    elif op == "-":
        x = sub(a, b)
    elif op == "*":
        x = mul(a, b)
    elif op == "/":
        x = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print('{:d} {} {:d} = {:d}'.format(a, op, b, int(x)))
