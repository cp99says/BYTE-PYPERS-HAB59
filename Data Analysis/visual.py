
import plotly.graph_objs as go
import plotly.express as px
import data_extraction as de
import plotly.offline as po
import pandas as pd

vd=de.vendordata
p_items=vd[vd['Vendor ID'] == 'v100']['Item'].values
p_total=vd[vd['Vendor ID'] == 'v100']['Total']
print(p_items,p_total)
'''

table=pd.pivot_table(vd,values='Item',index='Total')
data=[go.bar(x=table.values,y=table.index,name="Items Listed vs Total Price")]

layout=go.layout(title='Items Listed vs Total Price')


fig=go.Figure(data=data,layout=layout)
po.plot(fig)
'''