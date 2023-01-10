#include <iostream>
using namespace std;

double fibonacci_rec(double n)
{
    if (n <= 1)
    {
        return n;
    }
    return (fibonacci_rec(n - 1) + fibonacci_rec(n - 2));
}

void fibonacci(double n)
{
    double a = 0;
    double b = 1;
    double temp;

    for (double i = 0; i <= n; i++)
    {
        cout << a << ' ';

        temp = a;
        a = b;
        b = temp + b;
    }
}

int main()
{

    double n;
    cout << "Enter how many fibonacci numbers you want to prdouble: ";
    cin >> n;

    fibonacci(n);
    cout << '\n';

    cout << "Nth element is : " << fibonacci_rec(n) << endl;

    return 0;
}