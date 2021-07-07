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

