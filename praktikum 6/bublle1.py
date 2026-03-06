#=====================================
# Nama:herbert batubara
# kelas:TPL A/2
# Nim:J040321162
# Buble sort Ascending
#=====================================

def shortbubbleshort(alist):
    exchanges=True
    passnum=len(alist)-1
    while passnum>0 and exchanges:
        exchanges=False
        for i in range (passnum):
            if alist[i]> alist[i+1]:
                exchanges=True
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
        passnum=passnum-1
alist=[20,30,40,90,50,60,70,80,100,110]
shortbubbleshort(alist)
print(alist)
