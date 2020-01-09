# Calculate cost of orders in Bakery
class Calculation:
    def __init__(self, array, num, costs):
        """
        :param array: List of packs
        :param num:   Number of total orders
        :param costs: List of costs
        :return:
        """
        self.array = array
        self.num = num
        self.costs = costs

    # Calculation method
    def calculate_sub_sequence(self) -> list:
        Opt = [0 for i in range(0, self.num + 1)]
        sets = {i: [] for i in range(self.num + 1)}
        for i in range(1, self.num + 1):
            smallest = float("inf")
            for j in range(0, len(self.array)):
                if self.array[j] <= i:
                    smallest = min(smallest, Opt[i - self.array[j]])
                    if smallest == Opt[i - self.array[j]]:
                        sets[i] = [self.array[j]] + sets[i - self.array[j]]
            Opt[i] = 1 + smallest
        return sorted(sets[self.num])

    def calculate_costs(self, res) -> tuple:
        """
        :param res: Conditions of packs such as [2, 2, 2, 8]
        :return: Tuple variable that contain cost of total orders and per each pack
        """
        x, p = 0, []
        for i in list(set(res)):
            x += res.count(i) * [x for x in self.costs if x[0].__eq__(i)][0][1]
            p.append(["{} * {} ${}".format(res.count(i), i, [x for x in self.costs if x[0].__eq__(i)][0][1])])

        return x, p

# c = calculation([3, 5], 10, [[3, 6.99], [5, 8.99]])
# c = Calculation([2, 5, 8], 14, [[2, 9.95], [5, 16.95], [8, 24.95]])
# x = c.calculate_sub_sequence()
# p = c.calculate_costs(x)
# print(p)
