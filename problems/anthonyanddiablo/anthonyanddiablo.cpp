#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	double A, N;
	cin >> A >> N;

	if (sqrt(4*A*M_PI) <= N)
		cout << "Diablo is happy!";
	else
		cout << "Need more materials!";

	return 0;
}
