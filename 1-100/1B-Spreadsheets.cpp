#include <iostream>
#include <string>

using namespace std;

//R23C55 - BC23


string toAlpha(long input) {
    int alphSize(26);
    int n(input - 1);
    string out("");
    while(n > 0) {
        out += (n % alphSize == 0 ? 'A' : ('A' + (n%alphSize + 1)));
    }
    if (input % alphSize != 1) {++out[0];}
    size_t M = out.size();
    for (int i = 0; i <  M /2; i++) {
        char tmp = out[M-1-i];
        out[M-1-i] = out[i];
        out[i] = tmp;
    }
    return out;
}

long toNumeric(string letters) {
    
}

bool isCoordinates(const string line) {
    if (line[0] == 'R') {
        for (int i = 1; i < line.size() - 1; i++) 
            if (line[i-1] >= 0 && line[i-1] <= 9 && line[i] == 'C')
                return true;
    }
    return false;
}

int main() {
    int n;
    scanf("%d\n", &n);
    while(n--) {
        string line; getline(cin, line);
        if (isCoordinates(line)) {
            
        } else {
            
        }
    }

    return 0;
}