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