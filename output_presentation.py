import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import abc


class Plotter(abc.ABC):

    def style_setup(self) -> None:
        sns.set(style="darkgrid")
        pass

    def scatter_plot(self, x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Scatter Plot") -> None:
        fig, ax = plt.subplots()
        ax.scatter(x_data, y_data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        plt.show()
        return None

    def line_plot(self, x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Line Plot") -> None:
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        plt.show()
        return None

    def histogram(self, data, x_axis_name="OX", y_axis_name="OY", plot_title="Histogram Plot") -> None:
        data.sort()
        fig, ax = plt.subplots()
        ax.hist(data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        plt.show()
        return None

    # TODO naprawic kolory
    def scatter_and_histogram(self, x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Histogram Plot"):
        x_data.sort()
        y_data.sort()

        left, width = 0.1, 0.65
        bottom, height = 0.1, 0.65
        spacing = 0.005

        rect_scatter = [left, bottom, width, height]
        rect_histx = [left, bottom + height + spacing, width, 0.2]
        rect_histy = [left + width + spacing, bottom, 0.2, height]

        plt.figure(figsize=(8, 8))

        ax_scatter = plt.axes(rect_scatter)
        ax_scatter.tick_params(direction='in', top=True, right=True)
        ax_histx = plt.axes(rect_histx)
        ax_histx.tick_params(direction='in', labelbottom=False)
        ax_histy = plt.axes(rect_histy)
        ax_histy.tick_params(direction='in', labelleft=False)

        # the scatter plot:
        ax_scatter.scatter(x_data, y_data)

        # now determine nice limits by hand:
        binwidth = 0.25
        lim = np.ceil(np.abs([x_data, y_data]).max() / binwidth) * binwidth
        ax_scatter.set_xlim((-lim, lim))
        ax_scatter.set_ylim((-lim, lim))

        bins = np.arange(-lim, lim + binwidth, binwidth)
        ax_histx.hist(x_data, bins=bins, )
        ax_histy.hist(y_data, bins=bins, orientation='horizontal')

        ax_histx.set_xlim(ax_scatter.get_xlim())
        ax_histy.set_ylim(ax_scatter.get_ylim())

        plt.show()
        return None
