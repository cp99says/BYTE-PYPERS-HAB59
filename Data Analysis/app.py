import dash
import dash_html_components as html
import dash_core_components as dcc
#import data_extraction as de
import plotly.graph_objs as go

app=dash.Dash()
app.layout=html.Div([
    html.H1("Hello Dash")
])

if __name__=="__main__":
    app.run_server(port="1818",debug=True)