def distance(x1, y1, x2, y2):
    x = x1 - x2
    x **= 2
    y = y1 - y2
    y **= 2
    c = (y + x) ** 0.5
    return(c)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(distance(x1, y1, x2, y2))
