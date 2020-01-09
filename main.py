from back.bakery import BakeryOrders

if __name__ == '__main__':
    bo = BakeryOrders()
    lines, codes = bo.get_orders()
    bo.process_order(lines=lines, codes=codes)
