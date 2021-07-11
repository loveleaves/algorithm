# 图的遍历



## 深度优先遍历（DFS）

> 有递归和非递归两种表现形式。
>
> 递归实现如果层级太深，会导致栈溢出。
>
> 非递归实现利用栈stack结构。



#### [733. 图像渲染](https://leetcode-cn.com/problems/flood-fill/)

``` c++
const int dx[4] = {1, 0, 0, -1};
const int dy[4] = {0, 1, -1, 0};
void dfs(vector<vector<int>>& image, int x, int y, int color, int newColor) {
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
    if (currColor != newColor) {
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



## 广度优先遍历（BFS）

> 利用队列queue

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

