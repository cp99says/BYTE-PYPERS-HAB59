import data_extraction as de
import plotly.graph_objs as go
import plotly.express as px
#import data_extraction as de
import plotly.offline as po
import pandas as pd

vd=de.vendordata
def bar_plot_items_listed(id):
    p_items=vd[vd['Vendor ID'] == id]['Item'].values
    p_total=vd[vd['Vendor ID'] == id]['Total'].values
    x1,y1=0,0
    for i in p_items:
        x1=i
    for i in p_total:
        y1=i
    data=[go.Bar(x=x1,y=y1,name="Items Listed vs Total Price",marker={'color':'#660066'})]
    layout=go.Layout(title='Items Listed vs Total Price',
                    width=500,
                    height=400)
    vendor_items_plot=go.Figure(data=data,layout=layout)
    vendor_items_plot.update_layout(xaxis_title="Total Price of all Items",
                                  yaxis_title="Price in Rs(INR)",
                                  title={'y':0.9,
                                         'x':0.5,
                                         'xanchor': 'center',
                                         'yanchor': 'top'},
                                   plot_bgcolor = '#d0d0e1',
                                   paper_bgcolor = '#fff'
                                   )
    vendor_items_plot.show()
    po.plot(vendor_items_plot,auto_open=True)
#bar_plot_items_listed('v200')
def pie_plot_items_listed(id):
    p_items=vd[vd['Vendor ID'] == id]['Item'].values
    p_total=vd[vd['Vendor ID'] == id]['Total'].values
    for i in p_items:
        x1=i
    for i in p_total:
        y1=i
    layout=go.Layout(title='Items Listed vs Total Price',
                     width=500,
                    height=400)
    pie_vendor_items = go.Figure(data=[go.Pie(labels=x1, values=y1, pull=[0, 0.1])],layout=layout)
    pie_vendor_items.update_layout(title={'y':0.9,
                                         'x':0.5,
                                         'xanchor': 'center',
                                         'yanchor': 'top'})                               
                                   
    pie_vendor_items.show()
    po.plot( pie_vendor_items,auto_open=True)
#pie_plot_items_listed('v100')


# In[17]:


transaction = de.userdata.groupby('Vendor ID') 
transaction_vendor=transaction.get_group('v200') 
transaction_vendor.head()


# In[18]:


transaction_vendor['Month'].values


# In[19]:


def bar_plot(labels,values,month):
    layout=go.Layout(title=f'Items Listed vs Sold Price for {month}',
                     width=500,
                    height=400)
    width=[]
    for x in range(len(values)):
        width.append(0.5)
    #data=[go.Bar(x=x1,y=y1,name="Items Listed vs Total Price",marker={'color':'#660066'})]
    pp = go.Figure(data=[go.Bar(x=labels, y=values,text=values,textposition='auto',width=width,
                                marker={'color':'#ff9900'})],layout=layout)
    pp.update_layout(xaxis_title='Items Listed',
                    yaxis_title="Selling Price(Rs)",
                      title={'y':0.9,
                             'x':0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'})
    pp.show()
    po.plot(pp,filename=f'{month}.html',auto_open=True)


# In[20]:


m=['01','02','03','04','05','06','07','08','09','10','11','12']
m_names=['January','February','March','April','May','June','July','August','September',
         'October','November','December']
def monthly_sales(ven_id):
    transaction = de.userdata.groupby('Vendor ID') 
    transaction_vendor=transaction.get_group(ven_id) 
    transaction_vendor.head()
    def monthly_analysis_vendor(ven_list):

        sold_items=ven_list['Item List'].values
        sold_items_names=([sold_items[i][0] for i in range(len(sold_items))])
        sold_items_price=([sold_items[i][3] for i in range(len(sold_items))])    
        name_nd=[]
        price_nd=[]
        for i in range(0,len(sold_items_names)):
            if sold_items_names[i] not in name_nd:
                name_nd.append(sold_items_names[i])

        for name in name_nd:
           add=0
           indexes=[i for i in range(0,len(sold_items_names)) if sold_items_names[i]==name]
           for v in indexes:
               add=add+sold_items_price[v]
           price_nd.append(add)
        return [name_nd[0:],price_nd[0:]]
    available_month=[]
    for mo in m:
        for i in range(len(transaction_vendor)):
            if mo==(transaction_vendor['Month'].values)[i]:
                available_month.append(mo)
                break
    #print(available_month)
    monthly=transaction_vendor.groupby('Month')
    monthly.head()
    monthly_sales=monthly.get_group('08')
    monthly_sales.head()
    vendor_sold_items=[]
    final_vendor_sold_items=[]
    print(available_month)
    for i in available_month:
        monthly_sales=monthly.get_group(i)
        a=monthly_analysis_vendor(monthly_sales)
        vendor_sold_items.append(a)  


    print(vendor_sold_items)
    for month in range(len(available_month)):
        ind=m.index(available_month[month])
        mon_name=m_names[ind]
        bar_plot(vendor_sold_items[month][0],vendor_sold_items[month][1],mon_name)       
