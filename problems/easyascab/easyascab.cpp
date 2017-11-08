#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

struct Letter
{
	const char letter;
	vector<Letter> next;
	Letter(char letter) : letter(letter) {}
};

int main()
{
	char max;
	int i, n;
	cin >> max >> n;

	cout << max << endl << n;

	Letter *chars[n];
	for (i = 0; i < max; i++)
		chars[i] = new Letter((char)65+i);

	int len;
	string line1;
	string line2;
	cin >> line1;
	for (i = 1; i < n; i++) {

	}

	return 0;
}
