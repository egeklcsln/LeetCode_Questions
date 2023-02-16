# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if(head==None):
            return None
        

        if head.next==None:
            return None
        
        if head.next.next==head:
            return head
        
       
        a=head
        list = []
        while a.next!=None:
            if  a in list:
                return a
                  
            
            

            list.append(a)
            a=a.next


        
        return None