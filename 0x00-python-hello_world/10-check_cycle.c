#include "lists.h"

/**
*check_cycle - This function checks if a cycle exists in a listint_t list.
*@list: The listint_t list to be checked if it contains a cycle.
*POINT TO NOTE. a list with a cycle is a list without an end or NULL node
*the end node is pointing to either the first node in the list or to any other
*node in the list. Therefore trasversing the list will form a loop.
*Return: Returns 0 if the list does not contain a cycle and 1 if it does.
*/

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if ((list == NULL) || (list->next == NULL))
	return (0);
	tortoise = list;
	hare = tortoise->next;
	while ((tortoise != NULL) && (hare->next != NULL)
	&& (hare->next->next != NULL))
	{
		if (tortoise == hare)
		return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}
