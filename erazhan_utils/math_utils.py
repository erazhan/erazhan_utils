# coding:utf-8
# -*- coding:utf-8 -*-
# @time: 2023/9/21 13:21
# @Author: erazhan
# @File: math_utils.py

# ----------------------------------------------------------------------------------------------------------------------
import math

def radian2angle(theta_radian):
    return theta_radian * 180/math.pi

def angle2radian(theta_angle):
    return theta_angle * math.pi/180


def calculate_polygon_area(points):
    """Shoelace公式（鞋带公式，也称Gauss公式）计算多边形面积"""
    n = len(points)
    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)

    area = abs(area) / 2
    return area

def is_point_in_polygon(point, polygon):
    """
    判断点是否在多边形内部

    参数:
    - point: 待判断的点，格式为 (x, y)
    - polygon: 多边形的顶点列表，每个顶点格式为 (x, y)

    返回值:
    - 0: 点在多边形外部
    - 1: 点在多边形内部
    - 2: 点在边上
    - 3: 点是多边形顶点
    """
    """
    这段代码使用射线法（Ray Casting Algorithm）来判断一个点是否在由若干个点构成的封闭多边形内部。下面是对代码原理的详细描述：

    遍历多边形的边：

    通过循环迭代多边形的每条边，其中每条边由相邻的两个顶点构成。
    使用两个变量 p1 和 p2 来表示边的两个端点。
    判断射线与边的交点：

    通过比较点的 y 坐标与边的两个端点的 y 坐标，确定射线是否与边相交。
    如果点的 y 坐标在两个端点的 y 坐标之间，并且点的 x 坐标小于等于两个端点的最大 x 坐标，则射线与边相交。
    计算交点的 x 坐标：

    如果边的两个端点的 y 坐标不相等，则通过线性插值计算交点的 x 坐标。
    如果边的两个端点的 y 坐标相等，则说明射线与边重合或平行，无需计算交点的 x 坐标。
    判断交点的数量：

    如果交点的数量为奇数，则点在多边形内部。
    如果交点的数量为偶数，则点在多边形外部。
    射线法的原理是基于射线从待判断的点出发，与多边形的边进行交点计数。当射线与多边形的边相交时，交点计数加一。如果射线与多边形的边重合或平行，则不计算交点。根据交点计数的奇偶性，可以判断点是否在多边形内部。

    这种方法的基本思想是，多边形是封闭的，射线从点沿着任意方向发出，如果射线与多边形的交点数量为奇数，那么点在多边形内部。这可以通过绘制一条水平线（或任意方向的射线）从点向右延伸，然后计算该水平线与多边形的交点数量来判断。

    射线法的优点是简单且易于实现，适用于一些简单的多边形。但它也有一些限制，例如对于自相交的多边形或存在洞的复杂多边形，射线法将无法正确判断。对于复杂情况，可能需要使用其他更复杂的算法来判断点是否在多边形内部。
    """
    num_vertices = len(polygon)
    inside = False

    # 待判断点的纵坐标要在边的两个点纵坐标之间，横坐标要小于边的两个点横坐标最大值
    # 可以理解为射线是从点出发，往横坐标正无穷处延伸，又或者说点在边（线段）的左方
    if any(point[0]==p[0] and point[1]==p[1] for p in polygon):
        return 3

    p1x, p1y = polygon[0]
    for i in range(1, num_vertices + 1):

        p2x, p2y = polygon[i % num_vertices]

        # 是否在平行坐标轴的边上
        if p1y == p2y and point[1] == p1y and point[0] < max(p1x,p2x) and point[0] > min(p1x,p2x):
            return 2

        if p1x == p2x and point[0] == p1x and point[1] < max(p1y,p2y) and point[1] > min(p1y,p2y):
            return 2

        # 边的两个点的纵坐标相等就不会走下面这段代码了，相等的逻辑上面已经处理。
        # 边的两个点纵坐标不等且point的横坐标小于最大值，
        if point[1] > min(p1y, p2y) and point[1] < max(p1y, p2y) and point[0] < max(p1x,p2x):

            xinters = (point[1] - p1y) * (p2x - p1x) / (p2y - p1y) + p1x # 其实就是平行与x轴的射线与边的交点，已经固定y了
            if point[0] == xinters:
                return 2

            if point[0] <= xinters:
                inside = not inside
        p1x, p1y = p2x, p2y

    if inside:
        return 1
    else:
        return 0

if __name__ == "__main__":

    raw_radian = math.pi
    print("raw_radian:", raw_radian)

    angle = radian2angle(raw_radian)
    print("angle:", angle)

    radian = angle2radian(angle)
    print("radian:", radian)

    A = [0, 0]
    B = [2, 0]
    C = [2, 2]
    D = [1, 1]
    E = [0, 2]

    points = [A, B, D, A, C, E]
    area = calculate_polygon_area(points)
    print("polygon_area:", area)
    pass