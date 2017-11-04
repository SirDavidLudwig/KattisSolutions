#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int t, n, m, imports;
	cin >> t;
	for (int i = 0; i < t; i++) {
		imports = 0;
		cin >> n;
		if (n == 0) {
			cout << 0 << endl;
			continue;
		}
		cin >> m;
		while (m != 0) {
			imports += max(m-2*n, 0);
			n = m;
			cin >> m;
		}
		cout << imports << endl;
	}
	return 0;
}
