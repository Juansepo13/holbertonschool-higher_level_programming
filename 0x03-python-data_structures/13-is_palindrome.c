#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to head of node.
 * Return: 0 if it is not a palindrome. 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	unsigned int Lenght = 1;
	listint_t *Iteration;

	if (head == NULL|| *head == NULL)
		return (1);

	Iteration = *head;
	while (Iteration)
	{
		Iteration = Iteration->next;
		Lenght++;
	}
	return (0);
}
