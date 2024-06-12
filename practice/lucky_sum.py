#Given 3 int values, a b c, return their sum. 
#However, if one of the values is 13 then it does not count towards the sum and values 
#to its right do not count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a,b,c):
    sum = a + b + c
    if a == 13:
        sum = 0
    else:
        if b == 13:
            sum -= b + c
        else:
            if c == 13:
                sum -= c
    print(sum)

lucky_sum(1, 2, 3) 
lucky_sum(1, 2, 13) 
lucky_sum(1, 13, 3) 