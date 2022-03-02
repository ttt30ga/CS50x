#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    int row;
    int spaces;
    int hashes;

    // Ask user for the height value
    do
    {
        height = get_int("Height: ");
    }

    // Accept only positive inputs from 1 to 8
    // If value is not accepted, ask again
    while (height < 1 || height > 8);

    // Loop through accepted value printing hashes and spaces
    for (row = 1; row <= height; row++)
    {
        for (spaces = (height - row); spaces > 0; spaces--)
        {
            printf(" ");
        }
        for (hashes = 1; hashes <= row; hashes++)
        {
            printf("#");
        }
        printf("\n");
    }
};
