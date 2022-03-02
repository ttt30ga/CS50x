#include "helpers.h"
#include "stdio.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through height - rows
    for (int i = 0; i < height; i++)
    {
        // Loop through width - columns
        for (int j = 0; j < width; j++)
        {
            // Store RGB values
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            // Avarage RGB values
            int avarage = round((r + g + b) / 3.0);

            // Assign RGB rounded values
            image[i][j].rgbtRed = avarage;
            image[i][j].rgbtGreen = avarage;
            image[i][j].rgbtBlue = avarage;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through height - rows
    for (int i = 0; i < height; i++)
    {
        // Loop through width - columns
        for (int j = 0; j < width; j++)
        {
            // Store RGB values
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            // Convert RGB to sepia
            int sepiaR = round((r * 0.393) + (g * 0.769) + (b * 0.189));
            int sepiaG = round((r * 0.349) + (g * 0.686) + (b * 0.168));
            int sepiaB = round((r * 0.272) + (g * 0.534) + (b * 0.131));

            // Assign RGB rounded values
            if (sepiaR > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = sepiaR;
            }

            if (sepiaG > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = sepiaG;
            }

            if (sepiaB > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = sepiaB;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through height - rows
    for (int i = 0; i < height; i++)
    {
        // Loop through width - columns
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE newImage[height][width];

    // Loop through height - rows
    for (int i = 0; i < height; i++)
    {
        // Loop through width - columns
        for (int j = 0; j < width; j++)
        {
            newImage[i][j] = image[i][j];
        }
    }

    // Loop through height - rows
    for (int i = 0; i < height; i++)
    {
        // Loop through width - columns
        for (int j = 0; j < width; j++)
        {
            float r = 0;
            float g = 0;
            float b = 0;
            float counter = 0;

            // Loop through row top and bottom of the current row
            for (int k = -1; k <= 1 ; k++)
            {
                // Loop through column left and right of the current column
                for (int l = -1; l <= 1; l++)
                {
                    // Create frame
                    if (i + k != -1 &&
                        i + k != height &&
                        j + l != -1 &&
                        j + l != width)
                    {
                        // Sum colors
                        r += newImage[i + k][j + l].rgbtRed;
                        g += newImage[i + k][j + l].rgbtGreen;
                        b += newImage[i + k][j + l].rgbtBlue;

                        // Count the number of pixels sorrounding a single pixel
                        counter++;
                    }
                    // Assign new value
                    image[i][j].rgbtRed = round(r / counter);
                    image[i][j].rgbtGreen = round(g / counter);
                    image[i][j].rgbtBlue = round(b / counter);
                }
            }
        }
    }
    return;
}
