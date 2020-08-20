# message = "This is my secret message"
message = "This is my secret mRssage?"
# message = "anak"
key = 13

SYMBOLS = "ABCEDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !.?"
# SYMBOLS = "abcdefghijklmnopqrstuvwxyz"
# print(len(SYMBOLS))

def encryptCaesar(message, key):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex + key) % 66
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    
    return translated

def decryptCaesar(cipher, key):
    translated = ""
    for symbol in cipher:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex - key) % 66
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    return translated

cipher = encryptCaesar(message, key)
print(f"Hasil Enkrip 'anak': {cipher}")
plain = decryptCaesar(cipher, key)
print(plain)