def count_lines():
    file_path = r'C:/Users/slamg/OneDrive/Рабочий стол/row.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return len(lines)

print("Number of lines:", count_lines())