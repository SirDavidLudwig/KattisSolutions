#include <iostream>

using namespace std;

int main()
{
	int i, k, n, t, total = 0;
	char m;
	cin >> k >> n;

	for (k--, i = 0; i < n && total < 210; i++) {
		cin >> t >> m;
		total += t;
		if (total < 210 && m == 'T') {
			k = (k+1) % 8;
		}
	}
	cout << k + 1 << endl;
	return 0;
}
