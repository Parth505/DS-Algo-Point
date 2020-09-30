class Node:
    def __init__(self , value):
        self.value  = value
        self.Next = None


class solution:
    def reverseLinkedList(self , head):
        prev  =  None 
        while head:
            temp = head 
            head = head.Next 
            temp.Next = prev 
            prev = temp 
        return prev
    
    
    
    




            