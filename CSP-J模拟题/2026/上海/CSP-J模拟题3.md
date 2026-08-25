# CSP-J/S 模拟（三）

**日期**：2026-07-26

**时长**：120 分钟

**说明**：J组不需要做附加题，S组需要做J的所有题目及附加题。

---

## 一、单项选择题

- 共 15 题，每题 2 分，共计 30 分
- 每题有且仅有一个正确选项

1. (2025)₈ + (2025)₁₆ 和以下哪个选项相等（ ）。
   A. (9244)₁₀
   B. (2100222)₄
   C. (10010000111010)₂
   D. (234A)₁₆

2. 以下（ ）函数声明是合法的。
   A. int Bubblesort(char a[][],int n)
   B. int Bubblesort(char a[10][],int n)
   C. int Bubblesort(char a[][20],int n)
   D. int Bubblesort(char [,] a,int n)

3. 设循环队列中数组的下标范围是0~n-1，其头尾指针分别为f和r，则其元素个数为（ ）。
   A. r-f
   B. r-f+1
   C. (r-f)%n+1
   D. (r-f+n)%n

4. 后缀表达式 1 2 + 3 * 14 7 / - 对应的前缀表达式为（ ）。
   A. 1 + 2 * 3 - 14 / 7
   B. - * 1 + 2 3 / 14 7
   C. - * + 1 2 3 / 14 7
   D. - 1 + 2 * 3 14 / 7

5. 给定一棵二叉树，其前序遍历结果为abdecfg，中序遍历结果为debacfg，则这棵树的后序遍历结果为（ ）。
   A. edbgfca
   B. edgbfca
   C. debgfca
   D. dbegfca

6. 下列是关于数据结构的说法不正确的是（ ）。
   A. 数据结构是带有结构的数据元素的集合
   B. 线性表的线性存储结构优于链式存储结构
   C. 队列是一个先进先出的线性表
   D. 队列是只能在一端插入，另一端删除的线性表

7. 已知无向图G含有16条边,其中度为4的顶点个数为3,度为3的顶点个数为4,其他顶点的度均小于3。G所含的顶点个数至少是（ ）。
   A. 10
   B. 11
   C. 13
   D. 15

8. 下面关于指针的说法正确的是（ ）。
   A. 在64位计算机中一个指针变量占4字节
   B. 指针运算实际上是地址操作、只能取地址和间接访问，不能进行加减运算
   C. 数组名不是指向数组元素的指针变量
   D. 指针只可以静态申请内存空间

9. 方程 a × b = (a or b)×(a and b)，在a,b都取[0,31]中的整数时，共有（ ）组解。
   A. 32
   B. 256
   C. 454
   D. 512

10. 双向链表中有两个指针域，llink和rlink，分别指向前驱及后继，设p指向链表中的一个结点，q指向一待插入结点，现要求在p前插入q，则正确的插入为（ ）。
    A. p->llink = q; q->rlink = p; p->llink->rlink = q;q->llink = p->llink;
    B. q->llink = p->llink; p->llink->rlink = q; q->rlink = p;p->llink = q->rlink;
    C. p->llink->rlink = q; q->rlink = p;q->llink = p->llink; p->llink = q;
    D. q->rlink = p; p->rlink = q;p->llink->rlink = q; q->rlink = p;

11. 将2,6,10,17分别存储到某个地址区间为0-10的哈希表中，如果哈希函数 h(x) =（ ）将不会产生冲突，其中a mod b表示a除以b的余数。
    A. x mod 11
    B. x² mod 11
    C. (2x) mod 11
    D. ⌊√x⌋ mod 11

12. 输入时n个不等的数构成的数组a，输出a中第二小的数。在最坏的情况下，该算法需要做（ ）次比较。

```cpp
if (a[1] < a[2])
{
    min1 = a[1];
    min2 = a[2];
}
else
{
    min1 = a[2];
    min2 = a[1];
}
for(int i = 3; i <= n; i++)
    if (a[i] < min2)
        if (a[i] < min1)
        {
            min2 = min1;
            min1 = a[i];
        }
        else
        {
            min2 = a[i];
        }
```

A. 2n - 1
B. 2n - 2
C. 2n - 3
D. 2n

13. 整型数组 a 中有 n 个元素，能计算 a 中有多少个数字大于 lower 且小于 upper 的函数，应该将下划线依次替换为（ ）。

```cpp
int solve(int a[], int n, int lower, int upper)
{
    std::sort(a, a + n);
    auto begin = std::________(a, a + n, lower);
    auto end = std::________(a, a + n, upper);
    return end - begin;
}
```

A. lower_bound、lower_bound
B. lower_bound、upper_bound
C. upper_bound、lower_bound
D. upper_bound、upper_bound

14. 若 f₀ = 0, f₁ = 1, fₙ₊₁ = (fₙ + fₙ₋₁)/2，则随着 i 的增大，fᵢ 将接近于（ ）。
    A. 1/2
    B. 2/3
    C. (√5 - 1)/2
    D. 1

15. 由四个没有区别的点构成的简单无向连通图的个数是（ ）。
    A. 6
    B. 7
    C. 8
    D. 9

---

## 二、阅读程序

- 判断题 1 分，选择题 3 分，共计 40 分
- 判断题正确填 T ，错误填 F；

### 第1题

```cpp
using i64 = long long;
i64 f(i64 n)
{
    i64 s = 1;
    i64 i = 2;
    while (i * i < n)
    {
        if (n % i == 0) {
            s += i;
            s += n / i;
        }
        ++i;
    }
    if (i * i == n) s += i;
    return s;
}
```

判断题

16. 当 n = 1 时，函数返回 1（ ）。
17. 当 n 是质数时，函数返回 n+1（ ）。
18. 存在两个数 m、n，且 f(m) = f(n)（ ）。
19. 程序的时间复杂度为 Θ(√n)（ ）。

选择题

20. f(100) 会进入 while 循环次数是（ ）。
    A. 7
    B. 8
    C. 9
    D. 10
21. 运行 f(1024) 时，返回值是（ ）。
    A. 512
    B. 1023
    C. 1024
    D. 2047

### 第2题

```cpp
int solve(int n, int a[])
{
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            int sum = 0;
            for (int k = j; k <= i; ++k) {
                sum += a[k];
            }
            ret += sum;
        }
    }
    return ret;
}
```

判断题

22. 若在进入 solve 函数执行其他操作之前，先对 a[] 排序，返回值不变（ ）。

23. 当 n = 1 时，函数返回值为 a[0]（ ）。

24. 若数组a[]中所有元素均为0，则当n取1到100之间的整数时，函数一定返回0（ ）。

选择题

25. 若 n = 10 且a = {1,1,...,1,1}，程序的返回值是（ ）。
    A. 10
    B. 100
    C. 165
    D. 210

26. 若 n = 5，且a = {3,1,4,1,5}，则程序返回（ ）。
    A. 14
    B. 75
    C. 78
    D. 80

27. 该程序的时间复杂度为（ ）。
    A. Θ(n)
    B. Θ(n²)
    C. Θ(n²·logn)
    D. Θ(n³)

28. 如果打算用更好的算法实现 solve 函数，那么最好的算法可以达到的时间复杂度为（ ）。
    A. Θ(n)
    B. Θ(n²)
    C. Θ(n²·log n)
    D. Θ(log n)

### 第3题

```cpp
using i64 = long long;

i64 solve1(i64 n)
{
    std::vector<i64> c(n);
    c[0] = 0;
    i64 sum = 0;
    for (i64 i = 1; i < n; ++i)
    {
        c[i] = c[i / 2] + (i % 2);
        sum += c[i];
    }
    return sum;
}

std::pair<i64,i64> solve2(i64 n)
{
    if (n == 0)
        return {0, 0};
    auto r = n % 2;
    auto q = n / 2;
    auto [s, c] = solve2(q);
    if (r == 1)
        return {s*2 + q + c, c + 1};
    else
        return {s*2 + q, c};
}
```

判断题

29. solve1(5) 返回 5（ ）。

30. solve2(8) 返回 {10, 1}（ ）。

31. 若输入参数n在0到1024之间，则solve1(n)的返回值与solve2(n)的第一项返回值必定相等（ ）。

选择题

32. solve1(n) 计算的是（ ）。
    A. 0到n-1之间，全体二进制数的零出现的数量
    B. 0到n-1之间，全体二进制数的一出现的数量
    C. 0到n之间，全体二进制数的零出现的数量
    D. 0到n之间，全体二进制数的一出现的数量

33. solve2(n) 的第二个返回值，计算的是（ ）。
    A. 参数n的二进制长度
    B. 参数n的十进制长度
    C. 参数n的在二进制表示下，0的数量
    D. 参数n的在二进制表示下，1的数量

34. solve1及solve2的时间复杂度是（ ）。
    A. Θ(n)、Θ(n)
    B. Θ(n)、Θ(log n)
    C. Θ(log n)、Θ(n)
    D. Θ(log n)、Θ(log n)

35. solve1(4096) 的返回值等于（ ）。
    A. 4096 × 5
    B. 4096 × 6
    C. 2048 × 5
    D. 2048 × 6

---

## 三、完善程序

- 单选题，每小题 3 分，共计 30 分

### 第1题

两人进行 N 次石头剪刀布游戏，给定对方的出拳序列，由R、P、S组成（分别表示石头、剪刀、布）。你的出拳需满足：

- 从未输过（每次非赢即平）。
- 相邻两次出拳不同。

求可能赢的最大对局数（即赢的次数，平局不计入）。

```cpp
#include<iostream>
int score(int a,int b){
    if(____(1)____) return 0;
    else if(a=='R' and b=='S')return 1;
    else if(____(2)____)return 1;
    else if(a=='P' and b=='R')return 1;
    else return -10000000;
}

int main(){
    ____(3)____
    int n;
    std::cin>>n;
    while(n-->0){
        char c;
        std::cin>>c;
        int newR = ____(4)____;
        int newS = ____(5)____;
        int newP = ____(6)____;
        R=newR;
        S=newS;
        P=newP;
    }
    std::cout<< ____(7)____;
}
```

36. (1)处应填（ ）。
    A. a != b
    B. a < b
    C. a > b
    D. a == b

37. (2)处应填（ ）。
    A. a=='S' and b=='P'
    B. a=='S' and b=='R'
    C. a=='P' and b=='S'
    D. a=='R' and b=='P'

38. (3)处应填（ ）。
    A. char R,S,P
    B. char R = 'R',S = 'S',P = 'P'
    C. int R = 0,S = 0,P = 0
    D. int R = 'R',S = 'S',P = 'P'

39. (4)(5)(6)处应填（ ）。
    A. score(R,c)、score(S,c)、score(P,c)
    B. score('R',c)、score('S',c)、score('P',c)
    C. R + score('R',c)、S + score('S',c)、P + score('P',c)
    D. std::max(S,P)+score('R',c)、std::max(R,P)+score('S',c)、std::max(R,S)+score('P',c)

40. (7)处应填（ ）。
    A. std::min(std::min(R,S),P)
    B. std::max(std::max(R,S),P)
    C. n - std::min(std::min(R,S),P)
    D. n - std::max(std::max(R,S),P)

### 第2题

给定 n 根火柴的长度 a₁,a₂,...,aₙ，请用这些火柴围成一个面积最大的三角形。注意所有的火柴都必须用上，不得丢弃。输出最大三角形的面积。假设最大面积为 s，则输出 16s²。1 ≤ aᵢ ≤ 40，数据保证至少有一种方案可以围成三角形。

```cpp
#include<iostream>
using i64 = long long;
int n;
int a[40];
bool mem[40][40*40][40*40];
i64 value[40][40*40][40*40];

i64 solve(int i, int x, int y, int z) {
    if (i < n) {
        if (mem[____(1)____] > 0) return value[____(2)____];
        auto s1 = solve(i+1, x + a[i], y, z);
        auto s2 = solve(i+1, x, y + a[i], z);
        auto s3 = solve(i+1, x, y, z + a[i]);
        mem[____(3)____] = true;
        return value[____(4)____] = ____(5)____;
    }
    else {
        if (____(6)____) return 0;
        i64 p = ____(7)____;
        return ____(8)____;
    }
}

int main()
{
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    std::cout << solve(0, 0, 0, 0);
}
```

41. (1)、(2)、(3)、(4)处应填（ ）。
    A. [i][x][y],[i][x][y],[i][x][y],[i][x][y]
    B. [i][x][y],[x][y][z],[i][x][y],[x][y][z]
    C. [x][y][z],[i][x][y],[x][y][z],[i][x][y]
    D. [x][y][z],[x][y][z],[x][y][z],[x][y][z]

42. (5)处应填（ ）。
    A. s1 + s2 + s3
    B. *std::max_element({s1, s2, s3}.begin(), {s1, s2, s3}.end())
    C. std::max(std::max(s1, s2), std::max(s3, z))
    D. std::max(std::max(s1, s2), s3)

43. (6)处应填（ ）。
    A. x + y <= z && x + z <= y && y + z <= x
    B. x + y <= z || x + z <= y || y + z <= x
    C. x + y > z || x + z > y || y + z > x
    D. x + y >= z && x + z >= y && y + z >= x

44. (7)处应填（ ）。
    A. x * y * z
    B. x + y + z
    C. (x * y) / 2
    D. (x + y + z) / 2

45. (8)处应填（ ）。
    A. p * (p - 2 * x) * (p - 2 * y)
    B. (p / 2) * (p / 2 - x) * (p / 2 - y) * (p / 2 - z)
    C. p * (p - 2 * x) * (p - 2 * y) * (p - 2 * z)
    D. p + (p - 2 * x) + (p - 2 * y) + (p - 2 * z)

---

## 四、附加题

- 判断题 1 分，选择题 3 分，共计 30 分
- 判断题正确填 T ，错误填 F；

### 第1题

```cpp
int exp();

int term()
{
    char begin, end;
    std::cin >> begin;
    int t = exp();
    std::cin >> end;
    if (t == 0)
        return 1;
    else
        return t * 2;
}

int exp()
{
    if (std::cin.peek() == '(')
    {
        return term() + exp();
    }
    else
    {
        return 0;
    }
}

int main()
{
    std::cout << exp() << "\n";
}
```

判断题

46. 输入(())()，程序运行结果输出3（ ）。

47. 输入((()))输出3（ ）。

48. 输出15的最短输入序列之一是(((())())())()（ ）。

选择题

49. 若输入是((())(()())(()()))，输出（ ）。
    A. 16
    B. 18
    C. 20
    D. 22

50. 以下哪个输入对应的输出为10（ ）。
    A. ((())())
    B. ((())()())()
    C. ((())()(())())
    D. ((())()())(())

51. 若输入字符串(()(())())，代码执行过程中term()函数被调用的次数是（ ）。
    A. 4
    B. 5
    C. 7
    D. 8

52. 若输入(()())(())()，则exp()函数总共被调用的次数是（ ）。
    A. 7
    B. 9
    C. 13
    D. 15

### 第2题

某个投资者有m元钱，有n个项目等待他的投资，每个项目只能投资一次。代码中的一个pair表示一个项目。其中第i个项目要求先支出成本cᵢ元，待项目完成后，可以收回全部成本，且获得pᵢ元利润，若投资者的钱不足cᵢ，就没法投资这个项目了。可以用老项目收回的成本及利润支付新项目的成本。若只能投资k个项目，那么投资者最终可以积累多少钱呢。

```cpp
struct pair
{
    int c;
    int p;
};

int solve(int n, int k, int m, pair a[])
{
    auto compare = [] (pair first, pair second) {
        return ____(1)____;
    };
    std::sort(a, a + n, compare);
    std::priority_queue<int> Q;
    int size = 0;
    while (k > 0) {
        while (____(2)____) {
            Q.push(____(3)____);
        }
        if (____(4)____) {
            ____(5)____;
        }
        k--;
    }
    return m;
}
```

53. (1)处应填（ ）。
    A. first.c < second.c
    B. first.c > second.c
    C. first.p < second.p
    D. first.p > second.p

54. (2)处应填（ ）。
    A. size < n && a[size].c <= m
    B. size < n && a[size].c < m
    C. size <= n && a[size].c <= m
    D. size < n || a[size].c <= m

55. (3)处应填（ ）。
    A. a[size++].p
    B. a[++size].p
    C. a[size++].c
    D. a[++size].c

56. (4)处应填（ ）。
    A. !Q.empty()
    B. Q.empty()
    C. size > 0
    D. k > 0

57. (5)处应填（ ）。
    A. m += Q.top(); Q.pop();
    B. m += Q.front(); Q.pop();
    C. m += Q.front().p - Q.front().c;
    D. Q.pop(); m += Q.top();

---

## 答案

| 题号 | 答案 | 题号 | 答案 | 题号 | 答案 | 题号 | 答案 |
|------|------|------|------|------|------|------|------|
| 1. | C | 2. | C | 3. | D | 4. | C |
| 5. | A | 6. | B | 7. | B | 8. | C |
| 9. | C | 10. | C | 11. | D | 12. | C |
| 13. | C | 14. | B | 15. | A | 16. | T |
| 17. | F | 18. | T | 19. | T | 20. | B |
| 21. | B | 22. | F | 23. | F | 24. | T |
| 25. | D | 26. | C | 27. | D | 28. | A |
| 29. | T | 30. | F | 31. | T | 32. | B |
| 33. | D | 34. | B | 35. | B | 36. | D |
| 37. | A | 38. | C | 39. | D | 40. | B |
| 41. | A | 42. | D | 43. | B | 44. | B |
| 45. | C | 46. | T | 47. | F | 48. | T |
| 49. | C | 50. | D | 51. | B | 52. | C |
| 53. | A | 54. | A | 55. | A | 56. | A |
| 57. | A |

> **审计注记（2026-08-22）**：
> - 第5题：原表给 C 有误。前序 abdecfg + 中序 debacfg 推得树为 a(b(d(−,e)), c(−,f(−,g)))，后序 **edbgfca = A**（官方答案图亦 A，已更正）。
> - 第19题：官方答案图给 F，但循环 `while (i*i<n)` 恰执行 ⌊√n⌋−1 次、每趟 O(1)（64 位乘除为硬件操作），时间复杂度**确为 Θ(√n)，T 才对**；官方键疑误，本表维持 T。
> - 第51/52题：程序中 `term() + exp()` 的求值顺序在 C++ 中未定义，函数调用次数依赖编译器实现。主流 g++ 实测：51 题 term 被调 **5** 次（B）、52 题 exp 被调 **13** 次（C），与本表一致；教学时宜向学生说明此点。