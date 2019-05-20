#include <iostream>
#include <vector>
#include "Intervals.h"
using namespace std;

int main()
{
	vector<int> input;
	int n;
	cin >> n;

	int num;
	while (n--)
	{
		cin >> num;
		input.push_back(num);
	}

	cout << Solution(input);
	
	system("pause");
	return 0;
}