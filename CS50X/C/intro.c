#include <stdio.h>
#include <stdlib.h>

void print_blocks();

int main(void)
{
    print_blocks();
}

void print_blocks()
{
    int blocks;
    int max_blocks = 100;
    int min_blocks = 2;

    do
    {
        // system("clear"); // for unix systems
        printf("How many blocks would you like to print? ");
        scanf("%d", &blocks);

        if (blocks < min_blocks)
        {
            printf("Please enter a number greater than %i.\n", min_blocks);
        }
        else if (blocks > max_blocks)
        {
            printf("Please enter a number less than %i.\n", max_blocks);
        }
    } while (blocks < min_blocks || blocks > max_blocks);

    // print a square of blocks
    for (int i = 0; i < blocks; i++)
    {
        for (int j = 0; j < blocks; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}