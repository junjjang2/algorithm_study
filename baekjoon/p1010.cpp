#include <iostream>
#include <vector>

using namespace std;

int main(){
    // M 개의 원소를 N 개의 집합으로 분할하는 경우의 수
    // N <= M
    // mCn = M! / (N! * (M-N)!)
    int T, N, M;
    int ans;
    std::cin >> T;
    while(T--){
        std::cin >> N >> M;
        ans = 1; 
        for(int i = 0; i < N; i++){
            ans *= (M-i);
            ans /= (i+1);
        }
        cout << ans << "\n";

    }
    
    return 0;
}
