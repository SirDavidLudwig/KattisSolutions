#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

double LENGTHS[30];

bool craft(int count, int s, int n, int *sheets, double &tape)
{
	if (s >= n)
		return false;
	if (count*2 - sheets[s] > 0) {
		if (!craft(count*2 - sheets[s], s+1, n, sheets, tape))
			return false;
	}
	tape += LENGTHS[s-1]*count;
	sheets[s] -= count*2;
	return true;
}

int main()
{
	int i, n; // 2 <= n <= 30
	cin >> n;
	int sheets[n+1];
	sheets[0] = sheets[n] = 0;
	double tape = 0;
	double w = pow(2, -5/4.0);
	double h = pow(2, -3/4.0);
	LENGTHS[0] = h;

	for (i = 1; i < n; i++) {
		cin >> sheets[i];
		if (w > h) {
			w *= 0.5;
			LENGTHS[i] = h;
		} else {
			h *= 0.5;
			LENGTHS[i] = w;
		}
	}

	if (craft(1, 1, n, sheets, tape)) {
		cout << fixed << setprecision(6) << tape << endl;
	} else {
		cout << "impossible" << endl;
	}

	return 0;
}
