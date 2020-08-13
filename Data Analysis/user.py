import data_extraction as de
import plotly.graph_objs as go
import plotly.express as px
#import data_extraction as de
import plotly.offline as po
import pandas as pd



# In[36]:
m=['01','02','03','04','05','06','07','08','09','10','11','12']
m_names=['January','February','March','April','May','June','July','August','September',
         'October','November','December']

transaction=de.userdata.groupby('User ID') 
transaction_vendor=transaction.get_group('b100') 
#transaction_vendor.head(7)


# In[24]:


def bar_plot(labels,values,month):
    layout=go.Layout(title=f'Expenditure for {month}',
                     width=500,
                    height=400)
    width=[]
    for x in range(len(values)):
        width.append(0.5)
    #data=[go.Bar(x=x1,y=y1,name="Items Listed vs Total Price",marker={'color':'#660066'})]
    pp = go.Figure(data=[go.Bar(x=labels, y=values,text=values,textposition='auto',width=width,
                                marker={'color':'#00b38f'})],layout=layout)
    pp.update_layout(xaxis_title='Items Bought',
                    yaxis_title="Total Buying Price(Rs)",
                      title={'y':0.9,
                             'x':0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'})
    # pp.show()
    # po.plot(pp,filename=f'{month}.html',auto_open=True)
    return pp


# In[33]:


def pie_plot(labels,values,month):
    layout=go.Layout(title=f'Expenditure/Item for {month}',
                     width=500,
                    height=400)
    pie_user_items = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.1],
                                            textinfo='label+percent',insidetextorientation='radial'
                                           )],layout=layout)
    pie_user_items.update_layout(title={'y':0.9,
                                         'x':0.5,
                                         'xanchor': 'center',
                                         'yanchor': 'top'})                               
                                   
    # pie_user_items.show()
    # po.plot(pie_user_items,auto_open=True)
    return pie_user_items

# In[34]:


def monthly_sales(user_id):
    transaction=de.userdata.groupby('User ID') 
    transaction_user=transaction.get_group(user_id) 
    transaction_user.head()
    def monthly_analysis_user(user_list):
        bought_items=user_list['Item List'].values
        bought_items_names=([bought_items[i][0] for i in range(len(bought_items))])
        bought_items_price=([bought_items[i][3] for i in range(len(bought_items))])    
        name_nd=[]
        price_nd=[]
        for i in range(0,len(bought_items_names)):
            if bought_items_names[i] not in name_nd:
                name_nd.append(bought_items_names[i])

        for name in name_nd:
           add=0
           indexes=[i for i in range(0,len(bought_items_names)) if bought_items_names[i]==name]
           for v in indexes:
               add=add+bought_items_price[v]
           price_nd.append(add)
        return [name_nd[0:],price_nd[0:]]
    available_month=[]
    for mo in m:
        for i in range(len(transaction_user)):
            if mo==(transaction_user['Month'].values)[i]:
                available_month.append(mo)
                break
    #print(available_month)
    monthly=transaction_user.groupby('Month')
    monthly.head()
    user_bought_items=[]
    final_user_sold_items=[]
    #print(available_month)
    for i in available_month:
        monthly_sales=monthly.get_group(i)
        a=monthly_analysis_user(monthly_sales)
        user_bought_items.append(a)  

    b_fig=[]
    p_fig=[]
    #print(user_bought_items)
    for month in range(len(available_month)):
        ind=m.index(available_month[month])
        mon_name=m_names[ind]
        b_fig.append(bar_plot(user_bought_items[month][0],user_bought_items[month][1],mon_name))  
        p_fig.append(pie_plot(user_bought_items[month][0],user_bought_items[month][1],mon_name))
        
    return b_fig,p_fig
