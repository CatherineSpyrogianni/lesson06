N = int(input("Give an integer number (>=0): "))

while N < 0:
    print(int(input("Give an integer number (>=0): ")))
if N == 0 or N == 1:
    print("The number is NOT prime! ")
else:
    for i in range(2,N):
        if  N % i == 0:
            print("The number is NOT prime! ")
            break
    else:
        print("The number is prime!")
