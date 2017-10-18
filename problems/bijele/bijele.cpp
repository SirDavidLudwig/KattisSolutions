#include <iostream>

using namespace std;

int main()
{
	int num, set[]{1, 1, 2, 2, 2, 8};
	for (int i = 0; i < 6; i++) {
		cin >> num;
		cout << set[i] - num << " ";
	}

	return 0;
}
