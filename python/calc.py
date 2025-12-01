nr1 = input("first number: ")
nr2 = input("second number: ")
print()
op = input("operator: ")
err = False
an = None
if op == '+':
    an = float(nr1) + float(nr2)
elif op == '*':
    an = float(nr1) * float(nr2)
elif op == '-':
    an = float(nr1) - float(nr2)
elif op == '/':
    if float(nr1) != 0.0 or float(nr2) != 0.0:
        an = float(nr1) / float(nr2)
    else:
        err = True
else:
    err = True

if err == True:
    print("ERROR")
else:
    print("answer:", an)
