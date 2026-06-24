1. B (10分)
2. D (10分)
3. B (10分)
4. C (10分)
5. B (10分)
6. A (10分)
7. A (10分)
8. A (10分)
9. C (10分)
10. D (10分)
11. F (10分)
12. F (10分)
13. F (10分)
14. T (10分)
15. F (10分)
16. <a href="https://fslong.iok.la/problem/P9396" target="_blank">租船</a> cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    cout << (n + k - 1) / k;
    return 0;
}
```

17. <a href="https://fslong.iok.la/problem/P9397" target="_blank">书架编号</a> cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, sum = 0;
    cin >> a >> b;
    for (int i = a; i <= b; i++)
        if (i % 2 == 0) sum += i;
    cout << sum;
    return 0;
}
```

18. <a href="https://fslong.iok.la/problem/P9398" target="_blank">酒店门牌号</a> cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int k, cnt = 0;
    cin >> k;
    for (int i = 100; i <= 999; i++) {
        int s = i / 100 + i / 10 % 10 + i % 10;
        if (s == k) cnt++;
    }
    cout << cnt;
    return 0;
}
```

19. <a href="https://fslong.iok.la/problem/P9399" target="_blank">单词分值</a> cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int sum = 0;
    for (char c : s) {
        if (c >= 'a' && c <= 'z')
            sum += c - 'a' + 1;
        else if (c >= 'A' && c <= 'Z')
            sum -= (int)c;
    }
    cout << sum;
    return 0;
}
```

20. <a href="https://fslong.iok.la/problem/P9400" target="_blank">零花钱</a> cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int a[1005];
    for (int i = 1; i <= n; i++) cin >> a[i];
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        int sum = 0;
        for (int j = i; j <= n; j++) {
            sum += a[j];
            if (sum == k) cnt++;
        }
    }
    cout << cnt;
    return 0;
}
```
