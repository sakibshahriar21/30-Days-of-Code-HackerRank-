#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int N,i,j;
    cin >> N;
    
    for(i=0; i<N; i++){
        
        string S;
        cin >> S;
        
        for(j=0; j<S.length(); j++){
            
            if(j%2 == 0){
                cout << S[j];
            }
        }
        
        cout << " ";
        
        for(j=0; j<S.length(); j++){
            
            if(j%2 == 1){
                cout << S[j];
            }
        }
        
        cout << endl;
    }
     
    return 0;
}
