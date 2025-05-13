import re
from text_to_num import text2num

number_words = {
    "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
    "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
    "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать", "тридцать",
    "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто",
    "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот",
    "восемьсот", "девятьсот", "тысяча", "тысячи", "тысяч",
    "миллион", "миллиона", "миллионов"
}

def replace_text_numbers(text):
    tokens = re.findall(r'\b[а-яё\-]+\b|[.,!?;:]', text, flags=re.IGNORECASE)
    result = []
    buffer = []

    def flush_buffer():
        if buffer:
            phrase = ' '.join(buffer)
            try:
                number = text2num(phrase.lower(), lang='ru')
                result.append(f"{number:,}".replace(",", " "))
            except Exception:
                result.extend(buffer)
            buffer.clear()

    for token in tokens:
        word = token.lower()
        if word in number_words:
            buffer.append(token)
        else:
            flush_buffer()
            result.append(token)

    flush_buffer()
    return re.sub(r'\s+([.,!?;:])', r'\1', ' '.join(result))


def main():
    input_path = "input.txt"
    output_path = "output.txt"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
        print(f"Прочитан файл: {input_path}")
    except FileNotFoundError:
        print(f"Файл {input_path} не найден.")
        return

    updated_text = replace_text_numbers(text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(updated_text)
    print(f"Результат записан в: {output_path}")

if __name__ == "__main__":
    main()
