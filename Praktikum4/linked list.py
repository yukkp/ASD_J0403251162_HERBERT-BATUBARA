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

#1)Membuat node dengan instransi class node
nodeA=Node("A")
nodeB=Node("B")
nodeC=Node("C")

#2)Menghubungkan  Node :A->B->C->None
head=nodeA
nodeA.next=nodeB
nodeB.next=nodeC

#3)Tranversal :Menelusuri node dari head sampai ke None
current=head
while current is not None:
    print(current.data) #menampilkan data dari note ini 
    current=current.next# pindah ke note berikutnya


