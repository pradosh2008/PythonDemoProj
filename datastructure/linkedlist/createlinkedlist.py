#create head and tail and intialize with null
#create a blank node and assign a value to it and reference it to null
#link head and tail with these node

#program to create single linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class SingleLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None


def main():
    sll=SingleLinkedlist()
    node1=Node(2)
    node2=Node(4)
    sll.head=node1
    #sll.head.next=node2
    node1.next=node2
    sll.tail=node2


if __name__ == '__main__':
    main()