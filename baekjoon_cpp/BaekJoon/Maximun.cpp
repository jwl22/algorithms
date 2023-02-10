#include <iostream>

using namespace std;

int main() {
	int count = 0;
	int num[9] = {};
	int maxNum = 0, maxNumIndex = 0;

	while (count < 9) {
		cin >> num[count];

		if (num[count] > maxNum) {
			maxNum = num[count];
			maxNumIndex = count;
		}

		count++;
	}
	cout << maxNum << '\n' << maxNumIndex + 1;

	return 0;
}