#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, row, column, space;
    do
 
  {
      //parasyti auksti 
  
  height = get_int("Height: ");
    }
//aukstis turi buti tarp 1 ir 8, jei nepatenka i sias salygas kartojamas klausimas kol skaicius patenka i sita skaiciaus reiksme

    while (height < 1 || height > 8);

//svarbu kad mano pirma eilute skaitosi 0, tada column yra 0, true, tuomet loop kartojamas vis dar row 0, bet column jau 1, not true, einam prie row 1, column 0, true, kartojam, row 1, column 1, true, kartojam row 1, column 2 not true, einam prie row 2 ir t.t.

    for (row = 0; row < height; row++)
   
    {
    
    // apskaiciuoti tarpus issivesti formule galima space = height - row - 1 (pvz kai height 4: row 0, spaces 3, 1 hash; row 1, spaces 2, 2 hash; row 2, spaces 2, 3 hash; row 3, spaces 0, 4 hash).
    for (space = 0; space < height - row - 1; space++)
   
    {

    printf(" ");

    }
    for (column = 0; column <= row; column++)
     {
         printf("#");
     }
    //konstanta spaces cia dabar, tai yra 2 tarpai ir po tarpu eina hashes, kuriu nereikia alignint i desine todel tik printinu hashes paprastai
     printf("  ");
       for (column = 0; column <= row; column++)
     {

         printf("#");
     }
     printf("\n"); 
  }
}
