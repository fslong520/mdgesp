1. D (10分)
2. D (10分)
3. C (10分)
4. B (10分)
5. B (10分)
6. A (10分)
7. A (10分)
8. B (10分)
9. A (10分)
10. C (10分)
11. F (10分)
12. F (10分)
13. T (10分)
14. T (10分)
15. F (10分)
16. cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int r;
    double pi = 3.14;
    cin >> r;
    double c = 2 * pi * r;
    double s = pi * r * r;
    printf("%.1f %.1f", c, s);
    return 0;
}
```
17. cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int mx = a;
    if (b > mx) mx = b;
    if (c > mx) mx = c;
    cout << mx;
    return 0;
}
```
18. cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    char ch;
    cin >> ch;
    cout << char(ch - 32);
    return 0;
}
```
19. cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, cnt = 0, m1 = 0, m2 = 0, m3 = 0, m4 = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x > 100) cnt++;
        if (x > m1) { m4 = m3; m3 = m2; m2 = m1; m1 = x; }
        else if (x > m2) { m4 = m3; m3 = m2; m2 = x; }
        else if (x > m3) { m4 = m3; m3 = x; }
        else if (x > m4) { m4 = x; }
    }
    cout << cnt << " " << m1 + m2 + m3 + m4;
    return 0;
}
```
20. cpp (100分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    double d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
    printf("%.1f", d);
    return 0;
}
```
