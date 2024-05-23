#Given 3 int values, a b c, return their sum. 
#However, if one of the values is the same as another of the values, it does not count towards the sum.

def lone_sum(a,b,c):
    sum = 0

    if a - b != 0 and a - c != 0 and b - c != 0:
        sum = a + b + c
    else:
        if a - b != 0 and a - c != 0:
            sum = a
        else: 
            if a - b != 0 and b - c != 0:
                sum = b
            else: 
                if c - a != 0 and c - b != 0:
                    sum = c
    print(sum)

lone_sum(1, 2, 3) 
lone_sum(3, 2, 3)
lone_sum(3, 3, 3) 