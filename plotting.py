import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import abc


class Plotter(abc.ABC):

    @staticmethod
    def style_setup() -> None:
        sns.set(style="darkgrid")
        pass

    @staticmethod
    def scatter_plot(x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Scatter Plot") -> None:
        fig, ax = plt.subplots()
        plt.grid(True)
        ax.scatter(x_data, y_data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)

        plt.show()
        return None

    @staticmethod
    def line_plot(x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Line Plot") -> None:
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        plt.show()
        return None

    @staticmethod
    def multiline_plot(x_data, y1_data, y2_data, y3_data, x_axis_name="OX", y_axis_name="OY", plot_title="Line Plot",
                       legend=["Dataset 1", "Dataset 2", "Dataset 3"]):

        fig, ax = plt.subplots()
        plt.grid(True)
        plt1 = ax.plot(x_data, y1_data)
        plt2 = ax.plot(x_data, y2_data)
        plt3 = ax.plot(x_data, y3_data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        ax.legend((plt1[0], plt2[0], plt3[0]), (legend[0], legend[1], legend[2]))
        plt.show()

    @staticmethod
    def histogram(data, x_axis_name="OX", y_axis_name="OY", plot_title="Histogram Plot") -> None:
        data.sort()
        fig, ax = plt.subplots()
        ax.hist(data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        plt.show()
        return None

    # TODO naprawic kolory
    @staticmethod
    def scatter_and_histogram(x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Histogram Plot"):
        # x_data.sort()
        # y_data.sort()

        left, width = 0.1, 0.65
        bottom, height = 0.1, 0.65
        spacing = 0.005

        rect_scatter = [left, bottom, width, height]
        rect_histx = [left, bottom + height + spacing, width, 0.2]
        rect_histy = [left + width + spacing, bottom, 0.2, height]

        ax_scatter = plt.axes(rect_scatter)
        ax_scatter.tick_params(direction='in', top=True, right=True)
        ax_histx = plt.axes(rect_histx)
        ax_histx.tick_params(direction='in', labelbottom=False)
        ax_histy = plt.axes(rect_histy)
        ax_histy.tick_params(direction='in', labelleft=False)
        ax_scatter.scatter(x_data, y_data)

        binwidth = 0.25
        lim = np.ceil(np.abs([x_data, y_data]).max() / binwidth) * binwidth

        bins = np.arange(-lim, lim + binwidth, binwidth)
        ax_histx.hist(x_data, bins=bins, )
        ax_histy.hist(y_data, bins=bins, orientation='horizontal')

        ax_histx.set_xlim(ax_scatter.get_xlim())
        ax_histy.set_ylim(ax_scatter.get_ylim())

        plt.show()
        return None

    @staticmethod
    def barplot(data, xlabels, ylabel, title):
        ind = np.arange(len(data))
        fig, ax = plt.subplots()
        barplt = ax.bar(ind, data, width=0.5)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.set_xticks(ind)
        ax.set_xticklabels(xlabels)
        fig.tight_layout()
        plt.show()

    @staticmethod
    def grouped_barplot(data_1: list, data_2: list, data_3: list, data_4: list, xlabels: list, legend: list,
                        ylabel, title):
        ind = np.arange(len(data_1))  # the x locations for the groups
        width = 0.20  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind - width * 3 / 2, data_1, width,
                        label=legend[0])
        rects2 = ax.bar(ind - width / 2, data_2, width,
                        label=legend[1])
        rects3 = ax.bar(ind + width / 2, data_3, width,
                        label=legend[2])
        rects4 = ax.bar(ind + width * 3 / 2, data_4, width,
                        label=legend[3])
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.set_xticks(ind)
        # ax.set_xticklabels(xlabels)
        ax.legend()

        fig.tight_layout()

        plt.show()

    @staticmethod
    def barplot_threeway(data_high, data_avg, data_low, xlabels="OX", ylabel="OY", title="", legend=["", "", ""]):

        ind = np.arange(len(data_high))
        fig, ax = plt.subplots()
        plt.grid(True)
        plt1 = ax.bar(ind, data_high, width=0.5)
        plt2 = ax.bar(ind, data_avg, width=0.5)
        plt3 = ax.bar(ind, data_low, width=0.5)

        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.set_xticks(ind)
        ax.set(ylim=(0, 140))
        ax.set_xticklabels(xlabels)
        ax.legend((plt1[0], plt2[0], plt3[0]), (legend[0], legend[1], legend[2]))

        fig.tight_layout()
        plt.show()
