import math

def decryptMessage(key,message):

    # Number of columns
    numOfColumns = int(math.ceil(len(message)/float(key)))
    # Number of Rows
    numOfRows = key
    #Number of shaded boxes
    numShadedBoxes = (numOfRows * numOfColumns) - len(message)

    #Initalise ciphertext columns
    plainText = [''] * numOfColumns

    column = 0
    row = 0
    for symbol in message:
        plainText[column] += symbol
        column += 1 # go to next columns

        #If there are no more columns OR we hit a shaded box, go back to the first column or next row
        if(column == numOfColumns) or (column == numOfColumns -1) and (row >= numOfRows - numShadedBoxes):
            column = 0
            row += 1
    return ''.join(plainText)

if __name__ == '__main__':
    message = 'Cenoonommstmme oo snnio. s s c'
    key = 8
    
    plainText = decryptMessage(key,message)
    print(plainText)