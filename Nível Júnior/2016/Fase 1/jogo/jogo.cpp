#include <iostream>

int main() {
    
    int P, D_1, D_2;
    
    std::cin >> P;
    std::cin >> D_1;
    std::cin >> D_2;
    
    if (P == 0){
        if ((D_1 + D_2) % 2 == 0){
            std::cout << "0";
        }else{
            std::cout << "1";
        }
    }
        
    if (P == 1){
        if ((D_1 + D_2) % 2 == 0){
            std::cout << "1";
        }else{
            std::cout << "0";
        }
    }