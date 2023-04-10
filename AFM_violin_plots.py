import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px
from itertools import cycle


def make_plots(dataframe, title, group_list, paths, show=True):
    """
    :param dataframe takes in a dataframe where each column has Young's Modulus Data for a single run
            This is a truncated dataframe, only containing data that should be plotted
    :param title: title of the figure you are making
    :param paths: list containing the path to PNG and HTML folder
    :param group_list: array containing all the group names. Should match column names
    :param show: Should the plot open or not
    Shows plotly violin plot
    saves PNG and HTML
    """

    plot_title = title
    fig = go.Figure()

    palette = cycle(px.colors.sequential.Plasma)
    print(palette)

    for g in group_list:
        fig.add_trace(go.Violin(x=[g] * len(dataframe[g]),
                                y=dataframe[g],
                                name=g,
                                box_visible=True,
                                meanline_visible=True,
                                marker_color=next(palette
                                                  )))
        next(palette)
        next(palette)
        next(palette)
        next(palette)
        next(palette)

    fig.update_layout(
        font=dict(
            family="Arial",
            size=60,  # Set the font size here
            color="Black"
        ),
        title_text=plot_title,
        title_x=0.5,
        title_y=0.99
    )

    if show:
        fig.show()

    plotly.offline.plot(fig, filename=paths[1] + "/" + f'{title}.html')
    fig.write_image(paths[0] + "/" + title + ".png", width=2048, height=2048)



