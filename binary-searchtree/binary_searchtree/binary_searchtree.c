#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct anod * Ty_Node_Ptr;
typedef struct anod  
{ 	
	char sno[10]; 		
	char name[50];  	
	Ty_Node_Ptr leftChild, rightChild;  
} Ty_Node;

void print(Ty_Node *S, int l);
int insert(Ty_Node **node, Ty_Node *tmp);
void Del(Ty_Node **node, char name[]);
void print_node(Ty_Node *node);
int getheight(Ty_Node *node);
int getleafcount(Ty_Node *node);
Ty_Node *Search(Ty_Node *tree, char *name);

int levelcount;

int main()
{
	FILE *f;
	Ty_Node *S, *tmp, *find;
	tmp = NULL;
	char csno[10];
	char name[50];
	fopen_s(&f, "sdata.txt", "r");
	if (f == NULL)
	{
		printf("������ �����ϴ�.\n");
		return 1;
	}
	S = NULL;
	while (fscanf(f, "%s", csno) != EOF)
	{
		tmp = (Ty_Node*)malloc(sizeof(Ty_Node));
		strcpy(tmp->sno , csno);
		tmp->leftChild = NULL;
		tmp->rightChild = NULL;
		fscanf(f, "%s", tmp->name);
		insert(&S, tmp);
	}
	fclose(f);

	char A[5];
	while (1)
	{
		printf("������ �۾��� (in, sp, de, se, ht, ch, le, ex) ? ");
		scanf("%s", A);
		if (strcmp(A, "ex") == 0) 
		{
			printf("���α׷��� �����մϴ�.\n");
			break;
		}
		else if (strcmp(A, "in") == 0)
		{
			tmp = (Ty_Node*)malloc(sizeof(Ty_Node));
			tmp->leftChild = NULL;
			tmp->rightChild = NULL;
			scanf("%s %s", tmp->sno, tmp->name);
			int re = insert(&S, tmp);
			if (re == 1)
			{
				levelcount = 0;
				Search(S, tmp->name);
				printf("�Է� ����! level = %d\n", levelcount);
			}
			else if (re == 0)
				printf("�Է� ����!\n");
		}
		else if (strcmp(A, "sp") == 0)
		{
			printf("ȭ���� ������ ������ �����ϴ� : \n");
			print(S, 1);
		}
		else if (strcmp(A, "de") == 0)
		{
			scanf("%s", name);
			Del(&S, name);
		}
		else if (strcmp(A, "se") == 0)
		{
			levelcount = 0;
			scanf("%s", name);
			find = Search(S, name);
			if (find != NULL)
				printf("�й�: %s �̸�: %s ��巹��: %d\n", find->sno, find->name, levelcount);
			else
				printf("���� ���Դϴ�.\n");
		}
		else if (strcmp(A, "ht") == 0)
			printf("height = %d\n", getheight(S));
		else if (strcmp(A, "ch") == 0)
		{
			scanf("%s", name);
			find = Search(S, name);
			if (find != NULL)
			{
				if (find->leftChild->name == NULL || find->leftChild == NULL)
				{
					find ->leftChild;
					strcpy(find->leftChild->name, "NULL");
				}
				if (find->rightChild->name == NULL || find->rightChild == NULL)
				{
					find->rightChild;
					strcpy(find->leftChild->name, "NULL");
				}
				printf("left child = %s, right child = %s\n", find->leftChild->name, find->rightChild->name);
			}
			else
				printf("���� ���Դϴ�.\n");
		}
		else if (strcmp(A, "le") == 0)
			printf("number of leaf nodes = %d\n", getleafcount(S));
		else
			printf("�������� �ʴ� ����Դϴ�.\n");
	}

	return 0;
}

int insert(Ty_Node **node, Ty_Node *tmp)
{
	struct anod *cur;
	if (*node == NULL)
	{
		*node = tmp;
		return 1;
	}
	cur = *node;
	if (strcmp(cur->name, tmp->name) == 0)
	{
		cur->leftChild->name, NULL;
		cur->rightChild->name, NULL;
		return 0;
	}
	else if (strcmp(cur->name, tmp->name) < 0)
	{
		if (cur->leftChild != NULL)
			insert(&cur->leftChild, tmp);	//return���� if���� ���� warning�޽����� ������ ����Լ��̹Ƿ� �������ٰ� ������.
		else
		{
			cur->leftChild = tmp;
			cur-> rightChild->name, NULL;
			return 1;
		}
	}
	else
	{
		if (cur->rightChild != NULL)
			insert(&cur->rightChild, tmp);	//return���� if���� ���� warning�޽����� ������ ����Լ��̹Ƿ� �������ٰ� ������.
		else
		{
			cur->rightChild = tmp;
			cur->leftChild->name, NULL;
			return 1;
		}
	}
}

void print(Ty_Node *S, int l)
{
	if (!S) return;
	print(S->rightChild, l + 1);
	print_node(S);
	print(S->leftChild, l + 1);
}
void print_node(Ty_Node *node)
{
	printf("%s %s\n", node->name, node->sno);
}

Ty_Node *Search(Ty_Node *tree, char *name)
{
	if (tree == NULL)
		return NULL;
	if (!strcmp(tree->name, name))
		return tree;
	else if (strcmp(tree->name, name) > 0)
	{
		levelcount++;
		return Search(tree->rightChild, name);
	}
	else
	{
		levelcount++;
		return Search(tree->leftChild, name);
	}
}

void Del(Ty_Node **node, char name[])
{
	bool found = false;
	if (*node == NULL)
	{
		printf("Ʈ���� �������� �ʽ��ϴ�. \n");
		return;
	}
	Ty_Node* curr;
	Ty_Node* parent = NULL;
	curr = *node;
	while (curr != NULL)
	{
		if (strcmp(curr->name, name) == 0)
		{
			found = true;
			break;
		}
		else
		{
			parent = curr;
			if (strcmp(curr->name, name) < 0)
				curr = curr->leftChild;
			else
				curr = curr->rightChild;
		}
	}
	if (!found)
	{
		printf("�������� �ʴ� ���Դϴ�.\n");
		return;
	}
	if ((curr->leftChild == NULL && curr->rightChild != NULL) || (curr->leftChild != NULL) && (curr->rightChild == NULL))
	{
		if (curr->leftChild == NULL && curr->rightChild != NULL)
		{
			if (parent->leftChild == curr)
			{
				parent->leftChild = curr->rightChild;
				printf("���������� �����Ǿ����ϴ�. %s�� ��ġ ������ �Ͼ.\n", curr->rightChild->name);
				free(curr);
			}
			else
			{
				parent->rightChild = curr->rightChild;
				printf("���������� �����Ǿ����ϴ�. %s�� ��ġ ������ �Ͼ.\n", curr->rightChild->name);
				free(curr);
			}
		}
		else
		{
			if (parent->leftChild == curr)
			{
				parent->leftChild = curr->leftChild;
				printf("���������� �����Ǿ����ϴ�. %s�� ��ġ ������ �Ͼ.\n", curr->leftChild->name);
				free(curr);
			}
			else
			{
				parent->rightChild = curr->leftChild;
				printf("���������� �����Ǿ����ϴ�. %s�� ��ġ ������ �Ͼ.\n", curr->leftChild->name);
				free(curr);
			}
		}
		return;
	}
	if (curr->leftChild == NULL && curr->rightChild == NULL)
	{
		if (parent->leftChild == curr)
			parent->leftChild = NULL;
		else
			parent->rightChild = NULL;
		printf("���������� �����Ǿ����ϴ�. ��ġ������ �Ͼ�� �ʾҽ��ϴ�.\n");
		free(curr);
		return;
	}
	if (curr->leftChild != NULL && curr->rightChild != NULL)
	{
		Ty_Node* chkr;
		chkr = curr->rightChild;
		if ((chkr->leftChild == NULL) && (chkr->rightChild == NULL))
		{
			curr = chkr;
			printf("���������� �����Ǿ����ϴ�. %s�� ��ġ ������ �Ͼ.\n", chkr->name);
			free(chkr);
			curr->rightChild = NULL;
		}
		else 
		{
			if ((curr->rightChild)->leftChild != NULL)
			{
				Ty_Node* lcurr;
				Ty_Node* lcurrp;
				lcurrp = curr->rightChild;
				lcurr = (curr->rightChild)->leftChild;
				while (lcurr->leftChild != NULL)
				{
					lcurrp = lcurr;
					lcurr = lcurr->leftChild;
				}
				printf("���������� �����Ǿ����ϴ�. %s�� ��ġ ������ �Ͼ.\n", lcurr->name);
				strcpy(curr->sno, lcurr->sno);
				strcpy(curr->name, lcurr->name);
				free(lcurr);
				lcurrp->leftChild = NULL;
			}
			else
			{
				Ty_Node* tmp;
				tmp = curr->rightChild;
				printf("���������� �����Ǿ����ϴ�. %s�� ��ġ ������ �Ͼ.\n", tmp->name);
				strcpy(curr->sno, tmp->sno);
				strcpy(curr->name, tmp->name);
				curr->rightChild = tmp->rightChild;

				free(tmp);
			}
		}
		return;
	}
}

int getheight(Ty_Node *node)
{
	int left = 0, right = 0;
	if (NULL == node)
		return 0;
	if (node->leftChild)
		left = getheight(node->leftChild);
	if (node->rightChild)
		right = getheight(node->rightChild);

	return 1 + ((left > right) ? left : right);
}

int getleafcount(Ty_Node *node)
{
	int count = 0;
	if (node != NULL)
	{
		if (node->leftChild == NULL && node->rightChild == NULL) return 1;
		else
			count = getleafcount(node->leftChild) + getleafcount(node->rightChild);
	}
	return count;
}