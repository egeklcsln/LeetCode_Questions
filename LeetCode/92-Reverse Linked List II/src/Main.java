import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}


class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode a=head;
        ListNode b;
        ListNode temp;
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        if(head==null){
            return null;
        }
        if(head.next==null){
            return head;
        }
        for(int i=1;i<left;i++){
            a=a.next;
        }
        b=a;
        for(int j=0;j<right-left+1;j++){
            numbers.add(a.val);
            a=a.next;
        }

        for(int k=numbers.size()-1;k>-1;k--){
            b.val=numbers.get(k);
            b=b.next;
        }

        return head;





    }
}
