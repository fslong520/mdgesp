#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, a[1005];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n, greater<int>());
    int cnt1 = n * 20 / 100;
    int cnt2 = n * 30 / 100;
    int s1 = (cnt1 == 0) ? -1 : a[cnt1 - 1];
    int s2 = (cnt2 == 0 || cnt1 + cnt2 > n) ? -1 : a[cnt1 + cnt2 - 1];
    cout << s1 << " " << s2 << endl;
    return 0;
}
