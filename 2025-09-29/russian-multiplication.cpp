#include <iostream>
using namespace std;

int russian_multiplication(int a, int b) {
    int result = 0;
    while (a > 0) {
        if (a % 2 == 1) { // If 'a' is odd
            result += b;
        }
        a /= 2; // Halve 'a'
        b *= 2; // Double 'b'
    }
    return result;
} 

int main() {
    int a, b;
    cout << "Enter two integers to multiply: ";
    cin >> a >> b;
    int product = russian_multiplication(a, b);
    cout << "The product of " << a << " and " << b << " is: " << product << endl;
    return 0;
}