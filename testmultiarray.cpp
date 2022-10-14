#include <iostream>
#include <string> //std::stoi
#include <stdlib.h> //uselessleftover
#include <limits>
#include <array>
#include <fstream> //file I O

int i;
int PersonNr = 0;									// Resetting the PersonCount to 0
const int NoteCountCounterMax=2;									
const int ArrayCount = 100;
bool Gender[ArrayCount];							// init of variables
int Age[ArrayCount];
bool Single[ArrayCount];
float Schulden[ArrayCount];							//DELETE LATER
std::string Hobby[ArrayCount];
int NoteC[ArrayCount][NoteCountCounterMax];
std::string Vorname[ArrayCount];
std::string Name[ArrayCount];
std::string Ort[ArrayCount];						//SAVE LOAD MISSING
std::string fAnime[ArrayCount];						//SAVE LOAD MISSING
bool Cosplayer[ArrayCount];							//SAVE LOAD MISSING
std::string fFarbe[ArrayCount];						//SAVE LOAD MISSING
std::string Job[ArrayCount];						//SAVE LOAD MISSING
std::string Mag[ArrayCount];						//SAVE LOAD MISSING
std::string Hass[ArrayCount];						//SAVE LOAD MISSING
bool introextro[ArrayCount];						//SAVE LOAD MISSING
bool shy[ArrayCount];								//SAVE LOAD MISSING
std::string Kontakt[ArrayCount];					//SAVE LOAD MISSING
int scale[ArrayCount];								//SAVE LOAD MISSING
int NoteCountCounter[ArrayCount];
std::string Besonderheit[ArrayCount]; 				// 1
std::string Kompliment[ArrayCount]; 				// 2
std::string Eindruck[ArrayCount];					// 3
std::string Note[ArrayCount]; 		

const std::string DataName = "DataListSL.dat";

std::ifstream bindata;
int transferI;

void OpenIOData() { //loading file for data transfer
	bindata.open(DataName); // opens the file
   		if( !bindata ) { // file couldn't be opened
      		std::cerr << "Error: file could not be opened IO" << std::endl;
   			}
}

auto ImportCharacterSaveFile(int I,int NoteCountCounter) {
	char c;
	std::cout << i << " " << I << std::endl;
	transferI = I;
	 for ( int ii = 0 ; ii <= NoteC[transferI][NoteCountCounter]; ii++ ) {
				if (ii==0) {
				bindata.seekg(+1, std::ios_base::cur);
				}
		bindata.get(c);
		Note[transferI]+=c;
		std::cout << NoteC[transferI][NoteCountCounter] << " Character Count - Import Character File : " << Note[transferI] << std::endl;
	 }
	 std::cout << Note[transferI] << std::endl;
}

void LoadDataBIN() { //loads the data out of an existing data
	OpenIOData();
	bindata >> PersonNr;
	std::cout << "Loading List of " << PersonNr << " Person/s" << std::endl;
	char c;
		for (int I = 1;I<=PersonNr && I<=ArrayCount;I++) {
			std::cout << " Das ist I : " << I << std::endl;						//I echo
		bindata >> Vorname[I] >> Name[I] >> Age[I] >> Gender[I] >> Hobby[I]; //load Data per PersonNr
		for (int iii=0;iii<NoteCountCounterMax;iii++) {
			bindata >> NoteC[I][NoteCountCounter[iii]];
			std::cout << "Das ist der iii : " << iii <<  " Das ist NoteC[I][NoteCounterCoutner[iii]] :" << NoteC[I][NoteCountCounter[iii]] << std::endl;
			ImportCharacterSaveFile(I,NoteCountCounter[iii]);
			NoteCountCounter[iii]+=1;
		}
		}
	bindata.close();
}

int getALOT(int) {
    transferI++;
    return transferI;
}

int main() {
    int i = 1;

    transferI = i;
    i = transferI;
    std::cout << "i ist: " << i << std::endl;
	std::cout << "PersonNr ist: " << PersonNr << std::endl;
	LoadDataBIN();
	for (int I=i;I<=PersonNr;I++) {
	std::cout << Vorname[I] << Name[I] << Age[I] << Gender[I] << Hobby[I] << Note[I] << std::endl;
	}
}