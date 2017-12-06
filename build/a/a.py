from PIL import Image
from PIL import ImageDraw
import math

sz = (1080, 720)
wt = (255, 255, 255)
blk = (0, 0, 0)
inc = 0.001


def calPositon(a, b, t):
    x0 = a[0]
    y0 = a[1]
    x1 = b[0]
    y1 = b[1]

    x = math.fabs(x0 - x1)
    y = math.fabs(y0 - y1)

    if x0 - x1 != 0:
        k = (y0 - y1) / (x0 - x1)
        if k >= 0:
            x = x * t + x0
            y = y * t + y0
        else:
            x = x * t + x0
            y = y0 - y * t
        return (x, y)
    else:
        y = y0 + y * t
        x = x0 + x * t
        return (x, y)


def changePoint(point):
    # point[1] = sz[1] - point[1]
    newpoint = (point[0], sz[1] - point[1])
    return newpoint


def drawPoints(point, im):
    point = changePoint(point)
    im.putpixel(point, blk)


def drawLine(a, b, im):
    a = changePoint(a)
    b = changePoint(b)
    out = ImageDraw.Draw(im)
    out.line((a, b), blk)


def solve(points, t):
    # print(points)
    if len(points) == 1:
        return points[0]
    else:
        newpoints = list()
        for i in range(0, len(points) - 1):
            a = calPositon(points[i], points[i + 1], t)
            newpoints.append(a)
        return solve(newpoints, t)


if __name__ == "__main__":
    im = Image.new("RGB", sz, wt)
    # im.show()
    nums = input("plaese in put the x and y of points: ").split(' ')
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    # print(int(nums[0]))
    points = list()
    for i in range(0, len(nums) - 1, 2):
        x = nums[i]
        y = nums[i + 1]
        xy = (x, y)
        points.append(xy)
    # print(points)
    for i in range(0, len(points) - 1):
        drawPoints(points[i], im)
        drawPoints(points[i + 1], im)
        drawLine(points[i], points[i + 1], im)

    im.show()
    t = 0
    while t <= 1 + inc:
        print(t)
        t += inc
        point = solve(points, t)
        intpoint = (int(point[0]), int(point[1]))
        # im.putpixel((int(point[0]),int(point[1])), blk)
        drawPoints(intpoint, im)
    im.show()
