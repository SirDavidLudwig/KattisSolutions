#include <cmath>
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main()
{
	int i, j, n;
	double spacing = M_PI * 60 / 28;
	unordered_map<char, int> circle;
	circle[' '] = 0;
	circle['\''] = 1;
	for (i = 2; i < 28; i++)
	circle[(char)(i + 63)] = i;

	cin >> n;
	getchar();
	string line;
	int distance;
	int last = -1;
	double t;
	for (i = 0; i < n; i++) {
		getline(cin, line);
		t = line.length();
		for (j = 1; j < line.length(); j++) {
			distance = abs(circle[line[j]] - circle[line[j-1]]);
			if (distance > 14)
				distance = 28 - distance;
			t += distance*spacing/15.0;
		}
		cout << fixed << t << endl;
	}
	return 0;
}
