if __name__ == '__main__':
    """
    File:    factor_me.py
    Author:  Antionne Andries
    Date:    10/1/2021
    Section: 36
    E-mail:  a345@umbc.edu
    Description: it factors a number into its prime factors less than 50
    """
    primeFactsLessFifty = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    collect = []
    computedNum = 0
    count = 0
    num = int(input("Enter a number to factor: "))
    for i in range(len(primeFactsLessFifty)):
        if num % primeFactsLessFifty[i] == 0:
            computedNum = num / primeFactsLessFifty[i]
            while computedNum % primeFactsLessFifty[i] == 0:
                computedNum /= primeFactsLessFifty[i]
                count += 1
            for k in range(count):
                collect.append(primeFactsLessFifty[i])
            count = 0
            collect.append(str(primeFactsLessFifty[i]))
    if len(collect) == 0:
        print("We didn't find any factors \n"
              "This part of the number couldn't be factored with primes less than 50: " + str(num))
    print(*collect, sep="*")
