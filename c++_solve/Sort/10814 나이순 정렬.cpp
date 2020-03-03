#include <iostream>
#include <map>

using namespace std;

int main()
{
    int n;
    multimap<int, string> sorted_map;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int num;
        string str;
        cin >> num >> str;
        sorted_map.insert(make_pair(num, str));
    }
    for (const auto &t : sorted_map)
        cout << t.first << " " << t.second << '\n';
}