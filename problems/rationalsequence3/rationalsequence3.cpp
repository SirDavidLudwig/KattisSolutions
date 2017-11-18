#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int i, j, n, index;
	int k, p, q, t, pathLen;
	cin >> t;

	for (i = 0; i < t; i++) {
		p = q = 1;
		cin >> k >> n;
		if (n == 1) {
			cout << k << " 1/1" << endl;
			continue;
		}
		int pathDelta[pathLen = log2(n--)];
		for (j = pathLen-1; j >= 0; j--) {
			pathDelta[j] = n;
			n = (n - 1) / 2;
		}
		for (j = 0; j < pathLen; j++) {
			if (1 + 2*n == pathDelta[j]) {
				n = 2*n + 1;
				q += p;
			} else {
				n = 2*n + 2;
				p += q;
			}
		}
		cout << k << ' ' << p << '/' << q << endl;
	}
	return 0;
}
