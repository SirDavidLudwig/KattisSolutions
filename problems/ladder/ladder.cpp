#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int h, angle;
	double len;
	cin >> h >> angle;
	cout << ceil(h/sin(M_PI/180 * angle));
	return 0;
}
