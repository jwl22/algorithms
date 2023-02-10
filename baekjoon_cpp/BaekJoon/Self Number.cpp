#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector<int> sequence;
	int sum = 0, num = 0;

	for (int i = 1; i <= 10000; i++) {	//자릿수 더하는 함수 제작 코드
		num = i;
		sum += num;
		do{
			sum += num % 10;
			num = num / 10;
		} while (num);
		sequence.push_back(sum);
		sum = 0;
	}

	sort(sequence.begin(), sequence.end());	//함수 벡터 정렬
	sequence.erase(unique(sequence.begin(), sequence.end()), sequence.end());	//unique로 중복 제거

	for (int i = 1; i <= 10000; i++) {
		if (find(sequence.begin(), sequence.end(), i) == sequence.end()) {
			cout << i << '\n';
		}
	}

	return 0;
}
