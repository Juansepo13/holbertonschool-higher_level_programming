#include "lists.h"

/**
 *check_cycle - Checks if a singly linked list has a cycle in it.
 *@list: Linked list.
 *
 *Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *A = list, *B = list;

	while (A != NULL && B != NULL && B->next != NULL)
	{
		A = A->next;
		B = B->next->next;
		if (A == B)
			return (1);
	}

	return (0);
}
