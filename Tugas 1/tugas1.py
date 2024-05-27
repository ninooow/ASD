class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertFirst(self,data):
        newNode = Node(data)
        if self.tail == None :
            self.tail = newNode
        if self.head != None:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
    def insertLast(self,data):
        newNode = Node(data)
        if self.head == None :
            self.head = newNode
        if self.tail != None :
            self.tail.next = newNode 
            newNode.prev = self.tail
        self.tail = newNode 
    def deleteFirst(self):
        current = self.head
        self.head = current.next
        if self.head != None:
            current = current.next
            current.prev = None
        else :
            self.tail = None
    def deleteLast(self):
        current = self.tail
        self.tail = current.prev
        if self.tail != None:
            current = self.tail
            current.next = None
        else:
            self.head = None
    def delete(self, data):
        current = self.head
        if data == self.head.data:
            current = self.head
            self.head = current.next
            if self.head != None:
                current = current.next
                current.prev = None
            else :
                self.tail = None
        elif data == self.tail.data:
            current = self.tail
            self.tail = current.prev
            if self.tail != None:
                current = self.tail
                current.next = None
            else:
                self.head = None
        else :
            while current != None :
                if current.data == data :
                    befcurrent = current.prev
                    aftcurrent = current.next
                    befcurrent.next = aftcurrent
                    aftcurrent.prev = befcurrent
                    break
                current = current.next
    def find(self,data):
        current = self.head
        isFound = False
        while current != None:
            if current.data == data:
                isFound = True
                break
            current = current.next
        if isFound :
            print(f"{data} ada")
        else:
            print(f"{data} tidak ada")
    def displayList(self):
        current  = self.head
        while current != None :
            print(current.data, end=" ")
            current = current.next
        print()
    
    def tukar(self):
        curHead = self.head
        nilaiHead = curHead.data
        self.head = curHead.next
        curHead = curHead.next
        curHead.prev = None
        
        curTail = self.tail
        nilaiTail = curTail.data
        self.tail=curTail.prev
        cur = curTail.prev
        curTail.next=None
        
        nodeHead = Node(nilaiTail)
        self.head.prev=nodeHead
        nodeHead.next=self.head
        self.head=nodeHead
        
        nodeTail = Node(nilaiHead)
        self.tail.next = nodeTail
        nodeTail.prev=self.tail
        self.tail=nodeTail
liss = LinkedList()
print("Insert First :")
liss.insertFirst(1)
liss.insertFirst(2)
liss.insertFirst(3)
liss.displayList()
print()

print("Insert Last :")
liss.insertLast(4)
liss.insertLast(5)
liss.insertLast(6)
liss.displayList()
print()

print("Delete First :")
liss.deleteFirst()
liss.displayList()
print()

print("Delete Last :")
liss.deleteLast()
liss.displayList()
print()

print("Delete : ")
liss.delete(1)
liss.delete(5)
liss.delete(4)
liss.displayList()
print()

print("Find : ")
liss.find(1)
liss.find(2)
liss.find(6)

liss.insertLast(4)
liss.insertLast(5)
liss.insertLast(6)
liss.displayList()
liss.tukar()
liss.displayList()
