#include <iostream>
using namespace std;

const int ADD = 1;
const int SUB = 2;
const int MULT = 3;
const int DIV = 4;
const int EXIT = 5;

int main() {
  // Variables to store options
  int a;
  int b;
  int choice;
  int running = true;

  do {
    bool first = true;
    do {
      if (!first) {
        cout << "Error. Please enter a number between " << ADD << " and " << EXIT << ".\n" << endl;
      }
      cout << ADD << ". Add two numbers." << endl;
      cout << SUB << ". Subtract two numbers." << endl;
      cout << MULT << ". Multiply two numbers." << endl;
      cout << DIV << ". Divide two numbers." << endl;
      cout << EXIT << ". Exit the program." << endl;
      cin >> choice;
    } while ((choice < ADD) || (choice > EXIT));

    // Action based on the users input.
    switch (choice) {
      case ADD:
        cout << "Please enter the first number: ";
        cin >> a;
        cout << "Please enter the second number: ";
        cin >> b;

        cout << "Result: " << a+b << endl;
        break;
      case SUB:
        cout << "Please enter the first number: ";
        cin >> a;
        cout << "Please enter the second number: ";
        cin >> b;

        cout << "Result: " << a-b << endl;
        break;
      case MULT:
        cout << "Please enter the first number: ";
        cin >> a;
        cout << "Please enter the second number: ";
        cin >> b;

        cout << "Result: " << a*b << endl;
        break;
      case DIV:
        cout << "Please enter the first number: ";
        cin >> a;
        cout << "Please enter the second number: ";
        cin >> b;

        cout << "Result: " << a/b << endl;
        break;
      case EXIT:
        running = false;
        break;
    }
    cout << endl;
  } while (running);

#ifdef _WIN32
  // This is a windows specific way to pause the output.
  system("pause");
#else
  // This is a general way to pause the output that should work on any OS.
  cout << "Press any key to continue...";
  getchar();
#endif
  return 0;
}
