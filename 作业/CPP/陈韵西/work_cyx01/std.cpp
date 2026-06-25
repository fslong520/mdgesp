#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, r = 1;
    cin >> n;
    for (int i = 2; i <= n; i++)
        r = (r + i) * abs(r - i);
    cout << r << endl;
    return 0;
}
