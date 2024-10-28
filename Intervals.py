#  File: Intervals.py

#  Description: The intervals were merged and returned in ascending order. In addition, the intervals were sorted based on the size of the intervals in ascending order.

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 09/05/2022

#  Date Last Modified: 09/09/2022

import sys
# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(tuples_list):
    # The tuples are turned into lists
    tuples_list = ordering(tuples_list)
    tuples_list = [list(t) for t in tuples_list]
    merging = [tuples_list[0]]
    for i in range(len(tuples_list)):
        conditions_met = False
        for j in range(len(merging)):
            # The intervals are being tested for various conditions. Based on the conditions, the intervals from merging will change
            if (tuples_list[i][0] < merging[j][0] and tuples_list[i][1] > merging[j][1]):
                merging[j][0] = tuples_list[i][0]
                merging[j][1] = tuples_list[i][1]
                conditions_met = True
            elif (tuples_list[i][0] < merging[j][0] and tuples_list[i][0] <= merging[j][1] and tuples_list[i][1] <=
                  merging[j][1] and tuples_list[i][1] >= merging[j][0]):
                merging[j][0] = tuples_list[i][0]
                conditions_met = True
            elif (tuples_list[i][0] >= merging[j][0] and tuples_list[i][1] <= merging[j][1]):
                merging[j][0] = merging[j][0]
                conditions_met = True
            elif (tuples_list[i][0] >= merging[j][0] and tuples_list[i][0] <= merging[j][1] and tuples_list[i][1] >
                  merging[j][1]):
                merging[j][1] = tuples_list[i][1]
                conditions_met = True
        # A new interval is added if the conditions are not met.
        if conditions_met == False:
            merging.append(tuples_list[i])

    # The lists are converted back to tuples
    merging = [tuple(t) for t in merging]

    return ordering(merging)

# This returns the tuples in ascending order based on the first value in the tuple.
def ordering(tuples_list):
    ordered = []
    all_values = False
    # The mutable list removes the values that are added to ordered
    mutable_list = tuples_list
    # The while loop goes on until all values from tuple list are added to ordered
    while not all_values:
        value_change = False
        min_value = 100000000000
        min_tuple = ()
        # This loop determines the min value for the tuples
        for i in range(len(mutable_list)):
            first_value = mutable_list[i][0]
            if (first_value < min_value):
                min_value = mutable_list[i][0]
                min_tuple = mutable_list[i]
        # If an empty tuple is not returned, the min tuple is added to ordered. If not, the while loop stops.
        if min_tuple != ():
            ordered.append(min_tuple)
            mutable_list.remove(min_tuple)
        else:
            all_values = True
    return ordered

# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    # A dictionary was made with indexes and corresponding intervals
    size_interval = {}
    for i in range(len(tuples_list)):
        size_interval[i] = (tuples_list[i][1] - tuples_list[i][0])
    # A list was made with all the intervals. They were sorted in ascending order.
    order_size = []
    for i in range(len(tuples_list)):
        order_size.append((tuples_list[i][1] - tuples_list[i][0]))
    order_size = sorted(order_size)
    # A list of the sorted intervals is made
    size_sorted = []
    i = 0
    # The while loop runs until size_sorted has all the tuples
    while i < (len(tuples_list) - 1):
        # if there are multiple tuples with the same size, ordered is called to order them in ascending order
        if (order_size[i] == order_size[i+1]):
            tuples = []
            for key in size_interval:
                if(size_interval[key] == order_size[i]):
                    tuples.append(tuples_list[key])
                    i = i + 1
            list_tuples = ordering(tuples)
            for j in range(len(list_tuples)):
                size_sorted.append(list_tuples[j])
        else:
            for key in size_interval:
                if (size_interval[key] == order_size[i]):
                    size_sorted.append(tuples_list[key])
            i = i + 1
    if len(size_sorted) != len(tuples_list):
        for key in size_interval:
            if (size_interval[key] == order_size[len(order_size)-1]):
                size_sorted.append(tuples_list[key])
    return size_sorted

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
    assert merge_tuples([(1,2)]) == [(1,2)]
    # write your own test cases
    assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
    # write your own test cases
    assert merge_tuples([(-1, 5), (4, 6)]) == [(-1, 6)]
    assert sort_by_interval_size([(-2, 4), (-6, -5)]) == [(-6, -5), (-2, 4)]
    assert sort_by_interval_size([(-25, -14), (-5, -4), (-1, 0), (-3, -2)]) == [(-5, -4), (-3, -2), (-1, 0), (-25, -14)]
    assert merge_tuples([(-1, 0), (-1, 0), (-1, 0)]) == [(-1, 0)]

    return "all test cases passed"
    pass

def main():
    # The file is read in and all the tuples are inputed
    tuple_lst = []
    interval_file = sys.stdin
    for i in range(int(interval_file.readline().strip())):
        line = str(interval_file.readline().strip())
        lst_tuple = line.split()
        lst_tuple[0] = int(lst_tuple[0])
        lst_tuple[1] = int(lst_tuple[1])
        lst_tuple = tuple(lst_tuple)
        tuple_lst.append(lst_tuple)
    # merge the list of tuples
    tuple_lst = merge_tuples(tuple_lst)
    print(tuple_lst)
    # sort the list of tuples according to the size of the interval
    print(sort_by_interval_size(tuple_lst))
    # run your test cases
    # print(test_cases())
    # print(merge_tuples([(0, 100), (0,100)]))
    # print(sort_by_interval_size([(0, 100), (0,100)]))

  # write the output list of tuples from the two functions
  # [(-25, -14), (-10, -3), (2, 6), (12, 18), (22, 30)]
  # [(2, 6), (12, 18), (-10, -3), (22, 30), (-25, -14)]

if __name__ == "__main__":
  main()