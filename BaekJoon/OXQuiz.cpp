#include <iostream>

using namespace std;

int factorial(int count, int sum); //구현할 필요 없는 함수지만 공부한다는 생각으로 생성

int main() {
	string input;
	int testCount = 0, count = 0, sum = 0;

	cin >> testCount;

	for (int i = 0; i < testCount; i++) {
		cin >> input;
		const char* inputChar = input.c_str();

		sum = 0;
		count = 0;
		for (int j = 0; j < input.length(); j++) {
			if (inputChar[j] == 'O') {
				count++;
			}
			else {
				sum = factorial(count, sum);
				count = 0;
			}
		}
		if (count != 0) {
			sum = factorial(count, sum);
		}
		cout << sum << '\n';
	}

	return 0;
}

int factorial(int count, int sum) {
	for (int j = 0; j < count; j++) {
		sum += j + 1;
	}

	return sum;
}