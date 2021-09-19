#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;


struct ListNode {
    int val;
   ListNode *next;
   ListNode() : val(0), next(nullptr) {}
   ListNode(int x) : val(x), next(nullptr) {}
   ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *pre = nullptr, *q = nullptr;
        while (head) {
            q = head;
            head = head->next;
            q->next = pre;
            pre = q;
        }
        return q;
    }
};


void createList(ListNode* pHead){
    ListNode* p = pHead;
    for (int i = 1; i < 10; ++i) {
        ListNode* pNewNode = new ListNode;
        pNewNode->val = i;
        pNewNode->next = NULL;
        p->next = pNewNode;
        p = pNewNode;
    }
}

int main() {
    ListNode head;
    createList(&head);
    Solution solution;
    cout << head << endl;
    cout << solution.reverseList(head) << endl;
}