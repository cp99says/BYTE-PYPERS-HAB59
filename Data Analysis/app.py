import dash
import dash_html_components as html
import dash_core_components as dcc
from plotly.subplots import make_subplots
import vendor as v
b,p=v.monthly_sales('v300')
#import data_extraction as de
import plotly.graph_objects as go
layout=go.Layout(title='Animals',
                     width=500,
                    height=400)

# html.Ul([html.Li(x) for x in my_list])

app=dash.Dash()
app.layout = html.Div(className='row', children=[
    html.H1("Data Analysis (Byte PYPERS)"),
    
    html.Div(children=[
        dcc.Graph(figure=b[0],id="graph1", style={'display': 'inline-block'}),
        dcc.Graph(figure=p[0],id="graph2", style={'display': 'inline-block'})
        ]) 
])
   


if __name__=="__main__":
    app.run_server(port="1818",debug=True)