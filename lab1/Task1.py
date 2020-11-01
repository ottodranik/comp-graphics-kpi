import numpy as np
import graphics
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Task1:
    colors = ['red', 'orange', 'yellow', 'green', 'white']

    def main(self):
        self.matplotlib()
        self.graphics()
        self.tkinter()

    # Matplotlib
    def matplotlib(self):
        fig = plt.figure('Task #1: Matplotlib')
        plot_colors = list(reversed(self.colors))

        ax = fig.add_subplot()
        for i in range(5, 0, -1):
            x = i / 2 - i
            y = (5 - i) / 2
            yOffset = 2.5
            square = patches.Rectangle((x, y + yOffset), i, i, ec='black', lw=2, fc=plot_colors[i - 1])
            ax.add_patch(square)

        ax2 = fig.add_subplot()
        t = np.arange(0, 10, 0.1)
        for i in range(5, 0, -1):
            a = i / 1.5
            b = i / 2.5
            ellipsePart1 = a * np.cos(t)
            ellipsePart2 = b * np.sin(t)
            t = np.linspace(0, 2 * np.pi, 100)
            ax2.plot(ellipsePart1, ellipsePart2, color='black', lw=2)
            ax2.fill_between(ellipsePart1, ellipsePart2, color=plot_colors[i - 1])

        plt.axis('scaled')
        plt.axis('off')
        plt.show()

    # Graphics
    def graphics(self):
        win = graphics.GraphWin('Task #1: Graphics', 600, 600)
        win.setBackground("white")

        win.setCoords(0, 0, 500, 500)

        for i in range(1, 6):
            rect = graphics.Rectangle(graphics.Point(150 + 16 * i, 480 - 16 * i),
                                      graphics.Point(350 - 16 * i, 280 + 16 * i))
            rect.setFill(self.colors[i - 1])
            rect.draw(win)

        for i in range(1, 6):
            oval = graphics.Oval(graphics.Point(120 + 16 * i, 280 - 16 * i), graphics.Point(380 - 16 * i, 80 + 16 * i))
            oval.setFill(self.colors[i - 1])
            oval.draw(win)

        win.getMouse()
        win.close()

    # Tkinter
    def tkinter(self):
        win = tk.Tk()
        win.title('Task #1 - Tkinter')
        canvas = tk.Canvas(win, width=600, height=600, bg='white', cursor='pencil')

        for i in range(1, 6):
            canvas.create_rectangle([150 + 16 * i, 280 - 16 * i], [350 - 16 * i, 80 + 16 * i], fill=self.colors[i - 1],
                                    outline="black")

        for i in range(1, 6):
            canvas.create_oval([120 + 16 * i, 480 - 16 * i], [380 - 16 * i, 280 + 16 * i], fill=self.colors[i - 1],
                               outline="black")

        canvas.pack()
        tk.Button(win, text="Вихід", command=win.quit).pack()
        win.mainloop()
        win.quit()
