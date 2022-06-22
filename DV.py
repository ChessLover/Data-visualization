import dash
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html

data = pd.read_csv("games_cleaned.csv")
app = dash.Dash(__name__)


app.css.append_css({'external_url': '/assets/style.css'})

fig1 = px.bar(data['rated'].value_counts())
div1 = html.Div(
    children=[
        html.H1(children="Chess Games Dashboard", ),
        html.P(
            children="Rated games VS non-rated",
        ),
        dcc.Graph(figure=fig1)
    ]
)


fig2 = px.histogram(data, x='white_rating', nbins=15)
fig3 = px.histogram(data, x='black_rating', nbins=15)

div2 = html.Div(
    children=[
        html.H1(children="Players rating Distributions"),
        html.P(
            children="Distribution of White players according to ratings",
        ),
        dcc.Graph(figure=fig2),
        html.P(
            children="Distribution of Black players according to ratings",
        ),
        dcc.Graph(figure=fig3)
    ]
)


fig4 = px.bar(data['victory_status'].value_counts())
div3 = html.Div(
    children=[
        html.H1(children="Game result Analysis", ),
        dcc.Graph(figure=fig4)
    ]
)

fig5 = px.histogram(data, x='victory_status',  color='winner', text_auto=True)
div4 = html.Div(
    children=[
        html.H1(children="Winner statistics", ),
        html.P(
            children="Winner according to color",
        ),
        dcc.Graph(figure=fig5)
    ]
)


# Most frequent openings played 

counts = data.groupby("opening_name")["opening_name"].transform(len)
temp = counts > 100

fig6 = px.bar(data[temp]['opening_name'], orientation='h')
fig6.update_layout(yaxis={'categoryorder':'total ascending'})
div5 = html.Div(
    children=[
        html.H1(children="Opening statistics", ),
        html.P(
            children="Most frequent openings, which have been played more than 100 times",
        ),
        dcc.Graph(figure=fig6)
    ]
)

app.layout = html.Div(
    children=[div1, div2, div3, div4, div5]
)


if __name__ == '__main__':
    app.run_server(port= '8051', debug=True)