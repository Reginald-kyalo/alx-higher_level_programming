#include "lists.h"
/**
 * count_nodes - count number of nodes in a singly linked list
 * @head: pointer to start of head
 *
 * Return: number of nodes, 0 on failure
 */
int count_nodes(listint_t **head)
{
	int size = 0;
	listint_t *node = *head;

	if (node == NULL)
	{
		return (0);
	}
	while (node != NULL)
	{
		size++;
		node = (node->next);
	}
	return (size);
}
/**
 * create_array - creates array containing values in
 * singly linked list
 * @head: start of list
 * @size: number of nodes in list
 *
 * Return: pointer to array, NULL on failure
 */
int *create_array(listint_t **head, int size)
{
	int i = 0;
	int *array = malloc(size * sizeof(int));
	listint_t *node = *head;

	if (node == NULL || array == NULL)
	{
		return (NULL);
	}
	while (i < size)
	{
		array[i] = (node->n);
		i++;
		node = (node->next);
	}
	return (array);
}
/**
 * create_rev_array - creates a reversed version of another array
 * @array: array to be copied in reverse
 * @size: number of nodes
 *
 * Return: pointer to array, NULL on failure
 */
int *create_rev_array(int *array, int size)
{
	int *array_rev = malloc(size * sizeof(int));
	int i = 0;
	int j = size - i;

	if (array == NULL)
	{
		return (NULL);
	}
	while (i < size)
	{
		array_rev[i] = array[j];
		i++;
		j--;
	}
	return (array_rev);
}
/**
 * is_palindrome - checks whether a singly linked list
 * is a palindrome
 * @head: pointer to start of list
 *
 * Return: 1 if found, 0 if no found
 */
int is_palindrome(listint_t **head)
{
	int nodes = count_nodes(head);
	int *array = create_array(head, nodes);
	int *array_rev = create_rev_array(array, nodes);
	int i = 0;

	if (*head == NULL || nodes == 0 || array == NULL || array_rev == NULL)
	{
		return (0);
	}
	while (i < nodes)
	{
		if (array[i] == array_rev[i])
		{
			continue;
		}
		else
		{
			return (1);
		}
		i++;
	}
	return (0);
}
