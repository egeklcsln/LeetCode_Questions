public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sumList = new ListNode();
        ListNode sumListİ=sumList;
        int l1_val=0;
        int l2_val=0;
        int k=0;
        while(l1!=null||l2!=null ){
            if(l1!=null){
                l1_val=l1.val;
                l1=l1.next;
            }
            else{
                l1_val=0;
            }
            if(l2!=null){
                l2_val=l2.val;
                l2=l2.next;
            }
            else{
                l2_val=0;
            }

            sumListİ.val=(l1_val + l2_val +k)%10;
            if(l1!=null || l2!=null){
                sumListİ.next=new ListNode();
                sumListİ=sumListİ.next;
            }


            if((l1_val + l2_val + k)>=10){
                k=1;
            }
            else{
                k=0;
            }
        }

        sumListİ.next=null;

        if(k==1){
            sumListİ.next=new ListNode();
            sumListİ.next.val=1;
            sumListİ.next.next=null;
        }





        return sumList;




    }
}
