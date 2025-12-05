def caesar_encryption(text: str) -> str:
    if text is None:
        return None
    encryption_text = ""
    for char in text:
        if char.isalpha() and char.isascii():
            if char.islower():
                encryption_text += chr((ord(char) - ord("a") + 2) % 26 + ord("a"))
            else:
                encryption_text += chr((ord(char) - ord("A") + 2) % 26 + ord("A"))
        else:
            encryption_text += char
    return encryption_text


if __name__ == "__main__":
    test_input_text = input()
    print(caesar_encryption(test_input_text))
