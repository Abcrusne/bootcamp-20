#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
//int main(int argc, string argv[])
{
    // user write his/her text
    string s = get_string("Text: ");
    // to count characters, global variable
    int letters = 0;
    // to count spaces, global variable
    int words = 1; // man skaiciavo vienu zodziu maziau negu is tikruju, tai prilyginau 1.
    // to count sentences ! ? .  global variable
    int sentences = 0;
          printf("%c\n",s[0]); //prints output
    for (int i = 0; i < strlen(s); i++)
    {
    if((s[i] >= 'a' && s[i] <= 'z')|| (s[i] >= 'A' && s[i] <= 'Z')) // jei randa raide nuo a ir a iki z ir z arba nuo A ir A ir iki Z ir Z, skaiciuoja ta character'i.
       {
        printf("%c\n",s[i]); //prints output
    letters++;
       }
    else if(s[i]== ' ') //space means one word
       {
    words++; // jei randa tarpa skaiciuoja kaip words +1
       }
    else if((s[i]== '!') || (s[i]== '?') || (s[i]== '.')) // if it is found ! or ? or . it means sentences +1. skaiciuoja kaip viena sakini
       {
        sentences++;
       }
    }
        printf("\n Letters: %i, Words: %i, Sentences: %i\n", letters, words, sentences);
// index = 0.0588 * L - 0.296 * S - 15.8
    float L = (((float)letters * 100) / (float)words);
    float S = (((float)sentences * 100) / (float)words);

    float index = 0.0588 * L - 0.296 * S - 15.8;

    int grade = round(index); // pasiversti, suapvalinti float i integer


    if (grade >= 16)
    {
        printf("Grade: 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 1 || grade < 16)
    {
        printf("Grade: %i\n", grade);
    }
}
