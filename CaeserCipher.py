# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip
if __name__ == '__main__':

    # The string to be encrypted/decrypted:
    message = input('Please enter a message: ')
    # The encryption/decryption key:
    key = int(input('Key Value (must be an integer): '))

    # Whether the program encrypts or decrypts:
    mode = input('mode: ')  # Set to either 'encrypt' or 'decrypt'.

    # Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Stores the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            # Find symbol in SYMBOLS and return the symbolIndex that was found
            symbolIndex = SYMBOLS.find(symbol)
            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                # it would be subtract the translatedIndex value if it is greater then the length of the SYMBOL
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                # if translatedIndex is smaller than 0 then add through the symbol to get translatedIndex
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Output the translated string:
    print(translated)
    pyperclip.copy(translated)
