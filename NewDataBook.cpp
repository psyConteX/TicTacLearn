#include <stdlib.h>
#include <string>
#include <array>
#include <iostream>
#include <limits>
int var = 07;
int personNr = 0;
const int c_maxPersonNr = 100;
const int c_arrayCount = 19;

std::string dataName = "TestFile.txt";
std::string dataNames[c_arrayCount] = {
    "Person Nummer",
    "Vorname",
    "Name",
    "Alter",
    "Geschlecht",
    "Wohort",
    "Hobby",
    "Lieblings Film",
    "Lieblings Farbe",
    "Cosplayer",
    "Job",
    "Mag",
    "Hass",
    "Skala 1-10",
    "Kontakt",
    "Notiz",
    "Kompliment",
    "Besonderheit",
    "Eindruck"
    }; //etc..
 void ignoreLine()  //CIN Error Correction, Ignore Line
{
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}
enum DataNamesEnummeration
{
    PersonNummer,
    Vorname,
    Name,
    Alter,
    Geschlecht,
    Wohort,
    Hobby,
    LieblingsFilm,
    LieblingsFarbe,
    Cosplayer,
    Job,
    Mag,
    Hass,
    Skala1bis10,
    Kontakt,
    Notiz,
    Kompliment,
    Besonderheit,
    Eindruck 
};
class Person {
    private:
        std::string stringdata[c_arrayCount]; 
    public:
        unsigned long long int a_stringcharactercount[c_arrayCount];
    Person()
    {
        std::cout << "Person Constructed" << std::endl; //construction call in console
    }
    void setstringdata(std::string input, int arraynumber) {
        stringdata[arraynumber] = input;//setting the string in arraynumber for person
    }
    std::string getstringdata(int arraynumber) {
        return stringdata[arraynumber];
    }
    auto getcin(std::string, int i) { //get String text
		while (true) {
			std::string x;					//set x as string for later return	
			std::getline(std::cin >> std::ws,x); 		//read line for text
			this->a_stringcharactercount[i] = x.length(); 	//write char count in NoteC
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

};
float getcin(float) {//not used
		while (true) {
			float x;
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
int getcin(int) {  //not used
		while (true) {
			int x;
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
std::string getcin(std::string) { //not used
		while (true) {
			std::string x;
			std::cin >> x;
			if (!std::cin) {
			std::cin.clear();
			ignoreLine();
		}
		else {
            std::cin.clear();
            ignoreLine();
			return x;
		}
	}
}

int main() {
Person *e;// 
try { e = new Person [c_maxPersonNr]; } 
catch (std::bad_alloc xa) { std::cout << "Allocation Failure" << std::endl; return 1; }

for (int i = 0; i<c_maxPersonNr;i++) {
    for (int ii=0;ii<c_arrayCount;ii++) {
        e[i].setstringdata("Person: ",ii);
        std::string a;
        e[i].setstringdata(e[i].getcin(a,ii),ii);
        a = e[i].getstringdata(ii);
        unsigned long long int b;
        b = e[i].a_stringcharactercount[ii];
        std::cout << a << " PersoNr " << i << "NotizNr " << ii << "NotizAnzahl" << b <<  std::endl;
        }
    }
}

//WRITE BETTER INFO TEXT YOU DIP

//rewrite with classes seems like a prime example for that
//#get(Datatype) get string from console input
//#add to libary
//#save libary && export && dunno there was supposed to stand stomething here
//opendata to access file
//import libary with delimiter " "? "|" "#" "standartisierung mit mockaroo?"
//binary load/save?
//auto txt?
//enum type collection ###notthateasy  to increase
//add person
//remove person
//redo entry
//autotrack PersonID
//switch to take input
//better to input into a window
//increase array
//increase enummeration