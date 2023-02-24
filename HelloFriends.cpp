/*basically a addressbook with weird questions to fill in, all to learn a bit of c++*/

#include <iostream>
#include <string> //std::stoi
#include <stdlib.h> //uselessleftover
#include <limits>
#include <array>
#include <fstream> //file I O

const int ArrayCount = 1000; 	// init of variable arraycount / arbitrary count this would be better with a flexible array std#array
const int NoteCountCounterMax = 5; 
const std::string DataName = "DataListSL.dat"; //dataname
const std::string ReadableTXT = "ReadableData.txt"; //dataname readable
int PersonNr = 0;									// Resetting the PersonCount to 0
bool Gender[ArrayCount];							// init of variables
int Age[ArrayCount];
bool Single[ArrayCount];
int PersonNrEntryChange;
int PersonNrOld;
float Schulden[ArrayCount];							//DELETE LATER
std::string Hobby[ArrayCount];
int NoteC[ArrayCount][NoteCountCounterMax];
std::string Vorname[ArrayCount];
std::string Name[ArrayCount];
std::string Ort[ArrayCount];						
bool Cosplayer[ArrayCount];							
std::string fFarbe[ArrayCount];						
std::string Job[ArrayCount];						
std::string Mag[ArrayCount];						
std::string Hass[ArrayCount];						
bool introextro[ArrayCount];						
bool shy[ArrayCount];					
std::string Kontakt[ArrayCount];					
int scale[ArrayCount];								
int NoteCountCounter[ArrayCount];
int auskunft;										//
std::string fAnime[ArrayCount];						
std::string Besonderheit[ArrayCount]; 				// 
std::string Kompliment[ArrayCount]; 				// 
std::string Eindruck[ArrayCount];					//
std::string Note[ArrayCount]; 						//

enum NoteNumber
{
	AnimeNote,BesoNote,KompNote,EindNote,NotizNote
};

std::ofstream outdata;
std::ofstream boutdata;
std::ifstream bindata;


 void ignoreLine()  //CIN Error Correction, Ignore Line
{
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}
void PrintStr(std::string x) { std::cout << x; }
void Print(std::string x) { std::cout << x << std::endl; }
void PrintArrVar(std::string x, auto y)
{
	std::cout << x << " " << y << std::endl;
}
void PrintArrVar(std::string x, bool check, std::string TypeA, std::string TypeB)
{
	PrintStr(x);
	if (check==true) PrintStr(TypeA);
	else PrintStr(TypeB);
	std::cout << std::endl;
}

void ListPerson() { //List funcation
	for (int i = 1;i<=PersonNr;i++) { auskunft=0;
		std::cout << i << std::endl;
		std::cout << "PersonNr:" << i << "/" << PersonNr << std::endl;
		std::cout << "Name:" << Vorname[i] << ", " << Name[i] << std::endl;
		PrintArrVar("Age:", Age[i]);
		PrintArrVar("Gender: ", Gender[PersonNr], "Female", "Male");
		PrintArrVar("Hobby:",Hobby[i]);
		PrintArrVar("Wohnort:",Ort[i]);
		std::cout << "Favorit Anime: " << fAnime[i] << std::endl;
		std::cout << "Charcount Note: " << NoteC[i][4] << std::endl;
		std::cout << "Favorit Color: " << fFarbe[i] << std::endl;
		if (Cosplayer[PersonNr]==true) { std::cout << "Cosplayer" << std::endl;} else { std::cout << "No Cosplayer" << std::endl;}
		if (shy[PersonNr]==true) { std::cout << "Shy" << std::endl;} else { std::cout << "Not Shy" << std::endl; }
		if (introextro[PersonNr]==true) { std::cout << "Introvertiert" << std::endl;} else { std::cout << "Extrovertiert" << std::endl;}
		if (Single[PersonNr]==true) { std::cout << "Single" << std::endl; } else { std::cout << "Taken" << std::endl;}
		std::cout << "Job: " << Job[i] << std::endl;
		std::cout << "Mag: " << Mag[i] << std::endl;
		std::cout << "Hass: " << Hass[i] << std::endl;
		std::cout << "Skala 1-10: " << scale[i] << std::endl;
		std::cout << "Kontakt: " << Kontakt[i] << std::endl;
		std::cout << "Note: " << Note[i] << std::endl; 
		std::cout << "Charcount Note: " << NoteC[i][0] << std::endl;
		std::cout << "Kompliment: " << Kompliment[i] << std::endl;
		std::cout << "Charcount Note: " << NoteC[i][1] << std::endl;
		std::cout << "Besonderheit: " << Besonderheit[i] << std::endl;
		std::cout << "Charcount Note: " << NoteC[i][2] << std::endl;
		std::cout << "Eindruck: " << Eindruck[i] << std::endl;
		std::cout << "Charcount Note: " << NoteC[i][3] << std::endl;
	}
}
void SaveListPerson() { //save List in readable State
	for (int i = 1;i<=PersonNr && i<=ArrayCount;i++) {
		outdata << i << std::endl;
		outdata << "PersonNr:" << i << "/" << PersonNr << std::endl;
		outdata << "Name:" << Vorname[i] << ", " << Name[i] << std::endl; 
		outdata << "Age:" << Age[i] << std::endl;
		outdata << "Gender: ";
		if (Gender[PersonNr]==true) { outdata << "Female" << std::endl;} else { outdata << "Male" << std::endl;}
		outdata << "Hobby: " << Hobby[i] << std::endl;
		outdata << "Wohnort: " << Ort[i] << std::endl;
		outdata << "Favorit Anime: " << fAnime[i] << std::endl;
		outdata << "Charcount Note: " << NoteC[i][4] << std::endl;
		outdata << "Favorit Color: " << fFarbe[i] << std::endl;
		if (Cosplayer[PersonNr]==true) { outdata << "Cosplayer" << std::endl;} else { outdata << "No Cosplayer" << std::endl;}
		if (shy[PersonNr]==true) { outdata << "Shy" << std::endl;} else { outdata << "Not Shy" << std::endl; }
		if (introextro[PersonNr]==true) { outdata << "Introvertiert" << std::endl;} else { outdata << "Extrovertiert" << std::endl;}
		if (Single[PersonNr]==true) { outdata << "Single" << std::endl; } else { outdata << "Taken" << std::endl;}
		outdata << "Job: " << Job[i] << std::endl;
		outdata << "Mag: " << Mag[i] << std::endl;
		outdata << "Hass: " << Hass[i] << std::endl;
		outdata << "Skala 1-10: " << scale[i] << std::endl;
		outdata << "Kontakt: " << Kontakt[i] << std::endl;
		outdata << "Note: " << Note[i] << std::endl; 
		outdata << "Charcount Note: " << NoteC[i][0] << std::endl;
		outdata << "Kompliment: " << Kompliment[i] << std::endl;
		outdata << "Charcount Note: " << NoteC[i][1] << std::endl;
		outdata << "Besonderheit: " << Besonderheit[i] << std::endl;
		outdata << "Charcount Note: " << NoteC[i][2] << std::endl;
		outdata << "Eindruck: " << Eindruck[i] << std::endl;
		outdata << "Charcount Note: " << NoteC[i][3] << std::endl;
	}
	outdata.close();
}

void SaveListPersonBin() { 																																//save list serialized
	for (int i = 1;i<=PersonNr && i<=ArrayCount;i++) {
		if (i<=1) { boutdata << PersonNr << ' '; } 																										//save PersonNr once
		boutdata 	<< Vorname[i] << ' ' 
					<< Name[i] << ' ' 
					<< Age[i] << ' ' 
					<< Gender[i] << ' ' 
					<< Hobby[i] << ' ' 
					<< Ort[i] << ' ' 
					<< Cosplayer[i] << ' ' 
					<< fFarbe[i] << ' ' 
					<< Job[i] << ' ' 
					<< Mag[i] << ' '
					<< Hass[i] << ' '
					<< introextro[i] << ' '
					<< shy[i] << ' '
					<< Kontakt[i] << ' '
					<< scale[i] << ' '
					<< Single[i] << ' ';

			for ( int iii=0; iii<NoteCountCounterMax;iii++) {
			boutdata << NoteC[i][iii] << ' ';			//save Data per PersonNr
				if (iii==AnimeNote) {
					boutdata << fAnime[i];
				}
				else if (iii==NotizNote) {						//note
					boutdata << Note[i];
				}
				else if (iii==EindNote) {						//eindruck
					boutdata << Eindruck[i];
				}
				else if (iii==KompNote) {						//kompliment
					boutdata << Kompliment[i];
				}
				else if (iii==BesoNote) {		
					boutdata << Besonderheit[i];
				}
				else {
							std::cout << "Error SLPB 1/NoteCounter Overflow" << std::endl;
				}
			}
		}
		
	boutdata.close();
}

void OpenIOData() { //loading file for data transfer
	bindata.open(DataName); // opens the file
   		if( !bindata ) { // file couldn't be opened
      		std::cerr << "Error: file could not be opened IO" << std::endl;
   			}
}

auto ImportCharacterSaveFile(int i,int NoteCountCounter) {
	char c;
	std::cout << NoteC[i][NoteCountCounter] << " <-#NoteC | i" << i << " NoteCountCounter -> " << NoteCountCounter << std::endl;
	 for ( int ii = 0 ; ii <= NoteC[i][NoteCountCounter]; ii++ ) {
		std::cout << ii << " <- ii | i -> "  << i << std::endl;
				if (ii==0) {
				bindata.seekg(+1, std::ios_base::cur);
				}
			std::cout << NoteC[i][NoteCountCounter] << " NoteC <- | -> NoteCountCounter " << NoteCountCounter << std::endl;
			bindata.get(c);
				if (NoteCountCounter==4) {
							fAnime[i]+=c;
				}
				else if (NoteCountCounter==3) {						//note
							Note[i]+=c;
							std::cout << Note[i] << " Note" << std::endl;
				}
				else if (NoteCountCounter==2) {						//eindruck
							Eindruck[i]+=c;
							std::cout << Eindruck[i] << " Eindruck" << std::endl;
				}
				else if (NoteCountCounter==1) {						//kompliment
							Kompliment[i]+=c;
							std::cout << Kompliment[i] << " Kompliment" << std::endl;
				}
				else if (NoteCountCounter==0) {		
							Besonderheit[i]+=c;
							std::cout << Besonderheit[i] << " Besonderheit" << std::endl;
				}
				else {
							std::cout << "Fucking what?" << std::endl;
				}
	 }
	 std::cout << i << ' ' << NoteCountCounter << " test" << std::endl;
}

void LoadDataBIN() { //loads the data out of an existing data
	OpenIOData();
	bindata >> PersonNr;
	std::cout << "Loading List of " << PersonNr << " Person/s" << std::endl;
	char c;
		for (int i = 1;i<=PersonNr && i<=ArrayCount;i++) {
			std::cout << " Das ist i: " << i << std::endl;
		bindata >> Vorname[i] 
				>> Name[i]
				>> Age[i] 
				>> Gender[i] 
				>> Hobby[i] //save Data per PersonNr
				>> Ort[i] 
				>> Cosplayer[i]
				>> fFarbe[i]
				>> Job[i] 
				>> Mag[i]
				>> Hass[i]
				>> introextro[i]
				>> shy[i]
				>> Kontakt[i] 
				>> scale[i]
				>> Single[i];
				NoteCountCounter[i]=0;													//reset NoteCountCounter to 0 so Import Character 
			for (int iii=0;iii<NoteCountCounterMax;iii++) {
				bindata >> NoteC[i][iii];
				std::cout << NoteC[i][iii] << "  iii ist : " << iii << " i ist:" << i << " NoteCountCounteriii ist : " << NoteCountCounter[i] << std::endl;
				ImportCharacterSaveFile(i,iii);
				NoteCountCounter[i]+=1;
			}
		}
	bindata.close();
}

void OpenDataTXT() { //opens data for a readable save
	outdata.open(ReadableTXT); // opens the file
   		if( !outdata ) { // file couldn't be opened
      		std::cerr << "Error: file could not be opened TXT" << std::endl;
   			}
}

void OpenDataBIN() { //data as I/O variant
	boutdata.open(DataName); // opens the file
   		if( !boutdata ) { // file couldn't be opened
      		std::cerr << "Error: file could not be opened" << std::endl;
   			}
}

float getFloat() {	//get Float
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
char getChar() {	//get Integer
		while (true) {
			char x;
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
int getInt() {	//get Integer
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
bool getBoo() { //boolean check
	char b;
	std::cout << "'T'rue/'F'alse" << std::endl; //
	b = getChar();
	switch (b) {

		case 'T':
		case 't':
			return true;
			break;
		case 'F':
		case 'f':
			return false;
			break;
	}
}
std::string getStr() { //get String
		while (true) {
			std::string x;
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
auto getTxt(int i) { //get String text
		while (true) {
			std::string x;					//set x as string for later return	
			std::getline (std::cin,x); 		//read line for text
			NoteC[PersonNr][i] = x.length(); 	//write char count in NoteC
            if (!std::cin) {
			std::cin.clear();
			ignoreLine();
		}
		else {
			ignoreLine();
			std::cout << NoteC[PersonNr][i] << ' ' << PersonNr << ' ' << NoteCountCounter[PersonNr] << ' ' << i << std::endl;
			return x+' ';
		}
		}
}

int addNewPerson() { //Adding a New Person to the Array
		std::cout << "Adding new person: PersonNr:" << PersonNr << std::endl;	
		std::cout << "Vorname:" << std::endl;
		Vorname[PersonNr] = {getStr()};
		std::cout << "Name:" << std::endl;
		Name[PersonNr] = {getStr()};
		std::cout << "Alter:" << std::endl;
		Age[PersonNr] = {getInt()};
		std::cout << "Wohnort:" << std::endl;
		Ort[PersonNr] = {getStr()};
		std::cout << "Favorite Anime:" << std::endl;
		fAnime[PersonNr] = {getTxt(4)};
		std::cout << "Job:" << std::endl;
		Job[PersonNr] = {getStr()};
		std::cout << "Mag:" << std::endl;
		Mag[PersonNr] = {getStr()};
		std::cout << "Hass:" << std::endl;
		Hass[PersonNr] = {getStr()};
		std::cout << "Introverted(T) or Extroverted?(F):" << std::endl;
		introextro[PersonNr] = {getBoo()};
		std::cout << "Shy? Yes='T' No='F' :" << std::endl;
		shy[PersonNr] = {getBoo()};
		std::cout << "Kontakt:" << std::endl;
		Kontakt[PersonNr] = {getStr()}; 
		std::cout << "Scale 1-10:" << std::endl;
		scale[PersonNr] = {getInt()}; 
		std::cout << "Mann='F'/Frau='T'" << std::endl;
		Gender[PersonNr] = {getBoo()};
		std::cout << "Hobby:" << std::endl;
		Hobby[PersonNr] = {getStr()};
		std::cout << "Single? 'T'=Ja 'F'=Nein" << std::endl;
		Single[PersonNr] = {getBoo()};
		std::cout << "Cosplayer? 'T'=Ja 'F'=Nein" << std::endl;
		Cosplayer[PersonNr] = {getBoo()};
		std::cout << "Lieblings Farbe?" << std::endl;
		fFarbe[PersonNr] = {getStr()};
		std::cout << "Besonderheit:" << std::endl;
		Besonderheit[PersonNr] = {getTxt(0)};
		std::cout << "Kompliment:" << std::endl;
		Kompliment[PersonNr] = {getTxt(1)};
		std::cout << "Eindruck:" << std::endl;
		Eindruck[PersonNr] = {getTxt(2)};
		std::cout << "Notiz:" << std::endl;
		Note[PersonNr] = {getTxt(3)};
		return 0;
}

void addNewPersonEntry() {
		PersonNr++;
		addNewPerson();
}

void changePersonEntry() {
	Print("Welche Personal Nummer soll neu erfasst werden?");
	PersonNrEntryChange = getInt();
	PersonNrOld = PersonNr;
	PersonNr = PersonNrEntryChange;
	addNewPerson();
	PersonNr = PersonNrOld;
}

int main() {

	jump:	
	char b;
	Print("'E'ntry/E'n'd/'L'ist/'S'ave/'O'pen/'R'e-Entry"); //read input
	b = getChar();

	switch (b) { //read, input, end switch
	
	case 'e':
	case 'E':  //new entry
		addNewPersonEntry();
		goto jump;
	
	case 'n':
	case 'N':  //exit
		 break;
		 
	case 'l':
	case 'L':
		ListPerson(); //show list
		goto jump;

	case 's':
	case 'S': //save
		std::cout << "Saving" << std::endl;
		ListPerson();
		OpenDataTXT();
		SaveListPerson();
		OpenDataBIN();
		SaveListPersonBin(); 
		goto jump;
	
	case 'o':
	case 'O':
		std::cout << "Loading"	<< std::endl;
		LoadDataBIN();
		goto jump;

	case 'r':
	case 'R':
		changePersonEntry();
		goto jump;

	default: //error
		std::cout << "Wrong Input" << std::endl;
		ignoreLine();
		std::cin.clear();
		goto jump; 
	}	

}