import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go


class Task3:
    x = np.arange(0, 3 * np.pi, 0.1)
    y1 = 7 * 0.1 * np.cos(x)
    y2 = 7 * 0.1 * np.tan(x)
    y3 = 7 * 0.1 * (1 / np.tan(x))

    def main(self):
        self.matplotlib()
        self.plotly()
        self.bokeh()

    # Matplotlib data visualization
    def matplotlib(self):
        fig, ax = plt.subplots(
            2,
            2,
            constrained_layout=True,
            gridspec_kw={
                'width_ratios': [1, 1],
                'height_ratios': [1, 1]
            },
            figsize=(7, 7)
        )
        plt.subplots_adjust(hspace=0.5)
        fig.suptitle('Task #3: Matplotlib')
        ax[0][0].plot(self.y1, color='red', lw=1)
        ax[0][1].plot(self.y2, color='green', lw=1)
        ax[1][0].plot(self.y3, color='orange', lw=1)
        ax[1][1].plot(self.y1, color='red', lw=1, scalex=True, scaley=True)
        ax[1][1].plot(self.y2, color='green', lw=1, scalex=True, scaley=True)
        ax[1][1].plot(self.y3, color='orange', lw=1, scalex=True, scaley=True)

        plt.axis('scaled')
        plt.show()

    # Plotly data visualization
    def plotly(self):
        def build_plot(globalName, data, position, color, names=None):
            if type(data) is list:
                for i in range(len(data)):
                    fig.add_trace(
                        go.Scatter(y=data[i], x=self.x, name=names[i], marker_color=color[i]),
                        row=position[0], col=position[1]
                    )
            else:
                fig.add_trace(
                    go.Scatter(y=data, x=self.x, name=globalName, marker_color=color),
                    row=position[0], col=position[1]
                )
        fig = make_subplots(rows=2, cols=2)

        build_plot("y1", self.y1, [1, 1], 'red')
        build_plot("y2", self.y2, [1, 2], 'green')
        build_plot("y3", self.y3, [2, 1], 'orange')
        build_plot("Results", [self.y1, self.y2, self.y3], [2, 2], ['red', 'green', 'orange'], ['y1', 'y2', 'y3'])

        fig.show()

    # Bokeh data visualization
    def bokeh(self):
        import bokeh.plotting as bokehPlotting
        from bokeh.layouts import gridplot

        def build_plot(global_name, data, color, names=None):
            fig = bokehPlotting.figure(title=global_name)
            fig.grid.grid_line_alpha = 0.3
            fig.xaxis.axis_label = 'x'
            fig.yaxis.axis_label = global_name
            fig.legend.location = "top_left"
            if type(data) is list:
                for i in range(len(data)):
                    fig.line(self.x, data[i], color=color[i], legend_label=names[i])
            else:
                fig.line(self.x, data, color=color, legend_label=global_name)
            return fig

        p1 = build_plot("y1", self.y1, 'red')
        p2 = build_plot("y2", self.y2, 'green')
        p3 = build_plot("y3", self.y3, 'orange')
        p4 = build_plot("Results", [self.y1, self.y2, self.y3], ['red', 'green', 'orange'], ['y1', 'y2', 'y3'])

        bokehPlotting.show(gridplot([[p1, p2], [p3, p4]], plot_width=400, plot_height=400))  # open a browser
