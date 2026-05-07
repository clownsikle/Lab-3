import Lab3 as Lab3
print("Test_Lab3")


def test_SortAscending():
    test_array = [55,88,33,44,99,100,80,67,76]
    sorted_array = [33,44,55,67,76,80,88,99,100]
    assert(Lab3.bubble_sort(test_array,Lab3.SORT_ASCENDING) == sorted_array)

def test_SortDescending():
    test_array = [55,88,33,44,99,100,80,67,76]
    sorted_array = [100,99,88,80,76,67,55,44,33]
    assert(Lab3.bubble_sort(test_array,Lab3.SORT_DESCENDING) == sorted_array)
    
def test_nMorethanequal10():
    test_array = [1,3,7,5,2,4,6,9,8,11,10]
    assert(Lab3.bubble_sort(test_array,Lab3.SORT_DESCENDING) == 1)

def test_ZeroNumbers():
    test_array = []
    assert(Lab3.bubble_sort(test_array,Lab3.SORT_DESCENDING) == 0)

def test_nonINT():
    test_array = [55,88,33,44,99,100,80,67,"Yo"]
    assert(Lab3.bubble_sort(test_array,Lab3.SORT_ASCENDING) == 2)