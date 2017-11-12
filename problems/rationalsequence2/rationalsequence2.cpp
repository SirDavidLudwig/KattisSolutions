#include <iostream>

using namespace std;

int main()
{
	int i, j, n;
	int k, p, q, t;
	char slash;
	bool pathDelta[32];
	cin >> n;

	for (i = 0; i < n; i++) {
		cin >> k >> p >> slash >> q;
		j = 0;
		while (p != 1 || q != 1) {
			pathDelta[j++] = p > q;
			if (p > q)
				p -= q;
			else
				q -= p;
		}
		t = 1;
		while (j-- > 0);
			t = 2*t + pathDelta[j];
		cout << k << ' ' << t << endl;
	}
	return 0;
}
