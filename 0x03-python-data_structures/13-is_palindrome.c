#include "lists.h"

/**
 *is_palindrome - checks if a linked list is palindrome
 *@head: linked list
 *
 * Return: 1 on success
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *reversed_list = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	reverse(&reversed_list);
	while (current && reversed_list)
	{
		if (current->n == reversed_list->n)
		{
			reversed_list = reversed_list->next;
			current = current->next;
		}
		else
			return (0);
	}
	return (1);
}
/**
 *reverse - function to reverse alinked list
 *
 *@head: linked list
 */
void reverse(listint_t **head)
{
	listint_t *current = *head, *next = NULL,
		  *prev = NULL;


	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
