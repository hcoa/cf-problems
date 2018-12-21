#include <iostream>

using namespace std;

int main() {
    unsigned long long n = 0, m = 0, a = 0;
    scanf("%llu %llu %llu", &n, &m, &a);
    unsigned long long x = n/a + (n%a > 0);
    unsigned long long y = m/a + (m%a > 0);
    printf("%llu\n", x*y);
}