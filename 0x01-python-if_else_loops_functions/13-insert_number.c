#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - Inserts a number into a sorted singly linked list.
 *@head: Head of the Linked List.
 *@number: Value of the new node.
 *Return: Address of the new node. NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nwnmbr;
	listint_t *top;

	top = *head;
	nwnmbr = malloc(sizeof(listint_t));
	if (nwnmbr == NULL)
		return (NULL);
	nwnmbr->n = number;
	nwnmbr->next = NULL;
	if (*head == NULL || top->n > nwnmbr->n)
	{
		nwnmbr->next = *head;
		*head = nwnmbr;
		return (nwnmbr);
	}
	while (top->next != NULL)
	{
		if ((top->next->n > nwnmbr->n && top->n < nwnmbr->n)
		    || nwnmbr->n == top->n)
		{
			nwnmbr->next = top->next;
			top->next = nwnmbr;
			return (nwnmbr);
		}
		top = top->next;
	}
	nwnmbr->next = top->next;
	top->next = nwnmbr;
	return (nwnmbr);
}
