#include <iostream>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    std::cin >> N;

    std::vector<int> arr(N);
    std::vector<int> length(1000000, 0);

    for(int i = 0; i < N; i++){
        std::cin >> arr[i];
    }

    // O(N^2)
    for(int i=N-1; i>=0; i--){
        int maxLen = 0;
        for(int j=N-1; j>i; j--){
            if(arr[i] < arr[j]){
                if (maxLen < length[arr[j]])
                    maxLen = length[arr[j]];
            }
        }
        if (length[arr[i]] < maxLen + 1)
            length[arr[i]] = maxLen + 1;
    }

    //O(N)
    int maxLen = 0;
    for(int i = 0; i < 1000000; i++){
        if(maxLen < length[i])
            maxLen = length[i];
    }
    std::cout << maxLen << "\n";
    return 0;
}