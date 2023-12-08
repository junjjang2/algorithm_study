#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

// DP array를 2개나 쓸 이유가 없음
// 더 고민해보기
using vector2d = vector<vector<int>>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T, K;
    
    std::cin >> T;

    while(T--){
        std::cin >> K;

        vector2d arr(K, vector<int>(K, 0));
        vector2d tot_cost(K, vector<int>(K, 0));

        for(int i = 0; i<K; i++){
            std::cin >> arr[i][i];    
        }
        
        for(int depth = 1; depth < K; depth++){
            for(int ST=0; ST < K-depth; ST++){
                int ED = ST + depth;
                int min = INT_MAX;
                int min_cost = INT_MAX;
                for(int i = ST; i < ED; i++){
                    int temp = arr[ST][i] + arr[i+1][ED];
                    int cost = tot_cost[ST][i] + tot_cost[i+1][ED] + temp;
                    if(min_cost > cost){
                        min = temp;
                        min_cost = cost;
                    }
                }
                arr[ST][ED] = min;
                tot_cost[ST][ED] = min_cost;
            }
        }
        std::cout << tot_cost[0][K-1] << "\n";
    }
    return 0;
}

//         for(int depth = 1; depth < K; depth++){
//             for(int ST=0; ST < K-depth; ST++){
//                 int ED = ST + depth;
//                 int min = INT_MAX;
//                 int min_cost = INT_MAX;
//                 for(int i = ST; i < ED; i++){
//                     int temp = arr[ST][i] + arr[i+1][ED];
//                     int cost = tot_cost[ST][i] + tot_cost[i+1][ED] + temp;
//                     if(min_cost > cost){
//                         min = temp;
//                         min_cost = cost;
//                     }
//                 }
//                 arr[ST][ED] = min;
//                 tot_cost[ST][ED] = min_cost;
//             }
//         }
//         std::cout << tot_cost[0][K-1] << "\n";
//         for(int i =0; i<K; i++){
//             for(int j = 0; j<K; j++){
//                 std::cout << tot_cost[i][j] << " ";
//             }
//             std::cout << "\n";
//         }

//         for(int i = 0; i < K; i++){
//             delete[] arr[i];
//             delete[] tot_cost[i];
//         }
//         delete[] arr;        
//         delete[] tot_cost;
//     }

//     return 0;
// }