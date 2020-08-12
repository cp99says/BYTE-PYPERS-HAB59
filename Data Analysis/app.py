import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id = 'graph1',
        figure = {
            'data': [
                { 'x': [1, 2, 3], 'y': [4, 1, 2] },
            ],
        }
    ),
    dcc.Graph(
        id='graph2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [6, 5, 4]},
            ],
        }
    ),

    dcc.Graph(
        id='graph3',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [7, 4, 3]},
            ],
        }
    ),

])


if __name__ == '__main__':
    app.run_server(debug=True, port=5055)