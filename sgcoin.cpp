#include <iostream>

using namespace std;

long long H(long long previousHash, string &transaction, long long token) {
    long long v = previousHash;
    for (int i=0; i < transaction.length(); i++) {
        v = (v * 31 + transaction[i]) % 1000000007;
    }
    return (v * 7 + token) % 1000000007;
}

long long T(long long previousHash, string &transaction) {
    long long v = previousHash;
    for (int i=0; i < transaction.length(); i++) {
        v = (v * 31 + transaction[i]) % 1000000007;
    }

    return (((v * 7) % 1000000007) / 10000000 + 1) * 10000000 - ((v * 7) % 1000000007);
}


bool hasSevenTrailing(long long h) {
    int count = 0;
    while (h != 0 and h % 10 == 0) {
        h = h / 10;
        count += 1;
    }
    return count == 7;
}


int main() {
    long long h;
    cin >> h;
    string transA = "a";
    string transB = "b";
    long long tokenA = T(h, transA); 
    long long hA = H(h, transA, tokenA);
    long long tokenB = T(hA, transB); 
    long long hB = H(hA, transB, tokenB);
            
    cout << transA << " " << tokenA << " " << endl;
    cout << transB << " " << tokenB << " " << endl;
}
