#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long CreditCardNumber;

    do
    {
        CreditCardNumber = get_long("Write Credit Card Number: ");
    }
    // negali buti neigiamas skaicius, tai apsibreziam kad teigiami skaiciai
    while (CreditCardNumber <= 0);
// CreditCardNumber ivesta bus pradzioje, bet skaiciavimams naudoti persivadinsiu i siek tiek kitoki pavadinima
    long CreditCard = CreditCardNumber;
    int sum = 0;
    int count = 0;
    long divisor = 0;

//Pradedant nuo galo, gauti kas antra skaiciu. (Liekana % ir dalyba is 100 naudoti ir sumos funkcija) Pasitelkiant liekana gauti paskutini skaiciu, pvz, 1345 % 10 = 5.; dalinam is 100, gaunasi 13 - paskutinis skaitmuo 3; 13/100 gaunasi 0, daugiau skaiciu nera - stop. 5 ir 3 sudedami, gaunasi 8.
    while (CreditCard > 0)
    {
        int a = CreditCard % 10;
        sum = sum + a;
        CreditCard / 100;
    }
// dabar reikia pradeti nuo galo kas antra skaiciu padauginti is dvieju ir susumuoti.Bet su dvizenkliais skaiciais dar reikia padaryti % ir /. Pvz, 15%10, gaunasi 5, 15/10 gaunasi 1. 1+5=6.
CreditCard = CreditCardNumber / 10;
while (CreditCard > 0)
    {
        int a = CreditCard % 10;
        int b = a * 2;
        sum = sum + (b % 10) + (b/10);
        CreditCard / 100;
    }
//skaitmenu numeriui ir pirmiems skaitmenims gauti Visai privalomas pirmas skaitmuo 4 (digits nr 13 arba 16), American express 34 arba 37 (digits nr 15), Master Card 51,52,53,54,55 (digits nr 16)
CreditCard = CreditCardNumber;
while (CreditCard != 0)
{
CreditCard = CreditCard / 10;
count++;
}
for (int i = 0; i < count - 2; i++)
{
 divisor = divisor * 10;
}
int firstDigit = CreditCardNumber / divisor;
int firstTwoDigit = CreditCardNumber / (divisor / 10);
if (sum % 10 == 0)
{
    if (firstDigit == 4 && (count == 13 || count == 16))
    {
printf("Visa\n");
    }
    else if ((firstTwoDigit == 34 || firstTwoDigit ==37) && count == 15)
    {
        printf=("American express\n")
    }
    else if ((firstTwoDigit == 51 || firstTwoDigit == 52 || firstTwoDigit == 53 || firstTwoDigit == 54 || firstTwoDigit == 54) && count 16)
    {
        printf =("Master Card\n");
    }
    else
    {
printf("Invalid\n");
    }
}


}
