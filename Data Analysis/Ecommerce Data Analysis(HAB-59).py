#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo as p


# In[2]:


client=p.MongoClient("mongodb://localhost:27017/")


# ## Testing

# In[3]:


print(client.list_database_names())


# In[4]:


ven=client['vendor']
ven_details=ven.details
for d in ven_details.find():
    print(d)


# In[5]:


ven_item=ven.items
for d in ven_item.find():
    print(d['item'])


# In[6]:


ven_item=ven.items
for d in ven_item.find():
   print("Vendor name : ",d['vendor ID']) 
   for item in d['item']:
      for i in item:
            print(i)
            print(item[i]['price'])
            print(item[i]['quantity'])
            print("total Amount: ",(item[i]['price']*item[i]['quantity']))
   


# ## Database Extraction starts

# In[7]:


import pandas as pd
userdata=pd.DataFrame(columns=['User ID','Vendor ID','Date','Month','Item List'])
userdata


# In[8]:


user_details=client['buyer']
d_user_name=[]
d_userID=[]
u_d=user_details.details
for nm in u_d.find():
   d_user_name.append(nm['name'])
   d_userID.append(nm['buyer ID'])
print(d_user_name)
print(d_userID)


# In[9]:



u_t=user_details.transaction
t_user_ID=[]
t_vendor_ID=[]
t_day=[]
t_month=[]
t_item_details=[]
for tra in u_t.find():
    t_user_ID.append(tra['buyer ID'])
    t_vendor_ID.append(tra['vendor ID'])
    t_day.append(tra['date'][0:2])
    t_month.append(tra['date'][3:5])
    
    for items in tra['cart']:
        for i in items:
            cart_details=[]
            cart_details.append(i)
            cart_details.append(items[i]['quantity'])
            cart_details.append(items[i]['price'])
            cart_details.append(items[i]['quantity']*items[i]['price'])
            t_item_details.append(cart_details)
            
print(t_item_details)
print(t_day)
print(t_month)
print(t_vendor_ID)
print(t_user_ID) 
    
    


# In[10]:


#userdata=pd.DataFrame(columns=['User ID','Vendor ID','Date','Month','Item List'])

userdata['User ID']=t_user_ID
userdata['Vendor ID']=t_vendor_ID
userdata['Date']=t_day
userdata['Month']=t_month
userdata['Item List']=t_item_details
userdata.head(10)


# In[11]:


vendor_details=client['vendor']
d_vendor_name=[]
d_vendorID=[]
u_d=vendor_details.details
for nm in u_d.find():
   d_vendor_name.append(nm['name'])
   d_vendorID.append(nm['vendor ID'])
print(d_vendor_name)
print(d_vendorID)


# In[12]:


vendordata=pd.DataFrame(columns=['Vendor ID','Item','Price','Quantity','Total'])
vendordata


# In[13]:


v_items=vendor_details.items
l_n=[]
l_p=[]
l_q=[]
l_t=[]
v_ID=[]
for v_i in v_items.find():
   v_ID.append(v_i['vendor ID'])
   for it in v_i['item']:
        v_n=[]
        v_p=[]
        v_q=[]
        v_t=[]
        for i in it:
            v_n.append(i)
            v_p.append(it[i]["price"])
            v_q.append(it[i]["quantity"])
            v_t.append(it[i]["price"]*it[i]["quantity"])
        l_n.append(v_n)
        l_p.append(v_p)
        l_q.append(v_q)
        l_t.append(v_t)
print(l_n)
print(l_p)
print(l_q)
print(l_t)


# In[14]:


#vendordata=pd.DataFrame(columns=['Vendor ID','Item','Price','Quantity','Total'])
vendordata['Vendor ID']=v_ID
vendordata['Item']=l_n
vendordata['Price']=l_p
vendordata['Quantity']=l_q
vendordata['Total']=l_t
vendordata.head()


# ## Data Visualization
# 
# ###  Plotly and dash
# ### Vendor Data Analysis

# In[37]:


import plotly.graph_objs as go
import plotly.express as px
#import data_extraction as de
import plotly.offline as po
import pandas as pd

vd=vendordata
def bar_plot_items_listed(id):
    p_items=vd[vd['Vendor ID'] == id]['Item'].values
    p_total=vd[vd['Vendor ID'] == id]['Total'].values
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
bar_plot_items_listed('v200')


# In[16]:


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
pie_plot_items_listed('v100')


# In[17]:


transaction = userdata.groupby('Vendor ID') 
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
    transaction = userdata.groupby('Vendor ID') 
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


# In[21]:


monthly_sales('v300')


# ### User Data Analysis
# 

# In[22]:


userdata.head(10)


# In[36]:


transaction=userdata.groupby('User ID') 
transaction_vendor=transaction.get_group('b100') 
transaction_vendor.head(7)


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
    pp.show()
    po.plot(pp,filename=f'{month}.html',auto_open=True)


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
                                   
    pie_user_items.show()
    po.plot(pie_user_items,auto_open=True)


# In[34]:


def monthly_sales(user_id):
    transaction=userdata.groupby('User ID') 
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
    print(available_month)
    for i in available_month:
        monthly_sales=monthly.get_group(i)
        a=monthly_analysis_user(monthly_sales)
        user_bought_items.append(a)  


    print(user_bought_items)
    for month in range(len(available_month)):
        ind=m.index(available_month[month])
        mon_name=m_names[ind]
        bar_plot(user_bought_items[month][0],user_bought_items[month][1],mon_name)  
        pie_plot(user_bought_items[month][0],user_bought_items[month][1],mon_name)


# In[35]:


monthly_sales('b100')


# In[ ]:




