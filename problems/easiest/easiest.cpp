#include <iostream>

using namespace std;

int sumDigits(int n)
{
	int sum = 0;
	while (n != 0) {
		sum += n % 10;
		n /= 10;
	}
	return sum;
}

int main()
{
	int n, p, sum;
	cin >> n;
	while (n != 0) {
		sum = sumDigits(n);
		p = 11;
		while (sum != sumDigits(p*n))
			p++;
		cout << p << endl;
		cin >> n;
	}
	return 0;
}
