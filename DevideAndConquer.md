# 分治法



## 算法解释

分治问题由“分”（divide）和“治”（conquer）两部分组成，通过把原问题分为子问题，再将子问题进行处理合并，从而实现对原问题的求解。排序中的归并排序就是典型的分治问题。

## 表达式问题

#### [241. 为运算表达式设计优先级](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/)

``` c++
vector<int> diffWaysToCompute(string input) {
    vector<int> ways;
    for (int i = 0; i < input.length(); i++) {
        char c = input[i];
        if (c == '+' || c == '-' || c == '*') {
            vector<int> left = diffWaysToCompute(input.substr(0, i));
            vector<int> right = diffWaysToCompute(input.substr(i + 1));
            for (const int & l: left) {
                for (const int & r: right) {
                    switch (c) {
                        case '+': ways.push_back(l + r); break;
                        case '-': ways.push_back(l - r); break;
                        case '*': ways.push_back(l * r); break;
                    }
                }
            }
        }
    }
    if (ways.empty()) ways.push_back(stoi(input));
    return ways;
}
```

我们发现，某些被divide 的子字符串可能重复出现多次，因此我们可以用`memoization `来去重。或者与其我们从上到下用分治处理+`memoization`，不如直接从下到上用动态规划处理。

``` c++
vector<int> diffWaysToCompute(string input) {
    vector<int> data;
    vector<char> ops;
    int num = 0;
    char op = ’ ’;
    istringstream ss(input + "+");
    while (ss >> num && ss >> op) {
        data.push_back(num);
        ops.push_back(op);
    }
    int n = data.size();
    vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>()));
    for (int i = 0; i < n; ++i) {
        for (int j = i; j >= 0; --j) {
            if (i == j) {
                dp[j][i].push_back(data[i]);
            } else {
                for (int k = j; k < i; k += 1) {
                    for (auto left : dp[j][k]) {
                        for (auto right : dp[k+1][i]) {
                            int val = 0;
                            switch (ops[k]) {
                                case ’+’: val = left + right; break;
                                case ’-’: val = left - right; break;
                                case ’*’: val = left * right; break;
                            }
                            dp[j][i].push_back(val);
                        }
                    }
                }
            }
        }
    }
    return dp[0][n-1];
}
```

## Practice

试着先 用从上到下的分治（递归）写法求解，最好加上`memoization`；再用从下到上的动态规
划写法求解。

#### [932. 漂亮数组](https://leetcode-cn.com/problems/beautiful-array/)

``` c++

```

#### [312. 戳气球](https://leetcode-cn.com/problems/burst-balloons/)

``` c++

```

