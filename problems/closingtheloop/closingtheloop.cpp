#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int i, j, k, n, s, l, m, t;
	char c;
	for (cin >> n, i = 0; i < n; i++) {
		vector<int> blue;
		vector<int> red;
		cout << "Case #" << i+1 << ": ";
		for (cin >> s, j = 0; j < s; j++) {
			cin >> l >> c;
			(c == 'R' ? red : blue).push_back(l);
		}

		m = min(blue.size(), red.size());
		t = 0;
		sort(blue.rbegin(), blue.rend());
		sort(red.rbegin(), red.rend());
		for (k = 0; k < m; k++)
			t += blue[k] + red[k];
		cout << (t - 2*m) << endl;
	}
	return 0;
}
