#pragma once

#include <iostream>
#include <map>
#include <string>
#include <functional> 
#include <vector>
using namespace std;


string Solution(vector<pair<string, unsigned int>> input)
{
	string output = "";
	map<string, unsigned int> sumKeys; 
	for (int i = 0; i < input.size(); i++)
	{
		sumKeys[input[i].first] += input[i].second;
	}
	map<unsigned int, string, greater<unsigned int>> duplicateValues; 
	map<string, unsigned int>::iterator iter;
	for (iter = sumKeys.begin(); iter != sumKeys.end(); ++iter)
	{
		if (duplicateValues.find(iter->second) == duplicateValues.end())
		{
			duplicateValues[iter->second] = iter->first;
		}
		else {
			duplicateValues[iter->second].append(", ");
			duplicateValues[iter->second].append(iter->first);
		}
	}

	int printed = 0;
	map<unsigned int, string>::iterator it;
	for (it = duplicateValues.begin(); it != duplicateValues.end() && printed<3; ++it)
	{
		output.append(it->second);
		output.append(": ");
		output.append(to_string(it->first));
		output.append("\n");

		printed++;
	}
	return output;
}