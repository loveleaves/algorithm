# greedy algorithm



#### [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/)

### 解题思路

> 优先考虑剩下孩子里饥饿度最小的孩子

``` c++
int child = 0, cookie = 0;
while (child < g.size() && cookie < s.size())
{
    if (g[child] <= s[cookie]) ++child;
    ++cookie;
}
return child;
```



#### [135. 分发糖果](https://leetcode-cn.com/problems/candy/)

### 解题思路

> 只需要简单的两次遍历即可：首先把所有孩子的糖果数初始化为1；
>
> 先从左往右遍历一遍，如果右边孩子的评分比左边的高，则右边孩子的糖果数更新为左边孩子的
> 糖果数加1；再从右往左遍历一遍，如果左边孩子的评分比右边的高，且左边孩子当前的糖果数
> 不大于右边孩子的糖果数，则左边孩子的糖果数更新为右边孩子的糖果数加1
>
> 在每次遍历中，只考虑并更新相邻一侧的大小关系

``` c++
int candy(vector<int>& ratings) {
    int size = ratings.size();
    if (size < 2) return size;
    vector<int> num(size,1);
    for(int i = 1; i < size; ++i)
    {
        if (ratings[i] > ratings[i-1]) num[i] = num[i-1] + 1;
    }
    for(int i = size - 1; i > 0; --i)
    {
        if (ratings[i-1] > ratings[i]) num[i-1] = max(num[i-1],num[i] + 1);
    }
    return accumulate(num.begin(),num.end(),0);//注意accumulate返回值类型为第三个参数的类型
}
```

或使用**常数空间遍历**

``` c++
int candy(vector<int>& ratings) {
    int n = ratings.size();
    int ret = 1;
    int inc = 1, dec = 0, pre = 1;
    for (int i = 1; i < n; i++) {
        if (ratings[i] >= ratings[i - 1]) {
            dec = 0;
            pre = ratings[i] == ratings[i - 1] ? 1 : pre + 1;
            ret += pre;
            inc = pre;
        } else {
            dec++;
            if (dec == inc) {
                dec++;
            }
            ret += dec;
            pre = 1;
        }
    }
    return ret;
}
```



#### [435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)

``` c++
//优先保留结尾小且不相交的区间
int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    int n = intervals.size();
    sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    int removed = 0, prev = intervals[0][1];
    for (int i = 1; i < n; ++i)
    {
        if (intervals[i][0] < prev) ++removed;
        else prev = intervals[i][1];
    }
    return removed;
}
```



#### [605. 种花问题](https://leetcode-cn.com/problems/can-place-flowers/)

``` c++
//模拟法
bool canPlaceFlowers(vector<int>& flowerbed, int n) {
    int i, size = flowerbed.size();
    if (size == 1) {
        if (flowerbed[0] == 0) n--;
    }
    else if (size == 2) {
        if (flowerbed[0] == 0 && flowerbed[1] == 0)
            n--;
    }
    else {
        if (flowerbed[0] == 0 && flowerbed[1] == 0) {
            n--;
            flowerbed[0] = 1;
        }
        for (i = 2; i < size-1; i++) {
            if (flowerbed[i] == 0 && flowerbed[i-1] == 0&&flowerbed[i+1]==0) {
                n--;
                flowerbed[i] = 1;
                i++;
            }

        }
        if (flowerbed[size-2] == 0 && flowerbed[size-1] == 0) {
            n--;
            flowerbed[size-1] = 1;
        }
    }
    return n <= 0;

}
```

