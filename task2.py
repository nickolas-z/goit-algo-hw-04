from colorama import Style, init, Fore
from helpers import Application, print_execution_time



class Task2(Application):
    """
    Application class
    """

    @print_execution_time
    def merge_two_lists(self, list_a, list_b)->list:
        """
        Злиття двох списків
        Args:
            list_a: Перший список
            list_b: Другий список
        Return:
            merged: Результат злиття двох списків
        """
        merged = []
        i, j = 0, 0
        # Порівнюємо елементи двох списків і додаємо менший до результату
        while i < len(list_a) and j < len(list_b):
            if list_a[i] <= list_b[j]:
                merged.append(list_a[i])
                i += 1
            else:
                merged.append(list_b[j])
                j += 1
        # Додаємо залишки списків
        merged.extend(list_a[i:])
        merged.extend(list_b[j:])
        return merged

    @print_execution_time
    def merge_k_lists(self, lists)->list:
        """
        Злиття кількох списків
        Args:
            lists: Список списків
        Return:
            lists[0]: Результат злиття всіх списків
        """
        if not lists:
            return []
        while len(lists) > 1:
            merged_lists = []
            # Зливаємо списки попарно
            for i in range(0, len(lists), 2):
                list_a = lists[i]
                if i + 1 < len(lists):
                    list_b = lists[i + 1]
                    merged_list = self.merge_two_lists(list_a, list_b)
                else:
                    merged_list = list_a
                merged_lists.append(merged_list)
            lists = merged_lists
        return lists[0]


    @print_execution_time
    def run(self):
        init(autoreset=True)
        # Приклад використання
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        merged_list = self.merge_k_lists(lists)
        print("Відсортований список:", merged_list)

# Run the application
if __name__ == "__main__":
    try:
        Task2("Merge lists").run()
    except EOFError:
        print(f"\n{Fore.RED}Input ended unexpectedly. Exiting the application.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Operation cancelled (Ctrl+C). Exiting the application.")
