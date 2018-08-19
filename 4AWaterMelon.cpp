#include <iostream>

using namespace std;

int main() {
    int w;
    scanf("%d", &w);
    printf("%s\n", ((w <= 2 || w % 2) ? "NO" : "YES"));
}
