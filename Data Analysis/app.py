import dash
import dash_html_components as html
import dash_core_components as dcc
from plotly.subplots import make_subplots
#import data_extraction as de
import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']
layout=go.Layout(title='Animals',
                     width=500,
                    height=400)

fig1 = go.Figure(data=[go.Bar(x=animals, y=[20, 14, 23])],layout=layout)
fig2 = go.Figure(data=[go.Bar(x=animals, y=[15, 22, 22])],layout=layout)

app=dash.Dash()
app.layout = html.Div(className='row', children=[
    html.H1("Data Analysis (Byte PYPERS)"),
    
    html.Div(children=[
        dcc.Graph(figure=fig1,id="graph1", style={'display': 'inline-block'}),
        dcc.Graph(figure=fig2,id="graph2", style={'display': 'inline-block'})
    ])
])
 
if __name__=="__main__":
    app.run_server(port="1818",debug=True)