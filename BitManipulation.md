# 位运算



## 算法描述

​	位运算是算法题里比较特殊的一种类型，它们利用二进制位运算的特性进行一些奇妙的优化和计算。常用的位运算符号包括：“^”按位异或、“&”按位与、“|”按位或、“~”取反、“<<”算术左移和“>>”算术右移。以下是一些常见的位运算特性，其中0s 和1s 分别表示只由0 或1构成的二进制数字。

## 位运算基础问题

#### [461. 汉明距离](https://leetcode-cn.com/problems/hamming-distance/)

``` c++
int hammingDistance(int x, int y) {
    //内置计数函数：return __builtin_popcount(x ^ y);
    int diff = x ^ y, ans = 0;
    while (diff) {
        ans += diff & 1;
        diff >>= 1;
    }
    return ans;
}
```

#### [477. 汉明距离总和](https://leetcode-cn.com/problems/total-hamming-distance/)

``` c++
int totalHammingDistance(vector<int> &nums) {
    int ans = 0, n = nums.size();
    for (int i = 0; i < 30; ++i) {
        int c = 0;
        for (int val : nums) {
            c += (val >> i) & 1;
        }
        ans += c * (n - c);
    }
    return ans;
}
```

#### [190. 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)

``` c++
//使用算术左移和右移，可以很轻易地实现二进制的翻转
//注意算数左移和右移一般用在无符号数(unsigned)，有符号数可能出错
uint32_t reverseBits(uint32_t n) {
    uint32_t ans = 0;
    for (int i = 0; i < 32; ++i) {
        ans <<= 1;
        ans += n & 1;
        n >>= 1;// <==> n = n >> 1
    }
    return ans;
}
//分治法
private:
    const uint32_t M1 = 0x55555555; // 01010101010101010101010101010101
    const uint32_t M2 = 0x33333333; // 00110011001100110011001100110011
    const uint32_t M4 = 0x0f0f0f0f; // 00001111000011110000111100001111
    const uint32_t M8 = 0x00ff00ff; // 00000000111111110000000011111111

public:
    uint32_t reverseBits(uint32_t n) {
        n = n >> 1 & M1 | (n & M1) << 1;
        n = n >> 2 & M2 | (n & M2) << 2;
        n = n >> 4 & M4 | (n & M4) << 4;
        n = n >> 8 & M8 | (n & M8) << 8;
        return n >> 16 | n << 16;
    }
```

#### [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)

``` c++
//每个数字都出现两次，只有一个数字出现一次
//所以数组中的全部元素的异或运算结果即为数组中只出现一次的数字
int singleNumber(vector<int>& nums) {
    int ans = 0;
    for (auto num: nums) {
        ans ^= num;
    }
    return ans;
}
//或使用hashmap
int singleNumber(vector<int>& nums) {        
    unordered_map<int, int> um;
    for(int a: nums)
        um[a]++;
    for(auto it = um.begin(); it!=um.end(); it++){
        if(it->second==1)
            return it->first;
    }
    return 0;
}
```



## 二进制特性

利用二进制的一些特性，我们可以把位运算使用到更多问题上。
例如，我们可以利用二进制和位运算输出一个数组的所有子集。假设我们有一个长度为n 的数组，我们可以生成长度为n 的所有二进制，1 表示选取该数字，0 表示不选取。这样我们就获得了2^n 个子集。

- n & (n - 1)   :   该位运算技巧可以直接将 n 二进制表示的最低位 1 移除(当n为正数且只有一个1时，比如2的幂，结果n & (n - 1) =0)   `Brian Kernighan algorithm`
- n & (-n)    ：  该位运算技巧可以直接获取 n 二进制表示的最低位的 1 (如果 n 是正整数并且n & (-n) = n，那么 n 就是 2 的幂)。

#### [342. 4的幂](https://leetcode-cn.com/problems/power-of-four/)

``` c++
//直接与指定二进制数想与
bool isPowerOfFour(int n) {
    return n > 0 && !(n & (n - 1)) && (n & 1431655765);//二进制的10101...101
}
//或从右计数
bool isPowerOfFour(int n) {
    if (n <= 0) return false;
    int a = 0, b = 0;
    while (n) {
        if (n & 1) ++a;
        else ++b;
        if (a > 1) return false;
        n >>= 1;
    }
    if (b % 2 == 0) return true;
    else return false;
}
```

#### [318. 最大单词长度乘积](https://leetcode-cn.com/problems/maximum-product-of-word-lengths/)

``` c++
//bitmask + hash + bitmanipulation
int maxProduct(vector<string>& words) {
    unordered_map<int, int> hash;
    int ans = 0;
    for (const string & word : words) {
        int mask = 0, size = word.size();
        for (const char & c : word) {
            mask |= 1 << (c - ’a’);//bitmask
        }
        hash[mask] = max(hash[mask], size);
        for (const auto& [h_mask, h_len]: hash) {
            if (!(mask & h_mask)) {
                ans = max(ans, size * h_len);
            }
        }
    }
    return ans;
}
```

#### [338. 比特位计数](https://leetcode-cn.com/problems/counting-bits/)

``` c++
//动态规划
vector<int> countBits(int num) {
    vector<int> dp(num+1, 0);
    for (int i = 1; i <= num; ++i)
        dp[i] = i & 1? dp[i-1] + 1: dp[i>>1];
    // 等价于dp[i] = dp[i&(i-1)] + 1;
    return dp;
}
//位运算
int countOnes(int x) {
    int ones = 0;
    while (x > 0) {
        x &= (x - 1); //移出最低位1
        ones++;
    }
    return ones;
}

vector<int> countBits(int n) {
    vector<int> bits(n + 1);
    for (int i = 0; i <= n; i++) {
        bits[i] = countOnes(i);
    }
    return bits;
}
```

## Practice

#### [268. 丢失的数字](https://leetcode-cn.com/problems/missing-number/)

``` c++
//If two numbers are similar its xor is 0.
//So we simply take xor of all the numbers present in array and xor of n natural numbers.
//All the repeated numbers in both gets cancelled and we are left with missing number.
int missingNumber(vector<int>& nums) {
    int x = 0;
    for(int i = 0; i < nums.size(); ++i) {
        x = x ^ nums[i] ^ (i+1);
    }
    return x;
}
```

#### [260. 只出现一次的数字 III](https://leetcode-cn.com/problems/single-number-iii/)

``` c++
//先对所有数字进行一次异或，得到两个出现一次的数字的异或值；
//在异或结果中找到任意为 1 的位, 根据这一位对所有的数字进行分组；
//在每个组内进行异或操作，得到两个数字。
vector<int> singleNumber(vector<int>& nums) {
    int ret = 0;
    for (int n : nums)
        ret ^= n;
    int div = 1;
    while ((div & ret) == 0)
        div <<= 1;
    int a = 0, b = 0;
    for (int n : nums)
        if (div & n)
            a ^= n;
    else
        b ^= n;
    return vector<int>{a, b};
}
```

