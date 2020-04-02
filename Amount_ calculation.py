principal = float(input("What is the Principal? "))
rate = float(input("What is the Interest Rate? "))
number = float(input("What is the number of times it will be calculated yearly? "))
time = float(input("What is the Time Period? "))

Rate = rate / 100

Amount = principal * (1 + (Rate / number))**(number * time)

print(Amount)
