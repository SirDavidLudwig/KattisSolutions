#include <iostream>

using namespace std;

int main()
{
	int i, j;
	int t, n, v, lv;
	cin >> t;
	for (i = 0; i < t; i++) {
		cin >> n;
		cin >> lv;
		for (j = 1; j < n; j++) {
			cin >> v;
			if (lv+1 == v)
				lv = v;
			else {
				cout << j+1 << endl;
				break;
			}
		}
		for (j++; j < n; j++)
			cin >> v;
	}
	return 0;
}
