#import <stdio.h>
#import <cs50.h>
#import <string.h>
#import <ctype.h>
#import <math.h>

int main(void)
{
    // Ask user for text
    string text = get_string("Text: ");
    int str = strlen(text);

    // Store letters, words, sentences
    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; i < str; i++)
    {
        // If text is alphabetical and isn't '\0' count as letter
        if (isalpha(text[i]) && text[i] != '\0')
        {
            letters++;
        }
        // If text is space count as word
        if (text[i] == ' ')
        {
            words++;
        }
        // If text is .?! count as sentence
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    // printf("Total letters: %i\n", letters);
    // printf("Total words: %i\n", words);
    // printf("Total sentences: %i\n", sentences);

    float L = ((float)letters / (float)words) * 100;
    float S = ((float)sentences / (float)words) * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade_index = round(index);

    if (grade_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade_index);
    }
}
