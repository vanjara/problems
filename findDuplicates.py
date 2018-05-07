# /usr/bin/python2.7

# Converting Sam's Java code to Python for FindDuplicates
# https://github.com/samgh/Byte-by-Byte-Solutions/blob/master/java/FindDuplicates.java

from nose.tools import assert_equal


def findDuplicates(arr):

    resultSet = set()
    for i in range(len(arr)):

        index = abs(arr[i]) - 1

        if arr[index] < 0:
            resultSet.add(abs(arr[i]))
        else:
            arr[index] = - arr[index]

    for i in range(len(arr)):
        arr[i] = abs(arr[i])

    return resultSet


# a = [1,2,3]
# b = [1,2,1,2]
# c = [3,3,3]
# d = []

# print findDuplicates(a)
# print findDuplicates(b)
# print findDuplicates(c)
# print findDuplicates(d)

# Define Class for Testing
class TestDuplicates(object):

    def test(self, result):
        print "Length 1, no duplicates"
        assert_equal(result([1]), set([]))
        print "Length 2, no duplicates"
        assert_equal(result([1, 2]), set([]))
        print "Length 2, duplicates"
        assert_equal(result([1, 1]), set([1]))
        print "Length 4, no duplicates"
        assert_equal(result([1, 2, 3, 4]), set([]))
        print "Length 4, one duplicate"
        assert_equal(result([1, 1, 2, 3]), set([1]))
        print "Length 4, two duplicates"
        assert_equal(result([1, 1, 2, 2]), set([1, 2]))
        print "Length 4, repeated 4 times"
        assert_equal(result([1, 1, 1, 1]), set([1]))
        print "Passed all test cases"


# Run Tests
myTest = TestDuplicates()
myTest.test(findDuplicates)
