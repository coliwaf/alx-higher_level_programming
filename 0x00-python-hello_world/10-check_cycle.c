#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: List parameter to check
 *
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list, *b = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (b && b->next)
	{
		a = a->next;
		b = b->next->next;

		if (a == b)
			return (1);
	}
	return (0);
}
