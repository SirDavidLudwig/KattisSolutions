#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main()
{
	int n, p;
	string place;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> p;
		unordered_map<string, int> places(p);
		for (int j = 0; j < p; j++) {
			cin >> place;
			places[place] = 1;
		}
		cout << places.size() << endl;
	}
	return 0;
}
