#pragma once

#ifndef MKIN_H
#define MKIN_H

#include <bits/stdc++.h>
using namespace std;

// ═══════════════════════════════════════════════════════════════════
// 总测试点数量 & Subtask 分组配置
// ═══════════════════════════════════════════════════════════════════
//
//   Subtask 0: 样例        (case 1-2)   10分
//   Subtask 1: 小规模+特殊  (case 3-8)   20分
//   Subtask 2: Hack        (case 9-11)  15分
//   Subtask 3: 中大规模     (case 12-20) 30分
//   Subtask 4: 随机回归     (case 21-25) 25分
// ═══════════════════════════════════════════════════════════════════

const int TEST_CASES = 25;

struct SubtaskDef {
    int id, start, end;
};
const SubtaskDef SUBTASKS[] = {
    {0, 1, 2},    // 样例
    {1, 3, 8},    // 小规模 + 特殊性质
    {2, 9, 11},   // Hack 数据
    {3, 12, 20},  // 中大规模
    {4, 21, 25},  // 随机回归
};
const int SUBTASK_COUNT = sizeof(SUBTASKS) / sizeof(SUBTASKS[0]);

void test(int case_num, ofstream& fout)
{
    // ============================================================
    // Subtask 0: 样例数据（直接复制题目样例） — case 1-2  10分
    // ============================================================
    if (case_num == 1)
    {
        // 样例1：n=8, [5,3,5,1,3,3,1,5]
        fout << "8" << endl;
        fout << "5 3 5 1 3 3 1 5" << endl;
    }
    else if (case_num == 2)
    {
        // 样例2：n=5, [100,200,100,300,200]
        fout << "5" << endl;
        fout << "100 200 100 300 200" << endl;
    }

    // ============================================================
    // Subtask 1: 小规模 + 特殊性质 — case 3-8  20分
    // ============================================================
    else if (case_num == 3)
    {
        // n=3, 两个相同一个不同
        fout << "3" << endl;
        fout << "7 3 7" << endl;
    }
    else if (case_num == 4)
    {
        // n=1, 最小边界
        fout << "1" << endl;
        fout << "42" << endl;
    }
    else if (case_num == 5)
    {
        // n=10, 全部不同
        fout << "10" << endl;
        fout << "10 9 8 7 6 5 4 3 2 1" << endl;
    }
    else if (case_num == 6)
    {
        // 特殊性质1：已递增有序
        fout << "20" << endl;
        for (int i = 1; i <= 20; ++i)
            fout << i * 10 << " \n"[i == 20];
    }
    else if (case_num == 7)
    {
        // 特殊性质2：所有值相同
        fout << "20" << endl;
        for (int i = 0; i < 20; ++i)
            fout << "9" << " \n"[i == 19];
    }
    else if (case_num == 8)
    {
        // 特殊性质3：含极值 0 和 10000，混合多重复
        fout << "15" << endl;
        fout << "0 10000 500 0 9999 10000 0 777 888 999 111 222 333 444 555" << endl;
    }

    // ============================================================
    // Subtask 2: Hack 数据 — case 9-11  15分
    // ============================================================
    else if (case_num == 9)
    {
        // Hack 1: N=1 + 最大值边界
        fout << "1" << endl;
        fout << "10000" << endl;
    }
    else if (case_num == 10)
    {
        // Hack 2: N=2, 两个值相同
        fout << "2" << endl;
        fout << "7 7" << endl;
    }
    else if (case_num == 11)
    {
        // Hack 3: N=2, 两个值不同, 一最小一最大
        fout << "2" << endl;
        fout << "0 10000" << endl;
    }

    // ============================================================
    // Subtask 3: 中大规模数据 — case 12-20  30分
    // ============================================================
    else if (case_num >= 12 && case_num <= 20)
    {
        int N;
        if (case_num == 12) N = 50;
        else if (case_num == 13) N = 100;
        else if (case_num == 14) N = 200;
        else if (case_num == 15) N = 500;
        else N = 1000;  // case 16-20

        fout << N << endl;

        if (case_num == 16)
        {
            // 值范围小（1-50），大量重复
            for (int i = 0; i < N; ++i)
                fout << (rand() % 50 + 1) << " \n"[i == N - 1];
        }
        else if (case_num == 17)
        {
            // 全部不同
            for (int i = 0; i < N; ++i)
                fout << (i * 10 + 1) << " \n"[i == N - 1];
        }
        else if (case_num == 18)
        {
            // 全部相同
            for (int i = 0; i < N; ++i)
                fout << "5555" << " \n"[i == N - 1];
        }
        else if (case_num == 19)
        {
            // 逆序（递减）
            for (int i = N; i >= 1; --i)
                fout << i << " \n"[i == 1];
        }
        else if (case_num == 20)
        {
            // 随机 + 极值
            for (int i = 0; i < N; ++i) {
                int v;
                if (i < 5) v = 0;
                else if (i < 10) v = 10000;
                else v = rand() % 10001;
                fout << v << " \n"[i == N - 1];
            }
        }
        else
        {
            // case 12-15: 随机中等规模
            for (int i = 0; i < N; ++i)
                fout << (rand() % 500 + 1) << " \n"[i == N - 1];
        }
    }

    // ============================================================
    // Subtask 4: 随机回归 — case 21-25  25分
    // ============================================================
    else
    {
        int N;
        if (case_num == 21) N = 15;
        else if (case_num == 22) N = 300;
        else if (case_num == 23) N = 1000;
        else if (case_num == 24) N = 500;
        else N = 1000;

        fout << N << endl;

        if (case_num == 23)
        {
            // 仅两种值，奇偶交替
            for (int i = 0; i < N; ++i)
                fout << (i % 2 == 0 ? 1111 : 2222) << " \n"[i == N - 1];
        }
        else if (case_num == 24)
        {
            // 仅三种值
            int vals[] = {100, 200, 300};
            for (int i = 0; i < N; ++i)
                fout << vals[rand() % 3] << " \n"[i == N - 1];
        }
        else
        {
            // 完全随机
            for (int i = 0; i < N; ++i)
                fout << (rand() % 10001) << " \n"[i == N - 1];
        }
    }
}

#endif
