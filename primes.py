def gen_primes(n):
  primes=[]
  for v in range(2,n+1):
    isPrime = True
    for num in range (2, v):
      if v % num == 0:
        isPrime = False
        break
    if isPrime:
      primes.append(v)

  return primes

value = gen_primes(17)
print(value)

def sum_primes():
  value = int(input("Enter Primes to Sum:"))
  print(sum(gen_primes(value)))

sum_primes()