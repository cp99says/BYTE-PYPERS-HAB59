from vendor import listed_products,monthly_sales

lp1,lp2=listed_products('v100')
ms1,ms2=monthly_sales('v100')


with open('v.html','w') as f:
    for i in range(len(lp1)):
        f.write(lp1[i].to_html(full_html=False))
        f.write(lp2[i].to_html(full_html=False))
    for i in range(len(ms1)):
        f.write(ms1[i].to_html(full_html=False))
        f.write(ms2[i].to_html(full_html=False))