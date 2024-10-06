import os
import shutil
import argparse
from pathlib import Path
from colorama import Style, init, Fore
from helpers import Application, print_execution_time


class Task1(Application):
    """
    Application class
    """

    def parse_arguments(self)->None:
        """Парсинг аргументів командного рядка"""
        parser = argparse.ArgumentParser(
            description="Recursive file copier and sorter by file extension. Run file_generator.py to generate files."
        )
        parser.add_argument("source_dir", help="Path to the source directory")
        parser.add_argument(
            "dest_dir",
            nargs="?",
            default="dist",
            help="Path to the destination directory (default: dist)",
        )
        return parser.parse_args()


    def get_unique_filename(self, dest_dir, filename):
        """Генерує унікальне ім'я файлу, якщо файл уже існує"""
        base_name, extension = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(os.path.join(dest_dir, new_filename)):
            new_filename = f"{base_name}_{counter}{extension}"
            counter += 1
        return new_filename

    @print_execution_time
    def copy_and_sort_files(self, source_dir, dest_dir)->None:
        """Рекурсивно копіює файли із сортуванням за розширенням"""
        # Перебираємо всі елементи у директорії
        try:
            for item in os.listdir(source_dir):
                item_path = os.path.join(source_dir, item)

                if os.path.isdir(item_path):
                    # Якщо елемент є директорією, рекурсивно викликаємо функцію для неї
                    self.copy_and_sort_files(item_path, dest_dir)
                elif os.path.isfile(item_path):
                    # Якщо елемент є файлом, сортуємо його за розширенням
                    # Отримуємо розширення файлу без крапки
                    file_extension = Path(item).suffix[1:]  
                    # Якщо файл не має розширення, використовуємо 'no_extension'
                    if (not file_extension): 
                        file_extension = "no_extension"

                    # Створюємо новий шлях у директорії призначення на основі розширення файлу
                    new_dir = os.path.join(dest_dir, file_extension)
                    os.makedirs(new_dir, exist_ok=True)

                    # Уникнення перезапису файлів
                    new_file_name = self.get_unique_filename(new_dir, item)
                    new_file_path = os.path.join(new_dir, new_file_name)

                    # Копіюємо файл до відповідної піддиректорії
                    shutil.copy2(item_path, new_file_path)
                    print(
                        f"Copy {Style.BRIGHT}{Fore.CYAN}{item_path}{Style.RESET_ALL} to {Style.BRIGHT}{Fore.CYAN}{new_file_path}{Style.RESET_ALL}"
                    )

        except PermissionError as e:
            print(f"Access denied {source_dir}: {e}")
        except Exception as e:
            print(f"Unknown error with {source_dir}: {e}")

    @print_execution_time
    def run(self):
        init(autoreset=True)

        args = self.parse_arguments()

        source_dir = args.source_dir
        dest_dir = args.dest_dir

        if not os.path.exists(source_dir):
            print(f"Directory {source_dir} is not exist.")
            return

        if not os.path.isdir(source_dir):
            print(f"{source_dir} is not a directory.")
            return

        os.makedirs(dest_dir, exist_ok=True)

        print(
            f"Сopy from {Style.BRIGHT}{Fore.CYAN}{source_dir}{Style.RESET_ALL} tо {Style.BRIGHT}{Fore.CYAN}{dest_dir}{Style.RESET_ALL}"
        )
        self.copy_and_sort_files(source_dir, dest_dir)


# Run the application
if __name__ == "__main__":
    try:
        Task1("Copy and sort files").run()
    except EOFError:
        print(f"\n{Fore.RED}Input ended unexpectedly. Exiting the application.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Operation cancelled (Ctrl+C). Exiting the application.")
