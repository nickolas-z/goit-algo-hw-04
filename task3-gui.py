import turtle


def draw_rods():
    """Функція для малювання стрижнів."""
    rod_height = 200
    rod_width = 10
    positions = [-150, 0, 150]
    for x in positions:
        rod = turtle.Turtle()
        rod.hideturtle()
        rod.speed(0)
        rod.penup()
        rod.goto(x, -100)
        rod.pendown()
        rod.goto(x, rod_height - 100)


class Disk:
    """Клас для представлення дисків."""

    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.shapesize(1, size)
        self.turtle.color(self.get_color())
        self.turtle.penup()
        # Видаляємо виклик self.update_position() з конструктора

    def get_color(self):
        """Визначає колір диска на основі його розміру."""
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        return colors[(self.size - 1) % len(colors)]

    def update_position(self):
        """Оновлює позицію диска на екрані."""
        x_positions = {"A": -150, "B": 0, "C": 150}
        x = x_positions[self.position]
        y = -100 + 20 * (rods[self.position].index(self))
        self.turtle.goto(x, y)

    def move_to(self, new_position):
        """Анімація переміщення диска на новий стрижень."""
        x_positions = {"A": -150, "B": 0, "C": 150}
        x_new = x_positions[new_position]
        y_up = 150  # Підняти диск над стрижнями

        # Підняти диск
        self.turtle.goto(self.turtle.xcor(), y_up)
        # Перемістити горизонтально
        self.turtle.goto(x_new, y_up)
        # Опустити диск
        y_new = -100 + 20 * len(rods[new_position])
        self.turtle.goto(x_new, y_new)

        # Оновити позицію в моделі
        self.position = new_position


def hanoi(n, source, auxiliary, target):
    """Рекурсивна функція для вирішення задачі Ханойської вежі."""
    if n > 0:
        hanoi(n - 1, source, target, auxiliary)
        # Перемістити диск
        disk = rods[source].pop()
        disk.move_to(target)
        rods[target].append(disk)
        hanoi(n - 1, auxiliary, source, target)


def main():
    global rods
    n = int(
        turtle.numinput(
            "Кількість дисків", "Введіть кількість дисків (1-6):", minval=1, maxval=6
        )
    )
    screen = turtle.Screen()
    screen.title("Ханойська вежа")
    turtle.hideturtle()
    turtle.speed(0)
    draw_rods()

    # Ініціалізація стрижнів
    rods = {"A": [], "B": [], "C": []}

    # Створення та розміщення дисків на стрижні A
    for i in range(n, 0, -1):
        disk = Disk(i, "A")
        rods["A"].append(disk)
        disk.update_position()  # Викликаємо update_position() після додавання диска до стрижня

    hanoi(n, "A", "B", "C")
    turtle.done()

if __name__ == "__main__":
    main()
