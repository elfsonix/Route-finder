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

        # plt.figure(figsize=(8, 8))

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
        # ax_scatter.set_xlim((-lim, lim))
        # ax_scatter.set_ylim((-lim, lim))

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

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.set_xticks(ind)
        # ax.set_xticklabels(xlabels)
        ax.legend()

        # def autolabel(rects, xpos='center'):
        #     """
        #     Attach a text label above each bar in *rects*, displaying its height.
        #
        #     *xpos* indicates which side to place the text w.r.t. the center of
        #     the bar. It can be one of the following {'center', 'right', 'left'}.
        #     """
        #
        #     ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        #     offset = {'center': 0, 'right': 1, 'left': -1}
        #
        #     for rect in rects:
        #         height = rect.get_height()
        #         ax.annotate('{}'.format(height),
        #                     xy=(rect.get_x() + rect.get_width() / 2, height),
        #                     xytext=(offset[xpos] * 3, 3),  # use 3 points offset
        #                     textcoords="offset points",  # in both directions
        #                     ha=ha[xpos], va='bottom')

        # autolabel(rects1, "left")
        # autolabel(rects2, "right")

        fig.tight_layout()

        plt.show()