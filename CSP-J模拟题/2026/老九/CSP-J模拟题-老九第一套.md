# CSP-J 入门级第一轮模拟试卷（第1套）

**来源**：老九
**考试时间**：120分钟
**满分**：100分
**命题范围**：计算机基础、C++基础、数据结构与算法、数学与逻辑、阅读程序、完善程序

---

## 一、单项选择题

- 共 15 题，每题 2 分，共计 30 分
- 每题有且仅有一个正确选项

1. 十进制数 45 转换成二进制数是（ ）。
   A. (101101)₂
   B. (110101)₂
   C. (101011)₂
   D. (110011)₂

2. 在计算机中，通常用一个字节表示（ ）。
   A. 2个二进制位
   B. 4个二进制位
   C. 8个二进制位
   D. 16个二进制位

3. 下列设备中，主要用作输出设备的是（ ）。
   A. 键盘
   B. 鼠标
   C. 扫描仪
   D. 显示器

4. 在 C++中，表达式 17 / 5 + 17 % 5 的值是（ ）。
   A. 3
   B. 4
   C. 5
   D. 5.4

5. 执行下面的代码后，变量 x 的值是（ ）。

```cpp
int x = 3;
x += x * 2;
```

   A. 6
   B. 9
   C. 12
   D. 15

6. 若 int a[10];，则数组 a 的合法下标范围是（ ）。
   A. 1 到 10
   B. 0 到 10
   C. 0 到 9
   D. 1 到 9

7. 一个栈按顺序压入元素 1, 2, 3, 4。在压入过程中可以随时弹出，则下列序列中不可能成为完整弹出序列的是（ ）。
   A. 4, 3, 2, 1
   B. 2, 1, 4, 3
   C. 3, 1, 2, 4
   D. 1, 2, 3, 4

8. 一个队列当前从队首到队尾依次为 2, 5, 7。依次执行"入队 9、出队一次、入队 4"后，队首元素是（ ）。
   A. 2
   B. 5
   C. 7
   D. 9

9. 对长度为 n 的有序数组进行二分查找，其最坏时间复杂度是（ ）。
   A. O(1)
   B. O(log n)
   C. O(n)
   D. O(n log n)

10. 对序列 5, 1, 4, 2, 3 进行一趟从左到右的冒泡排序（相邻逆序时交换），得到的序列是（ ）。
    A. 1, 4, 2, 3, 5
    B. 1, 2, 3, 4, 5
    C. 5, 1, 2, 3, 4
    D. 1, 5, 2, 3, 4

11. 一棵具有 20 个结点的树共有（ ）条边。
    A. 18
    B. 19
    C. 20
    D. 21

12. 无向完全图 K6 共有（ ）条边。
    A. 6
    B. 12
    C. 15
    D. 30

13. 从 1, 2, 3, 4, 5 中选出两个不同的数，不考虑选择顺序，共有（ ）种选法。
    A. 5
    B. 8
    C. 10
    D. 20

14. 设命题 P 为"所有质数都是奇数"，命题 Q 为"存在一个偶数是质数"。下列说法正确的是（ ）。
    A. P真，Q真
    B. P真，Q假
    C. P假，Q真
    D. P假，Q假

15. 有 8 个外观相同的小球，其中恰有 1 个较轻。使用没有砝码的天平，保证找出较轻小球至少需要称量（ ）次。
    A. 1
    B. 2
    C. 3
    D. 4

---

## 二、阅读程序

- 共 40 分
- 除特殊说明外，假设输入数据均合法，程序运行环境支持 C++17。

### （一）（每题 3 分，共 12 分）

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        int x = i;
        while (x > 0) {
            ans += x % 10;
            x /= 10;
        }
    }
    cout << ans << endl;
    return 0;
}
```

16. 当输入为 5 时，输出为（ ）。
    A. 5
    B. 10
    C. 15
    D. 20

17. 当输入为 12 时，输出为（ ）。
    A. 48
    B. 51
    C. 54
    D. 78

18. 该程序的功能是（ ）。
    A. 计算 1 到 n 的整数之和
    B. 计算 n 的各位数字之和
    C. 计算 1 到 n 中所有整数的各位数字之和
    D. 统计 1 到 n 中十进制数字的总个数

19. 若 n 是一个不超过 10⁹ 的正整数，该程序的时间复杂度最接近（ ）。
    A. O(log n)
    B. O(n)
    C. O(n log n)
    D. O(n²)

### （二）（每题 3 分，共 12 分）

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    int best = 1, len = 1;
    for (int i = 1; i < n; i++) {
        if (a[i] > a[i - 1]) len++;
        else len = 1;
        best = max(best, len);
    }
    cout << best << endl;
    return 0;
}
```

20. 输入如下：

```
7
1 2 2 3 5 4 6
```

    输出为（ ）。
    A. 2
    B. 3
    C. 4
    D. 5

21. 若输入序列严格递减，程序输出为（ ）。
    A. 0
    B. 1
    C. n−1
    D. n

22. 程序计算的是（ ）。
    A. 最长严格上升子序列的长度
    B. 最长非下降连续子段的长度
    C. 最长严格上升连续子段的长度
    D. 所有严格上升连续子段的数量

23. 若将判断条件 a[i] > a[i - 1] 改为 a[i] >= a[i - 1]，程序将计算（ ）。
    A. 最长严格上升连续子段长度
    B. 最长非下降连续子段长度
    C. 最长非上升连续子段长度
    D. 最长非下降子序列长度

### （三）（每题 4 分，共 16 分）

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    vector<int> deg(n + 1, 0);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        deg[v]++;
    }

    priority_queue<int, vector<int>, greater<int>> q;
    for (int i = 1; i <= n; i++)
        if (deg[i] == 0) q.push(i);

    vector<int> ans;
    while (!q.empty()) {
        int u = q.top();
        q.pop();
        ans.push_back(u);
        for (int v : g[u]) {
            deg[v]--;
            if (deg[v] == 0) q.push(v);
        }
    }

    if ((int)ans.size() < n) cout << -1 << endl;
    else {
        for (int x : ans) cout << x << ' ';
        cout << endl;
    }
    return 0;
}
```

24. 该程序使用的核心算法是（ ）。
    A. 深度优先搜索求连通块
    B. Dijkstra最短路
    C. Kahn算法求拓扑序
    D. Kruskal最小生成树

25. 输入如下：

```
4 4
1 2
1 3
2 4
3 4
```

    程序输出为（ ）。
    A. 1234
    B. 1324
    C. 4231
    D. -1

26. 使用小根堆 priority_queue<int, vector<int>, greater<int>> 的主要作用是（ ）。
    A. 保证每次选择编号最小的当前入度为 0 的结点
    B. 保证每次选择出度最小的结点
    C. 将所有边按权值排序
    D. 判断图是否连通

27. 若输入图含有有向环，则（ ）。
    A. 程序一定陷入死循环
    B. ans 中一定会出现重复结点
    C. 最终 ans.size() < n，程序输出 −1
    D. 程序仍会输出字典序最小的结点排列

---

## 三、完善程序

- 共 2 题，15 空，每空 3 分，共计 30 分
- 每空有且仅有一个正确选项

### （一）判断质数（共 15 分）

下面的程序读入正整数 n，判断它是否为质数。若是，输出 Yes；否则输出 No。

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;

    bool prime = true;
    if (____①____) prime = false;
    for (long long i = 2; ____②____ && prime; i++) {
        if (____③____) {
            prime = false;
        }
    }

    if (____④____) cout << ____⑤____ << endl;
    else cout << "No" << endl;
    return 0;
}
```

28. ①处应填（ ）。
    A. n < 0
    B. n <= 1
    C. n == 2
    D. n % 2 == 0

29. ②处应填（ ）。
    A. i < n
    B. i * i <= n
    C. i + i <= n
    D. i <= n / 2 + 1

30. ③处应填（ ）。
    A. n / i == 0
    B. i % n == 0
    C. n % i == 0
    D. n % i != 0

31. ④处应填（ ）。
    A. n
    B. i
    C. prime
    D. !prime

32. ⑤处应填（ ）。
    A. "Yes"
    B. "No"
    C. prime
    D. n

### （二）最短路（共 15 分）

给定一个 n 行 m 列的网格，字符 `.` 表示可以通过，字符 `#` 表示障碍。程序计算从左上角 (0, 0) 到右下角 (n − 1, m − 1) 最少需要走多少步。每一步可以向上、下、左、右移动一格；若无法到达，输出 −1。保证起点和终点不是障碍。

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> s(n);
    for (auto &row : s) cin >> row;

    vector<vector<int>> dis(n, vector<int>(m, -1));
    queue<pair<int, int>> q;
    q.push({0, 0});
    ____①____;

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    while (____②____) {
        auto [x, y] = q.front();
        ____③____;
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (s[nx][ny] == '#') continue;
            if (____④____) continue;
            dis[nx][ny] = ____⑤____;
            q.push({nx, ny});
        }
    }

    cout << dis[n - 1][m - 1] << endl;
    return 0;
}
```

33. ①处应填（ ）。
    A. dis[0][0] = -1
    B. dis[0][0] = 0
    C. dis[n - 1][m - 1] = 0
    D. s[0][0] = '#'

34. ②处应填（ ）。
    A. q.empty()
    B. q.size() == 1
    C. !q.empty()
    D. dis[n - 1][m - 1] == -1

35. ③处应填（ ）。
    A. q.push(x, y)
    B. q.pop()
    C. q.clear()
    D. dis[x][y]++

36. ④处应填（ ）。
    A. dis[nx][ny] == -1
    B. dis[nx][ny] != -1
    C. dis[x][y] == -1
    D. nx == x && ny == y

37. ⑤处应填（ ）。
    A. dis[x][y]
    B. dis[x][y] - 1
    C. dis[x][y] + 1
    D. dis[nx][ny] + 1

---

## 答案

> 注：本卷无官方答案表，以下答案由 AI 自行推算，供参考。

| 题号 | 答案 | 题号 | 答案 | 题号 | 答案 | 题号 | 答案 |
|------|------|------|------|------|------|------|------|
| 1. | A | 2. | C | 3. | D | 4. | C |
| 5. | B | 6. | C | 7. | C | 8. | B |
| 9. | B | 10. | A | 11. | B | 12. | C |
| 13. | C | 14. | C | 15. | B | 16. | C |
| 17. | B | 18. | C | 19. | B | 20. | B |
| 21. | B | 22. | C | 23. | B | 24. | C |
| 25. | A | 26. | A | 27. | C | 28. | B |
| 29. | B | 30. | C | 31. | C | 32. | A |
| 33. | B | 34. | C | 35. | B | 36. | B |
| 37. | C |