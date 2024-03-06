
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"Количество строк в файле '{file_path}': {line_count}")
    except FileNotFoundError:
        print("Файл не найден.")
    except IsADirectoryError:
        print("Указанный путь является каталогом, а не файлом.")

file_path = input("Введите путь к текстовому файлу: ")
count_lines_in_file(file_path)