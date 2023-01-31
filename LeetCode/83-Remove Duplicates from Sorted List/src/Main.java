public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}


class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode r=head;
        while(r!=null && r.next!=null){
            if(r.val == r.next.val){
                r.next=r.next.next;
            }
            else{
                r=r.next;
            }

        }
        return head;


    }
}