#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

int main(int argc, string argv[])         // apsibreziu funkcija

{
    if (argc != 2)                        // mums reikia dvieju argumentu todel reikia patikrinti (./substitution ir key ), todel argc turi buti 2;  (argc - argumentai, argv zenklai tu argumentu)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    for (int i = 0, len = strlen(argv[1]); i < len; i++)
        if (!isalpha(argv[1][i]))
        {
            printf("Key must contain only alphabetics.\n");
            return 1;
        }
        
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");


    //  for (int i = 0, len = strlen(argv[1]); i < len; i++)

}