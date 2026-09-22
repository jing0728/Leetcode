orders = [
    "SO1001,Apex Auto,12",
    "SO1002,Brightway,5",
    "SO1003,Apex Auto,8",
    "SO1004,Cornerstone,20",
    "SO1005,Brightway,7",
]
def parse_order(line):
    so,company,qty=line.split(",")
    return so,company,int(qty)

def total_quantity(orders):
    total=0
    for qty in orders:
        so,company,qty=parse_order(qty)
        total+=qty
    return total

def big_orders(orders, min_qty):
    ans=list()
    for order in orders:
        so,company,qty=parse_order(order)
        if qty>=min_qty:
            ans.append(so)
    return ans
def totals_by_company(orders):
    ans={}
    for order in orders:
        so,company,qty=parse_order(order)
        ans[company]=ans.get(company,0)+qty
    return ans

print(parse_order("SO1001,Apex Auto,12"))   # 期望 ('SO1001', 'Apex Auto', 12)
print(total_quantity(orders))               # 期望 52
print(big_orders(orders, 10))               # 期望 ['SO1001', 'SO1004']
print(big_orders(orders, 8))                # 期望 ['SO1001', 'SO1003', 'SO1004']
print(totals_by_company(orders))            # 期望 {'Apex Auto': 20, 'Brightway': 12, 'Cornerstone': 20}