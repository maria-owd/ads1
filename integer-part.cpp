#include <iostream>
using namespace std;

int integerPart(double x) {
    int p;
    if (x > 0) {
        p = 0;
        while (x > 0) {
            p = p + 1;
            x = x - 1;
        }
    } else {
        //for negative numbers, the integer part, 
        // is the largest integer less than or equal to x.
        p = -1; 
        while (x < 0) {
            p = p - 1;
            x = x + 1;
        }
    }
    return p;
}

int main() {
    double x;
    cout << "Enter a real number: ";
    cin >> x;

    int p = integerPart(x);
    cout << "The integer part is: " << p << endl;

    return 0;
}