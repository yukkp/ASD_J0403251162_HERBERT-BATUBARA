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

    def search(self, key):
        temp = self.head

        if temp is None:
            print("Linked List kosong")
            return

        while temp:
            if temp.data == key:
                print("Data",(key)," ditemukan")
                return
            temp = temp.next

        print("Data",key," tidak ditemukan")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Contoh Program
ll = LinkedList()
ll.append(3)
ll.append(7)
ll.append(12)
ll.append(19)
ll.display()

ll.search(12)
ll.search(10)
