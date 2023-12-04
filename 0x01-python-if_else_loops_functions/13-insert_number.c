#include "lists.h"
/**
 *listint_t - function that inserts a number into a sorted singly linked list.
 *
 *@head: pointer to pointer of first node of listint_t list
 *@number: integer to be included in new node
 *Return: addres of the new element or null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || new->n < current->n)
	{
		new->next = current;
	  	return (*head = new); 
	}
	else
	{
		while (current->next != NULL && current->next->n < number)
			current = current->next;
		
		new->n = number;
		new->next = current->next; 
		current->next = new;
	}
return (new);	
}
