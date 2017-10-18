#include <iostream>

using namespace std;

int main()
{
	int num, result = 0;
	cin >> num;
	while (num > 0) {
		result = result << 1;
		result += num & 1;
		num = num >> 1;
	}
	cout << result << endl;
	return 0;
}
