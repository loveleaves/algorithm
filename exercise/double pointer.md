# 双指针

[TOC]

## 算法解释

双指针主要用于遍历数组，两个指针指向不同的元素，从而协同完成任务。也可以延伸到多
个数组的多个指针。

- 若两个指针指向同一数组，遍历方向相同且不会相交，则也称为滑动窗口（两个指针包围的
  区域即为当前的窗口），经常用于区间搜索。
- 若两个指针指向同一数组，但是遍历方向相反，则可以用来进行搜索，待搜索的数组往往是
  排好序的。

#### [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

``` c++
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int pos = n-- + m-- - 1;
    while(n >= 0 && m >= 0) {
        nums1[pos--] = nums1[m] > nums2[n] ? nums1[m--] : nums2[n--];
    }
    while(n >= 0) {
        nums1[pos--] = nums2[n--];
    }
}
```

#### [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

``` c++
vector<int> twoSum(vector<int>& numbers, int target) {
    int head = 0, tail = numbers.size() - 1;
    while(head <= tail) {
        int sum = numbers[head] + numbers[tail];
        if(sum == target) return {head + 1, tail + 1};
        else if(sum < target) ++head;
        else --tail;
    }
    return {-1,-1};
}
```

#### [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

``` c++
ListNode *detectCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast != nullptr) {
        slow = slow->next;
        if (fast->next == nullptr) {
            return nullptr;
        }
        fast = fast->next->next;
        if (fast == slow) {
            ListNode *ptr = head;
            while (ptr != slow) {
                ptr = ptr->next;
                slow = slow->next;
            }
            return ptr;
        }
    }
    return nullptr;
}
```



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



#### [567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)

``` c++
bool checkInclusion(string s1, string s2) {
    int n = s1.length(), m = s2.length();
    if (n > m)
    {
        return false;
    }
    vector<int> cnt(26);
    for (int i = 0; i < n; ++i)
    {
        --cnt[s1[i] - 'a'];
    }
    int left = 0;
    for (int right = 0; right < m; ++right)//右边界向右移动
    {
        int x = s2[right] - 'a';
        ++cnt[x];
        while (cnt[x] > 0)//左边界向右移动
        {
            --cnt[s2[left] - 'a'];//移出元素注意恢复其原始状态
            ++left;
        }
        if (right - left + 1 == n)
        {
            return true;
        }
    }
    return false;
}
```

#### [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)

``` c++
int trap(vector<int>& height) {
    int ans = 0;
    int left = 0, right = height.size() - 1;
    int leftMax = 0, rightMax = 0;
    while (left < right) {
        leftMax = max(leftMax, height[left]);
        rightMax = max(rightMax, height[right]);
        if (height[left] < height[right]) {
            ans += leftMax - height[left];
            ++left;
        } else {
            ans += rightMax - height[right];
            --right;
        }
    }
    return ans;
}
```

