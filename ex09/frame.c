#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int get_max_len(char *str)
{
    int max_len = 0;
    int current_len = 0;

    while (*str)
    {
        if (*str == ' ') {
            if (current_len > max_len)
                max_len = current_len;
            current_len = 0;
        }
        else
            current_len++;
        str++;
    }
    if (current_len > max_len)
        max_len = current_len;
    return (max_len);
}

void print_spaces(int n)
{
    while (n--)
        printf(" ");
}

void print_ast(int n)
{
    while (n--)
        printf("*");
    printf("\n");
}

int main(int argc, char **argv)
{
    int max_len;
    int current_len;
    int i;
    char *str;

    if (argc != 2)
        return (EXIT_FAILURE);
    str = strdup(argv[1]);
    max_len = get_max_len(str);
    print_ast(max_len + 4);
    char *token = strtok(str, " ");
    while (token != NULL)
    {
        current_len = strlen(token);
        printf("* %s", token);
        print_spaces(max_len - current_len);
        printf(" *\n");
        token = strtok(NULL, " ");
    }
    print_ast(max_len + 4);
    free(str);
    return (EXIT_SUCCESS);
}
