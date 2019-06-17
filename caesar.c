#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int conv(int, int, int);


int main(int argc, string argv[])
{
// Counting Command-Line Arguments and checking if all numbers
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n"); 
        return 1;
    }
    else
    {
        string input =  argv[1];  
        int len = strlen(input), i = 0;
        int num_check = 0;        //  0 - true, 1 - false
        while (i < len)
        {
            if ((isdigit(input[i]) == 0) && (input[i] != 0))
            {
                num_check = 1;
            }
            i++;
        }
        if (num_check != 0)
        {
            return 1;
        }
    }
//ask for plain text----------       
    string text = get_string("plaintext:  ");
    // printf("\n");
// make ciphertext
    int key = atoi(argv[1]);
    printf("ciphertext: ");
    for (int j = 0, m = strlen(text); j < m; j++)
    {
        int i = text[j];  
        //for big letters
        if ((i >= 'A') && (i <= 'Z'))
        {
            i = conv(i, key, 65);         
        }
        //for small letters
        else if ((i >= 'a') && (i <= 'z'))
        {
            i = conv(i, key, 97);       
        }
//print ciphertext char
        text[j] = i;
        //printf("%i %c |", text[j],text[j] );
        printf("%c", text[j]);
        
    }
    printf("\n");
    return 0;
}

//function - convert to alphabetical
int conv(int i, int k, int step)
{
    int a = i - step;
    a = (a + k) % 26;
    i = a + step;  
    return i;  
}
