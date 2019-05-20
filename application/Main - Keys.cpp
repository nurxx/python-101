#include <iostream>
#include <vector>
#include <utility>
#include "Keys.h"
using namespace std;

int main()
{
	vector<pair<string,unsigned int>> input;
	int n;
	cin >> n;

    string key;
    unsigned int value;
	while (n--)
	{
		cin >> key>> value;
		input.push_back(make_pair(key,value));
	}

	cout << Solution(input);
	
	system("pause");
	return 0;
}