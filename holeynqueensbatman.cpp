#include <iostream>
#include <utility>
#include <vector>
#include <set>


using namespace std;

vector<pair<int, int>> queens;
set<int> columns;

int nqueens(set<pair<int, int>>& holes, int n, int s_i) {
    int total = 0;
    if (queens.size() == n) {
        return 1;
    }
    int i = s_i + 1;
    for (int j=0; j<n; j++) {
        if ((columns.find(j) == columns.end()) and holes.find({i,j}) == holes.end()) {
            bool valid = true;
            for (auto q : queens) {
                int x;
                int y;
                x = q.first;
                y = q.second;
                int d_x = abs(i - x);
                int d_y = abs(j - y);
                if (d_x == d_y or d_x == 0 or d_y == 0) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                queens.push_back({i, j});
                columns.insert(j);
                total += nqueens(holes, n, i);
                columns.erase(j);
                queens.pop_back();
            }
        }
    }
    return total;
}


int main() {
    int n;
    int m;
    cin >> n;
    cin >> m;
    while (n + m != 0) {
        std::set<pair<int, int>> holes;
        for (int i=0; i<m; i++){
            int x;
            int y;
            cin >> x >> y;
            holes.insert({x, y});
        }
        cout << nqueens(holes, n, -1) << endl;
        cin >> n;
        cin >> m;
    }

}
