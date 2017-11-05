#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int d, v;
	cin >> d >> v;
	cout << fixed;
	while (d != 0 && v != 0) {
		cout << pow((12*(M_PI*(d*d*d/4.0)-v)-M_PI*d*d*d)/(2*M_PI), 1/3.0) << endl;
		cin >> d >> v;
	}
	return 0;
}
