#include <algorithm>
#include <set>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct edge {
    int u;
    int v; 
    int d;
};

bool cmp(edge& x, edge& y) {
    return x.d < y.d;
}

int find(vector<int>& parent, int i) {
    if (parent[i] == i) {
        return i;
    }
    return find(parent, parent[i]);
}

void uni (vector<int>& parent, vector<int>& rank, int x, int y){
    int xroot = find(parent, x);
    int yroot = find(parent, y);

    if (rank[xroot] < rank[yroot]){
        parent[xroot] = yroot;
    } else if (rank[xroot] > rank[yroot]) {
        parent[yroot] = xroot;
    } else {
        parent[yroot] = xroot;
        rank[xroot]++;
    }
}


int main() {
    int n;
    cin >> n;

    vector<edge> edges;
    for (int i=0; i < n; i++) {
        for (int j=0; j < n; j++) {
            int num;
            cin >> num;
            if (j > i){
                edges.push_back({i, j, num});
            }
        }
    }
    sort(edges.begin(), edges.end(), cmp);

    vector<int> parent;
    vector<int> rank;
    for (int i=0; i < n; i++) {
        parent.push_back(i);
        rank.push_back(0);
    }
    
    for (auto i : edges) {
        int x = find(parent, i.u);
        int y = find(parent, i.v);
        if (x != y) {
            cout << i.u + 1 << " " << i.v + 1 << endl;
            uni(parent, rank, x, y);
        }
    }
}

