x = int(input("shkruaj numrin e pikeve: "))

if x >= 0 and x <= 29:
    print("t ie ki noten 1")
elif x >= 30 and x <= 49:
    print("ti e ki noten 2")
elif x >= 50 and x <= 69:
    print("ti e ki noten 3")  # Corrected the message
elif x >= 70 and x <= 89:
    print("ti e ki noten 4")
elif x >= 90 and x <= 100:  # Adjusted the upper limit from >= to <=
    print("ti e ki noten 5")
else:
    print("Numri i dhene nuk eshte ne rangun e duhur.")
