#include <iostream>

int main() {

    int M;
    int N;
    int Diferenca;
    int Orlando;
    
    std::cin >> M;
    std::cin >> N;
    
    if (M > N){
        Diferenca = M - N;
        Orlando = Diferenca + M;
    }else{
        Diferenca = N - M;
        Orlando = Diferenca + N;        
    }
    
        std::cout << Orlando;

    return 0;
}