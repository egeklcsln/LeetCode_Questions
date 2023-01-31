public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}


class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode r=head;
        ListNode i=head;
        int s=0;
        while(r!=null){
            r=r.next;
            s+=1;
        }
        if(s%2==1){
            for(int k=0;k<(int)(s/2);k++){
                i=i.next;
            }
        }
        else{
            for(int k=0;k<(s/2);k++){
                i=i.next;
            }
        }




        return i;




    }
}
