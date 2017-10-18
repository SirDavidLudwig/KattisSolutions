#include <iostream>

using namespace std;

int main()
{
	int testCases, num;
	cin >> testCases;
	for (int i = 0; i < testCases; i++) {
		cin >> num;
		cout << num << (num & 1 ? " is odd" : " is even") << endl;
	}
	return 0;
}
