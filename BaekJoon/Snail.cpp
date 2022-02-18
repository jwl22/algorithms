#include <iostream>
using namespace std;

int main() {
	int A, B, V;
	cin >> A >> B >> V;
	
	int day = (V - A) / (A - B) + 1;

	if ((day - 1) * (A - B) + A < V) {
		day++;
	}

	cout << (int)day << '\n';

	return 0;
}