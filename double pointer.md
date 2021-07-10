# 双指针

使用两个指针head和tail进行前后位置确定。



#### [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

``` c++
void moveZeroes(vector<int>& nums) {
    int head = 0,tail = 0,n = nums.size();
    while(head < n && tail < n-1)
    {
        if(nums[head] == 0)
        {
            tail = tail >=head ? tail : (head == n-1 ? n-2 : head);
            swap(nums[head],nums[++tail]);
        }
        else ++head;
    }
}
```



#### [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

``` c++
vector<int> twoSum(vector<int>& numbers, int target) {
    int head = 0, tail = numbers.size() - 1;
    while(head <= tail)
    {
        int sum = numbers[head] + numbers[tail];
        if(sum == target) return {head + 1, tail + 1};
        else if(sum < target) ++head;
        else --tail;
    }
    return {-1,-1};
}
```



#### [557. 反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)

``` c++
string reverseWords(string s) {
    int length = s.length();
    int i = 0;
    while (i < length) {
        int start = i;
        while (i < length && s[i] != ' ') {
            i++;
        }

        int left = start, right = i - 1;
        while (left < right) {
            //swap(s[left++], s[right--]);注意swap实现方式
            char temp = s[left];
            s[left++] = s[right];
            s[right--] = temp;
        }
        while (i < length && s[i] == ' ') {
            i++;
        }
    }
    return s;
}
```



#### [19. 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

> 在对链表进行操作时，一种常用的技巧是添加一个哑节点（dummy node），它的next 指针指向链表的头节点。这样我们就不需要对头节点进行特殊的判断了。
>
> 比如此题删除头节点时要进行特殊判断。
>
> 同时删除节点问题要考虑被删除节点的空间释放问题，下面不考虑。

``` c++
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode* dummy = new ListNode(0, head);//增加哑节点避免特殊判断
    ListNode* first = head;
    ListNode* end = dummy;
    for (int i = 0; i < n; ++i) {
        first = first->next;
    }
    while (first) {
        first = first->next;
        end = end->next;
    }
    end->next = end->next->next;
    ListNode* ans = dummy->next;
    delete dummy;
    return ans;
}
```

