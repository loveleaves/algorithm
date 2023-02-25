# 字符串处理



## 字符串比较

#### [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)

``` c++
bool isAnagram(string s, string t) {
    if (s.length() != t.length()) {
        return false;
    }
    vector<int> counts(26, 0);
    for (int i = 0; i < s.length(); ++i) {
        ++counts[s[i]-’a’];
        --counts[t[i]-’a’];
    }
    for (int i = 0; i < 26; ++i) {
        if (counts[i]) {
            return false;
        }
    }
    return true;
}
```

#### [205. 同构字符串](https://leetcode-cn.com/problems/isomorphic-strings/)

``` c++
bool isIsomorphic(string s, string t) {
    vector<int> s_first_index(256, 0), t_first_index(256, 0);
    for (int i = 0; i < s.length(); ++i) {
        if (s_first_index[s[i]] != t_first_index[t[i]]) {
            return false;
        }
        s_first_index[s[i]] = t_first_index[t[i]] = i + 1;
    }
    return true;
}
```

#### [647. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)

或[Manacher 算法](https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/)

``` c++
int countSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); ++i) {
        count += extendSubstrings(s, i, i); // 奇数长度
        count += extendSubstrings(s, i, i + 1); // 偶数长度
    }
    return count;
}
int extendSubstrings(string s, int l, int r) {
    int count = 0;
    while (l >= 0 && r < s.length() && s[l] == s[r]) {
        --l;
        ++r;
        ++count;
    }
    return count;
}
```

#### [696. 计数二进制子串](https://leetcode-cn.com/problems/count-binary-substrings/)

``` c++
int countBinarySubstrings(string s) {
    int pre = 0, cur = 1, count = 0;
    for (int i = 1; i < s.length(); ++i) {
        if (s[i] == s[i-1]) {
            ++cur;
        } else {
            pre = cur;
            cur = 1;
        }
        if (pre >= cur) {
            ++count;
        }
    }
    return count;
}
```



## 字符串理解

#### [227. 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii/)

``` c++
// 主函数
int calculate(string s) {
    int i = 0;
    return parseExpr(s, i);
}
// 辅函数- 递归parse从位置i开始的剩余字符串
int parseExpr(const string& s, int& i) {
    char op = '+';
    long left = 0, right = 0;
    while (i < s.length()) {
        if (s[i] != ' ') {
            long n = parseNum(s, i);
            switch (op) {
                case '+' : left += right; right = n; break;
                case '-' : left += right; right = -n; break;
                case '*' : right *= n; break;
                case '/' : right /= n; break;
            }
            if (i < s.length()) {
                op = s[i];
            }
        }
        ++i;
    }
    return left + right;
}
// 辅函数- parse从位置i开始的一个数字
long parseNum(const string& s, int& i) {
    long n = 0;
    while (i < s.length() && isdigit(s[i])) {
        n = 10 * n + (s[i++] - '0');
    }
    return n;
}
```

#### [224. 基本计算器](https://leetcode-cn.com/problems/basic-calculator/)

``` c++

```

#### [282. 给表达式添加运算符](https://leetcode-cn.com/problems/expression-add-operators/)

``` c++

```



## 字符串匹配

#### [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

或[KMP算法](https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode-solution-ds6y/)

KMP --> TO DO LIST

``` c++
// 主函数
int strStr(string haystack, string needle) {
    int k = -1, n = haystack.length(), p = needle.length();
    if (p == 0) return 0;
    vector<int> next(p, -1); // -1表示不存在相同的最大前缀和后缀
    calNext(needle, next); // 计算next数组
    for (int i = 0; i < n; ++i) {
        while (k > -1 && needle[k+1] != haystack[i]) {
            k = next[k]; // 有部分匹配，往前回溯
        }
        if (needle[k+1] == haystack[i]) {
            ++k;
        }
        if (k == p-1) {
            return i - p + 1; // 说明k移动到needle的最末端，返回相应的位置
        }
    }
    return -1;
}
// 辅函数- 计算next数组
void calNext(const string &needle, vector<int> &next) {
    for (int j = 1, p = -1; j < needle.length(); ++j) {
        while (p > -1 && needle[p+1] != needle[j]) {
            p = next[p]; // 如果下一位不同，往前回溯
        }
        if (needle[p+1] == needle[j]) {
            ++p; // 如果下一位相同，更新相同的最大前缀和最大后缀长
        }
        next[j] = p;
    }
}
```

## Practice

