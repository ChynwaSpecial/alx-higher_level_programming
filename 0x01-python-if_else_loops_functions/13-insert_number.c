#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head pointer
 * @number: number to store in the new node
 * Return: new node address, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner;
	listint_t *new_node;

	runner = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new_node->next = runner->next;
			runner->next = new_node;
			return (new_node);
		}
		runner = runner->next;
	}

	new_node->next = NULL;
	runner->next = new_node;
	return (new_node);
}
