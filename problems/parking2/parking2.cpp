#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int left, right, shortest;
	int t, n, x, j;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		int x[n];
		left = 100;
		right = -1;
		for (j = 0; j < n; j++) {
			cin >> x[j];
			left = min(left, x[j]);
			right = max(right, x[j]);
		}
		shortest = INT32_MAX;
		for (j = 0; j < n; j++) {
			shortest = min(shortest, abs(left - x[j]) + 2*right - x[j] - left);
		}
		cout << shortest << endl;
	}
	return 0;
}
