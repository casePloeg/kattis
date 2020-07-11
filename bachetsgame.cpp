#include <iostream>
#include <vector>
#include <array>

using namespace std;

int main() {
    int n;
    int m;
    while (cin >> n) {
        cin >> m;
        int x;
        vector<int> moves;
        for (int i=0; i < m; i++){
            cin >> x;
            moves.push_back(x);
        }

        array<int, 1000001> dp;
        for (int i=0; i<n+1; i++){
            dp[i] = 0;
            for (int j=0; j<m; j++){
                if (i - moves[j] == 0){
                    dp[i] = 1;
                    break;
                } else {
                    bool possible;
                    possible = i - moves[j] > 0;
                    if (possible) {
                        if (dp[i-moves[j]] != 1){
                            dp[i] = 1;
                            break;
                        }
                    }
                }
            }
        }
        int w = dp[n];
        if (w == 1) {
            cout << "Stan wins" << endl;
        } else {
            cout << "Ollie wins" << endl;
        }

    }
}
