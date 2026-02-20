#==============================
# nama= Herbert Batubara
# nim= J0403251162
# kelas= Tpl A/2
#==============================

#==============================
#Implementasi Dasar : Node Pada Linked List
#==============================

class Node:
    # Konstruktor yang DiJalankan secara otomatis ketika class note dipanggil
    def __init__(self, data):
        self.data=data #menyimpan nilai atau data pada list
        self.next=None # pointer ini menuju ke note berikutnya

    def is_empty(self):
        return self.front is None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    #membuat fungsi menambah  data baru pada bagian paling belakang
    
    def is_empty(self):
        return self.front is None

    def enqueue(self,data):
        nodeBaru=Node(data)
        
        if self.is_empty():
            self.front=nodeBaru
            self.rear=nodeBaru
            return
    
        self.rear.next=nodeBaru #letakkan data baru pada setelahnya rear
        self.rear=nodeBaru#jadikan data baru sebagai rear

    def dequeue(self):
        data_terhapus=self.front.data
        self.front=self.front.next

        if self.front is None:
            self.rear=None
        return data_terhapus

    def tampilkan(self):
        current=self.front
        print('front->',end='')
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print('Rear')

q=queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()

