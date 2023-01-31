public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}


class Solution {
    public ListNode reverseList(ListNode head) {
        if(head==null){
            return head;
        }
        ListNode current=head;
        ListNode prev=null;
        ListNode next=null;

        while(current!=null){
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }

        return prev;





    }
}
