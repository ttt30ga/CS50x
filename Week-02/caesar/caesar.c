#import <stdio.h>
#import <cs50.h>
#import <ctype.h>
#import <string.h>
#import <stdlib.h>

int main(int argc, string argv[])
{
    // Ask user for the key and make sure is a digit
    // * is a pointer to access argv[1] - without it the program doesn't work
    if (argc == 2) // && isdigit(*argv[1])
    {
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            // Returns error message if key includes anything other than digits
            if (isdigit(argv[1][i]) == false)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        // Ask user for text
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");

        int k = strlen(plaintext);
        int key = atoi(argv[1]);

        // Reads plaintext and converts it to ciphertext
        for (int i = 0; i < k; i++)
        {
            if (islower(plaintext[i]))
            {
                printf("%c", ((((plaintext[i] - 'a') + key) % 26) + 'a'));
            }
            else if (isupper(plaintext[i]))
            {
                printf("%c", ((((plaintext[i] - 'A') + key) % 26) + 'A'));
            }
            else
            {
                printf("%c", plaintext[i]);
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
