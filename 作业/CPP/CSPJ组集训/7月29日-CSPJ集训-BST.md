---
title: "7月29日-CSPJ集训-BST"
description: "二叉搜索树（BST）性质、插入、查找、删除"
date: 2025-07-29
tags: ["BST", "二叉搜索树", "CSPJ集训"]
math: true
---

# 二叉搜索树（BST）作业

**日期：** 2025年7月29日  
**总分：** 300 分（客观题 100 分 + 编程题 200 分）  
**答题时间：** 90 分钟

---

## 一、单项选择题（每题 5 分，共 100 分）

### 第 1 题

下列关于二叉搜索树（BST）的说法，正确的是（ ）。

A. BST中任一节点的左子树所有节点值均大于该节点值  
B. 对BST进行中序遍历可以得到一个递增有序序列  
C. BST的前序遍历序列一定是有序的  
D. BST中任一节点的右子树所有节点值均小于该节点值  

---

### 第 2 题

以下代码实现了二叉排序树的哪种操作？

```cpp
TreeNode* op(TreeNode* root, int val) {
    if (root == nullptr) return new TreeNode(val);
    if (val < root->val) {
        root->left = op(root->left, val);
    } else {
        root->right = op(root->right, val);
    }
    return root;
}
```

A. 查找  
B. 插入  
C. 删除  
D. 遍历  

---

### 第 3 题

给定如下二叉搜索树查找函数：

```cpp
bool search(TreeNode* root, int x) {
    if (root == nullptr) return false;
    if (root->val == x) return true;
    if (x < root->val) return search(root->left, x);
    return search(root->right, x);
}
```

关于该函数在最坏情况下的时间复杂度，说法正确的是（ ）。

A. 最坏情况下访问节点数为 O(log n)  
B. 最坏情况下访问节点数为 O(n)  
C. 无论如何，访问节点数都不超过树高的一半  
D. 一定比在普通二叉树中搜索快  

---

### 第 4 题

依次将 5, 3, 7, 2, 4, 6, 8 插入一棵初始为空的二叉搜索树，最终树的根节点是（ ）。

A. 2  
B. 4  
C. 5  
D. 7  

---

### 第 5 题

对第 4 题构建的 BST，中序遍历的结果是（ ）。

A. 2, 3, 4, 5, 6, 7, 8  
B. 5, 3, 2, 4, 7, 6, 8  
C. 8, 7, 6, 5, 4, 3, 2  
D. 5, 7, 3, 8, 6, 4, 2  

---

### 第 6 题

在二叉搜索树中删除一个叶子节点，正确的做法是（ ）。

A. 将该节点替换为其左子节点  
B. 将该节点替换为其右子节点  
C. 将该节点的父节点指向该节点的指针置为 nullptr  
D. 将该节点与中序后继交换后删除  

---

### 第 7 题

将有序序列 {1, 2, 3, 4, 5} 按顺序依次插入一棵初始为空的二叉搜索树，最终树的形状是（ ）。

A. 完全二叉树  
B. 平衡二叉树  
C. 退化为链表的斜树  
D. 满二叉树  

---

### 第 8 题

在C++ STL中，`map` 和 `set` 容器的底层实现通常是（ ）。

A. 哈希表  
B. 红黑树（平衡二叉搜索树）  
C. 数组  
D. 链表  

---

### 第 9 题

在二叉搜索树中查找元素 3，从根节点 10 开始，以下哪个查找路径是可能的？

A. 10 → 5 → 2 → 3  
B. 10 → 8 → 12 → 3  
C. 10 → 15 → 7 → 3  
D. 10 → 6 → 9 → 3  

---

### 第 10 题

若一棵二叉搜索树的先序遍历序列为 8, 3, 1, 6, 4, 7, 10, 14, 13，则其中序遍历序列为（ ）。

A. 1, 3, 4, 6, 7, 8, 10, 13, 14  
B. 8, 3, 1, 6, 4, 7, 10, 14, 13  
C. 1, 4, 7, 6, 3, 13, 14, 10, 8  
D. 8, 10, 14, 13, 3, 6, 7, 4, 1  

---

### 第 11 题

以下关于BST性质的说法，错误的是（ ）。

A. BST的插入操作不需要调整树结构  
B. 不同的插入顺序可能产生不同形状的BST  
C. BST的查找效率只与树高有关  
D. 对BST进行层序遍历得到的结果一定有序  

---

### 第 12 题

给定以下代码，它实现了二叉树的哪种遍历？

```cpp
void traverse(TreeNode* root) {
    if (root == nullptr) return;
    traverse(root->left);
    cout << root->val << " ";
    traverse(root->right);
}
```

A. 前序遍历  
B. 中序遍历  
C. 后序遍历  
D. 层序遍历  

---

### 第 13 题

将序列 {50, 30, 80, 20, 40, 70, 90, 10, 25, 35, 45} 依次插入BST后，节点 40 的父节点是（ ）。

A. 20  
B. 30  
C. 35  
D. 45  

---

### 第 14 题

BST 的查找效率在最好情况下为 O(log n)，这要求树的结构接近于（ ）。

A. 完全二叉树  
B. 平衡二叉树  
C. 斜树  
D. 满二叉树  

---

### 第 15 题

若一棵BST共有 7 个节点，且中序遍历序列为 {1, 2, 3, 4, 5, 6, 7}，则以下哪个**不可能**是该BST的先序遍历序列？

A. 4, 2, 1, 3, 6, 5, 7  
B. 1, 2, 3, 4, 5, 6, 7  
C. 7, 6, 5, 4, 3, 2, 1  
D. 4, 2, 5, 1, 3, 6, 7  

---

### 第 16 题

关于BST中节点的前驱与后继，下列说法正确的是（ ）。

A. 一个节点的中序后继一定在其右子树中  
B. 一个节点的中序前驱一定在其左子树中  
C. 根节点没有前驱  
D. 叶子节点没有后继  

---

### 第 17 题

在BST中，设某节点有左子节点，则以下说法正确的是（ ）。

A. 该节点左子树中所有节点的值均小于该节点的父节点的值  
B. 该节点左子树中所有节点的值均小于该节点的值  
C. 该节点左子树中所有节点的值均大于该节点的值  
D. 该节点左子树中所有节点的值均大于该节点父节点的值  

---

### 第 18 题

将序列 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 按任意顺序插入BST，树的高度不可能为以下哪个值？

A. 10  
B. 5  
C. 4  
D. 3  

---

### 第 19 题

二叉搜索树与二分查找（折半查找）的关系，下列说法正确的是（ ）。

A. BST的查找过程与二分查找完全相同  
B. 对有序数组建立平衡BST，查找效率与二分查找相同  
C. BST查找一定比二分查找快  
D. 二分查找只能用于链表  

---

### 第 20 题

下列关于BST构建的说法，正确的是（ ）。

A. 给定 BST 的中序遍历序列，可以唯一确定一棵 BST  
B. 给定 BST 的先序遍历序列，可以唯一确定一棵 BST  
C. 给定 BST 的层序遍历序列，可以唯一确定一棵 BST  
D. BST 的中序遍历序列一定是递增的，因此无法唯一确定树结构  

---

## BST 操作模板（供编程题参考）

### 链式版（指针）

```cpp
#include <bits/stdc++.h>
using namespace std;

struct BST {
    struct Node {
        int val;
        Node *l, *r;
        Node(int v) : val(v), l(nullptr), r(nullptr) {}
    };

    Node* root;
    BST() : root(nullptr) {}

    void ins(int v, Node*& p = root) {
        if (!p) { p = new Node(v); return; }
        if (v < p->val) ins(v, p->l);
        else ins(v, p->r);
    }

    bool sch(int v, Node* p = root) {
        if (!p) return false;
        if (p->val == v) return true;
        return v < p->val ? sch(v, p->l) : sch(v, p->r);
    }

    int mn(Node* p = root) {
        while (p->l) p = p->l;
        return p->val;
    }

    int mx(Node* p = root) {
        while (p->r) p = p->r;
        return p->val;
    }

    void ino(Node* p = root) {
        if (!p) return;
        ino(p->l);
        cout << p->val << ' ';
        ino(p->r);
    }
};
```

### 数组版（静态空间）

```cpp
struct BST {
    static const int N = 1005;
    int l[N], r[N], val[N], root, idx;

    BST() : root(0), idx(0) {}

    void ins(int v, int &p) {
        if (!p) { p = ++idx; val[p] = v; l[p] = r[p] = 0; return; }
        if (v < val[p]) ins(v, l[p]);
        else ins(v, r[p]);
    }

    bool sch(int v, int p) {
        if (!p) return false;
        if (val[p] == v) return true;
        return v < val[p] ? sch(v, l[p]) : sch(v, r[p]);
    }

    int mn(int p) {
        while (l[p]) p = l[p];
        return val[p];
    }

    int mx(int p) {
        while (r[p]) p = r[p];
        return val[p];
    }

    void ino(int p) {
        if (!p) return;
        ino(l[p]);
        cout << val[p] << ' ';
        ino(r[p]);
    }
};
```

### 动态数组版（vector）

```cpp
#include <vector>

struct bst {
    struct dog { int v, l, r; };
    vector<dog> t;
    int root;

    bst() : root(0) { t.push_back({0, 0, 0}); }

    void ins(int v, int &p) {
        if (!p) { p = t.size(); t.push_back({v, 0, 0}); return; }
        if (v < t[p].v) ins(v, t[p].l);
        else ins(v, t[p].r);
    }

    bool sch(int v, int p) {
        if (!p) return false;
        if (t[p].v == v) return true;
        return v < t[p].v ? sch(v, t[p].l) : sch(v, t[p].r);
    }

    int mn(int p) {
        while (t[p].l) p = t[p].l;
        return t[p].v;
    }

    int mx(int p) {
        while (t[p].r) p = t[p].r;
        return t[p].v;
    }

    void ino(int p) {
        if (!p) return;
        ino(t[p].l);
        cout << t[p].v << ' ';
        ino(t[p].r);
    }

    string dfs(int p, int v) {
        if (t[p].v == v) return "";
        if (v < t[p].v) return "L" + dfs(t[p].l, v);
        else return "R" + dfs(t[p].r, v);
    }
};
```

### vector 解法·图书分类

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct bst {
    struct dog { int v, l, r; };
    vector<dog> t;
    int root;

    bst() : root(0) { t.push_back({0, 0, 0}); }

    void ins(int v, int &p) {
        if (!p) { p = t.size(); t.push_back({v, 0, 0}); return; }
        if (v < t[p].v) ins(v, t[p].l);
        else ins(v, t[p].r);
    }

    string dfs(int p, int v) {
        if (t[p].v == v) return "";
        if (v < t[p].v) return "L" + dfs(t[p].l, v);
        else return "R" + dfs(t[p].r, v);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, v;
    cin >> n >> m;
    bst tree;
    while (n--) { cin >> v; tree.ins(v, tree.root); }
    while (m--) { cin >> v; cout << tree.dfs(tree.root, v) << '\n'; }
    return 0;
}
```

## 二、编程题（每题 100 分，共 200 分）

---

### 第 1 题 图书分类（100 分）— <a href="https://fslong.iok.la/problem/P9818" target="_blank">🧑‍💻 在线答题</a>

**题目描述**

学校图书馆新进了一批图书，管理员使用"二叉搜索树"的方式为每本书分配一个编号并上架。

上架规则如下：
- 第一本书放在根位置
- 后续每本书的编号与当前节点比较：若编号小于当前节点，则往左走；若大于，则往右走。走到空位时放入。

现在，管理员想标记某本书的位置：从根节点出发，每向左走一步记录一个 L，每向右走一步记录一个 R，到达该书所在节点后输出路径。

**输入格式**

第一行两个整数 n 和 m（1 ≤ n, m ≤ 1000），n 表示图书总数，m 表示查询次数。

第二行 n 个互不相同的正整数 a₁, a₂, ..., aₙ，表示按顺序上架的图书编号。

接下来 m 行，每行一个正整数 x，表示要查询位置的图书编号。保证 x 在树中。

**输出格式**

对于每个查询，输出一行字符串，表示从根到该节点的路径（L 表示左，R 表示右）。若查询的是根节点，则输出一个空行。

**样例输入**

```
7 3
5 3 7 2 4 6 8
5
2
8
```

**样例输出**

```

LL
RR
```

**数据范围**

对于 30% 的数据，n ≤ 10。  
对于 60% 的数据，n ≤ 100。  
对于 100% 的数据，1 ≤ n, m ≤ 1000，1 ≤ aᵢ, x ≤ 10⁹。

---

### 第 2 题 BST 验证（100 分）— <a href="https://fslong.iok.la/problem/P9819" target="_blank">🧑‍💻 在线答题</a>

**题目描述**

给定一个整数序列，判断它是否可能是某一棵二叉搜索树的先序遍历序列。

**输入格式**

第一行一个整数 n（1 ≤ n ≤ 1000），表示序列长度。  
第二行 n 个正整数 a₁, a₂, ..., aₙ。

**输出格式**

如果可能是某棵 BST 的先序遍历，输出 YES，否则输出 NO。

**样例输入 1**

```
5
5 3 2 4 8
```

**样例输出 1**

```
YES
```

**样例输入 2**

```
4
5 3 8 4
```

**样例输出 2**

```
NO
```

**提示**

BST 先序遍历的特点是：第一个元素为根，其后连续一段比根小的为左子树，再之后连续一段比根大的为右子树。左右子树递归满足此性质。

**数据范围**

对于 30% 的数据，n ≤ 10。  
对于 60% 的数据，n ≤ 100。  
对于 100% 的数据，1 ≤ n ≤ 1000，1 ≤ aᵢ ≤ 10⁹。

---

## 三、参考答案速查

| 题号 | 答案 | 题号 | 答案 | 题号 | 答案 | 题号 | 答案 |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 1 | B | 6 | C | 11 | D | 16 | A |
| 2 | B | 7 | C | 12 | B | 17 | B |
| 3 | B | 8 | B | 13 | B | 18 | D |
| 4 | C | 9 | A | 14 | B | 19 | B |
| 5 | A | 10 | A | 15 | D | 20 | D |

编程题参考代码见解析。
