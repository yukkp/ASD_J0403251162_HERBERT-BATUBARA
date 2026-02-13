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

    def delete_node(self, key):
        temp = self.head


        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Data tidak ditemukan")
            return

        prev.next = temp.next
        print("Data berhasil dihapus")

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

print("Sebelum dihapus:")
ll.display()

ll.delete_node(12)

print("Sesudah dihapus:")
ll.display()

