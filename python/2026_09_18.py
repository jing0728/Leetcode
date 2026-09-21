"""场景

你从系统里导出了一批订单，每条是一个字符串，格式是 订单号,客户,数量：

python
orders = [
    "SO1001,Apex Auto,12",
    "SO1002,Brightway,5",
    "SO1003,Apex Auto,8",
    "SO1004,Cornerstone,20",
    "SO1005,Brightway,7",
]

第 1 步： 把每条订单打印成下面的样子。

SO1001: 12
SO1002: 5
SO1003: 8
SO1004: 20
SO1005: 7

第 2 步： 算出所有订单的总数量并打印。正确答案是 52。

第 3 步： 找出数量大于等于 10 的订单，把它们的订单号放进一个新列表并打印。正确答案是 ['SO1001', 'SO1004']。

挑战（选做）： 统计每个客户的总数量。正确答案是 Apex Auto 20，Brightway 12，Cornerstone 20。"""
orders = [
    "SO1001,Apex Auto,12",
    "SO1002,Brightway,5",
    "SO1003,Apex Auto,8",
    "SO1004,Cornerstone,20",
    "SO1005,Brightway,7",
]
"""
x=0
new=[]
customer_total={}
for i in range(0,len(orders)):
    text = orders[i].split(",")
    print(text[0],": ",text[2])
    x+=int(text[2])
    if int(text[2]) >= 10:
        new.append(text[0])
    customer_name = text[1]
    qty=int(text[2]) 
    if customer_name in customer_total:
        customer_total[customer_name]+=qty
    else:
        customer_total[customer_name]=qty
    

print("订单总数量是:",x)
print("数量大于10的订单是",new)
print(customer_total)
"""
"""
orders = [
    "SO1001,Apex Auto,12",
    "SO1002,Brightway,5",
    "SO1003,Apex Auto,8",
    "SO1004,Cornerstone,20",
    "SO1005,Brightway,7",
]
total=0
new=[]
customer_total={}
for order in orders:
    text = order.split(",")
    print(f"{text[0]}: {text[2]}")
    qty = int(text[2])
    so=text[0]
    company=text[1]
    total += qty
    if qty>=10:
        new.append(so)
    if company in customer_total:
        customer_total[company]+=qty
    else:
        customer_total[company]=qty

print("订单总数是：",total)
print("数量大于10的订单是",new)
print(customer_total)
"""

orders = [
    "SO1001,Apex Auto,12",
    "SO1002,Brightway,5",
    "SO1003,Apex Auto,8",
    "SO1004,Cornerstone,20",
    "SO1005,Brightway,7",
]

total=0
new=[]
customer_total={}
for order in orders:
    text = order.split(",")
    so,company,qty=text
    qty=int(qty)
    print(f"{so}: {qty}")
    total+=qty
    if qty >=10:
        new.append(so)
    if company in customer_total:
        customer_total[company]+=qty
    else:
        customer_total[company]=qty

print("订单总数是：",total)
print("数量大于10的订单是",new)
print(customer_total)