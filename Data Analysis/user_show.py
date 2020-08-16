from user import monthly_sales

ms1,ms2=monthly_sales('b100')

with open('u.html','w') as f:
    for i in range(len(ms1)):
        f.write(ms1[i].to_html(full_html=False))
        f.write(ms2[i].to_html(full_html=False))