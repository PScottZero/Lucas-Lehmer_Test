# Lucas-Lehmer_Test
This code uses the Lucas-Lehmer Test to see if a given number is a Mersenne Prime, a prime number that can be written in the form of 2^p - 1 where p is a prime integer.

HOW THE LUCAS-LEHMER TEST WORKS:

Say you want to know if 7 is prime. 7 is a number that can be written in the form of 2^p - 1, which is 2^3 - 1. In order to see if 7 is infact a Mersenne Prime, we can check it against the following sequence:

n = n_previous^2 - 2 where n1 = 4 {4, 14, 194, 37634, ...}

To see if 7 is prime, we need to go to the index of one less than the exponent used in the Mersenne formula. In this case, we look at the second term of the sequence, 14, since the exponent used in this example is 3. Then we simply see if the number we are checking is a factor of the term. 7 is a factor of 14, therefore 14 mod 7 is 0. This means that 7 is prime without any doubt.

HOW THE PROGRAM WORKS:

First, the program starts with an exponent of 3. Even though 2^2 - 1 is a Mersenne Prime, the Lucas-Lehmer Test does not recognize it to be, so this number is just printed out at the start of the program. It then uses a quick test called Fermat's Little Theorem (see below) to see if the exponent is likely prime. If the exponent is likely prime, then the Lucas-Lehmer test will be performed to see if infact the exponent using the Mersenne equation generates a Mersenne Prime. It should be noted that all Mersenne Primes, when written in the form of 2^p - 1, have prime exponents. However, just because the exponent is prime, does not mean the resulting number is prime. For example, the Mersenne equation 2^11 - 1 is equal to 2047, which is not prime. However, our best bet to find Mersenne numbers is to check all prime exponents. After an exponent is fully tested, it increments two exponent values, which in this case would be to 5. This can be done because all prime numbers greater than 2 are odd, therefore we do not need to check even exponents. This pattern continues until the user presses ctrl-c, or the computer runs out of memory (which would likely take a long time to accomplish). Finding large Mersenne Primes can take an extremely long amount time. In fact, with our current technology, only 49 Mersenne Primes have been found, the largest being 2^74207281 - 1, which is roughly 22 million digits long. Since the computer you will most likely be running this on is not a supercomputer, the calculations will take a very long time. Be patient, and don't expect to break the current record for largest prime number anytime soon.

FERMAT'S LITTLE THEOREM:

This theorem is used by the program to quickly check to see if the exponent we are trying to use is likely prime. It is quick test, and allows the program to pass on certain exponents right off the bat. However, it should be noted that this theorem only tells us if a number is definitely not prime, or possibly prime. It will not tell us if a number is definitely prime. This means that it could think a non-prime number is possibly prime. However, the test is good enough to eliminate a few exponents to increase run-time efficiency.

The theorem states that you can check if a number p is probably prime if you plug it into the equation a^(p - 1) % p where a is any integer 1 < a < p. If after multiple tests with different a values, each resultant of the equation is 1, then the number p is most likely prime.
