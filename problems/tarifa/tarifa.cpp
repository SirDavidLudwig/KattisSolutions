#include <iostream>

using namespace std;

int main()
{
	int x, n, p;
	cin >> x >> n;

	int total = x;
	for (int i = 0; i < n; i++) {
		cin >> p;
		total += x - p;
	}
	cout << total << endl;
	return 0;
}
