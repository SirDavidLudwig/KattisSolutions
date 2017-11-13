#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int i = 1;
	int p, a, b, c, d, n;
	double highest, lowest, point;
	cin >> p >> a >> b >> c >> d >> n;

	highest = lowest = p*(sin(a*i+b)+cos(c*i+d)+2);
	for (i++; i <= n; i++) {
		point = p*(sin(a*i+b)+cos(c*i+d)+2);
		if (point > highest) {
			lowest += point - highest;
			highest += point - highest;
		} else if (point < lowest) {
			lowest = point;
		}
	}

	cout << fixed << highest - lowest << endl;

	return 0;
}
