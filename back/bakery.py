from back.colors import Colors
from back.divide import Calculation
from back.model import Bakery


class BakeryOrders():
    def __init__(self):
        # Add instance in Bakery
        obj1 = Bakery(name="Vegemite Scroll", code="VS5", packs=([3, 6.99], [5, 8.99]))
        obj2 = Bakery(name="Blueberry Muffin", code="MB11", packs=([2, 9.95], [5, 16.95], [8, 24.95]))
        obj3 = Bakery(name="Croissant", code="CF", packs=([3, 5.95], [9, 9.95], [9, 16.99]))

    def get_orders(self):
        codes = [instance.code for instance in Bakery.instances]  # Read codes of all instances in Bakery class

        while True:  # While True get multi lines input from input
            print(Colors.HEADER + "Please enter your order list, containing series of lines: " + Colors.ENDC)
            lines = []
            while True:
                line = input()
                if line:
                    lines.append(line)
                else:
                    return lines, codes

    def process_order(self, lines, codes) -> bool:
        print("--------- Start calculation entered datum ---------")
        for it in lines:
            inp = it.split(" ")
            if len(inp) == 2:
                for item in codes:
                    if item.__eq__(inp[1]):
                        try:
                            # Get all packs field from Bakery instances
                            packs = list([instance.packs for instance in Bakery.instances][item.index(inp[1])])
                            # Create instance of Calculation class and pass datum
                            cls = Calculation([x[0] for x in packs], int(inp[0]), packs)
                            # Start calculation
                            result = cls.calculate_sub_sequence()
                            # Process cost of order
                            x = cls.calculate_costs(result)
                            # Print datum
                            print(Colors.OKBLUE + "{} {} ${}".format(inp[0], inp[1], x[0]) + Colors.ENDC)
                            for m in x[1]:
                                print(Colors.OKBLUE + (' ' * (len(inp[0]) + len(inp[1]) + 2)) + "{}".format(
                                    m[0]) + Colors.ENDC)
                        except Exception as exp:
                            print("Error in processing: {}".format(exp))
            else:
                print("Entered value is not valid. Please enter two data seperated by space.\n")
                return False
        print("--------- End calculation entered datum ---------\n")
        return True
