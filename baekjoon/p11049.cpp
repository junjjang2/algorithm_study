#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// DP array를 2개나 쓸 이유가 없음
// 더 고민해보기
using vector2d = vector<vector<int>>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    
    std::cin >> N;

    vector2d dp(N, vector<int>(N, 0));
    vector<pair<int,int>> arr(N, {0,0});
    for(int i = 0; i<N; i++){
        std::cin >> arr[i].first >> arr[i].second;
    }
    
    for(int depth = 1; depth < N; depth++){
        for(int ST=0; ST < N-depth; ST++){
            int ED = ST + depth;
            int min_cost = INT_MAX;
            for(int i = ST; i < ED; i++){
                int cost = dp[ST][i] + dp[i+1][ED] + arr[ST].first * arr[i].second * arr[ED].second;
                if(min_cost > cost){
                    min_cost = cost;
                }
            }
            dp[ST][ED] = min_cost;
        }
    }    
    std::cout << dp[0][N-1] << "\n";

    return 0;
}
