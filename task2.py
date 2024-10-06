import matplotlib.pyplot as plt
import math
from colorama import Style, init, Fore
from helpers import Application, print_execution_time

class Task2(Application):
    """
    Application class
    """
    @print_execution_time
    def koch_snowflake(self, order, scale=10):

        def koch_curve(ax, x1, y1, x2, y2, level):
            if level == 0:
                ax.plot([x1, x2], [y1, y2], color="b")
            else:
                dx = x2 - x1
                dy = y2 - y1
                x3 = x1 + dx / 3
                y3 = y1 + dy / 3

                x5 = x1 + 2 * dx / 3
                y5 = y1 + 2 * dy / 3

                # Координати вершини трикутника
                angle = math.atan2(dy, dx) - math.pi / 3
                dist = math.hypot(dx, dy) / 3
                x4 = x3 + dist * math.cos(angle)
                y4 = y3 + dist * math.sin(angle)

                # Рекурсивно малюємо 4 нові лінії
                koch_curve(ax, x1, y1, x3, y3, level - 1)
                koch_curve(ax, x3, y3, x4, y4, level - 1)
                koch_curve(ax, x4, y4, x5, y5, level - 1)
                koch_curve(ax, x5, y5, x2, y2, level - 1)

        fig, ax = plt.subplots()

        # Визначаємо три точки початкового трикутника
        x0 = 0
        y0 = 0

        x1 = scale
        y1 = 0

        x2 = scale / 2
        y2 = scale * math.sin(math.pi / 3)

        # Малюємо три сторони трикутника
        koch_curve(ax, x0, y0, x1, y1, order)
        koch_curve(ax, x1, y1, x2, y2, order)
        koch_curve(ax, x2, y2, x0, y0, order)

        ax.set_aspect("equal")
        ax.axis("off")
        plt.show()

    @print_execution_time
    def run(self):
        init(autoreset=True)
        print(
            f"{Fore.RED}Рівень рекурсії 7 обчислюється 21 секунду, тому рівень обмежено до 7."
        )
        while True:
            level = int(input("Введіть рівень рекурсії (від 0 до 7): "))
            if -1 < level < 8:
                break
            else:
                print(f"{Fore.RED}Рівень рекурсії має бути від 0 до 7. Спробуйте ще раз.")
        self.koch_snowflake(level)

# Run the application
if __name__ == "__main__":
    try:
        Task2("Fractal").run()
    except EOFError:
        print(f"\n{Fore.RED}Input ended unexpectedly. Exiting the application.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Operation cancelled (Ctrl+C). Exiting the application.")
