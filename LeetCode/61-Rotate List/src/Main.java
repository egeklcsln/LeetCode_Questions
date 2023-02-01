public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}


class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        ListNode r=head;
        int s=1;
        ListNode a;
        if(head==null){
            return null;
        }
        if(head.next==null){
            return head;
        }


        while(r.next!=null){
            r=r.next;
            s+=1;
        }
        if(k>s){
            k=k%s;
        }

        r.next=head;
        for(int i=0;i<k;i++){
            for(int j=1;j<s;j++){
                head=head.next;
            }
        }
        a=head;
        for(int p=1;p<s;p++){
            a=a.next;
        }
        a.next=null;
        return head;
    }
}