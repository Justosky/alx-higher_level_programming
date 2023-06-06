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
		listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

		if (new_node == NULL)
		{
			return (NULL);
		}
		new_node->n = number;
		new_node->next = NULL;

		if (*head == NULL || number < (*head)->n)
		{
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}
}
