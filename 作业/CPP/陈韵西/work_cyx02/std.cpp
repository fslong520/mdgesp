#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int tot = 0;    // 总蘑菇数
    int cur = 10;   // 当日应采数（如为工作日）
    int work = 0;   // 连续工作日计数

    for (int i = 1; i <= n; i++) {
        if (work == 7) {
            work = 0;       // 第8天休整，采0朵
        } else {
            tot += cur;     // 采蘑菇
            cur += 3;       // 次日多采3朵
            work++;         // 工作日计数+1
        }
    }

    cout << tot << endl;

    return 0;
}
