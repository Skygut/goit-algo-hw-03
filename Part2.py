import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def rounder(*args):
    for _ in range(3):
        koch_curve(*args)
        args[0].right(120)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    rounder(t, order, size)

    window.mainloop()


def main():
    number = None

    while True:
        val = input("Enter recursion number:>>> ")
        try:
            number = int(val)
            break
        except ValueError:
            print(f"Invalid value: {val}. The value must be an integer.")

    draw_koch_curve(number)


if __name__ == "__main__":
    main()
