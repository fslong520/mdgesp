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
    srand(time(0));

    if (case_num == 1) {
        fout << "10\n95 88 92 75 82 78 60 65 70 85" << endl;
    }
    else if (case_num == 2) {
        fout << "6\n90 85 80 75 70 65" << endl;
    }
    else if (case_num == 3) {
        fout << "1\n80" << endl;
    }
    else if (case_num == 4) {
        fout << "2\n80 90" << endl;
    }
    else if (case_num == 5) {
        fout << "5\n50 60 70 80 90" << endl;
    }
    else if (case_num == 6) {
        fout << "10\n";
        for (int i = 0; i < 10; i++) fout << 75 << " ";
        fout << endl;
    }
    else if (case_num == 7) {
        fout << "100\n";
        for (int i = 0; i < 100; i++) fout << (i % 101) << " ";
        fout << endl;
    }
    else if (case_num == 8) {
        fout << "1000\n";
        for (int i = 0; i < 1000; i++) fout << (i % 3 == 0 ? 100 : 0) << " ";
        fout << endl;
    }
    else if (case_num == 9) {
        fout << "1\n50" << endl;
    }
    else if (case_num == 10) {
        fout << "2\n100 0" << endl;
    }
    else if (case_num == 11) {
        fout << "1000\n";
        for (int i = 0; i < 1000; i++) fout << (rand() % 101) << " ";
        fout << endl;
    }
    else if (case_num >= 12 && case_num <= 20) {
        int n = rand() % 990 + 10;
        fout << n << "\n";
        for (int i = 0; i < n; i++) fout << (rand() % 101) << " ";
        fout << endl;
    }
    else {
        int n = rand() % 1000 + 1;
        fout << n << "\n";
        for (int i = 0; i < n; i++) fout << (rand() % 101) << " ";
        fout << endl;
    }
}
#endif
