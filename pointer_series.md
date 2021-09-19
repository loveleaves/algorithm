# 指针三剑客



## 链表

### 介绍

由于每个节点存有一个值和一个指向下一个节点的指针 ==》递归

`LeetCode`默认链表格式如下：

``` c++
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
```

由于在进行链表操作时，尤其是删除节点时，经常会因为对当前节点进行操作而导致内存或指针出现问题。常用技巧：

- 1.尽量处理当前节点的下一个节点而非当前节点本身；
- 2.建立虚拟节点(dummy node)（或称哨兵），使其指向当前链表的头节点，结果返回dummy->next 即可。

**Note**

`LeetCode`提交代码无需进行内存回收，实际工程需考虑内存回收问题。

### 基本操作

#### [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)

``` c++
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
```



## 树



## 图

