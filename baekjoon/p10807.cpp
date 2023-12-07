#include <iostream>

using namespace std;

int main(){
    int N, X, v;
    int arr[201] = {0}; // -100 <= X <= 100 : 201개
    cin >> N;
    while(N--){
        cin >> X;
        arr[X + 100]++;
    }
    cin >> v;
    cout << arr[v + 100] << "\n";
    return 0;
}
