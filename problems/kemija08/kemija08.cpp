#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n;
	string line;
	getline(cin, line);
	n = line.size();

	for (int i = 0; i < n;) {
		cout << line[i];
		if (line[i] == 'a' || line[i] == 'e' || line[i] == 'i' || line[i] == 'o' || line[i] == 'u')
			i += 3;
		else
			i++;
	}
	return 0;
}
