1. B (10分)
2. D (10分)
3. B (10分)
4. A (10分)
5. B (10分)
6. C (10分)
7. D (10分)
8. A (10分)
9. B (10分)
10. C (10分)
11. T (10分)
12. T (10分)
13. F (10分)
14. F (10分)
15. T (10分)
16. cpp (100分)
参考代码：
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int a, b;
    cin >> a >> b;
    cout << a * b - 1 << endl;
    return 0;
}
```
17. cpp (100分)
参考代码：
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int d; cin >> d;
        ans += min(d, 10 - d);
    }
    cout << ans << endl;
    return 0;
}
```
18. cpp (100分)
参考代码：
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    long long ans = 0;
    for (int i = 0; i < n; i += 2) ans += a[i+1] - a[i];
    cout << ans << endl;
    return 0;
}
```
19. cpp (100分)
参考代码：
```cpp
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1005;
int v[MAXN], memo[MAXN][MAXN], n;
int dfs(int i, int j) {
    if (i > j) return 0;
    if (i == j) return v[i];
    if (memo[i][j] != -1) return memo[i][j];
    int left = v[i] - dfs(i+1, j);
    int right = v[j] - dfs(i, j-1);
    return memo[i][j] = max(left, right);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    int total = 0;
    for (int i = 0; i < n; i++) { cin >> v[i]; total += v[i]; }
    memset(memo, -1, sizeof(memo));
    int diff = dfs(0, n-1);
    cout << (total + diff) / 2 << endl;
    return 0;
}
```
20. cpp (100分)
参考代码：
```cpp
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 505;
int a[MAXN][MAXN], memo[MAXN][MAXN];
int n, m;
const int INF = -1e9;
int dfs(int i, int j) {
    if (i > n || j > m) return INF;
    if (a[i][j] == -1) return INF;
    if (i == n && j == m) return a[i][j];
    if (memo[i][j] != -1) return memo[i][j];
    int down = dfs(i+1, j), right = dfs(i, j+1);
    int best = max(down, right);
    if (best == INF) return memo[i][j] = INF;
    return memo[i][j] = a[i][j] + best;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> a[i][j];
    memset(memo, -1, sizeof(memo));
    int ans = dfs(1, 1);
    if (ans < 0) cout << -1 << endl;
    else cout << ans << endl;
    return 0;
}
```
