import java.lang.Math;
import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}


class Solution {
    public int getDecimalValue(ListNode head) {
        ListNode r=head;
        ListNode i=head;
        int s=0;
        int number=0;
        ArrayList<Integer> numberList = new ArrayList<Integer>();
        while(r!=null){
            numberList.add(r.val);
            r=r.next;
        }
        s=numberList.size() - 1;
        for(int k=0;k<numberList.size();k++){
            number+=(numberList.get(k))*(Math.pow(2,s));

            s-=1;
        }
        return number;







    }
}