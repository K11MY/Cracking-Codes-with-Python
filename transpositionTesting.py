import random, sys, transpositionEncrypt, decryptTransposition




def main():
    random.seed(50) #set random seed to static value

    # Generate 20 random test
    for i in range(20):
        # Genereate random message to test
        # Message will have random length (betwewen 4 and 40)
        message = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ' * random.randint(4,40)

        #Convert the message string to a list to shuffle it:
        message = list(message)
        random.shuffle(message)
        #Convert list back to string
        message = ''.join(message)
        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # check all possible keys for each message
        for key in range (1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = decryptTransposition.decryptMessage(key, encrypted)

            # If the decryption doesn't match the original message, display an error message and quit
            if message != decrypted:
                print('There is something wrong with the key %s and message %s' % (key,message))
                print('Decrypted as: ' + decrypted)
                sys.exit()
        print('Transposition cipher test passed')

if __name__ == '__main__':
    main()
