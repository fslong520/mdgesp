# CSP-J 集训进制与位运算（三）

> CSPJ组集训 7月16日作业
> 主题：数据表示·进制·位运算（对应第2课）
> 客观题 20 道（5分/题） + 编程题 4 道（100分/题）

---

## 一、选择题（2题，选自历年真题题库）

### 第 1 题（2016 真题）
十进制 0.5 转成八进制小数是？
- A. 0.8
- B. 0.4
- C. 0.2
- D. 0.1
- **答案：B**
- **解析**：0.5 × 8 = 4.0，整数部分为 4，小数部分为 0，结束。结果 0.4₈。

### 第 2 题（2017 真题）
8 位二进制补码 10101011 表示的十进制数是？
- A. 43
- B. -85
- C. -43
- D. -84
- **答案：B**
- **解析**：补码 10101011，首位 1 为负数。取反加 1 得 01010101 = 85，故原数为 -85。

---

## 二、程序阅读题（10题）

### 第 3 题【阅读程序】
```cpp
int n = 45, r = 0;
while (n) {
    r = r * 2 + (n & 1);
    n >>= 1;
}
cout << r << endl;
```
- A. 45
- B. 101100
- C. 101101
- D. 110101
- **答案：C**
- **解析**：位运算版十进制转二进制。45 = 101101₂，每次取末位 n&1 再左移累加。r 最终为 101101₂ 的十进制表示 = 45，但输出的是二进制位拼成的十进制数 101101。

### 第 4 题【阅读程序】
```cpp
int n = 13, c = 0;
while (n) {
    c++;
    n &= n - 1;
}
cout << c << endl;
```
- A. 2
- B. 3
- C. 4
- D. 13
- **答案：B**
- **解析**：popcount 统计二进制中 1 的个数。13 = 1101₂，有 3 个 1。每次 n &= n-1 消去最低位 1，3 次后 n = 0。

### 第 5 题【阅读程序】
```cpp
int n = 52, c = 0;
while (n) {
    c++;
    n &= n - 1;
}
cout << c << endl;
```
- A. 2
- B. 4
- C. 3
- D. 5
- **答案：C**
- **解析**：52 = 110100₂，有 3 个 1。popcount = 3。

### 第 6 题【阅读程序】
```cpp
int x = 12;
int lb = x & (-x);
cout << lb << endl;
```
- A. 4
- B. 2
- C. 12
- D. 8
- **答案：A**
- **解析**：lowbit 运算：x = 12 = 1100₂，-x 的补码 = 0100₂，x & -x = 0100₂ = 4。取最低位 1 及其后所有 0。

### 第 7 题【阅读程序】
```cpp
int x = 7;
int lb = x & (-x);
cout << lb << endl;
```
- A. 7
- B. 1
- C. 3
- D. 5
- **答案：B**
- **解析**：x = 7 = 111₂，-x = 001₂，x & -x = 001₂ = 1。最低位 1 就是最后一位。

### 第 8 题【阅读程序】
```cpp
int a = 5, b = 10;
a ^= b; b ^= a; a ^= b;
cout << a << " " << b << endl;
```
- A. 5 10
- B. 5 5
- C. 10 10
- D. 10 5
- **答案：D**
- **解析**：XOR 交换：a ^= b → a = 15; b ^= a → b = 5; a ^= b → a = 10。最终 a = 10, b = 5。

### 第 9 题【阅读程序】
```cpp
bool isPow2(int x) {
    return x > 0 && (x & (x - 1)) == 0;
}
cout << isPow2(8) << endl;
```
- A. 0
- B. 8
- C. 1
- D. false
- **答案：C**
- **解析**：8 = 1000₂，8-1 = 0111₂，8 & 7 = 0。x > 0 且 x & (x-1) == 0，故为 2 的幂，输出 1（true）。

### 第 10 题【阅读程序】
```cpp
int n = 11, c = 0;
while (n) {
    c++;
    n &= n - 1;
}
cout << c << endl;
```
- A. 3
- B. 2
- C. 4
- D. 5
- **答案：A**
- **解析**：11 = 1011₂，有 3 个 1。popcount = 3。

---

## 三、程序补全题（8题）

### 第 11 题【补全程序】
补全十进制转二进制（除基取余法），使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    string r = "";
    while (n > 0) {
        r = char('0' + ___①___) + r;
        n /= 2;
    }
    cout << r << endl;
    return 0;
}
```
① 处应填？
- A. n / 2
- B. n % 2
- C. n & 1
- D. n >> 1
- **答案：B**
- **解析**：除基取余法：每次 n % 2 得余数（0 或 1），拼接到结果字符串前面。

### 第 12 题【补全程序】
补全位运算版十进制转二进制，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    string r = "";
    while (n > 0) {
        r = char('0' + (n & 1)) + r;
        n ___①___ ;
    }
    cout << r << endl;
    return 0;
}
```
① 处应填？
- A. <<= 1
- B. /= 2
- C. >>= 1
- D. &= 1
- **答案：C**
- **解析**：位运算版：n & 1 取末位，右移一位去掉已取出的位。

### 第 13 题【补全程序】
补全 lowbit 函数，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int lowbit(int x) {
    return ___①___;
}
int main() {
    int n;
    cin >> n;
    cout << lowbit(n) << endl;
    return 0;
}
```
① 处应填？
- A. x & (x - 1)
- B. x | (-x)
- C. x ^ (-x)
- D. x & (-x)
- **答案：D**
- **解析**：lowbit 取最低位 1 及其后所有 0，公式为 x & (-x)。

### 第 14 题【补全程序】
补全统计二进制中 1 个数的函数，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int popcnt(int x) {
    int c = 0;
    while (x) {
        c++;
        x ___①___ ;
    }
    return c;
}
int main() {
    int n;
    cin >> n;
    cout << popcnt(n) << endl;
    return 0;
}
```
① 处应填？
- A. &= x - 1
- B. >>= 1
- C. |= x >> 1
- D. ^= x
- **答案：A**
- **解析**：popcount 经典写法：x &= x - 1 消去最低位 1，循环次数即为 1 的个数。

### 第 15 题【补全程序】
补全判断奇偶的位运算表达式，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    if (n ___①___ == 1)
        cout << "odd" << endl;
    else
        cout << "even" << endl;
    return 0;
}
```
① 处应填？
- A. % 2
- B. & 1
- C. | 1
- D. ^ 1
- **答案：B**
- **解析**：n & 1：取末位。末位为 1 是奇数，为 0 是偶数。

### 第 16 题【补全程序】
补全二进制转十进制的左移累加法，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    string s;
    cin >> s;
    int r = 0;
    for (char c : s)
        r = ___①___ + (c - '0');
    cout << r << endl;
    return 0;
}
```
① 处应填？
- A. r * 10 + (c - '0')
- B. r + (c - '0') * 2
- C. (r << 1)
- D. r << 1 + (c - '0')
- **答案：C**
- **解析**：左移累加法：每次将已有结果左移 1 位（乘 2），加上当前位。

### 第 17 题【补全程序】
补全判断 2 的幂的表达式，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    if (n > 0 && ___①___ == 0)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
```
① 处应填？
- A. n & (n + 1)
- B. n | (n - 1)
- C. n ^ (n - 1)
- D. n & (n - 1)
- **答案：D**
- **解析**：判断 2 的幂：x & (x-1) 消去最低位 1，若结果为 0 且 x > 0，则 x 是 2 的幂。

### 第 18 题【补全程序】
补全取第 j 位值的位运算表达式，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, j;
    cin >> x >> j;
    int bit = ___①___;
    cout << bit << endl;
    return 0;
}
```
① 处应填？
- A. (x >> j) & 1
- B. (x << j) & 1
- C. x & (1 << j)
- D. x | (1 << j)
- **答案：A**
- **解析**：取第 j 位：先右移 j 位使目标位到最低位，再 & 1 取出。

### 第 19 题【补全程序】
补全将第 j 位置 1 的位运算表达式，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, j;
    cin >> x >> j;
    x = ___①___;
    cout << x << endl;
    return 0;
}
```
① 处应填？
- A. x & (1 << j)
- B. x ^ (1 << j)
- C. x | (1 << j)
- D. x & ~(1 << j)
- **答案：C**
- **解析**：将第 j 位置 1：用 1 << j 构造掩码，再与 x 按位或。

### 第 20 题【补全程序】
补全将第 j 位清 0 的位运算表达式，使程序正确运行。
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, j;
    cin >> x >> j;
    x = ___①___;
    cout << x << endl;
    return 0;
}
```
① 处应填？
- A. x | (1 << j)
- B. x ^ (1 << j)
- C. x & (1 << j)
- D. x & ~(1 << j)
- **答案：D**
- **解析**：将第 j 位清 0：先对 1 << j 取反得到掩码，再与 x 按位与。

---

## 四、编程题（4题）

### 第 1 题 NOIP2017 普及组 T1 成绩 ★ [noip2017t1]

**题目描述**
总成绩 = 作业 × 20% + 小测 × 30% + 期末 × 50%。输入三个非负整数 A, B, C，输出总成绩。

**输入格式**：一行三个非负整数 A B C（均为 10 的倍数，≤ 100）
**输出格式**：一行一个整数

**样例**
- 输入：100 100 80 → 输出：90
- 输入：60 90 80 → 输出：79

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << (a * 20 + b * 30 + c * 50) / 100 << endl;
    return 0;
}
```

---

### 第 2 题 NOIP2016 普及组 T1 铅笔 ★ [noip2016t1]

**题目描述**
小明需要 n 支铅笔。每盒 k 支，价格 p 元，必须整盒购买。求最少花费。

**输入格式**：三个正整数 n, k, p（n ≤ 10000）
**输出格式**：一行一个整数

**样例**
- 输入：57 2 2 → 输出：58
- 输入：50 30 30 → 输出：60

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, k, p;
    cin >> n >> k >> p;
    int boxes = (n + k - 1) / k;
    cout << boxes * p << endl;
    return 0;
}
```

---

### 第 3 题 2022 CSP-J J2 T2 解密 ★★ [cspj2022t2]

**题目描述**
给定 k 次询问，每次给定 n, e, d，求 p, q 使 n = pq，ed = (p-1)(q-1)+1。无解输出 NO。

**输入格式**：第一行 k，接下来 k 行每行三个正整数 n, d, e
**输出格式**：k 行，每行两个正整数 p, q（p ≤ q）或 NO

**样例**
- 输入：10 / 770 77 5 → 输出：2 385
- 输入：633 1 211 → 输出：NO

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int k;
    cin >> k;
    while (k--) {
        long long n, e, d;
        cin >> n >> d >> e;
        long long m = n - e * d + 2;
        long long delta = m * m - 4 * n;
        if (delta < 0) { cout << "NO" << endl; continue; }
        long long sq = sqrt(delta);
        if (sq * sq != delta) { cout << "NO" << endl; continue; }
        long long p = (m - sq) / 2, q = (m + sq) / 2;
        if (p * q != n || p <= 0 || q <= 0) { cout << "NO" << endl; continue; }
        cout << p << " " << q << endl;
    }
    return 0;
}
```

---

### 第 4 题 2023 CSP-J J2 T2 公路 ★★ [cspj2023t2]

**题目描述**
n 个站点排成一列，站点 i 到 i+1 距离 v_i 公里，站点 i 油价 a_i 元/升，每升行驶 d 公里。油箱无限大，初始为空。从站点 1 到站点 n 最少花费。

**输入格式**：第一行 n, d；第二行 n-1 个 v_i；第三行 n 个 a_i
**输出格式**：一行一个整数

**样例**
- 输入：5 4 / 10 10 10 10 / 9 8 9 6 5 → 输出：79

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    int n;
    ll d;
    cin >> n >> d;
    vector<ll> v(n - 1);
    for (int i = 0; i < n - 1; i++) cin >> v[i];
    vector<ll> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    ll cost = 0, fuel = 0, minPrice = a[0];
    for (int i = 0; i < n - 1; i++) {
        ll need = (v[i] + d - 1) / d;
        if (fuel < need) {
            ll buy = need - fuel;
            cost += buy * minPrice;
            fuel += buy;
        }
        fuel -= need;
        minPrice = min(minPrice, a[i + 1]);
    }
    cout << cost << endl;
    return 0;
}
```
