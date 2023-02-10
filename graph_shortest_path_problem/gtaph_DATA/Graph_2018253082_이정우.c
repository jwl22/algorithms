#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define Max_vertex 12
#define TRUE 1
#define FALSE 0

double COST[Max_vertex][Max_vertex]; // 비용정보를 가지는 인접행렬 표현.
double distance[Max_vertex];  // 알고리즘이 사용하는 거리정보.
int pred[Max_vertex];   // 선행자 정보. 
int set_S[Max_vertex]; // 각 원소마다 0 은 해당 정점이 S 에 들어있지 않음을, 1 은 들어있음을 나타낸다.

void Read_and_make_graph(char *f_name);
void initialize_cost();
int shortest_path(int start, int destination);
int choose(double dis[], int found[]);

int main()
{
	int s, d;
	char Ch[50];
	strcpy(Ch, "graphdata.txt");
	initialize_cost();
	Read_and_make_graph(Ch);
	//int i, j;
	//for (i = 0; i < Max_vertex; i++)
	//{
	//	for (j = 0; j < Max_vertex; j++)
	//		printf("%lf ", COST[i][j]);
	//	printf("\n");
	//}
	do {
		printf("최소경로를 찾을 두 정점을 입력하시오>  ");
		scanf("%d %d", &s, &d);
		if ((s == -1 || d == -1))
			break;
		if (s < -1 || d < -1 || s>11 || d>11)
		{
			printf("0~11범위로 입력해주십시오.\n");
			continue;
		}
		if (s == d)
		{
			printf("같은 정점을 입력하셨습니다.\n");
			continue;
		}
		shortest_path(s, d);
	} while (1);
	printf("  프로그램을 종료합니다.");

	return 0;
}

void initialize_cost()
{
	int i, j;
	for (i = 0; i < Max_vertex; i++)
		for (j = 0; j < Max_vertex; j++)
			COST[i][j] = -1;
}

void Read_and_make_graph(char *f_name)
{
	FILE *f;
	fopen_s(&f, f_name, "r");
	if (!f)
	{
		printf("파일 읽기 에러.\n");
		getchar();
	}
	char line[500];
	char str[10];
	char *r;
	int i, j, l, nr, num, v, dv;
	double cost;

	r = fgets(line, 500, f);
	if (!r)
	{
		printf("라인 읽기 에러.\n");
		getchar();
	}
	nr = sscanf(line, "%d", &num);
	if (nr != 1)
	{
		printf("읽기 에러.\n");
		getchar();
	}
	do {
		r = fgets(line, 500, f);
		if (!r)
			break;
		l = strlen(line);
		i = 0;
		while (i < l && line[i] == ' ')
			i++;
		j = 0;
		while (i < l&&line[i]!=' ')
		{
			str[j] = line[i];
			i++; j++;
		}
		str[j] = '\0';
		v = atoi(str);

		do {
			while (i < l && line[i] == ' ')
				i++;
			if (i >= l)
				break;
			j = 0;
			while (i < l&& line[i] != ' ')
			{
				str[j] = line[i];
				i++; j++;
			}
			str[j] = '\0';
			dv = atoi(str);

			j = 0;
			while (i < l && line[i] == ' ')
				i++;
			while (i < l && line[i] != ' ')
			{
				str[j] = line[i];
				i++; j++;
			}
			str[j] = '\0';
			cost = atof(str);

			COST[v][dv] = cost;
		} while (1);
	} while (1);
	fclose(f);
}

int shortest_path(int start, int destination)
{
	int i, u, w, count, tm = 0, save[Max_vertex];
	for (i = 0; i < Max_vertex; i++)
	{
		save[i] = -1;
		set_S[i] = FALSE;
		distance[i] = 99999;
		pred[i] = start;
	}
	distance[start] = 0;
	pred[start] = -1;

	for (count = 0; count < Max_vertex - 1; count++)
	{
		u = choose(distance, set_S);
		set_S[u] = TRUE;
		for (w = 0; w < Max_vertex; w++)
			if (!set_S[w] && COST[u][w] != -1 && distance[u] != 99999 && distance[u] + COST[u][w] < distance[w])
			{
				distance[w] = distance[u] + COST[u][w];
				pred[w] = u;
			}
	}
	int j = destination;
	do {
		j = pred[j];
		save[tm] = j;
		tm++;
	} while (j != start);
	printf("경로: ");
	printf("%d, ", start);
	for (i = tm - 2; i >= 0; i--)
		printf("%d, ", save[i]);
	printf("%d  ", destination);
	printf("총비용: %g \n", distance[destination]);
	return 0;
}

int choose(double dis[], int found[])
{
	int i, minpos;
	double min = 100000;
	minpos = -1;

	for (i = 0; i < Max_vertex; i++)
	{
		if (dis[i] <= min && !found[i])
		{
			min = dis[i];
			minpos = i;
		}
	}
	return minpos;
}