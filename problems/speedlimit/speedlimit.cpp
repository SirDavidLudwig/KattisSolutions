#include <iostream>

using namespace std;

int main()
{
	int n, s, t, lt, d;
	cin >> n;
	while (n != -1) {
		d = 0;
		lt = 0;
		for (int i = 0; i < n; i++) {
			cin >> s >> t;
			d += s*(t-lt);
			lt = t;
		}
		cin >> n;
		cout << d << " miles" << endl;
	}
	return 0;
}
