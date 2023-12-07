#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    std::map<int, int> mp;
    int N, M, a, b;
    std::cin >> N;

    while(N--){
        std::cin >> a;
        if(mp.find(a) == mp.end()){
            mp[a] = 1;
        }
        else{
            mp[a] += 1;
        }
    }
    std::cin >> M;
    while(M--){
        std::cin >> b;
        if(mp.find(b) == mp.end()){
            std::cout << "0 ";
        }
        else{
            std::cout << mp[b] << " ";
        }
    }
    std::cout << "\n";
    return 0;
}