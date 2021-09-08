A = str(input("Kies een heel getal "))
B = str(input("Kies nog een heel getal "))


if A > B:
    Max = B
    print("A is het grootste getal met een waarden met " + Max)
elif A < B:
    Min = A
    print("A is het kleinste getal met een waarden van " + Min)
elif A == B:
    print("A en B zijn even groot ")
    
print("Het maximum is " + B)
print("Het minimum is " + A)