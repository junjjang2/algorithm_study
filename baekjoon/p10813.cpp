#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N, M;
    std::cin >> N >> M;
    vector<int> arr(N, 0); 
    for(int i = 0; i < N; i++){
        arr[i] = i+1;
    }
    int i, j;
    while(M--){
        cin >> i >> j;
        swap(arr[i-1], arr[j-1]);
        
    }
    for(auto i : arr){
        cout << i << " ";
    }
    cout << "\n";
    return 0;
}
