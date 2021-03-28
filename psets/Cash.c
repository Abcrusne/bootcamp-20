clea
#include <math.h>


int main(void)
{
    float dollars;

    do
    {
        dollars = get_float("Change: ");
    }
    // negali buti neigiamas skaicius pinigu siuo atveju, tai apsibreziam kad teigiami skaiciai
    while (dollars < 0);

// centus pasiversti is doleriu, ir tam kad butu suapvalinti iki artimiausio cento 'round' nes man reikia monetu kieki gauti
    int cents = round(dollars * 100);
    int coins = 0;
//kol galim naudoti 25 tol naudojam, tada 10, tada 5 ir tada 1
    while (cents >= 25)
    {
        cents = cents - 25;
        coins++;
    }
    while (cents >= 10)
    {
        cents = cents - 10;
        coins++;
    }
    while (cents >= 5)
    {
        cents = cents - 5;
        coins++;
    }
    while (cents >= 1)
    {
        cents = cents - 1;
        coins++;
    }
    printf("Coins: %i\n", coins);
}
