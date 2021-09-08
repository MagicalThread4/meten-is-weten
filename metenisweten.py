A = str(input("Kies een heel getal "))
B = str(input("Kies nog een heel getal "))


if A > B:
    max = B
    print("A is het grootste getal met een waarden met " + max )
elif A < B:
    min = A
    print("A is het kleinste getal met een waarden van " + min )
elif A == B:
    print("A en B zijn even groot ")
    
