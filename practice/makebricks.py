def make_bricks(small, big, goal):
    if goal>=5:
        if goal/big == 5:
            return True
        else:
            if small >= goal%5: 
                return True 
            else:
                return False
    else:
        if small >= goal:
            return True
        else:
            return False

print(make_bricks(3,1,8))
print(make_bricks(3,1,9))
print(make_bricks(3,2,10))