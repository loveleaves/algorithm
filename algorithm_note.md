# algorithm-note



### leetcode-28 实现[strStr()](https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode-solution-ds6y/)

> 本题是经典的**字符串单模匹配**的模型，因此可以使用字符串匹配算法解决，常见的字符串匹配算法包括暴力匹配、Knuth-Morris-Pratt 算法、Boyer-Moore 算法、Sunday 算法等，官方解法讲解 Knuth-Morris-Pratt 算法。



## 二分查找

> `left + ((right -left) >> 1)` 其实和 `(left + right) / 2`是等价的，这样写的目的一个是为了防止 `(left + right)`出现溢出，一个是用右移操作替代除法提升性能。

> `left + ((right -left) >> 1)` 对于目标区域长度为奇数而言，是处于正中间的，对于长度为偶数而言，是中间偏左的。因此左右边界相遇时，只会是以下两种情况：

- `left/mid` , `right` (left, mid 指向同一个数，right指向它的下一个数)
- `left/mid/right` （left, mid, right 指向同一个数）



### 动态规划

> [背包九讲专题](https://www.bilibili.com/video/BV1qt411Z7nE?from=search&seid=3231012459135651472)
>
> [背包九讲blog](https://www.cnblogs.com/jbelial/articles/2116074.html)
>
> 



