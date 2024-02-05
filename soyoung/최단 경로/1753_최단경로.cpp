#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

#define endl '\n'
#define int long long
#define pii pair<int, int>
#define MAX 998244353

using namespace std;
template<typename T>
using priority_stack = priority_queue<T, vector<T>, greater<T>>;

vector<pair<int, int>> edges[20010];

void dijkstra(int start, int vertex_cnt) {
    vector<int> dist(vertex_cnt + 1, MAX);
    priority_stack<pair<int, int>> pq;
    pq.push(make_pair(0, start));
    dist[start] = 0;
    while (!pq.empty()) {
        int vertex = pq.top().second;
        int weight = pq.top().first;
        pq.pop();
        if (weight > dist[vertex]) continue;
        dist[vertex] = weight;
        for (auto a : edges[vertex]) {
            int new_weight = weight + a.second;
            if (dist[a.first] > new_weight) {
                dist[a.first] = new_weight;
                pq.push(make_pair(dist[a.first], a.first));
            }
        }
    }
    for (int i = 1; i <= vertex_cnt; i++) {
        if (dist[i] == MAX) cout << "INF";
        else cout << dist[i];
        cout << '\n';
    }
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N, M, X;
    cin >> N >> M >> X;
    vector<int> dist(N + 1, MAX);
    for (int i = 0; i < M; i++) {
        int v1, v2, w;
        cin >> v1 >> v2 >> w;
        edges[v1].push_back(make_pair(v2, w));
    }
    dijkstra(X, N);
}

//다익스트라 알고리즘