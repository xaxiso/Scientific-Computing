import numpy as np
from scipy import optimize
import statistics as stat


def ellipseFit(data):

    center0 = [0, 0]

    def f(x):
        # x[0] = 0
        # x[1] = 0
        for i in range(len(data[0])):
            # x[0] += data[0][i]
            # x[1] += data[1][i]
            center0[0] += data[0][i]
            center0[1] += data[1][i]
        # x[0] /= len(data[0])
        # x[1] /= len(data[1])
    center0[0] /= len(data[0])
    center0[1] /= len(data[1])


    # center0[0] /= len(data[0])
    # center0[1] /= len(data[1])

    # cx = stat.mean(data[0])
    # cy = stat.mean(data[1])
    # center0 = [cx, cy]

    center = optimize.fmin(f, center0, disp=False)

    # print(center)

    sse, radius = sseOfEllipseFit(center, data)
    theta = [center, radius]

    return theta, sse


def sseOfEllipseFit(center, data):
    sse = 0
    def s(x):
        for i in range(len(data[0])):
            s += ((data[0][i]-x[0])/x[1] + (data[1][i]-x[2])/x[3] - 1)**2

    radius = linalg.lstsq(center, data, rcond=None)[0]
    # A = np.vstack([data[0], np.ones(len(data[0]))]).T
    # rx, ry = np.linalg.lstsq(A, data[1], rcond=None)[0]

    return sse, radius



def main():
    def Load_Coordinates():
        data = [[float(val) for val in input().split()] for i in range(2)]
        return data

    for _ in range(10):
        data = Load_Coordinates()
        cx, cy, a, b = ellipseFit(data)
        print("{} {} {} {}".format(cx, cy, a, b))

if __name__ == '__main__':
    main()