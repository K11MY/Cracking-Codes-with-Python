import time, os, sys, transpositionEncrypt, decryptTransposition


def main():
    fileName = 'helloworld.txt'
    outputFileName = 'encryptedFile.txt'

    myKey = 10
    encryptMode = 'encrypt'

    if not os.path.exists(fileName):
        print('The file %s does not exist.' % (fileName))
        sys.exit()

    # If output file already exist the user can quit or continue to encrypt new file
    if os.path.exists(fileName):
        print('This will overwrite the file %s. (C)ontinue or (Quit)' % (outputFileName))
        response = input('> ')
        # if response does not start with c exit the system
        if not response.lower().startswith('c'):
            sys.exit()
    # Read the message from the input file
    fileObj = open(fileName)
    content = fileObj.read()
    fileObj.close()
    print('%sing...' % (encryptMode.title()))
    # Measure how long the encryption and decryption takes
    startTime = time.time()
    if encryptMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif encryptMode == 'decrypt':
        translated = decryptTransposition.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time:%s seconds' % (encryptMode.title(), totalTime))

    # Write the translated message to the textfile
    outputFileObj = open(outputFileName, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (encryptMode, fileName, len(content)))
    print('%sed file is %s.' % (encryptMode.title(), fileName))


if __name__ == '__main__':
    main()
