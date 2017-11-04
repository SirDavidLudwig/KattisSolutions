#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int x, y;
	cin >> x >> y;
	if (x == 0 && y == 0)
		cout << "Not a moose" << endl;
	else
		cout << (x == y ? "Even " : "Odd ") << max(x, y)*2 << endl;
	return 0;
}
