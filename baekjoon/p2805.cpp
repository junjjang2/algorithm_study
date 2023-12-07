#include <iostream>
#include <vector>

using namespace std;

long long getCuttedTree(int* trees, int N, int height){
    long long sum = 0;
    for(int i = 0; i < N; i++){
        if(trees[i] > height){
            sum += trees[i] - height;
        }
    }
    return sum;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, length;
    std::cin >> N >> M;
    int* trees = new int[N]{0};

    for(int i = 0; i < N; i++){
        std::cin >> trees[i];
    }

    int left = 0;
    int right = 1000000000;
    int mid;
    int ans = 0;

    while(left<=right){
        mid = (left+right) / 2;
        if(getCuttedTree(trees, N, mid) >= M){
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