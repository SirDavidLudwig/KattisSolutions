#include <cmath>
#include <chrono>
#include <iostream>

using namespace std;

int main()
{
	long total = 0;
	double x0, x1, sq;
	int j, t, x, y;
	double h;
	cin >> t;
	cout << fixed;
	for (int i = 0; i < t; i++) {
		cin >> x >> y;
		h = (x+y-sqrt(x*x+y*y-x*y))/6;
		cout << h*(x-h-h)*(y-h-h) << endl;
	}
	return 0;
}
