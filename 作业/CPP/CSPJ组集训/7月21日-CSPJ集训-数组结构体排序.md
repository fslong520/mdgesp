---
title: "7 月 21 日作业 - CSP-J 集训数组·结构体·排序"
description: CSPJ组集训 7月21日作业 - 历年真题数组·排序·结构体精选20题 + T3编程2道
---

<uyk class="water">

---

# ⚙️ CSP-J 集训 · 数组·结构体·排序

---

# 客观题 20 道（5分/题） + 编程题 2 道（100分/题）

> 以下题目选自近年 CSP-J 及 NOIP 普及组初赛真题

---

### 第 1 题（2025 真题·阅读程序）当输入为 "3 1 3 2 1" 时，输出结果为 2。

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
#define ll long long
int n, k;
int a[200007];
int ans[200007];
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  std::sort(a + 1, a + n + 1);
  n = std::unique(a + 1, a + n + 1) - a - 1;
  for (int i = 1, j = 0; i <= n; ++i) {
    for (; j < i && a[i] - a[j + 1] > k; ++j)
      ;
    ans[i] = ans[j] + 1;
  }
  printf("%d\n", ans[n]);
}
```

- A. 正确
- B. 错误

**答案：A**

**解析：** 排序去重得 1 2 3，极差 ≤1 最少分组 2。

---

### 第 2 题（2025 真题·阅读程序）假设输入的 n 为正整数，输出的答案一定小于等于 n，大于等于 1。

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
#define ll long long
int n, k;
int a[200007];
int ans[200007];
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  std::sort(a + 1, a + n + 1);
  n = std::unique(a + 1, a + n + 1) - a - 1;
  for (int i = 1, j = 0; i <= n; ++i) {
    for (; j < i && a[i] - a[j + 1] > k; ++j)
      ;
    ans[i] = ans[j] + 1;
  }
  printf("%d\n", ans[n]);
}
```

- A. 正确
- B. 错误

**答案：A**

**解析：** ans 每轮至少 +1，最多 +n，故答案在 [1, n] 范围内。

---

### 第 3 题（2025 真题·阅读程序）将第 14 行的 `n=std::unique(a+1,a+n+1)-a-1;` 删去后，有可能出现与原本代码不同的输出结果。

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
#define ll long long
int n, k;
int a[200007];
int ans[200007];
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  std::sort(a + 1, a + n + 1);
  n = std::unique(a + 1, a + n + 1) - a - 1;
  for (int i = 1, j = 0; i <= n; ++i) {
    for (; j < i && a[i] - a[j + 1] > k; ++j)
      ;
    ans[i] = ans[j] + 1;
  }
  printf("%d\n", ans[n]);
}
```

- A. 正确
- B. 错误

**答案：B**

**解析：** 重复元素极差 0 不影响分组，删去去重不影响结果。

---

### 第 4 题（2025 真题·阅读程序）假设输入的 a 数组和 k 均为正整数，执行第 18 行代码时，一定满足的条件不包括？

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
#define ll long long
int n, k;
int a[200007];
int ans[200007];
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  std::sort(a + 1, a + n + 1);
  n = std::unique(a + 1, a + n + 1) - a - 1;
  for (int i = 1, j = 0; i <= n; ++i) {
    for (; j < i && a[i] - a[j + 1] > k; ++j)
      ;
    ans[i] = ans[j] + 1;
  }
  printf("%d\n", ans[n]);
}
```

- A. j ≤ i
- B. a[i] - a[j] > k
- C. j ≤ n
- D. a[j] < a[i]

**答案：B**

**解析：** j 循环结束后 a[i]-a[j+1] ≤ k，a[i]-a[j] 不一定 > k。

---

### 第 5 题（2025 真题·阅读程序）当输入的 n=100、k=2、a={1,2,…,100} 时，输出为？

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
#define ll long long
int n, k;
int a[200007];
int ans[200007];
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  std::sort(a + 1, a + n + 1);
  n = std::unique(a + 1, a + n + 1) - a - 1;
  for (int i = 1, j = 0; i <= n; ++i) {
    for (; j < i && a[i] - a[j + 1] > k; ++j)
      ;
    ans[i] = ans[j] + 1;
  }
  printf("%d\n", ans[n]);
}
```

- A. 34
- B. 100
- C. 50
- D. 33

**答案：A**

**解析：** 100 个数，极差 ≤2 每 3 个一组 → ceil(100/3)=34。

---

### 第 6 题（2025 真题·阅读程序）假设输入的 a 数组和 k 均为正整数，但 a 数组不一定有序，若误删去第 13 行的 sort，程序有可能出现的问题有？

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
#define ll long long
int n, k;
int a[200007];
int ans[200007];
int main() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  std::sort(a + 1, a + n + 1);
  n = std::unique(a + 1, a + n + 1) - a - 1;
  for (int i = 1, j = 0; i <= n; ++i) {
    for (; j < i && a[i] - a[j + 1] > k; ++j)
      ;
    ans[i] = ans[j] + 1;
  }
  printf("%d\n", ans[n]);
}
```

- A. 输出的答案比原本答案更大
- B. 输出的答案比原本答案更小
- C. 出现死循环行为
- D. 以上均可能发生

**答案：B**

**解析：** 乱序导致 j 提前停止，答案可能变小。

---

### 第 7 题（2022 真题·阅读程序）该算法最准确的时间复杂度分析结果为 O(log n + k)。

```cpp
#include <iostream>
using namespace std;

int n, k;

int solve1() {
    int l = 0, r = n;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (mid * mid <= n) l = mid + 1;
        else r = mid - 1;
    }
    return l - 1;
}

double solve2(double x) {
    if (x == 0) return x;
    for (int i = 0; i < k; i++)
        x = (x + n / x) / 2;
    return x;
}

int main() {
    cin >> n >> k;
    double ans = solve2(solve1());
    cout << ans << ' ' << (ans * ans == n) << endl;
    return 0;
}
```

- A. 正确
- B. 错误

**答案：A**

**解析：** solve1 二分查找 O(log n)，solve2 迭代 k 次 O(k)，总复杂度 O(log n + k)。

---

### 第 8 题（2022 真题·阅读程序）当输入为 "9801 1" 时，输出的第一个数为 "99"。

```cpp
#include <iostream>
using namespace std;

int n, k;

int solve1() {
    int l = 0, r = n;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (mid * mid <= n) l = mid + 1;
        else r = mid - 1;
    }
    return l - 1;
}

double solve2(double x) {
    if (x == 0) return x;
    for (int i = 0; i < k; i++)
        x = (x + n / x) / 2;
    return x;
}

int main() {
    cin >> n >> k;
    double ans = solve2(solve1());
    cout << ans << ' ' << (ans * ans == n) << endl;
    return 0;
}
```

- A. 正确
- B. 错误

**答案：A**

**解析：** 9801 = 99²，solve1 返回 99，solve2(99) 返回 99。

---

### 第 9 题（2022 真题·阅读程序）对于任意输入的 n，随着所输入 k 的增大，输出的第二个数会变成 "1"。

```cpp
#include <iostream>
using namespace std;

int n, k;

int solve1() {
    int l = 0, r = n;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (mid * mid <= n) l = mid + 1;
        else r = mid - 1;
    }
    return l - 1;
}

double solve2(double x) {
    if (x == 0) return x;
    for (int i = 0; i < k; i++)
        x = (x + n / x) / 2;
    return x;
}

int main() {
    cin >> n >> k;
    double ans = solve2(solve1());
    cout << ans << ' ' << (ans * ans == n) << endl;
    return 0;
}
```

- A. 正确
- B. 错误

**答案：B**

**解析：** 只有 n 是完全平方数时，第二个数才会是 1。

---

### 第 10 题（2022 真题·阅读程序）该程序存在缺陷。当输入的 n 过大时，第 12 行的乘法有可能溢出，因此应当将 mid 强制转换为 64 位整数再计算。

```cpp
#include <iostream>
using namespace std;

int n, k;

int solve1() {
    int l = 0, r = n;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (mid * mid <= n) l = mid + 1;
        else r = mid - 1;
    }
    return l - 1;
}

double solve2(double x) {
    if (x == 0) return x;
    for (int i = 0; i < k; i++)
        x = (x + n / x) / 2;
    return x;
}

int main() {
    cin >> n >> k;
    double ans = solve2(solve1());
    cout << ans << ' ' << (ans * ans == n) << endl;
    return 0;
}
```

- A. 正确
- B. 错误

**答案：B**

**解析：** n ≤ 47000，mid ≤ 216，mid×mid ≤ 47000² < 2³¹，不会溢出。

---

### 第 11 题（2022 真题·阅读程序）当输入为 "2 1" 时，输出的第一个数最接近？

```cpp
#include <iostream>
using namespace std;

int n, k;

int solve1() {
    int l = 0, r = n;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (mid * mid <= n) l = mid + 1;
        else r = mid - 1;
    }
    return l - 1;
}

double solve2(double x) {
    if (x == 0) return x;
    for (int i = 0; i < k; i++)
        x = (x + n / x) / 2;
    return x;
}

int main() {
    cin >> n >> k;
    double ans = solve2(solve1());
    cout << ans << ' ' << (ans * ans == n) << endl;
    return 0;
}
```

- A. 1
- B. 1.414
- C. 1.5
- D. 2

**答案：C**

**解析：** solve1 返回 1，solve2(1) 迭代 1 次得 (1 + 2/1)/2 = 1.5。

---

### 第 12 题（2022 真题·阅读程序）当输入为 "3 10" 时，输出的第一个数最接近？

```cpp
#include <iostream>
using namespace std;

int n, k;

int solve1() {
    int l = 0, r = n;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (mid * mid <= n) l = mid + 1;
        else r = mid - 1;
    }
    return l - 1;
}

double solve2(double x) {
    if (x == 0) return x;
    for (int i = 0; i < k; i++)
        x = (x + n / x) / 2;
    return x;
}

int main() {
    cin >> n >> k;
    double ans = solve2(solve1());
    cout << ans << ' ' << (ans * ans == n) << endl;
    return 0;
}
```

- A. 1.7
- B. 1.732
- C. 1.75
- D. 2

**答案：B**

**解析：** solve1 返回 1，solve2(1) 迭代 10 次逼近 √3 ≈ 1.732。

---

### 第 13 题（2022 真题·阅读程序）当输入为 "256 11" 时，输出的第一个数？

```cpp
#include <iostream>
using namespace std;

int n, k;

int solve1() {
    int l = 0, r = n;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (mid * mid <= n) l = mid + 1;
        else r = mid - 1;
    }
    return l - 1;
}

double solve2(double x) {
    if (x == 0) return x;
    for (int i = 0; i < k; i++)
        x = (x + n / x) / 2;
    return x;
}

int main() {
    cin >> n >> k;
    double ans = solve2(solve1());
    cout << ans << ' ' << (ans * ans == n) << endl;
    return 0;
}
```

- A. 等于 16
- B. 接近但小于 16
- C. 接近但大于 16
- D. 前三种情况都有可能

**答案：A**

**解析：** 256 = 16²，solve1 返回 16，solve2(16) 返回 16。

---

### 第 14 题（2025 真题）对数组 [6,1,5,2,4] 进行冒泡排序升序排列，需要多少次交换？

- A. 5
- B. 6
- C. 7
- D. 8

**答案：B**

**解析：** 交换次数等于逆序对数量。(6,1)(6,5)(6,2)(6,4)(5,2)(5,4) 共 6 个。

---

### 第 15 题（2022 真题）以下关于排序的说法，错误的是？

- A. 冒泡排序是稳定的
- B. 简单选择排序是稳定的
- C. 简单插入排序是稳定的
- D. 归并排序是稳定的

**答案：B**

**解析：** 不稳定排序：选择、希尔、快速、堆排序。冒泡、插入、归并稳定。

---

### 第 16 题（2024 真题）对 1000 个元素进行二分查找，最多需要比较多少次？

- A. 25
- B. 10
- C. 7
- D. 1

**答案：B**

**解析：** ⌊log₂1000⌋ + 1 = 9 + 1 = 10 次（2⁹ = 512 < 1000 ≤ 2¹⁰ = 1024）。

---

### 第 17 题（2021 真题）在 N 个数中找出最大数，最少需要比较多少次？

- A. N
- B. N - 1
- C. N + 1
- D. N(N - 1)/2

**答案：B**

**解析：** 先假设第 1 个为最大值，依次与剩余 N−1 个数各比较 1 次，共 N−1 次。

---

### 第 18 题（2020 真题）冒泡排序对 n 个数排序，最好情况下比较次数是？

- A. n
- B. n - 1
- C. n(n - 1)/2
- D. n²/2

**答案：B**

**解析：** 最好情况数据已有序，第一趟比较 n−1 次即结束。

---

### 第 19 题（2019 真题）对 100 个有序元素进行折半查找，最多需要比较多少次？

- A. 6
- B. 7
- C. 8
- D. 9

**答案：B**

**解析：** ⌊log₂100⌋ + 1 = 6 + 1 = 7 次（2⁶ = 64 < 100 ≤ 2⁷ = 128）。

---

### 第 20 题（2018 真题）以下哪种排序算法不需要进行关键字比较？

- A. 基数排序
- B. 冒泡排序
- C. 堆排序
- D. 直接插入排序

**答案：A**

**解析：** 基数排序按位分配收集，不进行关键字比较。其余三种均需比较。

---

# 编程题（每题 100 分，共 200 分）

> 以下题目选自近年 CSP-J 及 NOIP 普及组复赛真题

---

### 第 1 题 NOIP2016 普及组 T3 海港 ★★★ [noip2016t3]（100 分）— <a href="https://fslong.iok.la/problem/NOIP2016T3" target="_blank">🧑‍💻 在线答题</a>

**【题目描述】**

小李是一个海港工作人员。每天都有许多船只到达海港，船上通常有许多来自不同国家的乘客。

他需要统计每艘船到达后的 24 小时内（含当前船）到达的船只上的乘客来自多少个不同的国家。

**【输入格式】**

第一行一个正整数 n，表示船的数量。

接下来 n 行，每行描述一艘船：第一个整数 t 表示时间（秒），第二个整数 k 表示该船乘客数量，接下来 k 个整数 x 表示乘客国籍。

**【输出格式】**

输出 n 行，每艘船到达时输出一个整数，表示当前 24 小时（86400 秒）内到达的乘客中不同国籍的数量。

**【样例输入】**

```
3
1 4 4 1 2 2
2 2 2 3
10 1 3
```

**【样例输出】**

```
4
4
5
```

**【数据范围】**

1 ≤ n ≤ 10⁵，0 ≤ t ≤ 10⁹，1 ≤ k ≤ 10⁵，1 ≤ x ≤ 10⁵

所有 t 严格递增。总乘客数 ≤ 3×10⁵。

---

### 第 2 题 2023 CSP-J 第二轮 T3 一元二次方程 ★★★ [cspj2023t3]（100 分）— <a href="https://fslong.iok.la/problem/CSPJ2023T3" target="_blank">🧑‍💻 在线答题</a>

**【题目描述】**

给定一元二次方程 ax² + bx + c = 0（a ≠ 0），求该方程的最大实数根，以最简分数形式输出。若无实数根输出 NO。

**【输入格式】**

第一行一个正整数 T，表示方程个数。

接下来 T 行，每行三个整数 a, b, c。

**【输出格式】**

输出 T 行，每行一个结果。若方程有实数解，输出最大实数根的最简分数形式（分母为正）；若无实数解，输出 NO。

**【样例输入】**

```
3
1 -2 1
1 2 1
1 1 1
```

**【样例输出】**

```
1
-1
NO
```

**【数据范围】**

1 ≤ T ≤ 5000，|a|,|b|,|c| ≤ 5000，a ≠ 0。

**【提示】**

判别式 Δ = b² − 4ac。Δ < 0 时无实数根；Δ = 0 时有唯一根 −b/(2a)；Δ > 0 时最大根为 (−b + √Δ)/(2a)。当 √Δ 为整数时以最简分数输出。

---

# 📋 答案汇总

| 题号 | 答案 | 题号 | 答案 |
|:----:|:----:|:----:|:----:|
| 1 | A | 11 | C |
| 2 | A | 12 | B |
| 3 | B | 13 | A |
| 4 | B | 14 | B |
| 5 | A | 15 | B |
| 6 | B | 16 | B |
| 7 | A | 17 | B |
| 8 | A | 18 | B |
| 9 | B | 19 | B |
| 10 | B | 20 | A |

---

</div>
