#include <iostream>

int main() {

    int D;
    
    std::cin >> D;
    
    D = D - 3;
    
    if (D % 8 == 3){
        std::cout << "1";
    }
    if (D % 8 == 4){
        std::cout << "2";
    }
    if (D % 8 == 5){
        std::cout << "3";
    }

    return 0;
}