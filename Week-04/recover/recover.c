#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int BLOCK_SIZE = 512;
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Ask user for arg
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open file
    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 2;
    }

    // Create buffer
    BYTE buffer[BLOCK_SIZE];

    // Count images found;
    int img_count = 0;
    char filename[8];
    FILE *new_file = NULL;

    // Loop through each block
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (img_count != 0)
            {
                fclose(new_file);
            }
            sprintf(filename, "%03i.jpg", img_count); // Write new jpg file
            new_file = fopen(filename, "w"); // Open the new created file
            img_count++;
        }

        // Write new image
        if (img_count != 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, new_file);
        }
    }

    // Close files
    fclose(file);
    fclose(new_file);
}
