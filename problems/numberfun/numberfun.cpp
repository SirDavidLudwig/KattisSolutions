#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int i;
	double a, b, c;
	int n;
	cin >> n;

	for (i = 0; i < n; i++) {
		cin >> a >> b >> c;
		if (a+b == c || a*b == c || abs(a-b) == c || b/a == c || a/b == c)
			cout << "Possible" << endl;
		else
			cout << "Impossible" << endl;
	}
	return 0;
}
