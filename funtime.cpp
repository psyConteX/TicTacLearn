#include <iostream>
int berechneStunde(int x, int y) {
    int z = y - x;
    return z;
}
float berechneFahrtkosten(int fahrzeugtyp,int tarifart,int gefahreneStrecke,int startzeit,int endezeit) {
    float km_preis;
    float gesamtkosten;
    float stundenpreis;
    float km_kosten;
    float zeitkosten;
    switch(fahrzeugtyp) {
    case 1:
        km_preis = 0.22;
        stundenpreis = 2.20;
        break;
    case 2:
        km_preis = 0.26;
        stundenpreis = 2.80;
        break;
    case 3:
        km_preis = 0.33;
        stundenpreis = 4.20;
        break;
    default: std::cout << "Error" << std::endl;
    };
    int benutzteZeit = berechneStunde(startzeit,endezeit);
    km_kosten=km_preis*gefahreneStrecke;
    zeitkosten=benutzteZeit*stundenpreis;
    gesamtkosten=km_kosten+zeitkosten;
    if (tarifart) gesamtkosten=gesamtkosten*0.8;
    return gesamtkosten;
}
int calca3() {
    int i = 0;
    int z = 0;
    while (i<20) {
        int j = i;
        while (j<20) {
            z+=j;
            j++;
            std::cout << " i= " << i << " z= " << z << " j= " << j << std::endl;
        }
        i+=5;
    }
    return z;
}


int main() {
    float gesamtkosten = berechneFahrtkosten(3,1,200,8,18);
    std::cout << "Hier ist das ergebniss: " << gesamtkosten << std::endl;
    int A3 = calca3();
    std::cout << "Die Antwort ist: " << A3 << std::endl;

}