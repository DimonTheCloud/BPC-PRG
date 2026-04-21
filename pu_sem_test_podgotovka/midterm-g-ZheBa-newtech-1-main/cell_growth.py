# import csv
# cell_growth_1 = ("data/cell_growth_0.csv")
# with open(cell_growth_1, "r") as cell_obj:
#     reader0 = csv.reader(cell_obj)
#     list1 = list(reader0)
# for time in list1:
#     times = time[3]
#     print(times)
# for cell in list1:
#     cells = cell[4]
#     print(cells)
# print(reader0)
# print(list1)
# def growth_0():
#     cell_growth_1 = ('data\cell_growth_0.csv')
#     with open(cell_growth_1, "r") as cell_obj:
#         reader0 = csv.reader(cell_obj)
#         list1 = list(reader0)
#     return list1
# def growth_1():
#     cell_growth_2 = ('data\cell_growth_0.csv')
#     with open(cell_growth_2, "r") as cell2_obj:
#         reader1 = csv.reader(cell2_obj)
#         list2 = list(reader1)
#     return list2
# def get_growth_rates(list1, list2):
def get_growth_rates(times, cell_count):
    i = 0
    result = []
    length = len(times)
    for time in range(length):
        i += 1
        result1 = times[i] - times[(i - 1)]
        result2 = cell_count[i] - cell_count[(i - 1)]
        result3 = result2 / result1
        result.append(result3)
    return result

def get_growth_phases(growth_rates):
    result21 = []
    for rates in growth_rates:
        if rates <= 10.0:
            result21.append('stationary')
        if rates >= 20.0 and rates <= 80.0:
            result21.append('lag')
        if rates > 80.0:
            result21.append('log')

    return result21

# times = [0.0, 2.0, 3.0, 4.0, 6.0]
# cell_count = [100.0, 120.0, 160.0, 210.0, 240.0]
# result = []
# i = 0
# length = len(times)
# for i in range(length):
#
#     i += 1
#     result1 = times[i] - times[(i - 1)]
#     result2 = cell_count[i] - cell_count[(i - 1)]
#     result3 = result2 / result1
#     result.append(result3)
#
#     print(result)








if __name__ == "__main__":
    times = [0.0, 2.0, 3.0, 4.0, 6.0]
    cell_count = [100.0, 120.0, 160.0, 210.0, 240.0]
