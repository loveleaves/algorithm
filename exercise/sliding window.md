# 滑动窗口

> 维持一个队列，两边界按要求移动。
>
> 如右移动：满足条件时右边界right向右移动（元素加入队列），不满足条件左边界left向右移动（元素移除队列）。

#### [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

使用无序集合容器使用find()函数

``` c++
int lengthOfLongestSubstring(string s) {
    if(s.size() == 0) return 0;
    unordered_set<char> lookup;//使用无序集合容器
    int maxStr = 0;
    int left = 0;
    for(int i = 0; i < s.size(); ++i)
    {
        while (lookup.find(s[i]) != lookup.end())
        {
            lookup.erase(s[left]);//向右滑动窗口
            ++left;
        }
        maxStr = max(maxStr,i-left+1);
        lookup.insert(s[i]);
    }
    return maxStr;
}
```

或根据题意使用数组存放对应字符的数量

``` c++
int lengthOfLongestSubstring(string s) {
    int freq[128] = {0};//存放所有字符数量，方便查看对应数量
    int left = 0, ans = 0;
    for(int j = 0; j < s.size(); ++j)
    {
        ++freq[s[j]];
        while(freq[s[j]]>1)
            --freq[s[left++]];//重复则向右滑动
        ans = max(ans,j-left+1);
    }
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
    vector<int> cnt1(26), cnt2(26);//整体比较
    //可不使用整体比较，在同一个vector上进行操作
    for (int i = 0; i < n; ++i)
    {
        ++cnt1[s1[i] - 'a'];
        ++cnt2[s2[i] - 'a'];
    }
    if (cnt1 == cnt2)
    {
        return true;
    }
    for (int i = n; i < m; ++i)
    {
        ++cnt2[s2[i] - 'a'];
        --cnt2[s2[i - n] - 'a'];
        if (cnt1 == cnt2)
        {
            return true;
        }
    }
    return false;
}
```



#### [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)



#### [30. 串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)



#### [209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)



#### [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)



#### [438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)



