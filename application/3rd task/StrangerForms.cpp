#include <iostream>
#include <vector>
#include <string>
#include <cstring>

#include "Functions.h"
using namespace std;


int main()
{
    char matrix[ROWS][COLS];

    int rows, columns;
    cin >> rows >> columns;

    initializeMatrix(matrix, rows, columns);
    
    int configurationsCount;
    cin >> configurationsCount;

    vector<string> relations;
    string relation,central;
    cin >> central;
 
    vector<Seat> seats(configurationsCount+1,Seat(central[0],"x","y"));
    for (int i = 0; i < configurationsCount; i++)
    {
        cin >> relation;
        int index = find(seats, relation[2]);
              
        seats[i + 1].name = relation[0];

        if (relation[1] == 'R')
        {
            seats[i + 1].row.replace(seats[i+1].row.begin(), seats[i+1].row.end(), seats[index].row);
            seats[i + 1].col.replace(0, 1, seats[index].col);
            seats[i + 1].col.append("+1");
        }
        else if (relation[1] == 'L')
        {
            seats[i + 1].row.replace(seats[i+1].row.begin(), seats[i+1].row.end(), seats[index].row);
            seats[i + 1].col.replace(0, 1, seats[index].col);
            seats[i + 1].col.append("-1");
        }
        else if (relation[1] == 'A')
        {
       
            seats[i + 1].col.replace(seats[i+1].col.begin(), seats[i+1].col.end(), seats[index].col);
            seats[i + 1].row.replace(0, 1, seats[index].row);
            seats[i + 1].row.append("-1");
        }
    }
    vector<Seat> mySeats(seats);
    
    int result = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            vector<Pair> configurations = replace(seats, i, j);
            if (checkAll(matrix, rows, columns, configurations))
            {
                replaceConfigurationsInMatrix(matrix, configurations, seats);
                printMatrix(matrix, rows, columns);
                resetMatrix(matrix, rows, columns);
                seats = mySeats;
                result++;
            }
        }
    }
    cout << result << endl;
    
    system("pause");
    return 0;
}