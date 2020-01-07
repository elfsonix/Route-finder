import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import abc


class Plotter(abc.ABC):

    def style_setup(self) -> None:
        sns.set(style="darkgrid")
        pass

    def scatter_plot(self, x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Scatter Plot") -> None:
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        plt.show()
        return None

    def line_plot(self, x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Line Plot") -> None:
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        plt.show()
        return None

    def histogram(self, x_data, y_data, x_axis_name="OX", y_axis_name="OY", plot_title="Histogram Plot") -> None:
        x_data.sort()
        y_data.sort()
        fig, ax = plt.subplots()
        ax.hist(x_data)
        ax.set(xlabel=x_axis_name, ylabel=y_axis_name, title=plot_title)
        plt.show()
        return None

