num=int(input("enter a number:"))
digit_sum =0
while num >0:
    digit_sum += num % 10
    num //=10
print("sum of digits:",digit_sum)
