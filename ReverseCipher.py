#Reverse Cipher
if __name__ == '__main__':

    message = input('Enter Message: ')
    # where the output will store the string
    translated = ''
    # Finds index of last character by subtracting it from 1 (because it starts from 0)
    i = len(message) - 1

    while i >= 0:
        #message[i] is the last character in the string
        translated = translated + message[i]
        print('i is:',i,
              'message[i] is',message[i],
              'translater is',translated)
        # Goes through until i = -1 which means it start from the last character then the second last and the third last so on
        i = i - 1
    print(translated)
