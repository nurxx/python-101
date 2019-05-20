#define CATCH_CONFIG_MAIN 
#include "catch.hpp" // A multi-paradigm test framework for C++
#include "Keys.h"

/*

You can add tests as follows:

TEST_CASE(" - test name must be unique - ")
{
vector<pair<string,unsigned int>> input= { data };
string expected; // store the expected output of the program

//Then compare the output with expected using REQUIRE
REQUIRE(Solution(input)==expected);
}

*/

TEST_CASE("Sample Test Case 1")
{
	vector<pair<string, unsigned int>> input = { { "f",1 },{ "g",2 },{ "f",3 },{ "h",10 },{ "f",5 },{ "h",2 } };
	string expected;
	expected.append("h: 12\n");
	expected.append("f: 9\n");
	expected.append("g: 2\n");
	REQUIRE(Solution(input) == expected);
}
TEST_CASE(" Sample Test Case 2")
{
	vector<pair<string,unsigned int>> input = { {"a", 1},{"b", 1},{"c", 1} };
	string expected = "a, b, c: 1\n";
	REQUIRE(Solution(input) == expected);
}

TEST_CASE("Test 1 - testing the ', ' separation condition in top 3")
{
	vector<pair<string,unsigned int>> input = { { "a", 1 },{ "b",18 },{ "c",1 },{ "d",1 },{ "e",0 } };
	string expected;
	expected.append("b: 18\n");
	expected.append("a, c, d: 1\n");
    expected.append("e: 0\n");
	REQUIRE(Solution(input) == expected);
}

TEST_CASE("Test 2 - testing first condition - sum the values of duplicate keys in top 3")
{
	vector<pair<string, unsigned int>> input = { {"a",1},{"a",2},{"b",2} };
	string expected;
	expected.append("a: 3\n");
	expected.append("b: 2\n");
	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 3 - testing values sum and  key ', ' separation conditions in top 3")
{
	vector<pair<string, unsigned int>>input = { {"h",5},{"g",4},{"i",2},{"g",3},{"i",4},{"a",5},{"c",5},{"g",7} };
	string expected;
	expected.append("g: 14\n");
    expected.append("i: 6\n");
	expected.append("a, c, h: 5\n");
	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 4 - testing values sum of duplicate keys in top 3 ")
{
	vector<pair<string, unsigned int>> input = { {"a",1},{ "a",1 },{ "b",1 },{ "a",1 },{ "f",2 },{ "g",3 },
    { "g",8 },{ "b",15 },{ "s",7 },{ "g",9 },{ "p",4 },{ "s",16 },{ "x",1 },{ "v",5 },{ "p",8 },
    { "s",20 },{ "a",7 },{ "s",1 },{ "f",0 },{ "v",4 },{ "g",0 },{ "b",6 } };
	string expected;
    expected.append("s: 44\n");
   	expected.append("b: 22\n");
	expected.append("g: 20\n");
	REQUIRE(Solution(input) == expected);
}

TEST_CASE("Test 5 - testing values sum and  key ', ' separation conditions in top 3")
{
	vector<pair<string, unsigned int>>input =  { { "ac",8 },{ "ab",4 } ,{"a",2}, { "b",2 }, { "ab",4 }};
	string expected;
	expected.append("ab, ac: 8\n");
	expected.append("a, b: 2\n");
	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 6 - testing values sum and  key ', ' separation conditions in top 3")
{
	vector<pair<string, unsigned int>>input = { {"abra",2},{"abracadabra",4},{"ab",2} };
	string expected;
    expected.append("abracadabra: 4\n");
	expected.append("ab, abra: 2\n");
	REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 7 - testing values sum and  key ', ' separation conditions in top 3")
{
	vector<pair<string, unsigned int>> input = { {"name",1},{"name",2},{"name",3},{"password",1},{"password",2},{"password",3} };
	string expected;
	expected.append("name, password: 6\n");
	REQUIRE(Solution(input) == expected);
}
 
TEST_CASE("Test 8 - testing with keys consisting of digits both conditions ")
{
    vector<pair<string, unsigned int>> input = { { "1",1 },{ "2",2 },{ "3", 1 },{ "5", 8 },{ "4",4 },{ "1",1 } };
    string expected;
    expected.append("5: 8\n");
    expected.append("4: 4\n");
    expected.append("1, 2: 2\n");
    REQUIRE(Solution(input) == expected);
}
TEST_CASE("Test 9 - testing with keys consisting of digits - ', ' separation of the keys with duplicate values in top 3")
{
    vector<pair<string, unsigned int>> input = { { "1",50 },{ "20",50 },{ "3",50  },{ "50", 50 },{ "40",50 },{"pair",50},
    {"paid",50},{"park",50 } };
    string expected;
    expected.append("1, 20, 3, 40, 50, paid, pair, park: 50\n");
    REQUIRE(Solution(input) == expected);
}