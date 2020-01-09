from back.bakery import BakeryOrders


class TestBakeryOrders:
    def test_get_orders(self):
        bo = BakeryOrders()
        lines = ['10 VS5']
        codes = ['VS5', 'MB11', 'CF']
        po = bo.process_order(lines=lines, codes=codes)
        assert po == True
