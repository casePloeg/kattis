#include<algorithm>
#include<iostream>
#include<vector>

using namespace std;

struct edge {
    int u;
    int v; 
    int d;
}; 

bool cmp(edge& x, edge& y) {
    return x.d < y.d;
}

int find(vector<int>& parent, int i){
    if (parent[i] == i) {
        return i;
    }
    return find(parent, parent[i]);
}

void join (vector<int>& parent, vector<int>& rank, int x, int y) {
    int xroot = find(parent, x);
    int yroot = find(parent, y);

    if(rank[xroot] < rank[yroot]){
        parent[xroot] = yroot;
    } else if (rank[xroot] > rank[yroot]) {
        parent[yroot] = xroot;
    } else {
        parent[yroot] = xroot;
        rank[xroot]++;
    }
}

int diff(string a, string b) {
    int count = 0;
    for (int i=0; i < a.length(); i++) {
        if (a[i] != b[i]) {
            count++;
        }
    }
    return count;
}

int main() {
    int n;
    int k;
    cin >> n;
    cin >> k;
    vector<edge> edges;
    vector<string> nodes;
    for (int i=0; i < n; i++) {
        string node;
        cin >> node;
        nodes.push_back(node);
    }
    for (int i=0; i < n; i++) {
        for (int j=i+1; j < n; j++){
            edges.push_back({i, j, diff(nodes[i], nodes[j])});
        }
    }
    sort(edges.begin(), edges.end(), cmp);

    vector<int> parent;
    vector<int> rank;

    for (int i=0; i<n; i++) {
        parent.push_back(i);
        rank.push_back(0);
    }
    
    vector<edge> mst;
    int weight = 0;
    for (auto i : edges) { 
        int x = find(parent, i.u);
        int y = find(parent, i.v);
        if (x != y) {
            weight += i.d;
            mst.push_back(i);
            join(parent, rank, x, y);
        }
    }
    cout << weight << endl;
    for (auto i : mst) {
        cout << i.u << " " << i.v << endl;
    }

}

