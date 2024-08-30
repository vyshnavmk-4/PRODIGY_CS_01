def caesar_cipher(text, shift, mode):
    # Function to encrypt or decrypt the text using Caesar Cipher
    result = ""

    # Loop through each character in the input text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            start = ord('A')
            result += chr((ord(char) - start + shift * mode) % 26 + start)
        # Check if the character is a lowercase letter
        elif char.islower():
            start = ord('a')
            result += chr((ord(char) - start + shift * mode) % 26 + start)
        # If it's not a letter, just add the character as is
        else:
            result += char

    return result


def main():
    # Get user input
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Get mode input: 'e' for encrypt or 'd' for decrypt
    mode_input = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()

    if mode_input == 'e':
        # Encrypt the message
        encrypted_text = caesar_cipher(text, shift, 1)
        print(f"Encrypted message: {encrypted_text}")
    elif mode_input == 'd':
        # Decrypt the message
        decrypted_text = caesar_cipher(text, shift, -1)
        print(f"Decrypted message: {decrypted_text}")
    else:
        print("Invalid mode selected. Please choose 'e' or 'd'.")


if __name__ == "__main__":
    main()
