#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, a[1005];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);
    int cnt = 1;
    for (int i = 1; i < n; i++) {
        if (a[i] == a[i - 1]) cnt++;
        else {
            cout << a[i - 1] << " " << cnt << "\n";
            cnt = 1;
        }
    }
    if (n > 0) cout << a[n - 1] << " " << cnt << "\n";
    return 0;
}
