#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

int main()
{
	int r;
	cin >> r;
	cout << fixed << setprecision(4)
	     << M_PI * pow(r, 2) << endl
	     << 2 * pow(r, 2) << endl;
	return 0;
}
