#include <stdio.h>

int	main(int argc, char **argv)
{
	int	total = 0;
	int	as = 0;

	if (argc != 2)
	{
		printf("Invalid number of arguments.\n");
		return (1);
	}
	while (*argv[1])
	{
		if (*argv[1] == 'J' || *argv[1] == 'Q' || *argv[1] == 'K')
			total += 10;
		else if (*argv[1] == 'A')
		{
			++as;
			total += 11;
		}
		else if (*argv[1] >= '2' && *argv[1] <= '9')
			total += *argv[1] - '0';
		else
		{
			printf("Invalid card: %c\n", *argv[1]);
			return (1);
		}
		argv[1]++;
	}
	while (as > 0 && total > 21)
	{
		total -= 10;
		as--;
	}
	if (total == 21)
		printf("Blackjack!\n");
	else if (total > 21)
		printf("Bust! (Total: %d)\n", total);
	else
		printf("Total: %d\n", total);
}