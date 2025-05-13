def replace_text_numbers(text):
    return text

def main():
    input_path = "input.txt"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
        print("Файл успешно прочитан")
    except FileNotFoundError:
        print(f"Файл {input_path} не найден.")
        return

if __name__ == "__main__":
    main()
