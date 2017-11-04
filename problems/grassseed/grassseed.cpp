#include <iomanip>
#include <iostream>

using namespace std;

int main()
{
	double c, w, l, t = 0;
	int n;
	cin >> c >> n;
	for (int i = 0; i < n; i++) {
		cin >> w >> l;
		t += w*l*c;
	}

	cout << fixed << setprecision(6) << t << endl;

	return 0;
}
