import dash
import dash_html_components as html
import dash_core_components as dcc

#import data_extraction as de


app=dash.Dash()
app.layout=html.Div([
    html.H1("Hello Dash")
])
#app.layout='temp-plot.html'

if __name__=="__main__":
    app.run_server(port="1818",debug=True)