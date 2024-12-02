multiplo = 8

while multiplo <= 500:
    print(multiplo, end=" - " if multiplo + 8 <= 500 else "\n")
    multiplo += 8
