import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px
from itertools import cycle

df = pd.read_excel("test_sns.xlsx")
groups = ['G1', 'G2', 'G3']

def make_plots(dataframe, title, show=True):
    """
    :param dataframe takes in a dataframe where each column has Young's Modulus Data for a single run
            This is a truncated dataframe, only containing data that should be plotted
    Shows plotly violin plot
    saves PNG and HTML
    """

    plot_title = title
    fig = go.Figure()

    palette = cycle(px.colors.sequential.Plasma)
    print(palette)

    for g in groups:
        fig.add_trace(go.Violin(x=[g] * len(df[g]),
                                y=df[g],
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
    plotly.offline.plot(fig, filename=f'{title}.html')


make_plots(df, "Sample 6 Spot 5")
