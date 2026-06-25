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
        fout << "7\n1 3 4 5 6 9 10" << endl;
    }
    else if (case_num == 2) {
        fout << "5\n100 200 300 400 500" << endl;
    }
    else if (case_num == 3) {
        fout << "1\n42" << endl;
    }
    else if (case_num == 4) {
        int a[] = {1,2,3,4,5};
        fout << "5\n";
        for (int x : a) fout << x << " ";
        fout << endl;
    }
    else if (case_num == 5) {
        int a[] = {10,9,8,7,6,5,4,3,2,1};
        fout << "10\n";
        for (int x : a) fout << x << " ";
        fout << endl;
    }
    else if (case_num == 6) {
        int n = 10;
        fout << n << "\n";
        for (int i = 0; i < n; i++) fout << 99 << " ";
        fout << endl;
    }
    else if (case_num == 7) {
        int n = 10;
        fout << n << "\n";
        for (int i = 0; i < n; i++) fout << (i * 10) << " ";
        fout << endl;
    }
    else if (case_num == 8) {
        int a[] = {5,6,7,8,9,10,100,101,102,103,104,105};
        fout << "12\n";
        for (int x : a) fout << x << " ";
        fout << endl;
    }
    else if (case_num == 9) {
        fout << "2\n10000 9999" << endl;
    }
    else if (case_num == 10) {
        fout << "1000\n";
        for (int i = 0; i < 1000; i++) fout << (i * 2) << " ";
        fout << endl;
    }
    else if (case_num == 11) {
        fout << "5\n1 2 3 4 5" << endl;
    }
    else if (case_num >= 12 && case_num <= 20) {
        int n = rand() % 990 + 10;
        fout << n << "\n";
        for (int i = 0; i < n; i++) fout << (rand() % 10000 + 1) << " ";
        fout << endl;
    }
    else {
        int n = rand() % 1000 + 1;
        fout << n << "\n";
        for (int i = 0; i < n; i++) fout << (rand() % 10000 + 1) << " ";
        fout << endl;
    }
}
#endif
