import pymongo as p


# In[2]:


client=p.MongoClient("mongodb+srv://swarnabha:swarnabha_db@cluster0.4igvr.mongodb.net/BytePyper?retryWrites=true&w=majority")


# ## Testing

# In[3]:


#print(client.list_database_names())


# In[4]:


ven=client['vendor']
ven_details=ven.vendors
# for d in ven_details.find():
#     print(d)


# # In[5]:


# ven_item=ven.items
# for d in ven_item.find():
#     print(d['item'])


# In[6]:


# ven_item=ven.items
# for d in ven_item.find():
#    print("Vendor name : ",d['vendor ID']) 
#    for item in d['item']:
#       for i in item:
#             print(i)
#             print(item[i]['price'])
#             print(item[i]['quantity'])
#             print("total Amount: ",(item[i]['price']*item[i]['quantity']))
   


# ## Database Extraction starts

# In[7]:


import pandas as pd
userdata=pd.DataFrame(columns=['User ID','Vendor ID','Date','Month','Item List'])



# In[8]:


user_details=client['user']
d_user_name=[]
d_userID=[]
u_d=user_details.user_regs
for nm in u_d.find():
   d_user_name.append(nm['name'])
   d_userID.append(nm['buyer ID'])
#print(d_user_name)
#print(d_userID)


# In[9]:



u_t=user_details.transactions
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
            
# print(t_item_details)
# print(t_day)
# print(t_month)
# print(t_vendor_ID)
# print(t_user_ID) 
    
    


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
#print(d_vendor_name)
#print(d_vendorID)


# In[12]:


vendordata=pd.DataFrame(columns=['Vendor ID','Item','Price','Quantity','Total'])
vendordata


# In[13]:


v_items=vendor_details.list_items
l_n=[]
l_p=[]
l_q=[]
l_t=[]
v_ID=[]
for v_i in v_items.find():
   v_ID.append(v_i['vendor ID'])
   for it in v_i['Items']:
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
# print(l_n)
# print(l_p)
# print(l_q)
# print(l_t)


# In[14]:


#vendordata=pd.DataFrame(columns=['Vendor ID','Item','Price','Quantity','Total'])
vendordata['Vendor ID']=v_ID
vendordata['Item']=l_n
vendordata['Price']=l_p
vendordata['Quantity']=l_q
vendordata['Total']=l_t
#print(vendordata.head())
#print(userdata.head())
