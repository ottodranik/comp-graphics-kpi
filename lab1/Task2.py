import copy
import graphics
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as mtransforms


class Task2:
    colors = ['red', 'green', 'yellow', 'blue']
    colors_mono = ['black', 'gray', 'white']

    def main(self):
        self.matplotlib()
        self.graphics()
        self.tkinter()

    # Matplotlib
    def matplotlib(self):
        fig = plt.figure('Task #2 - Matplotlib')
        self.matplotlib_lines(fig)
        self.matplotlib_polygons(fig, self.colors)

        plt.axis('scaled')
        plt.axis('off')
        plt.show()

    # Matplotlib with lines -> monochromed
    def matplotlib_lines(self, fig):
        coords1 = [[-5, 5, 5, -5, -5], [12, 16, 12, 16, 12]]
        coords2 = [[-2, 2, -2, 2, -2], [9, 19, 19, 9, 9]]

        ax = fig.add_subplot()
        ax.plot(coords1[0], coords1[1], color='black')
        ax.plot(coords2[0], coords2[1], color='black')

    # Matplotlib with polygons -> colorized
    def matplotlib_polygons(self, fig, colors):
        ax = fig.add_subplot()
        color_l = len(colors)

        triangle_base = patches.Polygon(
            [[-5, -2], [-5, 2], [0, 0]],
        )

        for i in range(4):
            triangle = copy.copy(triangle_base)
            t = mtransforms.Affine2D().rotate_deg(90 * i) + ax.transData
            triangle.set_transform(t)
            triangle.set_ec(colors[i % color_l]),
            triangle.set_fc(colors[(color_l - 1 - i) % color_l])
            ax.add_patch(triangle)

    # Graphics
    def graphics(self):
        win = graphics.GraphWin('Task #2: Graphics', 600, 600)
        win.setBackground("white")
        win.setCoords(0, 0, 600, 600)

        self.graphics_lines(win)
        self.graphics_polygons(win)

        win.getMouse()
        win.close()

    # Graphics with lines -> monochromed
    def graphics_lines(self, win):
        def build_obj(points):
            points_len = len(points)
            for i in range(len(points)):
                if (i + 1 < points_len):
                    lastPoint = graphics.Point(points[i + 1][0], points[i + 1][1])
                else:
                    lastPoint = graphics.Point(points[0][0], points[0][1])
                line = graphics.Line(graphics.Point(points[i][0], points[i][1]), lastPoint)
                line.setWidth(3)
                line.setOutline('black')
                line.draw(win)

        points1 = [[250, 350], [250, 450], [550, 350], [550, 450]]
        points2 = [[350, 250], [450, 250], [350, 550], [450, 550]]

        build_obj(points1)
        build_obj(points2)

    # Graphics with polygons -> colorized
    def graphics_polygons(self, win):
        def build_points(points):
            final = []
            for i in range(len(points)):
                final.append(graphics.Point(points[i][0], points[i][1]))
            return final

        def build_polygon(points, cline, cfill):
            p1, p2, p3, p4 = build_points(points)
            poly = graphics.Polygon(p1, p2, p3, p4)
            poly.setWidth(3)
            poly.setOutline(cline)
            poly.setFill(cfill)
            poly.draw(win)

        points1 = [[20, 120], [20, 220], [320, 120], [320, 220]]
        points2 = [[120, 20], [220, 20], [120, 320], [220, 320]]

        build_polygon(points1, self.colors[0], self.colors[1])
        build_polygon(points2, self.colors[3], self.colors[2])

    # Tkinter
    def tkinter(self):
        win = tk.Tk()
        win.title('Task #2 - Tkinter')
        canvas = tk.Canvas(win, width=600, height=600, bg='white')
        self.tkinter_lines(canvas)
        self.tkinter_polygons(canvas)
        canvas.pack()
        tk.Button(win, text="Вихід", command=win.quit).pack()
        win.mainloop()
        win.quit()

    # Tkinter with lines -> monochromed
    def tkinter_lines(self, canvas):
        def build_obj(points):
            points_len = len(points)
            for i in range(len(points)):
                if (i + 1 < points_len):
                    lastPoint = points[i + 1]
                else:
                    lastPoint = points[0]
                canvas.create_line(points[i], lastPoint, fill="black", width=3)

        points1 = [[250, 350], [250, 450], [550, 350], [550, 450]]
        points2 = [[350, 250], [450, 250], [350, 550], [450, 550]]

        build_obj(points1)
        build_obj(points2)

    # Tkinter with polygons -> colorized
    def tkinter_polygons(self, canvas):
        points1 = [[20, 120], [20, 220], [320, 120], [320, 220]]
        points2 = [[120, 20], [220, 20], [120, 320], [220, 320]]

        canvas.create_polygon(points1[0], points1[1], points1[2], points1[3],
                              fill=self.colors[0], outline=self.colors[1], width=3)
        canvas.create_polygon(points2[0], points2[1], points2[2], points2[3],
                              fill=self.colors[2], outline=self.colors[3], width=3)
