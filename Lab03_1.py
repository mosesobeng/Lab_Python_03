
n = 50
print 'The first 50 prime numbers are'
prime_count = 0

possible_prime = 2

while prime_count< n:
        divisor_counter = 0

    for i in range (1,possible_prime+1):
        if possible_prime % i ==0:
            divisor_counter +=1

        if divisor_counter==2:
            print possible_prime
            prime_count += 1

            if prime_count% 10 ==0:
                print

        possible_prime += 1

    

