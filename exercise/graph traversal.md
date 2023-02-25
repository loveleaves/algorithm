# ͼ�����ı���



## ������ȱ�����DFS��

> ������Ҫ����������ջ��ʵ�֣�Ҳ����ͨ����ջ�ȼ۵ĵݹ���ʵ�֡��������ṹ���ԣ�
> �������Ƕ��½ڵ���ñ�������˿����������š���ķ���ǰ�������У�
>
> 1. �ݹ�ʵ������㼶̫��ᵼ��ջ�����
>
> 2. һ����˵����������������͵�����Է�Ϊ**������**��**������**��**������**���ڱ������е�����λ�ã��ж��Ƿ���Կ�ʼ������������Լ��ڸ���������������**������**����������������ĵݹ���á�



#### [733. ͼ����Ⱦ](https://leetcode-cn.com/problems/flood-fill/)

``` c++
const int dx[4] = {1, 0, 0, -1};
const int dy[4] = {0, 1, -1, 0};
void dfs(vector<vector<int>>& image, int x, int y, int color, int newColor) {//������
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
    if (currColor != newColor) {//������
        dfs(image, sr, sc, currColor, newColor);
    }
    return image;
}
```

#### [695. �����������](https://leetcode-cn.com/problems/max-area-of-island/)

> ������**733.ͼ����Ⱦ**���ƣ�ֻ�Ǵ����е㶼��Ϊ��ʼ�����һ�飻
>
> ��Ϊ�˷�ֹ����ͬһ�ڵ��Σ����ʸõ������ֵΪ�㡣

``` c++
//�ݹ����
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
//�ǵݹ���ã�ʹ��stack
//�ѽ�������Ҫ�����Ľڵ���ջ��Ȼ���ջ����������
//stackΪ��ʱ��ʾ���д��ڵ���ѷ���
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

#### [617. �ϲ�������](https://leetcode-cn.com/problems/merge-two-binary-trees/)

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

#### [547. ʡ������(������Ȧ����)](https://leetcode-cn.com/problems/number-of-provinces/)

> ����[695. �����������](https://leetcode-cn.com/problems/max-area-of-island/)

``` c++
int findCircleNum(vector<vector<int>>& friends) {// ������
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
void dfs(vector<vector<int>>& friends, int i, vector<bool>& visited) {// ������
    visited[i] = true;
    for (int k = 0; k < friends.size(); ++k) {
        if (friends[i][k] == 1 && !visited[k]) {
            dfs(friends, k, visited);
        }
    }
}
```

#### [417. ̫ƽ�������ˮ������](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/)

``` c++
vector<int> direction{-1, 0, 1, 0, -1};
vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {// ������
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
void dfs(const vector<vector<int>>& matrix, vector<vector<bool>>& can_reach, int r, int c) {// ������
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

## ���ݷ���backtracking��

> ������������һ������������ֳ�Ϊ��̽������������Ҫ��¼�ڵ�״̬���������������ͨ����˵�����С���ϡ�ѡ��������ʹ�û��ݷ��ȽϷ��㡣
>
> ����˼�壬���ݷ��ĺ����ǻ��ݡ���������ĳһ�ڵ��ʱ��������Ƿ���Ŀǰ�Ľڵ㣨�����ӽڵ㣩����������Ŀ��ʱ�����ǻ��˵�ԭ���Ľڵ�������������Ұ���Ŀǰ�ڵ��޸ĵ�״̬��ԭ�������ĺô������ǿ���ʼ��ֻ��ͼ����״̬�����޸ģ�����ÿ�α���ʱ�½�һ��ͼ������״̬���ھ����д���ϣ�������ͨ�������������һ��������[�޸ĵ�ǰ�ڵ�״̬] --> [�ݹ��ӽڵ�] �Ĳ��裬ֻ�Ƕ��˻��ݵĲ��裬�����[�޸ĵ�ǰ�ڵ�״̬] --> [�ݹ��ӽڵ�] --> [�ظĵ�ǰ�ڵ�״̬]��
>
> ���ݵ�����С���ϣ�һ�ǰ����ô�״̬���������е�״̬�޸��ڵݹ���ɺ�ظġ�
>
> ���ݷ��޸�һ�������������һ�����޸����һλ���������������ϣ�һ�����޸ķ��ʱ�
> �ǣ�������������ַ�����

### ����һ�����С���ϡ��Ӽ��������
��ʾ���ⲿ����ϰ���԰���������Ϥ�������㷨����һЩ�����ͨ�õĽ���˼·������Ĳ����ǣ��Ȼ�ͼ���ٱ��롣ȥ˼�����Լ�֦�������� Ϊʲô�е�ʱ���� used ���飬�е�ʱ������������� begin ���������״̬������Ƶ��뷨��

- [46. ȫ����](https://leetcode-cn.com/problems/permutations/)
- [47. ȫ���� II](https://leetcode-cn.com/problems/permutations-ii/) ���������follow-up����δ����ظ�Ԫ�أ���
- [39. ����ܺ�](https://leetcode-cn.com/problems/combination-sum/)
- [40. ����ܺ� II](https://leetcode-cn.com/problems/combination-sum-ii/) ��������follow-up����δ����ظ�Ԫ�أ���
- [77. ���](https://leetcode-cn.com/problems/combinations/)
- [78. �Ӽ�](https://leetcode-cn.com/problems/subsets/)
- [90. �Ӽ� II](https://leetcode-cn.com/problems/subsets-ii/) ����֦����ͬ 47 �⡢39 �⡢40 �⣻
- [60. ��������](https://leetcode-cn.com/problems/permutation-sequence/) �������˼�֦��˼�룬��ȥ�˴���֦Ҷ��ֱ��������Ҫ��Ҷ�ӽ�㣻
- [93. ��ԭ IP ��ַ](https://leetcode-cn.com/problems/restore-ip-addresses/)

### ���Ͷ���Flood Fill
��ʾ��Flood �ǡ���ˮ������˼��Flood Fill ֱ���ǡ�������䡹����˼�������˺�ˮ�ܹ���һ�㿪ʼ��Ѹ��������ǰλ�ø����ĵ��Ƶ͵��������Ƶ�Ӧ�û��У�PS ����еġ���һ�°���һƬ�������ɫ���滻������ɨ����Ϸ����һ�´�һ��Ƭû���׵����򡹡�

�����⼸�����⣬˼�벻�ѣ����ǳ�ѧ��ʱ�����ܲ�����д�ԣ�����Ҳ���ѵ��ԡ����ǵĽ����Ƕ�д���飬�����˾���дһ�Σ��ο��淶�ı�дʵ�֣����� ``visited`` ���飬���÷������飬��ȡ˽�з��������Ѵ���д�ԡ�

- [733. ͼ����Ⱦ](https://leetcode-cn.com/problems/flood-fill/)
- [200. ��������](https://leetcode-cn.com/problems/number-of-islands/)

- [130. ��Χ�Ƶ�����](https://leetcode-cn.com/problems/surrounded-regions/)

- [79. ��������](https://leetcode-cn.com/problems/word-search/)

˵�����������ⶼ�������޸��������ݣ����� visited �����Ǳ�׼�����������ܻ����������ܶ࣬�ǲ��Ƕ�����д�ɳ�Ա���������⣬�������ò�׼�ļǵ���һ�����Թ١�

### ���������ַ����еĻ�������
��ʾ���ַ��������������֮�����ڣ��ַ�����ƴ�������¶����������һ��������û����ʾ�����ݡ��Ĺ��̣��������ʹ�� ``StringBuilder`` ƴ���ַ����������ۡ�
����������ǵ�����Ϊһ�����ͣ���ϣ���������ܹ�ע�⵽����ǳ�ϸ�ڵĵط���

- [17. �绰�������ĸ���](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

- [784. ��ĸ��Сдȫ����](https://leetcode-cn.com/problems/letter-case-permutation/) 

- [22. ��������](https://leetcode-cn.com/problems/generate-parentheses/) ������������ȱ���Ҳ�ܺ�д������ͨ������������һ��Ϊʲô�����㷨����������ȱ��������Ҷ��õݹ���д��

### �����ģ���Ϸ����

�����㷨�����ڼ򵥵��˹����ܣ���Щ�̳̰ѻ��ݽ�������������������û����ô�������������з���������������ۡ�����һЩ�򵥵���Ϸ�����⣬���������һ�����Ѷȣ���ҿ��Գ���һ�¡�

- [51. N �ʺ�](https://leetcode-cn.com/problems/n-queens/) ����ʵ����ȫ�������⣬ע��������״̬�������ڱ�����ʱ����Ҫ��סһЩ��Ϣ���ռ任ʱ�䣻
- [37. ������](https://leetcode-cn.com/problems/sudoku-solver/) ��˼·ͬ��N �ʺ����⡹����ʵ�϶����������͵��⣬�кܶ���׵����������ͼ�֦���Կ�������ٶȣ���[����ʽ����](https://www.sudokuwiki.org/Naked_Candidates)��
- [488. ������Ϸ](https://leetcode-cn.com/problems/zuma-game/)
- [529. ɨ����Ϸ](https://leetcode-cn.com/problems/minesweeper/)

### ��Ŀ����

#### [46. ȫ����](https://leetcode-cn.com/problems/permutations/)

``` c++
vector<vector<int>> permute(vector<int>& nums) {// ������
    vector<vector<int>> ans;
    backtracking(nums, 0, ans);
    return ans;
}

void backtracking(vector<int> &nums, int level, vector<vector<int>> &ans) {// ������
    if (level == nums.size() - 1) {
        ans.push_back(nums);
        return;
    }
    for (int i = level; i < nums.size(); i++) {
        swap(nums[i], nums[level]); // �޸ĵ�ǰ�ڵ�״̬
        backtracking(nums, level+1, ans); // �ݹ��ӽڵ�
        swap(nums[i], nums[level]); // �ظĵ�ǰ�ڵ�״̬
    }
}
```

#### [77. ���](https://leetcode-cn.com/problems/combinations/)

``` c++
vector<vector<int>> combine(int n, int k) {// ������
    vector<vector<int>> ans;
    vector<int> comb(k, 0);
    int count = 0;
    backtracking(ans, comb, count, 1, n, k);
    return ans;
}

void backtracking(vector<vector<int>>& ans, vector<int>& comb, int& count, int
                  pos, int n, int k) {// ������
    if (count == k) {
        ans.push_back(comb);
        return;
    }
    for (int i = pos; i <= n; ++i) {
        comb[count++] = i; // �޸ĵ�ǰ�ڵ�״̬
        backtracking(ans, comb, count, i + 1, n, k); // �ݹ��ӽڵ�
        --count; // �ظĵ�ǰ�ڵ�״̬
    }
}
```

#### [79. ��������](https://leetcode-cn.com/problems/word-search/)

``` c++
bool exist(vector<vector<char>>& board, string word) { // ������
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
                  & find, vector<vector<bool>>& visited, int pos) { // ������
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
    visited[i][j] = true; // �޸ĵ�ǰ�ڵ�״̬
    // �ݹ��ӽڵ�
    backtracking(i + 1, j, board, word, find, visited, pos + 1);
    backtracking(i - 1, j, board, word, find, visited, pos + 1);
    backtracking(i, j + 1, board, word, find, visited, pos + 1);
    backtracking(i, j - 1, board, word, find, visited, pos + 1);
    visited[i][j] = false; // �ظĵ�ǰ�ڵ�״̬
}
```

#### [51. N �ʺ�](https://leetcode-cn.com/problems/n-queens/)

``` c++
vector<vector<string>> solveNQueens(int n) { // ������
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
                  vector<bool> &ldiag, vector<bool> &rdiag, int row, int n) { // ������
    if (row == n) {
        ans.push_back(board);
        return;
    }
    for (int i = 0; i < n; ++i) {
        if (column[i] || ldiag[n-row+i-1] || rdiag[row+i]) {
            continue;
        }
        // �޸ĵ�ǰ�ڵ�״̬
        board[row][i] = 'Q';
        column[i] = ldiag[n-row+i-1] = rdiag[row+i] = true;
        // �ݹ��ӽڵ�
        backtracking(ans, board, column, ldiag, rdiag, row+1, n);
        // �ظĵ�ǰ�ڵ�״̬
        board[row][i] = '.';
        column[i] = ldiag[n-row+i-1] = rdiag[row+i] = false;
    }
}
```



## ������ȱ�����BFS��

> ��һ�����б����ģ������Ҫ�������ȳ��Ķ��У�Queue��������������ջ���б�����
>
> ���������������·�������⡣
>
> ������������͹���������������Դ���ɴ������⣬����һ���ڵ㿪ʼ�Ƿ��ܴﵽ��һ���ڵ㡣������������������õݹ����ʵ�֣���ʵ����������У��ݹ�һ����������⣬��һ������ܲ���ջ��������������ջʵ�ֵ���������������ö���ʵ�ֵĹ������������д���ϲ�û��̫����죬���ʹ����һ��������ʽ��Ҫ����ʵ�ʵĹ����������жϡ�

#### [934. ��̵���](https://leetcode-cn.com/problems/shortest-bridge/)

``` c++
vector<int> direction{-1, 0, 1, 0, -1};
// ������
int shortestBridge(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    queue<pair<int, int>> points;
    // dfsѰ�ҵ�һ�����죬����1ȫ����ֵΪ2
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
    // bfsѰ�ҵڶ������죬���ѹ����о�����0��ֵΪ2
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
// ������
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

#### [126. ���ʽ��� II](https://leetcode-cn.com/problems/word-ladder-ii/)

> - ����ʼ�ַ�������ֹ�ַ������Լ����ʱ������е��ַ�������ɽڵ㡣��ô���������ַ���ֻ��һ���ַ���ͬ����ô������������Ϊ��Ŀ��Ҫ����޸Ĵ������ٵ������޸ķ�ʽ��������ǿ���ʹ�ù������������ת��Ϊ�����ʼ�ڵ㵽��ֹ�ڵ����̾��롣
> - С���ɣ���ֱ�Ӵ���ʼ�ڵ���й������������ֱ���ҵ���ֹ�ڵ�Ϊֹ�����Ǵ���ʼ�ڵ����ֹ�ڵ�ֱ���й������������ÿ��ֻ��չ��ǰ��ڵ������ٵ���һ�ˣ��������ǿ��Լ����������ܽ������������˵��������̾���Ϊ4���������ֻ��һ������4 �㣬�ܱ����ڵ�������� 1 + 2 + 4 + 8 + 16 = 31����������Ǵ����˸��������㣬�ܱ����ڵ������ֻ�� 2*��1 + 2 + 4�� = 14��
> - ���������������ǻ���Ҫͨ�����ݷ����ؽ����п��ܵ�·����

``` c++
// ������
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
// ������
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



#### [733. ͼ����Ⱦ](https://leetcode-cn.com/problems/flood-fill/)

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

#### [695. �����������](https://leetcode-cn.com/problems/max-area-of-island/)

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

#### [617. �ϲ�������](https://leetcode-cn.com/problems/merge-two-binary-trees/)

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

#### [116. ���ÿ���ڵ����һ���Ҳ�ڵ�ָ��](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

- ��α���--��ͬһ��ڵ�ͬʱ���д���
- ����BFS

``` c++
Node* connect(Node* root) {
    if(root == nullptr) {
        return root;
    }
    queue<Node*> Q;
    Q.push(root);
    //while��forѭ������ͬһ��
    while(!Q.empty()) {
        int size = Q.size();
        for(int i = 0; i < size; ++i) {
            //forѭ������ֻ����ͬһ��
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

��������һ�����úõ�nextָ�룬�����������

``` c++
Node* connect(Node* root) {
    if(!root) {
        return root;
    }
    Node* leftmost = root;
    while(leftmost->left != nullptr) {
        //ͨ��node->left���Ʊ���ȫ����
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

#### [257. ������������·��](https://leetcode-cn.com/problems/binary-tree-paths/)

> ���ǻ��ݷ�ʹ�������ʲô����

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

#### [130. ��Χ�Ƶ�����](https://leetcode-cn.com/problems/surrounded-regions/)

> �����ȴ��������䣬Ȼ���ٿ������

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

#### [310. ��С�߶���](https://leetcode-cn.com/problems/minimum-height-trees/)

> ������ν������תΪ���������⣿��ʹ��������Ȼ��ǹ�������أ�

``` c++

```

[�ο�](https://leetcode-cn.com/problems/minimum-height-trees/solution/c-xun-xu-jian-jin-de-si-lu-bfsdfstuo-bu-hmk2y/)