#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int H, W, N;
		cin >> H >> W >> N;

		int Y, X;

		if (N % H == 0) {
			Y = H;
			X = N / H;
		}
		else {
			Y = N % H;
			X = N / H + 1;
		}
		if (X < 10) {
			cout << Y << '0' << X << '\n';
		}
		else {
			cout << Y << X << '\n';
		}
	}

	return 0;
}