#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, a[1005];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);
    int ans = 1, cnt = 1;
    for (int i = 1; i < n; i++) {
        if (a[i] == a[i - 1]) continue;
        if (a[i] == a[i - 1] + 1) cnt++;
        else cnt = 1;
        if (cnt > ans) ans = cnt;
    }
    cout << (n == 0 ? 0 : ans) << endl;
    return 0;
}
