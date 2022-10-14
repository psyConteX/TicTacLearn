#include <iostream>
#include <limits> // for std::numeric_limits


 void ignoreLine() 
{
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

double getDouble() {
	while (true) {
		std::cout << "Enter a double value: ";
		double x;
		std::cin >> x;
			if (!std::cin) {
				std::cin.clear();
				ignoreLine();
			}
			else {
				ignoreLine();
				return x;
			}
	}
}

void Count(double x) {
int i;
	for (i=1;i<=x;i++) {
		std::cout << i << std::endl;
	}
}



int main() {
	double x = getDouble();
	Count(x);
}