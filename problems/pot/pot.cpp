#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int cases;
	long long num;
	long long total = 0;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		cin >> num;
		total += pow(num/10, num%10);
	}
	cout << total << endl;
	return 0;
}
