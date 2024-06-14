#include <stdio.h>
#include <stdbool.h>

int main()
{
    // ternary operator
    int age = 21;
    char *can_vote = age >= 18 ? "you can vote!" : "you cannot vote!";

    printf("%s\n", can_vote);
    return 0;
}