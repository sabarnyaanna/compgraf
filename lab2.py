import turtle

NODES = [
    (0,    0),
    (1/3,  0),
    (1/3,  1/3),
    (2/3,  1/3),
    (2/3,  0),
    (2/3, -1/3),
    (1,   -1/3),
    (1,    0),
]

def draw_segment(t, x1, y1, x2, y2, depth, outward=1):
    if depth == 0:
        t.goto(x2, y2)
        return

    dx = x2 - x1
    dy = y2 - y1

    def pt(u, v):
        v = v * outward
        return (x1 + u * dx - v * dy,
                y1 + u * dy + v * dx)

    pts = [pt(u, v) for u, v in NODES]

    for i in range(len(pts) - 1):
        draw_segment(t,
                     pts[i][0], pts[i][1],
                     pts[i+1][0], pts[i+1][1],
                     depth - 1, outward)


def main():
    screen = turtle.Screen()
    screen.title("Фрактал: квадрат + ламана 1/3")
    screen.bgcolor("white")
    screen.setup(850, 850)
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(1)
    t.color("black")

    try:
        depth = int(input("Глибина рекурсії (0..4): "))
    except ValueError:
        depth = 3

    size = 360
    half = size / 2
    sides = [
        ((-half, -half), ( half, -half), +1), 
        (( half, -half), ( half,  half), +1),  
        (( half,  half), (-half,  half), +1),  
        ((-half,  half), (-half, -half), +1),  
    ]

    t.penup()
    t.goto(-half, -half)
    t.pendown()

    for (x1, y1), (x2, y2), out in sides:
        draw_segment(t, x1, y1, x2, y2, depth, out)

    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    main()