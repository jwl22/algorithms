#include <iostream>
using namespace std;

int main() {
	int maxNumber = 1;	// 1/1,2/1,2,3 �� ������ ���� �� ������ ���� ����� ����
	int inputNumber, count = 0;
	cin >> inputNumber;
	for (int i = 1; i < inputNumber; i++) {
		count++;
		if (maxNumber == count) {
			count = 0;
			maxNumber++;
		}
	}

	if (!(maxNumber % 2)) {
		cout << count + 1 << '/' << maxNumber - count << '\n';
	}
	else {
		cout << maxNumber - count << '/' << count + 1 << '\n';
	}

	return 0;
}