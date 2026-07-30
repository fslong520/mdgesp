---
title: "7 月 20 日作业 - CSP-J 集训递归"
description: 历年真题递归相关精选 20 题 + 编程题 2 道
---

<uyk class="water">

---

# ⚙️ CSP-J 集训 · 递归专项（第 6 课）

---

# 客观题 20 道（5 分/题） + 编程题 2 道（100 分/题）

> 以下题目选自近年 CSP-J 及 NOIP 普及组初赛真题

---

## Section A：互质三元组计数（2025 年真题 Q16–Q21）

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
inline int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int main() {
  int n;
  scanf("%d", &n);
  int ans = 0;
  for (int i = 1; i <= n; ++i) {
    for (int j = i + 1; j <= n; ++j) {
      for (int k = j + 1; k <= n; ++k) {
        if (gcd(i, j) == 1 && gcd(j, k) == 1 && gcd(i, k) == 1) ans++;
      }
    }
  }
  printf("%d\n", ans);
  return 0;
}
```

### 第 1 题（2025 真题）当输入为 2 时，程序并不会执行第 16 行的判断语句。

- A. 正确
- B. 错误

---
- **答案：A**
- **解析：** n=2时，k循环条件k<=n不满足（k从j+1=3开始），第16行不执行。
### 第 2 题（2025 真题）将第 16 行中的 `&& gcd(i,k)==1` 删去不会影响程序运行结果。

- A. 正确
- B. 错误

---
- **答案：B**
- **解析：** i,k互质不一定成立，如i=2,j=3,k=4时，gcd(2,4)=2≠1，删去后会多计数。
### 第 3 题（2025 真题）当输入的 n≥3 的时候，程序总是输出一个正整数。

- A. 正确
- B. 错误

---
- **答案：A**
- **解析：** n=3时，(1,2,3)两两互质，ans≥1，总是输出正整数。
### 第 4 题（2025 真题）将第 7 行的 `gcd(b, a%b)` 改为 `gcd(a, a%b)` 后，程序可能出现的问题是？

- A. 输出的答案大于原答案
- B. 输出的答案小于原答案
- C. 程序有可能陷入死循环
- D. 可能发生整型溢出问题

---
- **答案：B**
- **解析：** gcd(a,a%b)参数不交换，递归无法正确归约，最大公约数计算错误，导致答案变小。
### 第 5 题（2025 真题）当输入为 8 的时候，输出为？

- A. 37
- B. 42
- C. 35
- D. 25

---
- **答案：D**
- **解析：** n=8时手动模拟得25，即1到8中两两互质的三元组有25个。
### 第 6 题（2025 真题）调用 gcd(36, 42) 会返回？

- A. 6
- B. 252
- C. 3
- D. 2

---
- **答案：A**
- **解析：** gcd(36,42)=gcd(42,36)=gcd(36,6)=gcd(6,0)=6。

## Section B：素数计数与求和（2024 年真题 Q16–Q20）

```cpp
#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int countPrimes(int n) {
    int count = 0;
    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            count++;
        }
    }
    return count;
}

int sumPrimes(int n) {
    int sum = 0;
    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int x;
    cin >> x;
    cout << countPrimes(x) << " " << sumPrimes(x) << endl;
    return 0;
}
```

### 第 7 题（2024 真题）当输入为"10"时，程序的第一个输出为"4"，第二个输出为"17"。

- A. 正确
- B. 错误

---
- **答案：A**
- **解析：** 10以内素数有2,3,5,7共4个，和为2+3+5+7=17。
### 第 8 题（2024 真题）若将 isPrime(i)函数中的条件改为 i ≤ n / 2，输入"20"时，countPrimes(20)的输出将变为"6"。

- A. 正确
- B. 错误

---
- **答案：B**
- **解析：** 改为i<=n/2后，isPrime函数逻辑错误，但countPrimes仍会计算素数，输出不会变为6。
### 第 9 题（2024 真题）sumPrimes 函数计算的是从 2 到 n 之间的所有素数之和。

- A. 正确
- B. 错误

---
- **答案：A**
- **解析：** sumPrimes函数遍历2到n，累加所有素数，正确。
### 第 10 题（2024 真题）当输入为"50"时，sumPrimes(50)的输出为？

- A. 1060
- B. 328
- C. 381
- D. 275

---
- **答案：B**
- **解析：** 50以内素数：2,3,5,7,11,13,17,19,23,29,31,37,41,43,47，和为328。
### 第 11 题（2024 真题）如果将 for (int i = 2; i * i <= n; i++) 改为 for (int i = 2; i <= n; i++)，输入"10"时，程序的输出？

- A. 将不能正确计算 10 以内素数个数及其和
- B. 仍然输出"4"和"17"
- C. 输出"3"和"10"
- D. 输出结果不变，但运行时间更短

---
- **答案：B**
- **解析：** 改为i<=n后，isPrime函数仍能正确判断素数，输出不变但效率降低。

## Section C：递归函数（2024 年真题 Q27–Q32）

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int customFunction(int a, int b) {
    if (b == 0) {
        return a;
    }
    return a + customFunction(a, b-1);
}

int main() {
    int x, y;
    cin >> x >> y;
    int result = customFunction(x, y);
    cout << pow(result, 2) << endl;
    return 0;
}
```

### 第 12 题（2024 真题）当输入为"2 3"时，customFunction(2, 3)的返回值为"64"。

- A. 正确
- B. 错误

---
- **答案：B**
- **解析：** customFunction(2,3)=2+2+2+2=8，8²=64，但题目说返回值为64，实际返回值为8。
### 第 13 题（2024 真题）当 b 为负数时，customFunction(a, b)会陷入无限递归。

- A. 正确
- B. 错误

---
- **答案：A**
- **解析：** b为负数时，b-1会越来越小，永远不会等于0，导致无限递归。
### 第 14 题（2024 真题）当 b 的值越大，程序的运行时间越长。

- A. 正确
- B. 错误

---
- **答案：A**
- **解析：** b越大，递归次数越多，运行时间越长。
### 第 15 题（2024 真题）当输入为"5 4"时，customFunction(5, 4)的返回值为？

- A. 5
- B. 25
- C. 250
- D. 625

---
- **答案：B**
- **解析：** customFunction(5,4)=5+5+5+5+5=25，25²=625，但返回值为25。
### 第 16 题（2024 真题）如果输入 x=3 和 y=3，则程序的最终输出为？

- A. 27
- B. 81
- C. 144
- D. 256

---
- **答案：C**
- **解析：** customFunction(3,3)=3+3+3+3=12，12²=144。
### 第 17 题（2024 真题）若将 customFunction 函数改为"return a + customFunction(a-1, b-1);"，并输入"3 3"，则程序的最终输出为？

- A. 9
- B. 16
- C. 25
- D. 36

---
- **答案：D**
- **解析：** 修改后customFunction(3,3)=3+customFunction(2,2)=3+2+customFunction(1,1)=3+2+1+customFunction(0,0)=3+2+1+0=6，6²=36。

## Section D：递归基础（单题）

### 第 18 题（2022 真题）关于递归方法的描述正确的是？

- A. 递归是允许多组参数调用函数的编程技术
- B. 递归是通过调用自身来求解问题的编程技术
- C. 递归是面向对象的编程语言模型
- D. 递归是将高级语言转换为机器代码的技术

---
- **答案：B**
- **解析：** 递归的核心是函数调用自身，将原问题分解为规模更小的同类子问题。
### 第 19 题（2021 真题）递归函数 solve(7) 的值是多少？（已知 n<5 时返回 n!，n≥5 时返回 n×solve(n-2)）

- A. 5040
- B. 210
- C. 720
- D. 120

---
- **答案：B**
- **解析：** n<5时返回n!，n≥5时返回n×solve(n-2)。solve(7)=7×5×3!=7×5×6=210。
### 第 20 题（2020 真题）递归算法 XYZ(数组 A, n) 的输出是？

- A. 数组平均值
- B. 数组最大值
- C. 数组最小值
- D. 数组之和

---

# 编程题（每题 100 分，共 200 分）

> 以下题目选自历年 CSP-J 第二轮认证及 NOIP 普及组复赛真题

---
- **答案：B**
- **解析：** 递归分解后返回左右部分的最大值中的较大者，即求数组最大值。
### 第 1 题 NOIP2017 普及组 T3 棋盘 ★★★★(改) [noip2017pjt3g]（100 分）— <a href="https://fslong.iok.la/problem/NOIP2017PJT3G" target="_blank">🧑‍💻 在线答题</a>

【题目描述】

有一个 m×m 的棋盘，棋盘上有一些格子有颜色，颜色为 0（红色）或 1（黄色），其余格子为无色。你需要从 (1,1) 走到 (m,m)，只能站在有颜色的格子上。每次只能向上下左右四个方向走一格。

如果相邻的两个格子颜色相同，则不需要花费金币；如果颜色不同，则需要花费 1 金币。你可以花费 3 金币施展魔法，将一个与当前所在格子相邻的无色格子暂时变为指定颜色（0 或 1），使用魔法后必须等 2 步才能再次使用。

求从 (1,1) 到 (m,m)，中途必须经过至少一个无色格子 的最小花费。如果无法到达，输出 -1。

【输入格式】

第一行两个整数 m 和 n，分别表示棋盘大小和有色格子数量。
接下来 n 行，每行三个整数 x, y, c，表示第 x 行第 y 列的格子颜色为 c。保证 (1,1) 和 (m,m) 都在输入中。

【输出格式】

一行一个整数，表示最小花费。如果无法到达，输出 -1。

【样例输入】

```
5 7
1 1 0
1 2 0
2 2 1
3 3 1
3 4 0
4 4 1
5 5 0
```

【样例输出】

```
8
```

【数据范围】

- m ≤ 100
- n ≤ 1000

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
int m,n,cor[105][105],f[105][105][2];
int dx[]={-1,1,0,0},dy[]={0,0,-1,1};

void dfs(int x,int y,int used) {
    for(int d=0;d<4;d++) {
        int nx=x+dx[d],ny=y+dy[d];
        if(nx<1||nx>m||ny<1||ny>m) continue;
        if(cor[nx][ny]) {
            int w=(cor[nx][ny]!=cor[x][y]);
            if(f[x][y][used]+w<f[nx][ny][0]) {
                f[nx][ny][0]=f[x][y][used]+w;
                dfs(nx,ny,0);
            }
        } else if(!used) {
            for(int c=1;c<=2;c++) {
                int w=2+(c!=cor[x][y]);
                if(f[x][y][0]+w<f[nx][ny][1]) {
                    f[nx][ny][1]=f[x][y][0]+w;
                    cor[nx][ny]=c;
                    dfs(nx,ny,1);
                    cor[nx][ny]=0;
                }
            }
        }
    }
}

int main() {
    cin>>m>>n;
    memset(f,0x3f,sizeof(f));
    for(int i=0;i<n;i++) {
        int x,y,c;cin>>x>>y>>c;
        cor[x][y]=c+1;
    }
    f[1][1][0]=0;
    dfs(1,1,0);
    int ans=min(f[m][m][0],f[m][m][1]);
    cout<<(ans<0x3f3f3f3f?ans:-1)<<endl;
    return 0;
}
```

---

### 第 2 题 2025 CSP-J 第二轮 T3 异或和 ★★★(改) [cspj2025t3g]

**题目描述**
给定长度为 n 的非负整数序列 a1...an 和非负整数 k。定义区间 [l, r] 的权值为 al⊕...⊕ar。选择尽可能多的不相交区间（长度≥2），使每个区间权值**≥k**。求最多区间数。

**输入格式**：第一行 n, k；第二行 n 个整数
**输出格式**：一行一个整数

**样例**
- 输入：`4 2 / 2 1 0 3` → 输出：`2`
- 输入：`5 0 / 1 1 1 2 2` → 输出：`2`

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
int n,k,ans,pre,arr[500005];
map<int,int> last;

int main() {
    cin>>n>>k;
    for(int i=1;i<=n;i++) cin>>arr[i];
    last[0]=0; pre=0; ans=0;
    int cut=-1;
    for(int i=1;i<=n;i++) {
        pre^=arr[i];
        int need=pre^k;
        if(last.count(need)&&last[need]>=cut) {
            ans++;
            cut=i-1;
        }
        last[pre]=i;
    }
    cout<<ans<<endl;
    return 0;
}
```

---

## 答案汇总

| 题号 | 答案 | 题号 | 答案 |
|:----:|:----:|:----:|:----:|
| 1 | A | 2 | B |
| 3 | A | 4 | B |
| 5 | D | 6 | A |
| 7 | A | 8 | B |
| 9 | A | 10 | B |
| 11 | B | 12 | B |
| 13 | A | 14 | A |
| 15 | B | 16 | C |
| 17 | D | 18 | B |
| 19 | B | 20 | B |
