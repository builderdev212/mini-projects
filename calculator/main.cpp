#include <iostream>
#include "functions.h"
using namespace std;

int main() {
  cout << "\033[2J\033[1;1H";
  int running = 1;
  int input;
  while (running == 1) {
    cout << "Do you want to:\nAdd - 1\nSubtract - 2\nMultiply - 3\nDivide - 4\nModulous - 5\nExit - 6\n\nEnter the command number here: ";
    cin >> input;
    cout << endl;
    if (input < 1 || input > 6) {
      cout << "\033[2J\033[1;1H";
      cout << "Bad input.\n";
    } else if (input == 6) {
      cout << "\033[2J\033[1;1H";
      running = 0;
    } else {
      int x;
      int y;
      cout << "First number: ";
      cin >> x;
      cout << "Secound number: ";
      cin >> y;
      cout << "\033[2J\033[1;1H";
      switch (input) {
        case 1:
          cout << "Output: " << add(x,y) << "\n\n";
          break;
        case 2:
          cout << "Output: " << sub(x, y) << "\n\n";
          break;
        case 3:
          cout << "Output: " << mult(x, y) << "\n\n";
          break;
        case 4:
          cout << "Output: " << divide(x, y) << "\n\n";
          break;
        case 5:
          cout << "Output: " << mod(x, y) << "\n\n";
          break;
      }
    }
  }
  return 0;
}
