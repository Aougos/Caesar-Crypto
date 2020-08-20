message = ".XbpXo8Xka8Obsbopb8.fmebo9"
SYMBOLS = "ABCEDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !.?"

for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex - key) % 66
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print("Key #%s %s" % (key, translated))