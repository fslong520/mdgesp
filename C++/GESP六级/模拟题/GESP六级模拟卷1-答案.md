---
title: "GESP六级模拟卷1 - 答案与解析"
description: 模拟卷1全部答案与解析（含编程题完整参考代码）
---

# GESP 六级模拟卷 1 · 答案与解析

## 一、选择题答案

| 题号 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
| 答案 | C | C | A | C | A | A | A | D | D | C  | B  | B  | B  | A  | C  |

### 解析

1. **C**。基类析构函数声明为虚函数，通过基类指针删除派生类对象时会先调用派生类析构函数再调用基类析构函数，资源释放完整；构造函数在对象构造阶段执行，无法动态绑定，不能声明为虚函数（B 错）；虚函数是运行时（动态）绑定而非编译期静态绑定（A 错）；虚函数调用有动态绑定开销（D 错）。
2. **C**。同一基类指针 `Animal*` 指向不同派生类对象，调用 `speak()` 得到不同结果——运行时多态。
3. **A**。公有继承下，基类 public 成员仍 public，protected 成员仍 protected，private 成员不可访问。
4. **C**。压入 1,2,3,4 后栈顶为 4；弹两次弹出 4、3；再压入 5 后栈顶为 5。
5. **A**。入队 1、2、3 后元素落在位置 0、1、2，rear=3；出队一次 front=1；继续入队 4、5、6 依次填位置 3、4、5，rear 回到 0。故 front=1, rear=0。
6. **A**。完全二叉树按层序编号，节点 i 的左孩子编号为 2i，故 2×6=12。
7. **A**。前序 `ABDECF` 根为 A；中序 `DBEAFC` 分左子树 DBE、右子树 FC。左子树根 B（左 D、右 E），右子树根 C（左 F）。后序：左右根 → DEBFCA。
8. **D**。频率 {7,5,2,4}，哈夫曼树：合并 2+4=6，再合并 5+6=11，最后 7+11=18。深度：7 在第 1 层，5 在第 2 层，2 和 4 在第 3 层。WPL = 7×1 + 5×2 + 2×3 + 4×3 = 7+10+6+12 = 35。
9. **D**。三位格雷码序列：000,001,011,010,110,111,101,100，`110` 之后是 `111`（恰一位不同）。
10. **C**。BFS 逐层访问，先入先出，需队列；DFS 才用栈/递归。
11. **B**。BST 左子树值均小于根、右子树均大于根；50 > 45，去右子树。
12. **B**。一维滚动数组必须倒序遍历容量，防止同一件物品被重复使用（正序会变成完全背包）。
13. **B**。最优子结构 + 重叠子问题是动态规划的两大性质。
14. **A**。遇左括号入栈，遇右括号弹出配对；扫描完毕栈空说明全部匹配。
15. **C**。哈夫曼编码是最优前缀码，频率越高编码越短；编码不唯一（可交换左右子树），故 A/B/D 错。

## 二、判断题答案

| 题号 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|------|----|----|----|----|----|----|----|----|----|----|
| 答案 | F  | T  | T  | F  | T  | F  | T  | T  | F  | T  |

### 解析

16. **F**。构造调用了 3 次：`Test a`（默认构造）、`Test b = a`（拷贝构造）、`Test c`（默认构造）。
17. **T**。封装 = 数据 + 操作绑定 + 隐藏实现细节。
18. **T**。空树高度 0，非空树取左右子树高度较大者再加 1——正确。
19. **F**。BFS 应用队列实现；栈用于 DFS。
20. **T**。函数调用由调用栈管理，递归过深会栈溢出。
21. **F**。BST 操作平均为 $O(\log n)$，但退化（如按序插入成链）时最坏为 $O(n)$，并非"总是 $O(\log n)$"。
22. **T**。按 key 与根值比较决定进入左子树或右子树，直到空或找到——正确。
23. **T**。n 位格雷码与 n 位二进制码一一对应，共有 $2^n$ 个。
24. **F**。权值相等或合并顺序不同时，哈夫曼树不唯一（WPL 相同）。
25. **T**。满二叉树每层都满，必为完全二叉树；完全二叉树只要求最后一层靠左连续，不一定是满二叉树。

## 三、编程题题解

### 第 26 题【划段得分】—— 线性 DP + 位掩码（划分型 DP ①）

**思路**：`f[i]` 表示前缀 `s[1..i]` 的最大总分。枚举最后一段的起点 `j`，段 `s[j..i]` 合法（段内字符互异），则 `f[i] = max(f[i], f[j-1] + a[i-j+1])`。判断段内字符是否互异可用位掩码：从 `i` 向左扩展 `j`，遇到重复字符即停止。

**复杂度**：段内字符最多 26 种，每次扩展至多 26 步，$O(26n)$。

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main() {
    int n; cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    string s; cin >> s;
    s = " " + s;
    vector<int> f(n + 1, -1e9);
    f[0] = 0;
    for (int i = 1; i <= n; i++) {          // 枚举右端点
        int mask = 0;                        // 段内出现过的字符
        for (int j = i; j >= 1; j--) {       // 向左扩展，维护段 [j..i]
            int c = s[j] - 'a';
            if (mask & (1 << c)) break;      // 段内字符重复，停止扩展
            mask |= (1 << c);
            f[i] = max(f[i], f[j - 1] + a[i - j + 1]);
        }
    }
    cout << f[n] << endl;
    return 0;
}
```

### 第 27 题【分组积分】—— 线性 DP（划分型 DP ②）

**思路**：`f[i]` 表示 i 名同学的最大总效果。枚举最后一组人数 `j`（$L \le j \le R$），`f[i] = max(f[i], f[i-j] + a[j])`。注意只有可达的状态才转移。

**复杂度**：$O(n \cdot (R - L + 1))$，最坏 $O(n^2)$，n ≤ 1000 可过。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n, L, R; cin >> n >> L >> R;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    vector<int> f(n + 1, -1e9);
    f[0] = 0;
    for (int i = 1; i <= n; i++)               // 总人数 i
        for (int j = L; j <= R && j <= i; j++)  // 最后一组 j 人
            if (f[i - j] != -1e9)
                f[i] = max(f[i], f[i - j] + a[j]);
    cout << f[n] << endl;
    return 0;
}
```

### 第 28 题【森林派对】—— 树形 DP（最大权独立集）

**思路**：`f[u][0]` 表示不选 u 时 u 的子树最大快乐值，`f[u][1]` 表示选 u 时的值。

- 不选 u：孩子可任意选或不选，`f[u][0] = Σ max(f[v][0], f[v][1])`
- 选 u：孩子都不能选，`f[u][1] = w[u] + Σ f[v][0]`

答案 `max(f[1][0], f[1][1])`。用 `vector` 邻接表建图，一次 DFS 自底向上即可，n ≤ 1e5 直接递归可过。

**复杂度**：$O(n)$。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n;
long long w[100005], f[100005][2];
vector<int> g[100005];

void dfs(int u, int fa) {
    f[u][1] = w[u];                       // 选 u
    for (int v : g[u]) {
        if (v == fa) continue;
        dfs(v, u);                        // 先算孩子
        f[u][0] += max(f[v][0], f[v][1]); // 不选 u：孩子可任意
        f[u][1] += f[v][0];               // 选 u：孩子都不能选
    }
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> w[i];
    for (int i = 1; i < n; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    dfs(1, 0);
    cout << max(f[1][0], f[1][1]) << endl;
    return 0;
}
```

### 第 29 题【树的直径】—— 两遍 DFS（树的搜索）

**思路**：树的直径经典做法——任选一点出发 DFS，找到距离它最远的点 a；再从 a 出发 DFS，找到距离 a 最远的点 b，a 到 b 的距离即为直径。`vector` 邻接表建图，两遍递归 DFS 即可。

**复杂度**：两遍遍历 $O(n)$。

```cpp
#include <iostream>
#include <vector>
using namespace std;
int n, far, best;
vector<int> g[100005];

void dfs(int u, int fa, int dep) {
    if (dep > best) { best = dep; far = u; }   // 更新最远点
    for (int v : g[u])
        if (v != fa) dfs(v, u, dep + 1);
}

int main() {
    cin >> n;
    for (int i = 1; i < n; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    best = -1; dfs(1, 0, 0);      // 第一遍：任取 1 号点找最远点 far
    best = -1; dfs(far, 0, 0);    // 第二遍：far 到最远点的距离即直径
    cout << best << endl;
    return 0;
}
```