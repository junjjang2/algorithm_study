#include <iostream>
#include <vector>
#include <climits>
#include <queue>
using namespace std;

// 재귀함수 안쓰는 방법은 없나?

class DFS{
public:
    DFS(int M, int N){
        width = M;
        height = N;
        heights.assign(M, vector<int>(N, 0));
        dp.assign(M, vector<int>(N, -1));
        
        dp[0][0] = 1;
    };

    int dfs(int x, int y){
        if(dp[x][y] != -1)
            return dp[x][y];
        
        int cur_height = heights[x][y];

        int cnt = 0;
        if (x-1 >=0 && heights[x-1][y] > cur_height)
            cnt += dfs(x-1, y);
        if (y-1 >=0 && heights[x][y-1] > cur_height)
            cnt += dfs(x, y-1);
        if (x+1 < width && heights[x+1][y] > cur_height)
            cnt += dfs(x+1, y);
        if (y+1 < height && heights[x][y+1] > cur_height)  
            cnt += dfs(x, y+1);
        
        dp[x][y] = cnt;

        return cnt;
        
    }

    vector<vector<int>> dp;
    vector<vector<int>> heights;

private:
    int width;
    int height;

};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int M, N;
    std::cin >> M >> N;

    DFS df(M, N);

    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
                std::cin >> df.heights[i][j];
        }
    }

    std::cout << df.dfs(M-1, N-1) << "\n";

    return 0;
}
