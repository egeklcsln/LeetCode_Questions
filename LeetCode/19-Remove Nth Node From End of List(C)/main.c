struct ListNode {
      int val;
      struct ListNode *next;
  };
 
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
 struct ListNode* iter=head;
 struct ListNode* iter3=head;
 struct ListNode* iter4=head;
 struct ListNode* temp;

 int s=1;
if(head==NULL){
return head;
}

if(head->next==NULL && n==1){
    free(head);
    head=NULL;
    return head;
}
if(head->next==NULL && n==2){
    iter=head->next;
    free(head);
    head=iter;
    return head;
}


while(iter->next!=NULL){
    iter=iter->next;
    s=s+1;
}

if(s==2 && n==2){
iter4=head->next;
free(head);
head=iter4;
return head;
}
if(s==2 && n==1){
iter4=head->next;
free(iter4);
head->next=NULL;
return head;
}
if(s==n){
    iter4=head;
    head=head->next;
    free(iter4);
    return(head);
}









s= s-n;
struct ListNode* iter2=head;
for(int i=1;i<s;i++){
    iter2=iter2->next;
}


temp=iter2->next;
iter2->next=iter2->next->next;
free(temp);

return head;


}
int main(int argc, char *argv[]) {
	return 0;
}