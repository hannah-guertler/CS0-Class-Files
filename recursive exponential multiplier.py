'''5*2 = 2 + (2*4)

2^7 = 2 * 2^6
2^6 = 2 * 2^5

goes until base case
2^1
is concrete answer
uses that as variable to pass back up
this continues until answer is reached
function finally returns to screen

Use if (to say when base case is reached), else (for recursive step) then recursive step. Recur step modifies variables.

'''

def recurExp(number, exp):
    if exp == 1:
        return number
    else:
        return number * number * (exp - 1)
