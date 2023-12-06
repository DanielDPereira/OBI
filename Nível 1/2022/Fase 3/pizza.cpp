#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int a, b, r, g;

    cin >> a >> b >> r >> g;

    if (a < r*2 || b < r*2 || 360 % g != 0)
    {
	cout << "N\n";
    }
    else
    {
	cout << "S\n";
    }

    return 0;
}