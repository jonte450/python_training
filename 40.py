import math

def cal_p(x1,y1,x2,y2):
    dist = math.sqrt((x1-x2)**2+ (y2-y1)**2)
    return dist

print(cal_p(4,0,6,6))