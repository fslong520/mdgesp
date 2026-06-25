#pragma once
#ifndef MKIN_H
#define MKIN_H
#include <bits/stdc++.h>
using namespace std;

const int TEST_CASES = 25;
struct SubtaskDef { int id, start, end; };
const SubtaskDef SUBTASKS[] = {
    {0, 1, 2}, {1, 3, 8}, {2, 9, 11}, {3, 12, 20}, {4, 21, 25},
};
const int SUBTASK_COUNT = sizeof(SUBTASKS) / sizeof(SUBTASKS[0]);

void test(int case_num, ofstream& fout) {
    if (case_num == 1) { fout << "3" << endl; }
    else if (case_num == 2) { fout << "5" << endl; }
    else if (case_num == 3) { fout << "2" << endl; }
    else if (case_num == 4) { fout << "4" << endl; }
    else if (case_num == 5) { fout << "10" << endl; }
    else if (case_num == 6) { fout << "20" << endl; }
    else if (case_num == 7) { fout << "7" << endl; }
    else if (case_num == 8) { fout << "15" << endl; }
    else if (case_num == 9) { fout << "2" << endl; }
    else if (case_num == 10) { fout << "20" << endl; }
    else if (case_num == 11) { fout << "11" << endl; }
    else if (case_num >= 12 && case_num <= 20) {
        int n = rand() % 19 + 2; // 2..20
        fout << n << endl;
    }
    else {
        int n = rand() % 19 + 2;
        fout << n << endl;
    }
}
#endif
