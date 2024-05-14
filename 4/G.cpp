#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool check_if_plus_of_k(int a, int b, int n, int m, vector<vector<int>>& prefix, int k) {
    if (a - k < 0 || b - k < 0 || b + 2 * k - 1 >= m || a + 2 * k - 1 >= n) {
        return false;
    }

    int x1 = b - k, y1 = a;
    int x2 = b + 2 * k, y2 = a + k;
    int horiz = prefix[y2][x2] - prefix[y1][x2] - prefix[y2][x1] + prefix[y1][x1];

    if (horiz != 3 * k * k) {
        return false;
    }

    x1 = b, y1 = a - k;
    x2 = b + k, y2 = a + 2 * k;
    int vert = prefix[y2][x2] - prefix[y1][x2] - prefix[y2][x1] + prefix[y1][x1];

    if (vert != 3 * k * k) {
        return false;
    }

    return true;
}

int find_max_k(int i, int j, int max_k, int n, int m, vector<vector<int>>& prefix) {
    int l = max_k + 1;
    int r = min(n, m) / 3 + 1;
    int res = 0;

    while (r - l > 0) {
        int k = (l + r) / 2;
        if (check_if_plus_of_k(i, j, n, m, prefix, k)) {
            res = k;
            l = k + 1;
        } else {
            r = k;
            if (r <= max_k) {
                break;
            }
        }
    }
    return res;
}

int main() {

    ifstream inp("input.txt");
    int n, m;
    inp >> n >> m;
    vector<vector<char>> arr(n, vector<char>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            inp >> arr[i][j];
        }
    }

    vector<vector<int>> prefix(n + 1, vector<int>(m + 1));
    vector<vector<int>> prefix_rows(n, vector<int>(m + 1));

    for (int i = 0; i < n; i++) {
        int s = 0;
        for (int j = 0; j < m; j++) {
            s += (arr[i][j] == '#') ? 1 : 0;
            prefix_rows[i][j + 1] = s;
        }
    }

    for (int j = 1; j <= m; j++) {
        for (int i = 0; i < n; i++) {
            prefix[i + 1][j] = prefix[i][j] + prefix_rows[i][j];
        }
    }
   
    int max_k = 1;
    for (int i = max_k + 1; i < n; i++) {
        for (int j = max_k + 1; j < m; j++) {
            if (arr[i][j] == '#') {
                max_k = max(max_k, find_max_k(i, j, max_k, n, m, prefix));
            }
        }
    }

    cout << max_k;
    return 0;
}