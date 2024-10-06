from colorama import Style, init, Fore
from helpers import Application, print_execution_time


class Task3(Application):
    """
    Application class
    """
    @print_execution_time
    def hanoi(self, n, source, auxiliary, target, rods)->None:
        """Рекурсивний алгоритм вирішення задачі про вежі Ханойські"""
        if n > 0:
            self.hanoi(n - 1, source, target, auxiliary, rods)
            # Переміщення диска з джерела на ціль
            disk = rods[source].pop()
            rods[target].append(disk)
            print(f"Перемістити диск з {source} на {target}: {disk}")
            print(f"Проміжний стан: {rods}")
            self.hanoi(n - 1, auxiliary, source, target, rods)

    @print_execution_time
    def run(self):
        init(autoreset=True)
        n = int(input("Введіть кількість дисків (1-6): "))
        rods = {"A": list(range(n, 0, -1)), "B": [], "C": []}
        print(f"Початковий стан: {rods}")
        self.hanoi(n, "A", "B", "C", rods)
        print(f"Кінцевий стан: {rods}")


# Run the application
if __name__ == "__main__":
    try:
        Task3("Hanoi").run()
    except EOFError:
        print(f"\n{Fore.RED}Input ended unexpectedly. Exiting the application.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Operation cancelled (Ctrl+C). Exiting the application.")
