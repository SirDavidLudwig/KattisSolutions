#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	int n, w, h, m;
	cin >> n >> w >> h;
	double maxLen = sqrt(w*w+h*h);
	for (int i = 0; i < n; i++) {
		cin >> m;
		cout << (m <= maxLen ? "DA" : "NE") << endl;
	}
	return 0;
}
