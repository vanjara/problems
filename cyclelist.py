# /usr/bin/python2.7

# Converting Sam's Java code to Python

from nose.tools import assert_equal


class Node (object):
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithm using extra space. Mark visited nodes and check that you
# only visit each node once.
def hasCycle(node):
    visited = set()
    current = node

    while current is not None:
        if current in visited:
            return True
        else:
            visited.add(current)
        current = current.next

    return False


# Floyd's algorithm. Increment one pointer by one and the other by two.
# If they are ever pointing to the same node, there is a cycle.
# Explanation is at:
# https://www.quora.com/How-does-Floyds-cycle-finding-algorithm-work
def hasCycleFloyd(node):

    if node is None:
        return False
    slow = node
    fast = node.next

    while fast is not None and fast.next is not None:
        if (fast == slow):
            return True

        fast = fast.next.next
        slow = slow.next

    return False


# Tests
# Test Case 1 - create a cyclical linked list
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a  # Cycle Here!


# Test Case 2 - not a cycle
a1 = Node(4)
b1 = Node(5)
c1 = Node(6)

a1.next = b1
b1.next = c1

# Test Case 3 - None
a2 = None

# Test Case 4 - Single Node
a3 = Node(1)

# Test Case 5 - Single Node linked to itself
a4 = Node(1)
a4.next = a4


# Define Class for Testing
class TestLinkedListCycle(object):

    def test(self, sol):
        print "Testing Case 1 -- Cycle"
        assert_equal(sol(a), True)  # Case 1 - cycle
        print "Testing Case 2 -- Not a Cycle"
        assert_equal(sol(a1), False)  # Case 2 - not a cycle
        print "Testing Case 3 -- None"
        assert_equal(sol(a2), False)  # Case 3 - None
        print "Testing Case 4 -- Single Node"
        assert_equal(sol(a3), False)  # Case 4 - Single Node, not a cycle
        print "Testing Case 5 -- Single Node Cycle"
        assert_equal(sol(a4), True)  # Case 5 - Single Node cycle

        print "Passed all test cases"


# Run Tests
myTest = TestLinkedListCycle()
myTest.test(hasCycle)
# Test Floyd's algorithm implementation
myTest.test(hasCycleFloyd)
