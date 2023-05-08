/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
// main.cpp
class Solution {
public:
    void insertAtTail(ListNode* &head,ListNode* &tail, int data){
      //Keep adding new digits at the end of list.
        ListNode* temp = new ListNode(data);
        if(!head){
            head = temp;
            tail = temp;
        }
        else{
            tail->next = temp;
            tail = temp;
        }
        return;
    }

    ListNode* addList(ListNode* l1, ListNode* l2){
    //Create a List named ans to store digits.
        int carry = 0;

        ListNode* ansHead = NULL;
        ListNode* ansTail = NULL;

        //Keep adding nodes(digits) in ans List until both input lists are null or carry becomes zero.
        while(l1 || l2 || carry){
            int val1 = 0;
            if(l1) val1 = l1->val;
            int val2 = 0;
            if(l2) val2 = l2->val;

            int sum = val1+val2+carry;
            int digit = sum%10;

            insertAtTail(ansHead,ansTail,digit);

            carry = sum/10;
            if(l1) l1=l1->next;
            if(l2) l2=l2->next;
        }
        return ansHead;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      // Since addition is performed from right hand side and List is already ordered in that fashion, We start adding digits.
        ListNode* ans = addList(l1,l2);
        return ans;
    }
};

// @lc code=end

