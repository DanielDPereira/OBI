#include <bits/stdc++.h>
using namespace std;

class Number {
  public:
    vector<int> digits;

    Number(int N) {
      while (N > 0) {
        digits.push_back(N % 10);
        N /= 10;
      }
    }

    int rebuild() {
      if (digits.size() == 0)
        return -1;

      int res = 0;
      for (int i = digits.size() - 1; i >= 0; i--) {
        res = res * 10 + digits[i];
      }
      return res;
    }
};

void casa(Number &num1, Number &num2) {
  for (int i = min(num1.digits.size(), num2.digits.size()) - 1; i >= 0; i--) {
    if (num1.digits[i] > num2.digits[i]) {
      num2.digits.erase(num2.digits.begin() + i);
    } else if (num1.digits[i] < num2.digits[i]) {
      num1.digits.erase(num1.digits.begin() + i);
    }
  }
}

int main() {
  int A, B;
  cin >> A >> B;
  
  Number num1(A), num2(B);
  
  casa(num1, num2);

  A = num1.rebuild();
  B = num2.rebuild();

  cout << min(A, B) << ' ' << max(A, B) << endl;
  return 0;
}

