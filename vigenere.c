#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int conv(int, int, int);


int main(int argc, string argv[])
{
// Counting Command-Line Arguments and checking if all letters  
    if (argc != 2)
    {
        printf("Usage: ./vigenere keyword\n"); 
        return 1;
    }
    else
    {
        string input =  argv[1];  
        int i = 0, key_len; 
        key_len = strlen(argv[1]);
        int keyword[key_len];
        while (i < key_len)
        {
            if ((isalpha(input[i]) == 0))
            {
                printf("Usage: ./vigenere keyword\n"); 
                return 1;
            }
            //if letter convert to lovercase
            else
            {
                keyword[i] = tolower(input[i]);
            }          
            i++;
        }
        
        //ask for plain text----------       
        string text = get_string("plaintext:  ");
        // make ciphertext
        printf("ciphertext: ");
        for (int j = 0, m = strlen(text); j < m; j++)
        {
            int key;  
            int k = text[j];  
            //for big letters
            if ((k >= 'A') && (k <= 'Z'))
            {
                key = keyword[j % key_len] - 'a';
                k = conv(k, key, 'A');         
            }
            //for small letters
            else if ((k >= 'a') && (k <= 'z'))
            {
                key = keyword[j % key_len] - 'a';
                k = conv(k, key, 'a');       
            }
            //print ciphertext char
            text[j] = k;
            printf("%c", text[j]);

        }
        printf("\n");
    }

    return 0;
}

//function - convert to alphabetical
int conv(int i, int k, int step) //i - value in [], k - key current value, step - translation from ASCII to alphabet
{
    int a = i - step;
    a = (a + k) % 26;               
    i = a + step;  
    return i;  
}
