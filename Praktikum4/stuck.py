#==============================
# nama= Herbert Batubara
# nim= J0403251162
# kelas= Tpl A/2
#==============================

#==============================
#Implementasi Dasar Stuck
#==============================

class Node:
    # Konstruktor yang DiJalankan secara otomatis ketika class note dipanggil
    def __init__(self, data):
        self.data=data #menyimpan nilai atau data pada list
        self.next=None # pointer ini menuju ke note berikutnya

#Stack ada operasi push (Memasukkan head baru)dan pop (menghapus Head)

class stack:
    def __init__(self):
        self.top= None #top menuju ke nod epaling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None
    
    def push(self,data):
        #1 membuat node baru
        nodeBaru=Node(data)

        #2 node baru menuju ke top yang lama (head yang lama)
        nodeBaru.next=self.top

        #3 geser top pindah ke node baru
        self.top=nodeBaru

    def pop(self):# mengambil/menghapus node paling atas
        if self.is_empty():
            print('Stack kosong,tidak bisa pop')
            return None
        data_terhapus=self.top.data
        #A->None
        self.top=self.top.next
        return data_terhapus

    def peek(self):
        #melihat data yang paling atas
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        current=self.top
        print('Top:', end=" ")
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print('None')

s=stack()
s.push('A')
s.push('B')
s.push('C')
s.tampilkan()
print('Peek(lihat Top):', s.peek())
s.pop
s.tampilkan
