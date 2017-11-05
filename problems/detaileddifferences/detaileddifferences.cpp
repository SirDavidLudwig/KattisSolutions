#include <iostream>
#include <string>

using namespace std;

int main()
{
	string a, b;
	int n;
	cin >> n;
	getline(cin, a);
	for (int i = 0; i < n; i++) {
		getline(cin, a);
		getline(cin, b);
		int l = a.size();
		cout << a << endl << b << endl;
		for (int j = 0; j < l; j++)
			cout <<	(a[j] == b[j] ? '.' : '*');
		cout << endl << endl;
	}
	return 0;
}
