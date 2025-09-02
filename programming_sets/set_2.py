def shift_letter(letter, shift):
    if letter == " ":
        return " "
    num = ord(letter) - ord("A")
    new_num = (num + shift) % 26
    return chr(new_num + ord("A"))


def caesar_cipher(message, shift):
    result = ""
    for ch in message:
        result += shift_letter(ch, shift)
    return result


def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    shift = ord(letter_shift) - ord("A")
    num = ord(letter) - ord("A")
    new_num = (num + shift) % 26
    return chr(new_num + ord("A"))


def vigenere_cipher(message, key):
    result = ""
    key_index = 0
    for ch in message:
        if ch == " ":
            result += " "
        else:
            k = key[key_index % len(key)]
            result += shift_by_letter(ch, k)
            key_index += 1
    return result


def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    n = len(message)
    result = ""
    for i in range(n):
        index = (i // shift) + (n // shift) * (i % shift)
        result += message[index]
    return result


def scytale_decipher(message, shift):
    n = len(message)
    result = [""] * n
    for i in range(n):
        index = (i // shift) + (n // shift) * (i % shift)
        result[index] = message[i]
    return "".join(result)
