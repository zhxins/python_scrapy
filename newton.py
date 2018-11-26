def cube_newton(num):
    x = num / 3.0
    y = 0
    count = 1
    while abs(x - y) > 0.00000001:
        count, x
        count += 1
        y = x
        x = (2.0 / 3.0) * x + (num * 1.0) / (x * x * 3.0)
    return x


if __name__ == "__main__":
    print(cube_newton(128))

