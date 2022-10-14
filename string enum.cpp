#include <algorithm>
#include <cctype>
#include <functional>
#include <iostream>
#include <string>
using namespace std;

const char* months[] =
  { 
  "jan", "feb", "mar", "apr", "may", "jun",
  "jul", "aug", "sep", "oct", "nov", "dec"
  };

int main()
  {
  string user_input;
  cout << "Please type the name of your favorite month> " << flush;
  getline( cin, user_input );

  // We're only interested in the first three characters
  user_input += "---";  // (but make sure there actually are three...) 
  user_input.erase( 3 );

  // Convert user's input to lowercase
  transform(
    user_input.begin(),
    user_input.end(),
    user_input.begin(),
    ptr_fun <int, int> ( tolower )
    );

  // Find the index of the matching month
  int month = find(
                months,
                months +12,
                user_input
                )
            - months;

  if (month < 12)
    cout << "The month number is " << (month +1) << ".\n";
  else
    cout << "That was not a month name.\n";

  return 0;
  }