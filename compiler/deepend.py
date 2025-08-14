замены = {
    "функция": "def",
    "вернуть": "return",
    "вывести": "print",
    "если": "if",
    "иначе": "else",
}

def transpile(code):
    for ru, en in замены.items():
        code = code.replace(ru, en)
    return code

# Пример использования:
deep_end_code = """
функция сложить(a, b):
    вернуть a + b
"""
python_code = transpile(deep_end_code)
print(python_code)
