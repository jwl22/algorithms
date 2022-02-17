#include <iostream>
#include <string>
using namespace std;

int main() {
	string inputString;
	int count;
	getline(cin, inputString);
	if (inputString == " ") {
		count = 0;
	}
	else {
		count = 1;
	}
	
	for (int i = 1; i < inputString.size() - 1; i++) {
		if (inputString[i] == ' ') {
			count++;
		}
	}
	cout << count;

	return 0;
}