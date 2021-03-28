#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
bool KeyValidity (string s);              //apsibreziu funkcija, kuri bus skirta isiaiskint ar parasytas key is valid, t.y. ar isdigit

int main(int argc, string argv[])         // apsibreziu funkcija

{
    if (argc != 2 || !KeyValidity(argv[1]))                        // mums reikia dvieju argumentu todel reikia patikrinti (./caesar ir key ), todel argc turi buti 2;  (argc - argumentai, argv zenklai tu argumentu)
    {
        printf("Usage: ./caesar key\n");
        return (1);                      //(jeigu return zero program end, )
    }

        int key = atoi(argv[1]);       // savo key convertuoju is string i integer

        string plaintext = get_string("plaintext: ");

        printf("ciphertext: ");
        for (int i = 0, len = strlen(plaintext); i < len; i++)
        {

            if(isalpha(plaintext[i]))  //kad paimtu character'i ir ar tai alpha ar ne, (galima pasirasyti char a = plaintext[a])
            {
              char a = 'A' ;
              if (islower(plaintext[i]))
              a = 'a';
              
              printf("%c", (plaintext[i] - a + key) % 26 + a); // formule tokia: ci = (pi + k) % 26, bet pridedu dar 'a', nes pagal ASCII a yra 65, o man reikia 0, tai pvz jei key 1: (65-65 + 1) % 26 + 65 = (0 + 1) % 26 + 65 = 1+65 = 66. 66 yra B.
            }

            else

                printf("%c", plaintext[i]);
        }
  printf ("\n");
 }
 
  bool KeyValidity (string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
        if (!isdigit(s[i]))
            return false;
    return true;
}
