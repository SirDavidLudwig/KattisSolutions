#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int x1, x2;
	int n1, n2;
	int mov1 = false, mov2 = false;
	int step1 = 0, step2 = 0;
	int x1pos[100000], x2pos[100000];
	int i;
	cin >> x1 >> x2;

	cin >> n1;
	for (i = 0; i < n1; i++)
		cin >> x1pos[i];

	cin >> n2;
	for (i = 0; i < n2; i++)
		cin >> x2pos[i];

	for (i = 1; i <= 3000000; i++) {
		if (mov1)
			x1++;
		if (mov2)
			x2++;
		if (i == x1pos[step1]) {
			mov1 = !mov1;
			step1++;
		}
		if (i == x2pos[step2]) {
			mov2 = !mov2;
			step2++;
		}
		if (abs(x1 - x2) < 5) {
			cout << "bumper tap at time " << i << endl;
			return 0;
		}
	}

	cout << "safe and sound" << endl;
	return 0;
}
