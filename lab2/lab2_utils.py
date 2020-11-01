from graphics import *


# Draw figure
def draw_figure(win, color, *points):
  p1, p2, p3, p4, p5, p6 = points
  obj = Polygon(Point(*p1), Point(*p2), Point(*p3), Point(*p4), Point(*p5), Point(*p6))
  obj.setOutline(color)
  obj.setWidth(1)
  obj.draw(win)


# Get point coordinates
def get_point(total):
  new_x = total[0, 0]
  new_y = total[0, 1]
  return new_x, new_y


# Find center of figure
def get_center(points):
  x = []
  y = []
  for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])
  center_x = (max(x) - min(x)) / 2 + min(x)
  center_y = (max(y) - min(y)) / 2 + min(y)
  return center_x, center_y
