#include <stdio.h>

int main()
{
    printf("Loops in C --------------\n");
    // for loop
    for (int i = 1; i <= 5; i++)
    {
        printf("%d ", i);
    }

    // while loop
    printf("\n\nWhile loop --------------\n");
    int j = 1;

    while (j <= 10)
    {
        printf("%d ", j);
        j++;
    }

    // do-while loop
    printf("\n\nDo-while loop --------------\n");
    int k = 1;

    do
    {
        printf("%d ", k);
        k++;
    } while (k <= 15);

    return 0;
}