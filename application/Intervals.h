#pragma once

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

string Solution(vector<int> input)
{
	string output = "";
	map<int, int> m;

	for (int i = 0; i < input.size(); i++)
	{ 
		if(m.find(input[i])==m.end())
		{
			m[input[i]]++;
		}
	}

	std::map<int, int>::iterator it, iter, end, start;
	int consecutiveCount;
	for (it = m.begin(); it != m.end(); ++it)
	{
		start = it;
		end = it;
		consecutiveCount = it->second;

		iter = m.find(it->first + 1);

		if (iter != m.end())
		{
			while (iter != m.end())
			{
				it++;
				consecutiveCount += iter->second;
				end = iter;
				iter = m.find(it->first + 1);
			}
		}
		output.append("[");
		output.append(to_string(start->first));
		output.append(", ");
		output.append(to_string(end->first));
		output.append("] with consecutive count of ");
		output.append(to_string(consecutiveCount));
		output.append("\n");
	}
	return output;
}