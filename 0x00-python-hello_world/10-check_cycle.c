#include "lists.h"
/**
 *check_cycle - funciton to check if the linked list has 
 a cycle using  Floyd's cycle detection algorithm.
 *
 *@list: linked list
 *Return: 0 if there is no cycle, or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !(list->next))
		return (0);

	slow = list;
	fast = list->next;
	
	while(slow != NULL && fast != NULL && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
