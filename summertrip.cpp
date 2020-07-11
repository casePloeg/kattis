#include <iostream>
#include <array>

using namespace std;

int main() {
    string events;
    cin >> events;
    
    int count = 0;
    for (int i=0; i<events.length(); i++){
        int seen [26] = {0};
        for (int j=i+1; j<events.length(); j++){
            if (events[i] != events[j]) {
                char t = events[j];
                if (seen[int(t) - int('a')] == 0) {
                    count++;
                    seen[int(t) - int('a')] = 1;
                }
            } else {
                break;
            }

        }
    }
    cout << count << endl;
}
