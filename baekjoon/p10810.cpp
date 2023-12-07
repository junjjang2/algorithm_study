#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N, M;
    std::cin >> N >> M;
    vector<int> arr(N, 0); 

    int ST, ED, C;
    while(M--){
        cin >> ST >> ED >> C;
        for(int i = ST - 1; i < ED; i++){
            arr[i] = C;
        }
    }
    for(auto i : arr){
        cout << i << " ";
    }
    cout << "\n";
    return 0;
}
