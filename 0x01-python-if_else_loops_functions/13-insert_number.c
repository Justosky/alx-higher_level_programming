#include <stdlib.h>
#include "lists.h"

/**
*insert_node - This function adds a newnode to listint_t list and sets value
*it's nth memeber.
*@head: A pointer which points to the pointer that points to the first node.
*@number: The number which we want the new node to contain
*Return: Returns the newnode on success and and NULL on failure
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *Previous, *Current, *NewNode;
	
	NewNode = malloc(sizeof(listint_t));
	
	if (NewNode == NULL)
	{
		return (NULL);
	}
	Current = *head;
	Previous = NULL;
	NewNode->n = number;
	NewNode->next = NULL;

	if ((*head == NULL) || (number < (*head)->n))
	{
		NewNode->next = *head;
		*head = NewNode;
		return (NewNode);
	}
	
	for (; Current != NULL && Current->n <= number ;)
	{
		Previous = Current;
		Current = Current->next;
	}
	Previous->next = NewNode;
	NewNode->next = Current;
	return (NewNode);
}
