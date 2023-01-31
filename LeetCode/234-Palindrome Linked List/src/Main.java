import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode r = head;
        boolean bool = true;
        int s;
        ArrayList<Integer> numberList = new ArrayList<Integer>();
        if(head==null){
            return false;
        }
        if(head.next==null){
            return true;
        }
        while(r!=null){
            numberList.add(r.val);
            r=r.next;
        }
        s=numberList.size()-1;
        for(int i=0;i<((int)(numberList.size())/2);i++){
            if(numberList.get(i)!=numberList.get(s)){
                bool=false;
                break;
            }
            s-=1;
        }
        return bool;






    }
}
