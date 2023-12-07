#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<bool> arr(30, false); 

    int cnt = 28;
    int N;
    while(cnt--){
        cin >> N;
        arr[N-1] = true;
    }
    for(int i = 0; i < 30; i++){
        if(!arr[i])
            cout << i+1 << "\n";
    }
    return 0;
}
