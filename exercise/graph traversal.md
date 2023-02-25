# 图或树的遍历



## 深度优先遍历（DFS）

> 遍历需要用先入后出的栈来实现，也可以通过与栈等价的递归来实现。对于树结构而言，
> 由于总是对新节点调用遍历，因此看起来是向着“深”的方向前进。其中，
>
> 1. 递归实现如果层级太深，会导致栈溢出。
>
> 2. 一般来说，深度优先搜索类型的题可以分为**主函数**和**辅函数**。**主函数**用于遍历所有的搜索位置，判断是否可以开始搜索，如果可以即在辅函数进行搜索。**辅函数**则负责深度优先搜索的递归调用。



#### [733. 图像渲染](https://leetcode-cn.com/problems/flood-fill/)

``` c++
const int dx[4] = {1, 0, 0, -1};
const int dy[4] = {0, 1, -1, 0};
void dfs(vector<vector<int>>& image, int x, int y, int color, int newColor) {//辅函数
    if (image[x][y] == color) {
        image[x][y] = newColor;
        for (int i = 0; i < 4; i++) {
            int mx = x + dx[i], my = y + dy[i];
            if (mx >= 0 && mx < image.size() && my >= 0 && my < image[0].size()) {
                dfs(image, mx, my, color, newColor);
            }
        }
    }
}

vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
    int currColor = image[sr][sc];
    if (currColor != newColor) {//主函数
        dfs(image, sr, sc, currColor, newColor);
    }
    return image;
}
```

#### [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/)

> 和上面**733.图像渲染**类似，只是从所有点都作为起始点遍历一遍；
>
> 且为了防止访问同一节点多次，访问该点后置其值为零。

``` c++
//递归调用
int dfs(vector<vector<int>>& grid, int cur_i, int cur_j) {
    if (cur_i < 0 || cur_j < 0 || cur_i == grid.size() || cur_j == grid[0].size() || grid[cur_i][cur_j] != 1) {
        return 0;
    }
    grid[cur_i][cur_j] = 0;
    int di[4] = {0, 0, 1, -1};
    int dj[4] = {1, -1, 0, 0};
    int ans = 1;
    for (int index = 0; index != 4; ++index) {
        int next_i = cur_i + di[index], next_j = cur_j + dj[index];
        ans += dfs(grid, next_i, next_j);
    }
    return ans;
}
public:
int maxAreaOfIsland(vector<vector<int>>& grid) {
    int ans = 0;
    for (int i = 0; i != grid.size(); ++i) {
        for (int j = 0; j != grid[0].size(); ++j) {
            ans = max(ans, dfs(grid, i, j));
        }
    }
    return ans;
}
```

``` c++
//非递归调用，使用stack
//把接下来想要遍历的节点入栈，然后出栈来访问它们
//stack为空时表示所有待节点均已访问
int maxAreaOfIsland(vector<vector<int>>& grid) {
    int ans = 0;
    for (int i = 0; i != grid.size(); ++i) {
        for (int j = 0; j != grid[0].size(); ++j) {
            int cur = 0;
            stack<int> stacki;
            stack<int> stackj;
            stacki.push(i);
            stackj.push(j);
            while (!stacki.empty()) {
                int cur_i = stacki.top(), cur_j = stackj.top();
                stacki.pop();
                stackj.pop();
                if (cur_i < 0 || cur_j < 0 || cur_i == grid.size() || cur_j == grid[0].size() || grid[cur_i][cur_j] != 1) {
                    continue;
                }
                ++cur;
                grid[cur_i][cur_j] = 0;
                int di[4] = {0, 0, 1, -1};
                int dj[4] = {1, -1, 0, 0};
                for (int index = 0; index != 4; ++index) {
                    int next_i = cur_i + di[index], next_j = cur_j + dj[index];
                    stacki.push(next_i);
                    stackj.push(next_j);
                }
            }
            ans = max(ans, cur);
        }
    }
    return ans;
}
```

#### [617. 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees/)

``` c++
TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
    if (t1 == nullptr) {
        return t2;
    }
    if (t2 == nullptr) {
        return t1;
    }
    auto merged = new TreeNode(t1->val + t2->val);
    merged->left = mergeTrees(t1->left, t2->left);
    merged->right = mergeTrees(t1->right, t2->right);
    return merged;
}
```

#### [547. 省份数量(或朋友圈数量)](https://leetcode-cn.com/problems/number-of-provinces/)

> 类似[695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/)

``` c++
int findCircleNum(vector<vector<int>>& friends) {// 主函数
    int n = friends.size(), count = 0;
    vector<bool> visited(n, false);
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(friends, i, visited);
            ++count;
        }
    }
    return count;
}
void dfs(vector<vector<int>>& friends, int i, vector<bool>& visited) {// 辅函数
    visited[i] = true;
    for (int k = 0; k < friends.size(); ++k) {
        if (friends[i][k] == 1 && !visited[k]) {
            dfs(friends, k, visited);
        }
    }
}
```

#### [417. 太平洋大西洋水流问题](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/)

``` c++
vector<int> direction{-1, 0, 1, 0, -1};
vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {// 主函数
    if (matrix.empty() || matrix[0].empty()) {
        return {};
    }
    vector<vector<int>> ans;
    int m = matrix.size(), n = matrix[0].size();
    vector<vector<bool>> can_reach_p(m, vector<bool>(n, false));
    vector<vector<bool>> can_reach_a(m, vector<bool>(n, false));
    for (int i = 0; i < m; ++i) {
        dfs(matrix, can_reach_p, i, 0);
        dfs(matrix, can_reach_a, i, n - 1);
    }
    for (int i = 0; i < n; ++i) {
        dfs(matrix, can_reach_p, 0, i);
        dfs(matrix, can_reach_a, m - 1, i);
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; ++j) {
            if (can_reach_p[i][j] && can_reach_a[i][j]) {
                ans.push_back(vector<int>{i, j});
            }
        }
    }
    return ans;
}
void dfs(const vector<vector<int>>& matrix, vector<vector<bool>>& can_reach, int r, int c) {// 辅函数
    if (can_reach[r][c]) {
        return;
    }
    can_reach[r][c] = true;
    int x, y;
    for (int i = 0; i < 4; ++i) {
        x = r + direction[i], y = c + direction[i+1];
        if (x >= 0 && x < matrix.size()
            && y >= 0 && y < matrix[0].size() &&
            matrix[r][c] <= matrix[x][y]) {
            dfs(matrix, can_reach, x, y);
        }
    }
}
```

## 回溯法（backtracking）

> 是优先搜索的一种特殊情况，又称为试探法，常用于需要记录节点状态的深度优先搜索。通常来说，排列、组合、选择类问题使用回溯法比较方便。
>
> 顾名思义，回溯法的核心是回溯。在搜索到某一节点的时候，如果我们发现目前的节点（及其子节点）并不是需求目标时，我们回退到原来的节点继续搜索，并且把在目前节点修改的状态还原。这样的好处是我们可以始终只对图的总状态进行修改，而非每次遍历时新建一个图来储存状态。在具体的写法上，它与普通的深度优先搜索一样，都有[修改当前节点状态] --> [递归子节点] 的步骤，只是多了回溯的步骤，变成了[修改当前节点状态] --> [递归子节点] --> [回改当前节点状态]。
>
> 回溯的两个小诀窍：一是按引用传状态，二是所有的状态修改在递归完成后回改。
>
> 回溯法修改一般有两种情况，一种是修改最后一位输出，比如排列组合；一种是修改访问标
> 记，比如矩阵里搜字符串。

### 题型一：排列、组合、子集相关问题
提示：这部分练习可以帮助我们熟悉「回溯算法」的一些概念和通用的解题思路。解题的步骤是：先画图，再编码。去思考可以剪枝的条件， 为什么有的时候用 used 数组，有的时候设置搜索起点 begin 变量，理解状态变量设计的想法。

- [46. 全排列](https://leetcode-cn.com/problems/permutations/)
- [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/) （排列题的follow-up，如何处理重复元素？）
- [39. 组合总和](https://leetcode-cn.com/problems/combination-sum/)
- [40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/) （组合题的follow-up，如何处理重复元素？）
- [77. 组合](https://leetcode-cn.com/problems/combinations/)
- [78. 子集](https://leetcode-cn.com/problems/subsets/)
- [90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/) ：剪枝技巧同 47 题、39 题、40 题；
- [60. 排列序列](https://leetcode-cn.com/problems/permutation-sequence/) ：利用了剪枝的思想，减去了大量枝叶，直接来到需要的叶子结点；
- [93. 复原 IP 地址](https://leetcode-cn.com/problems/restore-ip-addresses/)

### 题型二：Flood Fill
提示：Flood 是「洪水」的意思，Flood Fill 直译是「泛洪填充」的意思，体现了洪水能够从一点开始，迅速填满当前位置附近的地势低的区域。类似的应用还有：PS 软件中的「点一下把这一片区域的颜色都替换掉」，扫雷游戏「点一下打开一大片没有雷的区域」。

下面这几个问题，思想不难，但是初学的时候代码很不容易写对，并且也很难调试。我们的建议是多写几遍，忘记了就再写一次，参考规范的编写实现（设置 ``visited`` 数组，设置方向数组，抽取私有方法），把代码写对。

- [733. 图像渲染](https://leetcode-cn.com/problems/flood-fill/)
- [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

- [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)

- [79. 单词搜索](https://leetcode-cn.com/problems/word-search/)

说明：以上问题都不建议修改输入数据，设置 visited 数组是标准的做法。可能会遇到参数很多，是不是都可以写成成员变量的问题，面试中拿不准的记得问一下面试官。

### 题型三：字符串中的回溯问题
提示：字符串的问题的特殊之处在于，字符串的拼接生成新对象，因此在这一类问题上没有显示「回溯」的过程，但是如果使用 ``StringBuilder`` 拼接字符串就另当别论。
在这里把它们单独作为一个题型，是希望朋友们能够注意到这个非常细节的地方。

- [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

- [784. 字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation/) 

- [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/) ：这道题广度优先遍历也很好写，可以通过这个问题理解一下为什么回溯算法都是深度优先遍历，并且都用递归来写。

### 题型四：游戏问题

回溯算法是早期简单的人工智能，有些教程把回溯叫做暴力搜索，但回溯没有那么暴力，回溯是有方向地搜索。「力扣」上有一些简单的游戏类问题，解决它们有一定的难度，大家可以尝试一下。

- [51. N 皇后](https://leetcode-cn.com/problems/n-queens/) ：其实就是全排列问题，注意设计清楚状态变量，在遍历的时候需要记住一些信息，空间换时间；
- [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/) ：思路同「N 皇后问题」；事实上对于数独类型的题，有很多进阶的搜索方法和剪枝策略可以提高速度，如[启发式搜索](https://www.sudokuwiki.org/Naked_Candidates)。
- [488. 祖玛游戏](https://leetcode-cn.com/problems/zuma-game/)
- [529. 扫雷游戏](https://leetcode-cn.com/problems/minesweeper/)

### 题目代码

#### [46. 全排列](https://leetcode-cn.com/problems/permutations/)

``` c++
vector<vector<int>> permute(vector<int>& nums) {// 主函数
    vector<vector<int>> ans;
    backtracking(nums, 0, ans);
    return ans;
}

void backtracking(vector<int> &nums, int level, vector<vector<int>> &ans) {// 辅函数
    if (level == nums.size() - 1) {
        ans.push_back(nums);
        return;
    }
    for (int i = level; i < nums.size(); i++) {
        swap(nums[i], nums[level]); // 修改当前节点状态
        backtracking(nums, level+1, ans); // 递归子节点
        swap(nums[i], nums[level]); // 回改当前节点状态
    }
}
```

#### [77. 组合](https://leetcode-cn.com/problems/combinations/)

``` c++
vector<vector<int>> combine(int n, int k) {// 主函数
    vector<vector<int>> ans;
    vector<int> comb(k, 0);
    int count = 0;
    backtracking(ans, comb, count, 1, n, k);
    return ans;
}

void backtracking(vector<vector<int>>& ans, vector<int>& comb, int& count, int
                  pos, int n, int k) {// 辅函数
    if (count == k) {
        ans.push_back(comb);
        return;
    }
    for (int i = pos; i <= n; ++i) {
        comb[count++] = i; // 修改当前节点状态
        backtracking(ans, comb, count, i + 1, n, k); // 递归子节点
        --count; // 回改当前节点状态
    }
}
```

#### [79. 单词搜索](https://leetcode-cn.com/problems/word-search/)

``` c++
bool exist(vector<vector<char>>& board, string word) { // 主函数
    if (board.empty()) return false;
    int m = board.size(), n = board[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    bool find = false;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            backtracking(i, j, board, word, find, visited, 0);
        }
    }
    return find;
}

void backtracking(int i, int j, vector<vector<char>>& board, string& word, bool
                  & find, vector<vector<bool>>& visited, int pos) { // 辅函数
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size()) {
        return;
    }
    if (visited[i][j] || find || board[i][j] != word[pos]) {
        return;
    }
    if (pos == word.size() - 1) {
        find = true;
        return;
    }
    visited[i][j] = true; // 修改当前节点状态
    // 递归子节点
    backtracking(i + 1, j, board, word, find, visited, pos + 1);
    backtracking(i - 1, j, board, word, find, visited, pos + 1);
    backtracking(i, j + 1, board, word, find, visited, pos + 1);
    backtracking(i, j - 1, board, word, find, visited, pos + 1);
    visited[i][j] = false; // 回改当前节点状态
}
```

#### [51. N 皇后](https://leetcode-cn.com/problems/n-queens/)

``` c++
vector<vector<string>> solveNQueens(int n) { // 主函数
    vector<vector<string>> ans;
    if (n == 0) {
        return ans;
    }
    vector<string> board(n, string(n, '.'));
    vector<bool> column(n, false), ldiag(2*n-1, false), rdiag(2*n-1, false);
    backtracking(ans, board, column, ldiag, rdiag, 0, n);
    return ans;
}

void backtracking(vector<vector<string>> &ans, vector<string> &board, ector<bool>&column,
                  vector<bool> &ldiag, vector<bool> &rdiag, int row, int n) { // 辅函数
    if (row == n) {
        ans.push_back(board);
        return;
    }
    for (int i = 0; i < n; ++i) {
        if (column[i] || ldiag[n-row+i-1] || rdiag[row+i]) {
            continue;
        }
        // 修改当前节点状态
        board[row][i] = 'Q';
        column[i] = ldiag[n-row+i-1] = rdiag[row+i] = true;
        // 递归子节点
        backtracking(ans, board, column, ldiag, rdiag, row+1, n);
        // 回改当前节点状态
        board[row][i] = '.';
        column[i] = ldiag[n-row+i-1] = rdiag[row+i] = false;
    }
}
```



## 广度优先遍历（BFS）

> 是一层层进行遍历的，因此需要用先入先出的队列（Queue）而非先入后出的栈进行遍历。
>
> 常常用来处理最短路径等问题。
>
> 深度优先搜索和广度优先搜索都可以处理可达性问题，即从一个节点开始是否能达到另一个节点。深度优先搜索可以利用递归快速实现，但实际软件工程中，递归一方面难以理解，另一方面可能产生栈溢出的情况；而用栈实现的深度优先搜索和用队列实现的广度优先搜索在写法上并没有太大差异，因此使用哪一种搜索方式需要根据实际的功能需求来判断。

#### [934. 最短的桥](https://leetcode-cn.com/problems/shortest-bridge/)

``` c++
vector<int> direction{-1, 0, 1, 0, -1};
// 主函数
int shortestBridge(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    queue<pair<int, int>> points;
    // dfs寻找第一个岛屿，并把1全部赋值为2
    bool flipped = false;
    for (int i = 0; i < m; ++i) {
        if (flipped) break;
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 1) {
                dfs(points, grid, m, n, i, j);
                flipped = true;
                break;
            }
        }
    }
    // bfs寻找第二个岛屿，并把过程中经过的0赋值为2
    int x, y;
    int level = 0;
    while (!points.empty()){
        ++level;
        int n_points = points.size();
        while (n_points--) {
            auto [r, c] = points.front();
            points.pop();
            for (int k = 0; k < 4; ++k) {
                x = r + direction[k], y = c + direction[k+1];
                if (x >= 0 && y >= 0 && x < m && y < n) {
                    if (grid[x][y] == 2) {
                        continue;
                    }
                    if (grid[x][y] == 1) {
                        return level;
                    }
                    points.push({x, y});
                    grid[x][y] = 2;
                }
            }
        }
    }
    return 0;
}
// 辅函数
void dfs(queue<pair<int, int>>& points, vector<vector<int>>& grid, int m, int n
         , int i, int j) {
    if (i < 0 || j < 0 || i == m || j == n || grid[i][j] == 2) {
        return;
    }
    if (grid[i][j] == 0) {
        points.push({i, j});
        return;
    }
    grid[i][j] = 2;
    dfs(points, grid, m, n, i - 1, j);
    dfs(points, grid, m, n, i + 1, j);
    dfs(points, grid, m, n, i, j - 1);
    dfs(points, grid, m, n, i, j + 1);
}
```

#### [126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)

> - 把起始字符串、终止字符串、以及单词表里所有的字符串想象成节点。那么，若两个字符串只有一个字符不同，那么它们相连。因为题目需要输出修改次数最少的所有修改方式，因此我们可以使用广度优先搜索，转换为求得起始节点到终止节点的最短距离。
> - 小技巧：不直接从起始节点进行广度优先搜索，直到找到终止节点为止；而是从起始节点和终止节点分别进行广度优先搜索，每次只延展当前层节点数最少的那一端，这样我们可以减少搜索的总结点数。举例来说，假设最短距离为4，如果我们只从一端搜索4 层，总遍历节点数最多是 1 + 2 + 4 + 8 + 16 = 31；而如果我们从两端各搜索两层，总遍历节点数最多只有 2*（1 + 2 + 4） = 14。
> - 在搜索结束后，我们还需要通过回溯法来重建所有可能的路径。

``` c++
// 主函数
vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& 											wordList) {
    vector<vector<string>> ans;
    unordered_set<string> dict;
    for (const auto &w: wordList){
        dict.insert(w);
    }
    if (!dict.count(endWord)) {
        return ans;
    }
    dict.erase(beginWord);
    dict.erase(endWord);
    unordered_set<string> q1{beginWord}, q2{endWord};
    unordered_map<string, vector<string>> next;
    bool reversed = false, found = false;
    while (!q1.empty()) {
        unordered_set<string> q;
        for (const auto &w: q1) {
            string s = w;
            for (size_t i = 0; i < s.size(); i++) {
                char ch = s[i];
                for (int j = 0; j < 26; j++) {
                    s[i] = j + 'a';
                    if (q2.count(s)) {
                        reversed? next[s].push_back(w): next[w].push_back(s);
                        found = true;
                    }
                    if (dict.count(s)) {
                        reversed? next[s].push_back(w): next[w].push_back(s);
                        q.insert(s);
                    }
                }
                s[i] = ch;
            }
        }
        if (found) {
            break;
        }
        for (const auto &w: q) {
            dict.erase(w);
        }
        if (q.size() <= q2.size()) {
            q1 = q;
        } else {
            reversed = !reversed;
            q1 = q2;
            q2 = q;
        }
    }
    if (found) {
        vector<string> path = {beginWord};
        backtracking(beginWord, endWord, next, path, ans);
    }
    return ans;
}
// 辅函数
void backtracking(const string &src, const string &dst, unordered_map<string,
         vector<string>> &next, vector<string> &path, vector<vector<string>> &ans) {
    if (src == dst) {
        ans.push_back(path);
        return;
    }
    for (const auto &s: next[src]) {
        path.push_back(s);
        backtracking(s, dst, next, path, ans);
        path.pop_back();
    }
}
```



#### [733. 图像渲染](https://leetcode-cn.com/problems/flood-fill/)

``` c++
const int dx[4] = {1, 0, 0, -1};
const int dy[4] = {0, 1, -1, 0};
vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
    int currColor = image[sr][sc];
    if (currColor == newColor) return image;
    int n = image.size(), m = image[0].size();
    queue<pair<int, int>> que;
    que.emplace(sr, sc);
    image[sr][sc] = newColor;
    while (!que.empty()) {
        int x = que.front().first, y = que.front().second;
        que.pop();
        for (int i = 0; i < 4; i++) {
            int mx = x + dx[i], my = y + dy[i];
            if (mx >= 0 && mx < n && my >= 0 && my < m && image[mx][my] == currColor) {
                que.emplace(mx, my);
                image[mx][my] = newColor;
            }
        }
    }
    return image;
}
```

#### [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/)

``` c++
int maxAreaOfIsland(vector<vector<int>>& grid) {
    int ans = 0;
    for (int i = 0; i != grid.size(); ++i) {
        for (int j = 0; j != grid[0].size(); ++j) {
            int cur = 0;
            queue<int> queuei;
            queue<int> queuej;
            queuei.push(i);
            queuej.push(j);
            while (!queuei.empty()) {
                int cur_i = queuei.front(), cur_j = queuej.front();
                queuei.pop();
                queuej.pop();
                if (cur_i < 0 || cur_j < 0 || cur_i == grid.size() || cur_j == grid[0].size() || grid[cur_i][cur_j] != 1) {
                    continue;
                }
                ++cur;
                grid[cur_i][cur_j] = 0;
                int di[4] = {0, 0, 1, -1};
                int dj[4] = {1, -1, 0, 0};
                for (int index = 0; index != 4; ++index) {
                    int next_i = cur_i + di[index], next_j = cur_j + dj[index];
                    queuei.push(next_i);
                    queuej.push(next_j);
                }
            }
            ans = max(ans, cur);
        }
    }
    return ans;
}
```

#### [617. 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees/)

``` c++
TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
    if (t1 == nullptr) {
        return t2;
    }
    if (t2 == nullptr) {
        return t1;
    }
    auto merged = new TreeNode(t1->val + t2->val);
    auto q = queue<TreeNode*>();
    auto queue1 = queue<TreeNode*>();
    auto queue2 = queue<TreeNode*>();
    q.push(merged);
    queue1.push(t1);
    queue2.push(t2);
    while (!queue1.empty() && !queue2.empty()) {
        auto node = q.front(), node1 = queue1.front(), node2 = queue2.front();
        q.pop();
        queue1.pop();
        queue2.pop();
        auto left1 = node1->left, left2 = node2->left, right1 = node1->right, right2 = node2->right;
        if (left1 != nullptr || left2 != nullptr) {
            if (left1 != nullptr && left2 != nullptr) {
                auto left = new TreeNode(left1->val + left2->val);
                node->left = left;
                q.push(left);
                queue1.push(left1);
                queue2.push(left2);
            } else if (left1 != nullptr) {
                node->left = left1;
            } else if (left2 != nullptr) {
                node->left = left2;
            }
        }
        if (right1 != nullptr || right2 != nullptr) {
            if (right1 != nullptr && right2 != nullptr) {
                auto right = new TreeNode(right1->val + right2->val);
                node->right = right;
                q.push(right);
                queue1.push(right1);
                queue2.push(right2);
            } else if (right1 != nullptr) {
                node->right = right1;
            } else {
                node->right = right2;
            }
        }
    }
    return merged;
}
```

#### [116. 填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

- 层次遍历--对同一层节点同时进行处理
- 基于BFS

``` c++
Node* connect(Node* root) {
    if(root == nullptr) {
        return root;
    }
    queue<Node*> Q;
    Q.push(root);
    //while和for循环控制同一层
    while(!Q.empty()) {
        int size = Q.size();
        for(int i = 0; i < size; ++i) {
            //for循环控制只处理同一层
            Node* node = Q.front();
            Q.pop();
            if(i < size - 1) {
                node->next = Q.front();
            }
            if(node->left != nullptr) {
                Q.push(node->left);
            }
            if(node->right != nullptr) {
                Q.push(node->right);
            }
        }
    }
    return root;
}
```

或利用上一层设置好的next指针，无需借助队列

``` c++
Node* connect(Node* root) {
    if(!root) {
        return root;
    }
    Node* leftmost = root;
    while(leftmost->left != nullptr) {
        //通过node->left控制遍历全部层
        Node* head = leftmost;
        while(head != nullptr) {
            head->left->next = head->right;
            if(head->next != nullptr) {
                head->right->next = head->next->left;
            }
            head = head->next;
        }
        leftmost = leftmost->left;
    }
    return root;
}
```



## Test

#### [257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/)

> 考虑回溯法使用与否有什么区别

### DFS

``` c++
vector<string> res;
vector<string> binaryTreePaths(TreeNode* root) {
    dfs(root,"");
    return res;
}
void dfs(TreeNode* root, string path) {
    if (!root) {
        return;
    }
    path += to_string(root->val);
    if (!root->left && !root->right) {
        res.push_back(path);
        return;
    }
    path += "->";
    dfs(root->left,path);
    dfs(root->right,path);
}
```

### BFS

``` c++
vector<string> binaryTreePaths(TreeNode* root) {
    vector<string> paths;
    if (root == nullptr) {
        return paths;
    }
    queue<TreeNode*> node_queue;
    queue<string> path_queue;

    node_queue.push(root);
    path_queue.push(to_string(root->val));

    while (!node_queue.empty()) {
        TreeNode* node = node_queue.front(); 
        string path = path_queue.front();
        node_queue.pop();
        path_queue.pop();

        if (node->left == nullptr && node->right == nullptr) {
            paths.push_back(path);
        } else {
            if (node->left != nullptr) {
                node_queue.push(node->left);
                path_queue.push(path + "->" + to_string(node->left->val));
            }

            if (node->right != nullptr) {
                node_queue.push(node->right);
                path_queue.push(path + "->" + to_string(node->right->val));
            }
        }
    }
    return paths;
}
```

#### [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)

> 可以先从最外侧填充，然后再考虑里侧

#### DFS

``` c++
int n, m;

void dfs(vector<vector<char>>& board, int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m || board[x][y] != 'O') {
        return;
    }
    board[x][y] = 'A';
    dfs(board, x + 1, y);
    dfs(board, x - 1, y);
    dfs(board, x, y + 1);
    dfs(board, x, y - 1);
}

void solve(vector<vector<char>>& board) {
    n = board.size();
    if (n == 0) {
        return;
    }
    m = board[0].size();
    for (int i = 0; i < n; i++) {
        dfs(board, i, 0);
        dfs(board, i, m - 1);
    }
    for (int i = 1; i < m - 1; i++) {
        dfs(board, 0, i);
        dfs(board, n - 1, i);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 'A') {
                board[i][j] = 'O';
            } else if (board[i][j] == 'O') {
                board[i][j] = 'X';
            }
        }
    }
}
```

### BFS

``` c++
const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

void solve(vector<vector<char>>& board) {
    int n = board.size();
    if (n == 0) {
        return;
    }
    int m = board[0].size();
    queue<pair<int, int>> que;
    for (int i = 0; i < n; i++) {
        if (board[i][0] == 'O') {
            que.emplace(i, 0);
            board[i][0] = 'A';
        }
        if (board[i][m - 1] == 'O') {
            que.emplace(i, m - 1);
            board[i][m - 1] = 'A';
        }
    }
    for (int i = 1; i < m - 1; i++) {
        if (board[0][i] == 'O') {
            que.emplace(0, i);
            board[0][i] = 'A';
        }
        if (board[n - 1][i] == 'O') {
            que.emplace(n - 1, i);
            board[n - 1][i] = 'A';
        }
    }
    while (!que.empty()) {
        int x = que.front().first, y = que.front().second;
        que.pop();
        for (int i = 0; i < 4; i++) {
            int mx = x + dx[i], my = y + dy[i];
            if (mx < 0 || my < 0 || mx >= n || my >= m || board[mx][my] != 'O') {
                continue;
            }
            que.emplace(mx, my);
            board[mx][my] = 'A';
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 'A') {
                board[i][j] = 'O';
            } else if (board[i][j] == 'O') {
                board[i][j] = 'X';
            }
        }
    }
}
```

#### [310. 最小高度树](https://leetcode-cn.com/problems/minimum-height-trees/)

> 考虑如何将这道题转为搜索类型题？是使用深度优先还是广度优先呢？

``` c++

```

[参考](https://leetcode-cn.com/problems/minimum-height-trees/solution/c-xun-xu-jian-jin-de-si-lu-bfsdfstuo-bu-hmk2y/)