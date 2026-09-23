from order_utils_2026_09_21 import parse_order, total_quantity, big_orders, totals_by_company
def load_orders(filename):
    new=[]
    with open(filename,"r") as f:
        for line in f:
            new.append(line.strip())
    return new
def save_customer_totals(customer_totals):
    with open("customer_totals.txt", "w") as f:
        for company, total in customer_totals.items():
            f.write(f"{company}: {total}\n")

orders = load_orders("orders.txt")
print(orders)
# 期望 ['SO1001,Apex Auto,12', 'SO1002,Apex Auto,12', ...]  五条订单字符串组成的列表
print(parse_order("SO1001,Apex Auto,12"))   # 期望 ('SO1001', 'Apex Auto', 12)
print(total_quantity(orders))               # 期望 52
print(big_orders(orders, 10))               # 期望 ['SO1001', 'SO1004']
print(totals_by_company(orders))            # 期望 {'Apex Auto': 20, 'Brightway': 12, 'Cornerstone': 20}
totals = totals_by_company(orders)

print(totals)

save_customer_totals(totals)