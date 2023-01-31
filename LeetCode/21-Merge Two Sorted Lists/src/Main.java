public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}


class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode iter1=list1;
        ListNode iter2=list2;

        if(iter1==null&& iter2==null){
            return null;
        }
        if(iter1==null){
            return iter2;
        }
        if(iter2==null){
            return iter1;
        }


        if(iter1.next==null&& iter2.next==null){
            if(iter1.val<iter2.val){
                iter1.next=new ListNode();
                iter1.next.val=iter2.val;
                iter1.next.next=null;
                return iter1;
            }
            iter2.next=new ListNode();
            iter2.next.val=iter1.val;
            iter2.next.next=null;
            return iter2;

        }



        while(iter1!=null){
            iter2=list2;


            if(iter2.val>iter1.val){
                ListNode temp=new ListNode();
                temp.val=iter1.val;
                temp.next=iter2;
                iter1=iter1.next;
                list2=temp;

                continue;
            }
            ListNode r =iter2;
            while(r.next!=null && r.next.val<iter1.val){
                r=r.next;
            }
            ListNode temp =new ListNode();
            temp.next = r.next;
            r.next=temp;
            temp.val=iter1.val;

            iter1=iter1.next;

        }

        return list2;




    }


}
