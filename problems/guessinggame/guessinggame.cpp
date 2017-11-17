#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int g, minG = 1, maxG = 10;
	string response;
	for (cin >> g; g != 0; cin >> g) {
		cin >> response >> response;
		if (response == "on") {
			if (g >= minG && g <= maxG)
				cout << "Stan may be honest" << endl;
			else
				cout << "Stan is dishonest" << endl;
			minG = 1;
			maxG = 10;
		} else if (response == "low") {
			minG = max(g + 1, minG);
		} else {
			maxG = min(g - 1, maxG);
		}
	}
	return 0;
}
