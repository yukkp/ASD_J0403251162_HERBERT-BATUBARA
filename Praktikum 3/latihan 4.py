class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

 
    def merge(self, list2):
        result = LinkedList()

        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next

        temp = list2.head
        while temp:
            result.append(temp.data)
            temp = temp.next

        return result


# Contoh Program
list1 = LinkedList()
list1.append(3)
list1.append(7)
list1.append(12)

list2 = LinkedList()
list2.append(19)
list2.append(25)

print("List 1:")
list1.display()

print("List 2:")
list2.display()


list3 = list1.merge(list2)

print("Hasil gabungan:")
list3.display()
