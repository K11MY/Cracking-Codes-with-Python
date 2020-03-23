import pyperclip
def encryptMessage(key,message):
    #Each string in ciphertext represents a column in the grid
    # output = cipherTexxt['','','','','','','','',] --> same length as key to create the column
    cipherText = [''] *key
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            '''Place the character at the currentIndex in the message at the
            end of the current column in the ciphertext list 
            '''
            cipherText[column] += message[currentIndex]

            #move currentIndex over:
            currentIndex += key
    # Convert ciphertext list into a single string value and return it
    return ''.join(cipherText)

def main():
    message = 'Common sense is not so common.'
    key = 8
    cipherText = encryptMessage(key,message)
    #marks end of the ciphertext
    print(cipherText + '|')

    pyperclip.copy(cipherText)

if __name__ == '__main__':
    main()