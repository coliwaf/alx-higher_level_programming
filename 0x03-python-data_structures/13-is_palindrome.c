#include "lists.h"

/**
 * rev_list - reverses a singly linked list
 * @head: list to reverse
 * Return: pointer to new head
 */
listint_t *rev_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: List parameter
 * Return: 1 if is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *a = *head, *b = *head;

	if (*head == NULL)
		return (1);

	while (b && b->next && b->next->next)
	{
		a = a->next;
		b = b->next->next;
	}

	a = rev_list(&a);
	b = *head;

	while (a && b)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}

	return (1);
}
