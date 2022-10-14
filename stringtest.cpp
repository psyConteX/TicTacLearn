#include <iostream>
#include <string> //std::stoi
#include <stdlib.h> //uselessleftover
#include <limits>
#include <array>
#include <fstream> //file I O



int NoteC;

 void ignoreLine()  //CIN Error Correction, Ignore Line
{
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

std::string getStr() { //get String
		while (true) {
			std::string x;					//set x as string for later return	
			std::getline (std::cin,x); 		//read line for text
			NoteC = x.length(); 	//reach char count in NoteC
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

int main() {
    std::string x;
	char c;
    x = getStr();
    std::cout << x << ' ' << NoteC << ' ' << std::endl;
	for (int i = 0; i <= NoteC; i++) {
		x.seekg(NoteC);
		std::cout << x.get(c);
	}
}