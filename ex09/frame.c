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

int	main(int argc, char **argv)
{
	int	max_len;

	if (argc != 2)
		return (EXIT_FAILURE);
	max_len = get_max_len(argv[1]);
	// printf("%d\n", get_max_len(argv[1]));
	printf("%d\n", get_len(argv[1]+1));
	printf("%ld\n", strlen(strtok(argv[1]+1, " ")));
}