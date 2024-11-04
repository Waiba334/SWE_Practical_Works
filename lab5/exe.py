#Implement a method to find the middle element of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

#Create a method to detect if the linked list has a cycle
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#Implement a method to remove duplicates from an unsorted linked list
    def remove_duplicates(self):
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next = current.next  # Remove the duplicate
            else:
                seen.add(current.data)
                prev = current
            current = current.next

#Add a method to merge two sorted linked lists into a single sorted linked list.
    def merge_sorted(self, other_list):
        dummy = Node(0)
        tail = dummy
        a = self.head
        b = other_list.head
        
        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        self.head = dummy.next

ll1 = LinkedList()
ll2 = LinkedList()

for value in [1, 3, 5, 7]:
    ll1.append(value)

for value in [2, 4, 6, 8]:
    ll2.append(value)

print("Middle of ll1:", ll1.find_middle())
print("Does ll1 have a cycle?", ll1.has_cycle())

ll1.remove_duplicates()
ll1.merge_sorted(ll2)

current = ll1.head
while current:
    print(current.data, end=" -> ")
    current = current.next