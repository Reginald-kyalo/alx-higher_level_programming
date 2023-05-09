#include "lists.h"
/**
 * check_cycle - checks for a cysle in a singly linked list
 * @lists: lsit of type listint_t
 *
 * Return: 0 no cycles found, 1 if found
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *test = list;

	while (current != NULL && test->next != NULL && test != NULL)
	{
		current = current->next;
		test = test->next->next;
		if (test == current)
			return (1);
	}
	return (0);
}
