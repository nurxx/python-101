#define CATCH_CONFIG_MAIN
#include "catch.hpp" // A multi-paradigm test framework for C++

#include "Intervals.h"
/*

You can add tests as follows:

TEST_CASE(" - test name must be unique - ")
{
vector<int> input= { data };
string expected; // store the expected output of the program

//Then compare the output with expected using REQUIRE
REQUIRE(Solution(input) == expected);
}

*/

TEST_CASE("Sample Test Case 1")
{
	vector<int> input = { -181,- 414, 441, 889,- 547,- 313, 622, 679, 782,- 640};
	string expected;
	expected.append("[-640, -640] with consecutive count of 1\n");
	expected.append("[-547, -547] with consecutive count of 1\n");
	expected.append("[-414, -414] with consecutive count of 1\n");
	expected.append("[-313, -313] with consecutive count of 1\n");
	expected.append("[-181, -181] with consecutive count of 1\n");
	expected.append("[441, 441] with consecutive count of 1\n");
	expected.append("[622, 622] with consecutive count of 1\n");
	expected.append("[679, 679] with consecutive count of 1\n");
	expected.append("[782, 782] with consecutive count of 1\n");
	expected.append("[889, 889] with consecutive count of 1\n");


	REQUIRE(Solution(input) == expected);
}

TEST_CASE("Sample Test Case 2")
{
	vector<int> input = { 123, 567, 124, 568, -100,-99 };
	string expected;
	expected.append("[-100, -99] with consecutive count of 2\n");
	expected.append("[123, 124] with consecutive count of 2\n");
	expected.append("[567, 568] with consecutive count of 2\n");

	REQUIRE(Solution(input) == expected);
}

TEST_CASE("Test 1 - testing with consecutive and non-consecutive numbers")
{
	vector<int>input = { 108,109,107,10010,10009,1708,1068,1699,1065,1700 };
	string expected; 
	expected.append("[107, 109] with consecutive count of 3\n");
	expected.append("[1065, 1065] with consecutive count of 1\n");
	expected.append("[1068, 1068] with consecutive count of 1\n");
	expected.append("[1699, 1700] with consecutive count of 2\n");
	expected.append("[1708, 1708] with consecutive count of 1\n");
	expected.append("[10009, 10010] with consecutive count of 2\n");

	REQUIRE(Solution(input) == expected);
}

TEST_CASE("Test 2 - testing with consecutive and non-consecutive numbers")
{
	vector<int> input = { 0,2,-2,4,-1,5,6,8 };
	string expected;
	expected.append("[-2, 0] with consecutive count of 3\n");
	expected.append("[2, 2] with consecutive count of 1\n");
	expected.append("[4, 6] with consecutive count of 3\n");
	expected.append("[8, 8] with consecutive count of 1\n");

	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 3 - testing with only consecutive numbers")
{
	vector<int> input = { 0,-1,-2,-3,-4,-5 };
	string expected;
	expected.append("[-5, 0] with consecutive count of 6\n");

	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 4 - testing for a only number")
{
	vector<int>input = { 0 };
	string expected;
	expected.append("[0, 0] with consecutive count of 1\n");

	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 5 - testing with consecutive and non-consecutive numbers")
{
	vector<int>input = { 8,9,1,97,-17000,58,-17001 };
	string expected;
	expected.append("[-17001, -17000] with consecutive count of 2\n");
	expected.append("[1, 1] with consecutive count of 1\n");
	expected.append("[8, 9] with consecutive count of 2\n");
	expected.append("[58, 58] with consecutive count of 1\n");
	expected.append("[97, 97] with consecutive count of 1\n");

	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 6 - testing with non-consecutive numbers")
{
	vector<int> input= {0,4,400,87,22,52,-421,412,78,214,142,-241};
    string expected;
    expected.append("[-421, -421] with consecutive count of 1\n");
    expected.append("[-241, -241] with consecutive count of 1\n");
    expected.append("[0, 0] with consecutive count of 1\n");
    expected.append("[4, 4] with consecutive count of 1\n");
    expected.append("[22, 22] with consecutive count of 1\n");
    expected.append("[52, 52] with consecutive count of 1\n");
    expected.append("[78, 78] with consecutive count of 1\n");
    expected.append("[87, 87] with consecutive count of 1\n");
    expected.append("[142, 142] with consecutive count of 1\n");
    expected.append("[214, 214] with consecutive count of 1\n");
    expected.append("[400, 400] with consecutive count of 1\n");
    expected.append("[412, 412] with consecutive count of 1\n"); 
                
	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 7- testing with consecutive and non-consecutive numbers")
{
	vector<int> input = { 456 ,-1098,458,489,-1096,500,-167,168,237,238,455,490,501,502,-1097,169,235,236 };
	string expected;
	expected.append("[-1098, -1096] with consecutive count of 3\n");
	expected.append("[-167, -167] with consecutive count of 1\n");
	expected.append("[168, 169] with consecutive count of 2\n");
	expected.append("[235, 238] with consecutive count of 4\n");
	expected.append("[455, 456] with consecutive count of 2\n");
	expected.append("[458, 458] with consecutive count of 1\n");
	expected.append("[489, 490] with consecutive count of 2\n");
	expected.append("[500, 502] with consecutive count of 3\n");

    REQUIRE(Solution(input) == expected);
}
