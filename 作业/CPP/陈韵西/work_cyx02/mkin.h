#pragma once

#ifndef MKIN_H
#define MKIN_H

#include <bits/stdc++.h>
using namespace std;

// ═══════════════════════════════════════════════════════════════════
// 总测试点数量 & Subtask 分组配置
// ═══════════════════════════════════════════════════════════════════
// 修改 test() 时同步更新下方 SUBTASK 数组，
// 以及 testdata/config.yaml 中的 cases 列表。
//
// 默认分组策略（5 个子任务，总分 100）：
//   Subtask 0: 样例        (case 1-2)   10分
//   Subtask 1: 小规模+特殊  (case 3-8)   20分
//   Subtask 2: Hack        (case 9-11)  15分
//   Subtask 3: 中大规模     (case 12-20) 30分
//   Subtask 4: 随机回归     (case 21-25) 25分
// ═══════════════════════════════════════════════════════════════════

const int TEST_CASES = 25;

// Subtask 分组：{subtask_id, start_case, end_case}
// 修改 test() 中 case 分组时同步更新此数组
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

// ═══════════════════════════════════════════════════════════════
// ⚠️ 只看这里：改 mkin.h，别动 mkdata.cpp！
// ═══════════════════════════════════════════════════════════════
// 
// ✅ 改这个文件（mkin.h）里的 test() 函数
// ❌ 别动 mkdata.cpp（框架代码，不需要改）
//
// 测试数据分组（25组）：请同步修改 SUBTASKS[] 和 config.yaml
// ═══════════════════════════════════════════════════════════════

void test(int case_num, ofstream& fout)
{
    // ============================================================
    // Subtask 0: 样例数据（直接复制题目样例） — case 1-2
    // ============================================================
    if (case_num == 1)
    {
        // 样例1：n=10 → 198
        fout << 10 << endl;
    }
    else if (case_num == 2)
    {
        // 样例2：n=7 → 133
        fout << 7 << endl;
    }
    
    // ============================================================
    // Subtask 1: 小规模 + 特殊性质 — case 3-8
    // ============================================================
    else if (case_num == 3)
    {
        // n=1（最小合法输入）
        fout << 1 << endl;
    }
    else if (case_num == 4)
    {
        // n=3（极小型）
        fout << 3 << endl;
    }
    else if (case_num == 5)
    {
        // n=5（小型）
        fout << 5 << endl;
    }
    else if (case_num == 6)
    {
        // n=8（正好第1个休整日，验休整逻辑）
        fout << 8 << endl;
    }
    else if (case_num == 7)
    {
        // n=14（第2周期的第6个工作日，接近下一个休整）
        fout << 14 << endl;
    }
    else if (case_num == 8)
    {
        // n=16（正好第2个休整日，验多周期休整）
        fout << 16 << endl;
    }
    
    // ============================================================
    // Subtask 2: Hack 数据 — case 9-11
    // ============================================================
    else if (case_num == 9)
    {
        // Hack 1：n=1（最小边界，漏判则错）
        fout << 1 << endl;
    }
    else if (case_num == 10)
    {
        // Hack 2：n=100（最大边界，验循环正确性）
        fout << 100 << endl;
    }
    else if (case_num == 11)
    {
        // Hack 3：n=7（周期边界，第7天最后一个工作日）
        fout << 7 << endl;
    }
    
    // ============================================================
    // Subtask 3: 中大规模数据 — case 12-20
    // ============================================================
    else if (case_num == 12)
    {
        // n=15（2个完整周期差1天）
        fout << 15 << endl;
    }
    else if (case_num == 13)
    {
        // n=30（中等规模）
        fout << 30 << endl;
    }
    else if (case_num == 14)
    {
        // n=50（中等偏大）
        fout << 50 << endl;
    }
    else if (case_num == 15)
    {
        // n=61（中大规模）
        fout << 61 << endl;
    }
    else if (case_num == 16)
    {
        // n=72（大规模）
        fout << 72 << endl;
    }
    else if (case_num == 17)
    {
        // n=83（大规模）
        fout << 83 << endl;
    }
    else if (case_num == 18)
    {
        // n=94（大规模）
        fout << 94 << endl;
    }
    else if (case_num == 19)
    {
        // n=99（近最大边界）
        fout << 99 << endl;
    }
    else if (case_num == 20)
    {
        // n=100（最大边界）
        fout << 100 << endl;
    }
    
    // ============================================================
    // Subtask 4: 随机回归测试 — case 21-25
    // ============================================================
    else if (case_num == 21)
    {
        // n=11（小随机）
        fout << 11 << endl;
    }
    else if (case_num == 22)
    {
        // n=23（中等随机）
        fout << 23 << endl;
    }
    else if (case_num == 23)
    {
        // n=42（中等随机）
        fout << 42 << endl;
    }
    else if (case_num == 24)
    {
        // n=65（大随机）
        fout << 65 << endl;
    }
    else
    {
        // n=88（大随机）
        fout << 88 << endl;
    }
}

#endif
