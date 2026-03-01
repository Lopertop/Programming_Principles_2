import re
import json

information = {}

with open("C:\\Users\\admin\\OneDrive\\Desktop\\python_cource\\practice_5\\task\\raw.txt", 'r', encoding='utf-8') as file:
    text = file.read()
    pattern_prices = r"Стоимость\s+(\d+\s?\,?\d+)"
    pattern_names = r"^\d+\.\s*\n?(.*?)(?=\n\d+,\d+)"
    pattern_amount = r"(\d+),\d+ x"
    pattern_datetime = r"Время: (\d{2}.\d{2}.\d{4} \d{2}:\d{2}:\d{2})"
    pattern_payment = r"([А-Яа-я\s]+):\s+[\d\s,.]+\s+ИТОГО:"

    prices = re.findall(pattern_prices, text)
    product_names = re.findall(pattern_names, text, re.MULTILINE | re.DOTALL)
    amounts = re.findall(pattern_amount, text)
    date_time = re.search(pattern_datetime, text)
    payment = re.search(pattern_payment, text)

    for i in range(len(prices)):
        information[i + 1] = {
            "product name": product_names[i].strip(),
            "price": prices[i].strip(),
            "amount": amounts[i].strip(),
        }

    information["date"] = date_time.group(1).strip()
    information["payment"] = payment.group(1).strip()

with open("C:\\Users\\admin\\OneDrive\\Desktop\\python_cource\\practice_5\\task\\result.json", 'w', encoding='utf-8') as json_file:
    json.dump(information, json_file, ensure_ascii=False, indent=4)