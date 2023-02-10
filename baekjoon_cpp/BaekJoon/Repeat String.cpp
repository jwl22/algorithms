#include <iostream>
#include <string>
using namespace std;

int main()
{
    int testCount;
    cin >> testCount;
    for (int i = 0; i < testCount; i++){
        int repeatCount;
        string inputString;
        cin >> repeatCount;
        cin >> inputString;

        for (int j = 0; j < inputString.length(); j++){
            for (int k = 0; k < repeatCount; k++) {
                cout << inputString[j];
            }
        }
        cout << endl;
    }
    return 0;
}