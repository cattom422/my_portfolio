#include "helpers.h"
#include<math.h>
//rgbtBlue
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0;i<height;i++)
    {
        for (int j=0;j<width;j++)
        {
            image[i][j].rgbtRed=image[i][j].rgbtGreen
            =image[i][j].rgbtBlue=(image[i][j].rgbtRed
            +image[i][j].rgbtGreen+image[i][j].rgbtBlue)/3;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0;i<height;i++)
    {
        for (int j=0;j<(width-width%2)/2;j++)
        {
            RGBTRIPLE temp=image[i][j];
            image[i][j]=image[i][width-1-j];
            image[i][width-1-j]=temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_new[height][width];
    for (int i=0;i<height;i++)
    {
        for (int j=0;j<width;j++)
        {
            int num=0;
            int Blue=0;
            int Green=0;
            int Red=0;
            for (int h=-1;h<2;h++)
            {
                for (int w=-1;w<2;w++)
                {
                    if (i+h>=0 && i+h<=height-1 &&
                    j+w>=0 && j+w<=width-1)
                    {
                        Blue+=image[i+h][j+w].rgbtBlue;
                        Green+=image[i+h][j+w].rgbtGreen;
                        Red+=image[i+h][j+w].rgbtRed;
                        num++;
                    }
                }
            }
            Blue/=num;
            Green/=num;
            Red/=num;
            image_new[i][j].rgbtBlue=(uint8_t) Blue;
            image_new[i][j].rgbtGreen=(uint8_t) Green;
            image_new[i][j].rgbtRed=(uint8_t) Red;
        }
    }
    //image=image_new;//仅为指针
    for (int i=0;i<height;i++)
    {
        for (int j=0;j<width;j++)
        {
            image[i][j]=image_new[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_new[height][width]; // New image to store the edge-detected values
    int kernel_x[3][3] = {{1, 2, 1}, {0, 0, 0}, {-1, -2, -1}}; // Sobel Gx kernel
    int kernel_y[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}}; // Sobel Gy kernel

    // Loop through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize the gradient sums for each channel
            int Blue_x = 0, Blue_y = 0;
            int Green_x = 0, Green_y = 0;
            int Red_x = 0, Red_y = 0;

            // Loop over the 3x3 grid around the pixel
            for (int h = -1; h <= 1; h++)
            {
                for (int w = -1; w <= 1; w++)
                {
                    // Check if the neighboring pixel is within image bounds
                    if (i + h >= 0 && i + h < height && j + w >= 0 && j + w < width)
                    {
                        // Get the RGB values of the neighboring pixel
                        RGBTRIPLE pixel = image[i + h][j + w];

                        // Apply the Sobel Gx and Gy kernels for each color channel
                        Blue_x += pixel.rgbtBlue * kernel_x[h + 1][w + 1];
                        Blue_y += pixel.rgbtBlue * kernel_y[h + 1][w + 1];

                        Green_x += pixel.rgbtGreen * kernel_x[h + 1][w + 1];
                        Green_y += pixel.rgbtGreen * kernel_y[h + 1][w + 1];

                        Red_x += pixel.rgbtRed * kernel_x[h + 1][w + 1];
                        Red_y += pixel.rgbtRed * kernel_y[h + 1][w + 1];
                    }
                }
            }

            // Calculate the magnitude of the gradients for each channel
            int Blue = round(sqrt(Blue_x * Blue_x + Blue_y * Blue_y));
            int Green = round(sqrt(Green_x * Green_x + Green_y * Green_y));
            int Red = round(sqrt(Red_x * Red_x + Red_y * Red_y));

            // Clamp values between 0 and 255
            if (Blue > 255)
                Blue = 255;
            if (Green > 255)
                Green = 255;
            if (Red > 255)
                Red = 255;

            // Store the calculated values in the new image
            image_new[i][j].rgbtBlue = (uint8_t)Blue;
            image_new[i][j].rgbtGreen = (uint8_t)Green;
            image_new[i][j].rgbtRed = (uint8_t)Red;
        }
    }

    // Copy the new image back into the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = image_new[i][j];
        }
    }
    return;
}
