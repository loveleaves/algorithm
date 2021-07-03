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

