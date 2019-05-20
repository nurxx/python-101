#pragma once

#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

const int ROWS = 500;
const int COLS = 500;

char original[ROWS][COLS];

struct Pair {
    int first;
    int second;
    Pair(int x, int y)
    {
        this->first = x;
        this->second = y;
    }
};
struct Seat {
    char name;
    string row;
    string col;
    Seat(char person, string x, string y)
    {
        this->name = person;
        this->row = x;
        this->col = y;
    }
};
int calculateInteger(string s)
{
    int minus = 0;
    int plus = 0;
    int number = stoi(s);
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '-')
        {
            minus++;
        }
        else if (s[i] == '+')
        {
            plus++;
        }
    }
    return (number - minus + plus);
}
void printMatrix(char matrix[ROWS][COLS], int rows, int cols)
{
    cout << " ";
    for (int i = 0; i < cols; i++)
    {
        cout << i;
    }
    cout << endl;
    for (int i = 0; i < rows; i++)
    {
        cout << i;
        for (int j = 0; j < cols; j++)
        {
            cout << matrix[i][j];
        }
        cout << endl;
    }

    for (int i = 0; i < cols; i++)
    {
        cout << '-';
    }
    cout << endl;
}
void initializeMatrix(char matrix[ROWS][COLS], int rows, int columns)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j< columns; j++)
        {
            cin >> matrix[i][j];
            original[i][j] = matrix[i][j];
        }
    }
}
void resetMatrix(char matrix[ROWS][COLS], int rows, int columns)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j< columns; j++)
        {
            matrix[i][j] = original[i][j];
        }
    }
}
bool isEmptySeat(char matrix[ROWS][COLS], int rows, int cols, int x, int y)
{
    if (x >= 0 && x < rows && y >= 0 && y < cols &&matrix[x][y] == '.')
        return true;

    return false;
}
vector<Pair> replace(vector<Seat>seats, int x, int y)
{
    vector<Pair>configurations;
    for (int i = 0; i < seats.size(); i++)
    {
        seats[i].row.replace(0, 1, to_string(x));
        seats[i].col.replace(0, 1, to_string(y));
        configurations.push_back(Pair(calculateInteger(seats[i].row), calculateInteger(seats[i].col)));
    }
    return configurations;
}
bool checkAll(char matrix[ROWS][COLS], int rows, int columns, vector<Pair>configurations)
{
    int count = 0;
    for (int i = 0; i < configurations.size(); i++)
    {
        if (isEmptySeat(matrix, rows, columns, configurations[i].first, configurations[i].second))
        {
            count++;
        }
    }
    if (count == configurations.size()) return true;

    return false;
}
void replaceConfigurationsInMatrix(char matrix[ROWS][COLS], vector<Pair>configurations, vector<Seat>seats)
{
    for (int i = 0; i < configurations.size(); i++)
    {
        matrix[configurations[i].first][configurations[i].second] = seats[i].name;
    }
}
int find(vector<Seat>seats, char person)
{
    for (int i = 0; i < seats.size(); i++)
    {
        if (seats[i].name == person)
            return i;
    }
    return -1;
}