---
title: "7 月 19 日作业 - CSP-J 集训函数与结构体"
description: C++ 语法精讲·函数·结构体 20题客观 + J2编程2题
---

<uyk class="water">

---

# ⚙️ CSP-J 集训 · 函数与结构体专项

---

# 客观题 20 道（5 分/题） + 编程题 2 道（100 分/题）

> 以下题目选自近年 CSP-J 及 NOIP 普及组初赛真题

---

### 第 1 题（2019 真题）阅读 BST 递归程序：如果 a 数组有重复的数字，则程序运行时会发生错误。

```cpp
#include <iostream>
using namespace std;
const int maxn = 10000;
int n;
int a[maxn];
int b[maxn];
int f(int l, int r, int depth) {
    if (l > r)
        return 0;
    int min = maxn, mink;
    for (int i = l; i <= r; ++i) {
        if (min > a[i]) {
            min = a[i];
            mink = i;
        }
    }
    int lres = f(l, mink - 1, depth + 1);
    int rres = f(mink + 1, r, depth + 1);
    return lres + rres + depth * b[mink];
}
int main() {
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < n; ++i)
        cin >> b[i];
    cout << f(0, n - 1, 1) << endl;
    return 0;
}
```

- A. 正确
- B. 错误
- C. 不确定，取决于数据规模
- D. 不确定，取决于 b 数组的值
- **答案：B**
- **解析：** 重复数字不影响程序运行，min 会取第一个遇到的最小值位置，程序逻辑不受影响。

---

### 第 2 题（2019 真题）阅读上述 BST 递归程序：如果 b 数组全为 0，则输出为 0。

- A. 正确
- B. 错误
- C. 输出为 1
- D. 输出为 n
- **答案：A**
- **解析：** b[i]=0 时，depth*b[mink]=0，每一层递归返回值均为 0，最终输出 0。

---

### 第 3 题（2019 真题）阅读上述 BST 递归程序：当 n=100 时，最坏情况下，与第 12 行的比较运算执行的次数最接近的是？

- A. 6
- B. 100
- C. 5000
- D. 600
- **答案：C**
- **解析：** 最坏情况（有序数组）每次递归只减少一个元素，比较次数约 n²/2 = 5000。

---

### 第 4 题（2019 真题）阅读上述 BST 递归程序：当 n=100 时，最好情况下，与第 12 行的比较运算执行的次数最接近的是？

- A. 5000
- B. 6
- C. 100
- D. 600
- **答案：C**
- **解析：** 最好情况（完全平衡树）每次平分，递归深度 log n，比较次数约 n = 100。

---

### 第 5 题（2019 真题）阅读上述 BST 递归程序：当 n=10 时，若 b 数组满足对任意 0 ≤ i < n 都有 b[i] = i + 1，那么输出最大为？

- A. 385
- B. 383
- C. 384
- D. 386
- **答案：A**
- **解析：** 完全平衡时 depth 最小，输出最大为 385。

---

### 第 6 题（2019 真题）阅读上述 BST 递归程序：当 n=100 时，若 b 数组满足对任意 0 ≤ i < n 都有 b[i] = 1，那么输出最小为？

- A. 582
- B. 579
- C. 581
- D. 580
- **答案：D**
- **解析：** 最坏情况（有序数组）depth 最大，输出最小为 580。

---

### 第 7 题（2019 真题）完善程序：矩阵变幻。①处应填？

```cpp
#include <cstdio>
using namespace std;
int n;
const int max_size = 1 << 10;
int res[max_size][max_size];

void recursive(int x, int y, int n, int t) {
    if (n == 0) {
        res[x][y] = ①;
        return;
    }
    int step = 1 << (n - 1);
    recursive(②, n - 1, t);
    recursive(x, y + step, n - 1, t);
    recursive(x + step, y, n - 1, t);
    recursive(③, n - 1, !t);
}

int main() {
    scanf("%d", &n);
    recursive(0, 0, ④);
    int size = ⑤;
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j)
            printf("%d", res[i][j]);
        puts("");
    }
    return 0;
}
```

- A. 1
- B. n % 2
- C. t
- D. 0
- **答案：C**
- **解析：** 递归到最底层（n==0），根据 t 值填 0 或 1。

---

### 第 8 题（2019 真题）完善程序：矩阵变幻。②处应填？

- A. x - step, y
- B. x, y - step
- C. x - step, y - step
- D. x, y
- **答案：D**
- **解析：** 左上角递归位置不变，仍为 (x, y)。

---

### 第 9 题（2019 真题）完善程序：矩阵变幻。③处应填？

- A. x + step, y + step
- B. x, y - step
- C. x - step, y
- D. x - step, y - step
- **答案：A**
- **解析：** 右下角递归位置为 (x + step, y + step)。

---

### 第 10 题（2019 真题）完善程序：矩阵变幻。④处应填？

- A. n - 1, 0
- B. n - 1, n % 2
- C. n, 0
- D. n, n % 2
- **答案：C**
- **解析：** 初始调用 n 层，t = 0。

---

### 第 11 题（2019 真题）完善程序：矩阵变幻。⑤处应填？

- A. n + 1
- B. 1 << n
- C. 1 << (n - 1)
- D. 1 << (n + 1)
- **答案：B**
- **解析：** 矩阵大小为 2^n，用位运算 1 << n 表示。

---

### 第 12 题（2025 真题）以下递归函数 `calc(5)` 的返回值是？

```cpp
int calc(int n){
    if(n<=1) return 1;
    if(n%2==0) return calc(n/2)+1;
    else return calc(n-1)+calc(n-2);
}
```

- A. 5
- B. 6
- C. 7
- D. 8
- **答案：B**
- **解析：** calc(5)=calc(4)+calc(3)，calc(4)=calc(2)+1=calc(1)+1+1=3，calc(3)=calc(2)+calc(1)=2+1=3，故 calc(5)=3+3=6。

---

### 第 13 题（2022 真题）`a+(b-c)*d` 的前缀表达式是？

- A. `*+a-bcd`
- B. `+a*-bcd`
- C. `abc-d*+`
- D. `abc-+d`
- **答案：B**
- **解析：** 运算符前移。先算 b-c 得 -bc，再算 *-bcd，最后 +a*-bcd。

---

### 第 14 题（2021 真题）`a*(b+c)*d` 的后缀表达式是？

- A. `abc+*d*`
- B. `abc+d**`
- C. `*a*bcd+`
- D. `abc*+d*`
- **答案：A**
- **解析：** 先算 b+c 得 bc+，再乘 a 得 abc+*，最后乘 d 得 abc+*d*。

---

### 第 15 题（2017 真题）`a*(b+c)*d` 的后缀形式是？

- A. `abcd*+*`
- B. `abc+*d*`
- C. `a*bc+*d`
- D. `b+c*a*d`
- **答案：B**
- **解析：** 先 b+c 得 bc+，再 *a 得 abc+*，最后 *d 得 abc+*d*。

---

### 第 16 题（2025 真题）`(a&&b)||(!c&&a)` 与以下哪个表达式**不**始终相等？

- A. `a&&(b||!c)`
- B. `(a||!c)&&(b||!c)&&(a||a)`
- C. `a&&(!b||c)`
- D. `!(a||!b)||(a&&!c)`
- **答案：C**
- **解析：** 原式化简 = a&&(b||!c)。C 选项 a&&(!b||c) 在 a=true,b=true,c=false 时原式为 true，C 为 false，不等价。

---

### 第 17 题（2020 真题）设 x = true，y = true，z = false，以下哪个逻辑表达式的结果为 true？

- A. (y ∨ z) ∧ x ∧ z
- B. x ∧ (z ∨ y) ∧ z
- C. (x ∧ y) ∧ z
- D. (x ∧ y) ∨ (z ∨ x)
- **答案：D**
- **解析：** D 选项：(x ∧ y) ∨ (z ∨ x) = (true ∧ true) ∨ (false ∨ true) = true ∨ true = true。A、B、C 均含 ∧ z = false 使其结果为 false。

---

### 第 18 题（2022 真题）字符串 `"abcab"` 有多少个内容不同的子串？

- A. 12
- B. 13
- C. 14
- D. 15
- **答案：B**
- **解析：** 枚举所有子串：a, b, c, ab, bc, ca, abc, bca, cab, abca, bcab, abcab，去重后共 13 个。

---

### 第 19 题（2016 真题）关于字符串的正确说法是？

- A. 字符串是一种特殊的线性表
- B. 串的长度必须大于零
- C. 字符串不可以用数组表示
- D. 空格串就是空串
- **答案：A**
- **解析：** 字符串是线性表的一种（每个字符一个元素）。空串长度可为 0，空格串 ≠ 空串。

---

### 第 20 题（2025 真题）完善程序：字符串解码。①处应填？

```cpp
#include<cctype>
#include<iostream>
#include<string>
using namespace std;
int main(){
    string z;
    cin>> z;
    string s="";
    for(int i=0;;){
        char ch= z[i];
        if( ①  &&isdigit(z[i+1])){
            int count=0;
            i++;
            while(i<z.length()&& isdigit(z[i])){
                count= count*10+(z[i]-'0');
                i++;
            }
            for(int j=0; j< count ;++j){
                s+= ch;
            }
        }else{
              s+= ch;
            i++;
        }
    }
    cout<< s<< endl;
    return 0;
}
```

- A. `i<z.length()`
- B. `i-1≥0`
- C. `i+1<z.length()`
- D. `isdigit(z[i])`
- **答案：C**
- **解析：** i+1 < z.length() 检查不越界，确保 z[i+1] 可安全访问。

---

## 三、编程题（2题）

### 第 1 题 2021 CSP-J 第二轮 T3 网络连接 ★★★ [cspj2021t3]

**题目描述**

网络中有若干计算机，每台计算机有唯一地址，格式为 `a.b.c.d:e`。

地址格式合法性规则：
- 地址须严格符合 `a.b.c.d:e` 格式
- a, b, c, d 为 0~255 的整数，e 为 0~65535 的整数
- 各部分为整数表示，除 "0" 外不含前导零

两种操作：
- `Server addr`：在 addr 注册新服务器。地址不合法输出 ERR；地址已存在输出 FAIL；成功输出 OK
- `Client addr`：连接 addr 的服务器。地址不合法输出 ERR；找到输出服务器编号（注册顺序）；否则输出 FAIL

**输入格式**

第一行正整数 n。接下来 n 行每行一个操作。

**输出格式**

每行一个输出。

**样例**

输入：
```
8
Server 1.2.3.4:80
Server 1.2.3.4:80
Client 1.2.3.4:80
Client 1.2.3.4:81
Server 01.2.3.4:80
Client 256.0.0.0:80
Server 1.2.3:80
Client 1.2.3.4:80
```

输出：
```
OK
FAIL
1
FAIL
ERR
ERR
ERR
1
```

**数据范围** n ≤ 1000

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
bool check(string s) {
    long long a = 0, b = 0, c = 0, d = 0, port = 0;
    int ret = sscanf(s.c_str(), "%lld.%lld.%lld.%lld:%lld", &a, &b, &c, &d, &port);
    if (ret != 5) return false;
    char buf[64];
    sprintf(buf, "%lld.%lld.%lld.%lld:%lld", a, b, c, d, port);
    if (s != buf) return false;
    return a >= 0 && a <= 255 && b >= 0 && b <= 255
        && c >= 0 && c <= 255 && d >= 0 && d <= 255
        && port >= 0 && port <= 65535;
}
int main() {
    int n;
    cin >> n;
    map<string, int> mp;
    for (int i = 1; i <= n; i++) {
        string op, ad;
        cin >> op >> ad;
        if (!check(ad)) { cout << "ERR\n"; continue; }
        if (op == "Server") {
            if (mp.count(ad)) cout << "FAIL\n";
            else { mp[ad] = i; cout << "OK\n"; }
        } else {
            if (mp.count(ad)) cout << mp[ad] << "\n";
            else cout << "FAIL\n";
        }
    }
    return 0;
}
```

---

### 第 2 题 2022 CSP-J 第二轮 T3 逻辑表达式 ★★★★ [cspj2022t3]

**题目描述**

给定逻辑表达式，仅含 `0` `1` `&` `|` `(` `)`。

& 和 | 同级，从左到右计算。需统计**短路求值**次数：
- `&` 左操作数为 0 → 不计算右操作数，& 短路次数 +1
- `|` 左操作数为 1 → 不计算右操作数，| 短路次数 +1

例 `1&0|1&0&0`，从左到右：
1. `1&0`：左=1，不短路，值=0
2. `0|1`：左=0，不短路，值=1
3. `1&0`：左=0，**短路**，值=0，&短路+1
4. `0&0`：左=0，**短路**，值=0，&短路+1

表达式值=0，&短路 2 次，|短路 1 次。

**输入格式**

一行字符串 s。

**输出格式**

第一行表达式值；第二行 & 短路次数和 | 短路次数。

**样例**

输入：
```
1&0|1&0&0
```

输出：
```
0
2 1
```

输入：
```
0|(1&0)&(1|0)
```

输出：
```
0
2 0
```

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
struct Node {
    int v, andCnt, orCnt;
    Node(int v = 0, int a = 0, int o = 0) : v(v), andCnt(a), orCnt(o) {}
};
Node calc(const string& s, int& i) {
    Node cur;
    if (s[i] == '0' || s[i] == '1') cur = Node(s[i++] - '0');
    else if (s[i] == '(') { i++; cur = calc(s, i); i++; }
    while (i < s.size() && s[i] != ')') {
        char op = s[i++];
        Node rhs = calc(s, i);
        if (op == '&') {
            if (cur.v == 0) { cur.andCnt++; cur.andCnt += rhs.andCnt + rhs.orCnt; }
            else { cur.v &= rhs.v; cur.andCnt += rhs.andCnt; cur.orCnt += rhs.orCnt; }
        } else {
            if (cur.v == 1) { cur.orCnt++; cur.andCnt += rhs.andCnt + rhs.orCnt; }
            else { cur.v |= rhs.v; cur.andCnt += rhs.andCnt; cur.orCnt += rhs.orCnt; }
        }
    }
    return cur;
}
int main() {
    string s;
    cin >> s;
    int i = 0;
    Node r = calc(s, i);
    cout << r.v << endl << r.andCnt << " " << r.orCnt << endl;
}
```

---

## 答案汇总

| 题号 | 答案 | 题号 | 答案 |
|:----:|:----:|:----:|:----:|
| 1 | B | 11 | B |
| 2 | A | 12 | B |
| 3 | C | 13 | B |
| 4 | C | 14 | A |
| 5 | A | 15 | B |
| 6 | D | 16 | C |
| 7 | C | 17 | D |
| 8 | D | 18 | B |
| 9 | A | 19 | A |
| 10 | C | 20 | C |

---

</div>
