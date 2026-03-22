list = []

for N in range(2, 100+1):
        for i in range(2,N):
            if  N % i == 0:
                break
        else:
            list.append(N)
print(list)

primes = tuple(list)
print(primes)