#include <iostream>
#include <vector>
#include <climits>

using namespace std;


int getSubCables(int* cables, int num, unsigned int length){
    int cnt = 0;
    for(int i = 0; i < num; i++){
        cnt += (unsigned int)cables[i] / length;
    }
    return cnt;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int K, N, length;

    std::cin >> K >> N;

    int* cables = new int[K]{0};

    for(int i = 0; i < K; i++){
        std::cin >> length;
        cables[i] = length;
    }

    unsigned int left = 1;
    unsigned int right = INT_MAX;
    unsigned int mid;
    int ans = 0;

    while(left<=right){
        mid = (left+right) / 2;
        if(getSubCables(cables, K, mid) >= N){
            ans = mid;
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }

    std::cout << ans << "\n";
    return 0;
}