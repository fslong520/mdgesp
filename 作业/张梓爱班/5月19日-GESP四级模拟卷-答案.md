1. A (2分)
2. B (2分)
3. B (2分)
4. C (2分)
5. A (2分)
6. B (2分)
7. C (2分)
8. B (2分)
9. A (2分)
10. B (2分)
11. B (2分)
12. C (2分)
13. A (2分)
14. B (2分)
15. C (2分)
16. T (2分)
17. F (2分)
18. T (2分)
19. T (2分)
20. T (2分)
21. T (2分)
22. F (2分)
23. F (2分)
24. T (2分)
25. F (2分)
26. cpp (25分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 105;
int a[N][N];

int main() {
    int n, m;
    cin >> n >> m;
    
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++)
            cin >> a[i][j];
    
    int maxSum = -1;
    for(int i = 1; i <= n - 1; i++) {
        for(int j = 1; j <= m - 1; j++) {
            int sum = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1];
            maxSum = max(maxSum, sum);
        }
    }
    
    cout << maxSum << endl;
    return 0;
}
```

27. cpp (25分)
参考代码:
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Student {
    string name;
    int chinese, math, english, total;
};

bool cmp(Student a, Student b) {
    if(a.total != b.total) return a.total > b.total;
    if(a.chinese != b.chinese) return a.chinese > b.chinese;
    return a.name < b.name;
}

int main() {
    int n;
    cin >> n;
    
    Student stu[1005];
    for(int i = 0; i < n; i++) {
        cin >> stu[i].name >> stu[i].chinese >> stu[i].math >> stu[i].english;
        stu[i].total = stu[i].chinese + stu[i].math + stu[i].english;
    }
    
    sort(stu, stu + n, cmp);
    
    for(int i = 0; i < n; i++) {
        cout << stu[i].name << " " << stu[i].chinese << " " 
             << stu[i].math << " " << stu[i].english << " " 
             << stu[i].total << endl;
    }
    
    return 0;
}
```
