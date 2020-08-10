#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pymongo as p


# In[32]:


client=p.MongoClient("mongodb://localhost:27017/")


# ## Testing

# In[33]:


print(client.list_database_names())


# In[34]:


ven=client['vendor']
ven_details=ven.details
for d in ven_details.find():
    print(d)


# In[35]:


ven_item=ven.items
for d in ven_item.find():
    print(d['item'])


# In[36]:


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

# In[37]:


import pandas as pd
userdata=pd.DataFrame(columns=['User ID','Vendor ID','Date','Month','Item List'])
userdata


# In[38]:


user_details=client['buyer']
d_user_name=[]
d_userID=[]
u_d=user_details.details
for nm in u_d.find():
   d_user_name.append(nm['name'])
   d_userID.append(nm['buyer ID'])
print(d_user_name)
print(d_userID)


# In[39]:


m=['01','02','03','04','05','06','07','08','09','10','11','12']
m_names=['January','February','March','April','May','June','July','August','September',
         'October','November','December']
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
    
    


# In[41]:


#userdata=pd.DataFrame(columns=['User ID','Vendor ID','Date','Month','Item List'])

userdata['User ID']=t_user_ID
userdata['Vendor ID']=t_vendor_ID
userdata['Date']=t_day
userdata['Month']=t_month
userdata['Item List']=t_item_details
userdata.head(10)


# In[46]:


vendor_details=client['vendor']
d_vendor_name=[]
d_vendorID=[]
u_d=vendor_details.details
for nm in u_d.find():
   d_vendor_name.append(nm['name'])
   d_vendorID.append(nm['vendor ID'])
print(d_vendor_name)
print(d_vendorID)


# In[68]:


vendordata=pd.DataFrame(columns=['Vendor ID','Item','Price','Quantity','Total'])
vendordata


# In[69]:


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


# In[70]:


#vendordata=pd.DataFrame(columns=['Vendor ID','Item','Price','Quantity','Total'])
vendordata['Vendor ID']=v_ID
vendordata['Item']=l_n
vendordata['Price']=l_p
vendordata['Quantity']=l_q
vendordata['Total']=l_t
vendordata.head()


# In[ ]:




