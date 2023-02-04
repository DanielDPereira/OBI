// https://olimpiada.ic.unicamp.br/pratique/p2/2010/f1/batalha/
//

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

char board[100][100];

int n, m;

vector<pair<int, int>> vals;


void dfs(int x, int y)
{
    if (x < 0 || x >= n || y < 0 || y >= m)
    {
	return;
    }

    if (board[x][y] == '.')
    {
	return;
    }

    board[x][y] = '.';

    vals.push_back({x, y});


    dfs(x, y+1);
    dfs(x, y-1);
    dfs(x+1, y);
    dfs(x-1, y);

}

int main()
{
    int tot =0;

    cin >> n >> m;

    for(int i = 0; i < n; i++)
    {
	for(int j = 0; j < m; j++)
	{
	    cin >> board[i][j];
	}
    }

    int k;
    cin >> k;

    vector<pair<int, int>> shots;

    for(int i = 0; i < k; i++)
    {
	int x, y;
	cin >> x >> y;
	x--;
	y--;
	shots.push_back({x, y});
    }


    int cnt = 0;

    for(int i = 0; i < n; i++)
    {
	for(int j = 0; j < m; j++)
	{
	    dfs(i, j);

	    if (vals.size() > 1)
	    {
	        for(auto i : shots)
		{
		    auto it = find(vals.begin(), vals.end(), i);

		    if(it != vals.end())
		    {
			cnt++;
		    }
		}
		if (cnt == vals.size())
		{
		    tot++;
		}

	    }

	    if (vals.size() == 1)
	    {
		board[i][j] = '#';
	    }

	    cnt = 0;
	    vals.clear();
	}
    }

    for (auto i : shots)
    {
	if(board[i.first][i.second] == '#')
	{
	    tot++;
	}
    }

    cout << tot;

}

