#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int i, j, n, m;
	cin >> n >> m;
	double prob[n+m];
	double largest = 0, delta = 1.0/n * 1.0/m;
	for (i = 0; i < n+m; i++)
		prob[i] = 0;
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			prob[i+j] += delta;
			largest = max(largest, prob[i+j]);
		}
	}
	for (i = 0; i < n+m; i++)
		if (prob[i] == largest)
			cout << i+2 << endl;
	return 0;
}
