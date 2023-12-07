#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, M;
    std::cin >> N >> M;
    vector<int> arr(N, 0); 
    for(int i = 0; i < N; i++){
        arr[i] = i+1;
    }

    int ST, ED;
    while(M--){
        cin >> ST >> ED;
        std::reverse(arr.begin() + ST - 1, arr.begin() + ED);
    }
    for(auto i : arr){
        cout << i << " ";
    }
    cout << "\n";
    return 0;
}
