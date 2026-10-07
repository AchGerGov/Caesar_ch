print("Шифр Цезаря")
def caesar_cipher(message, shift):
    encrypted_message = ""
    
    for char in message:
        if 'a' <= char <= 'z':  # Проверка на маленькие английские буквы
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_message += encrypted_char
        elif 'A' <= char <= 'Z':  # Проверка на большие английские буквы
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += encrypted_char
        elif 'а' <= char <= 'я':  # Проверка на маленькие русские буквы
            encrypted_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            encrypted_message += encrypted_char
        elif 'А' <= char <= 'Я':  # Проверка на большие русские буквы
            encrypted_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            encrypted_message += encrypted_char
        else:
            # Если символ не буква, добавляем его без изменений
            encrypted_message += char
            
    return encrypted_message

while True:
    # Ввод исходного сообщения и сдвига
    input_message = input("Введите исходное сообщение (или 'exit' для выхода): ")
    
    if input_message.lower() == "exit":
        print("Выход из программы.")
        break
    
    try:
        shift_value = int(input("Введите значение сдвига: "))
    except ValueError:
        print("Пожалуйста, введите целое число для сдвига.")
        continue

    # Шифруем сообщение
    encrypted = caesar_cipher(input_message, shift_value)

    print(f"Зашифрованное сообщение: {encrypted}")
