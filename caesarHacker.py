# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

#Store cipher text
message = 'qeFIP?eGSeECNNS,5coOMXXcoPSZIWoQI,\
avnl1olyD4l ylDohww6DhzDjhuDil,\
z.GM?.cEQc. 70c.7KcKMKHA9AGFK,\
?MFYp2pPJJUpZSIJWpRdpMFY,\
ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K\
Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key:
for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # Loop through each symbol in `message`:
    for symbol in message:
        #if all symbols exist decrypt it
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            # Handle the wrap-around:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
