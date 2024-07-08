# ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.
#An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

def valid_ISBN10(isbn):
    try:
        sum = 0
        n = 0
        for i in isbn:
            n += 1
            if i == 'X' and n == 10: i = '10'
            sum += int(i)*n
            print(i, n, int(i)*n, sum, sum/11)
        if sum//11 == sum/11 and n == 10:
            return True
        else:
            return False
    except:
        return False

valid_ISBN10('X123456788')
