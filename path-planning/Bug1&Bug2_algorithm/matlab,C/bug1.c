#include <stdio.h>
// #include <windows.h> // 윈도우
#include <unistd.h> // 리눅스

#define LAND 0
#define OBS 1
#define GOAL 2
#define BUG 3

int MAP[5][5] = {0,};
FILE *fp;

int MAPPlot(int MAP[5][5]);
int* goForward(int *bug);
int motionToGo(int *bug, int *goal);
int* boundaryFollowing1(int *bug, int *goal);
int boundaryFollowing2(int *bug, int *shortest_path);

void dosclear(){
    // system("cls"); // 윈도우
    system("clear"); // 리눅스
}

void dospause(){
    // Sleep(500); // 윈도우
    sleep(1); // 리눅스
}

int main() {
    fp = fopen("bug_history.txt", "w");

    // obs
    int obs_pos[3][2] = {{2,2},{3,2},{1,2}};
    for (int i = 0; i < 3; i++) {
        MAP[obs_pos[i][0]][obs_pos[i][1]] = OBS;
    }

    // goal
    int goal_pos[2] = {2,4};
    MAP[goal_pos[0]][goal_pos[1]] = GOAL;

    // bug (x,y,theta)
    int bug_pos[3] = {1,0,270};
    MAP[bug_pos[0]][bug_pos[1]] = BUG;

    // Bug 1 Algorithm
    int col = 0; // For Check Collision
    int shortest_path[2] = {0,0};
    dosclear();
    MAPPlot(MAP);
    fprintf(fp, "%d %d\n", bug_pos[0], bug_pos[1]);
    dospause();
    
    while (1) {
        if (col == 0) {
            col = motionToGo(bug_pos, goal_pos);
        }

        if (col == 1) {
            int *tmp = boundaryFollowing1(bug_pos, goal_pos); // 한 바퀴 돌면서 가장 가까운 지점 찾기
            shortest_path[0] = tmp[0];
            shortest_path[1] = tmp[1];
            col = boundaryFollowing2(bug_pos, shortest_path); //  가장 가까운 지점으로 이동
        }

        if (col == 2) {
            break;
        }
    }

    printf("도착!\n");
	return 0;
}

int MAPPlot(int MAP[5][5]){
    printf("   0  1  2  3  4\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", i);
        printf("|");
        for (int j = 0; j < 5; j++) {
            if (MAP[i][j] == 0) printf("  ");
            else if (MAP[i][j] == 1) printf("X ");
            else if (MAP[i][j] == 2) printf("G ");
            else if (MAP[i][j] == 3) printf("B ");
            printf("|");
        }
        printf("\n");
    }
    printf("  ￣￣￣￣￣￣￣￣\n\n");
    return 0;
}

int* boundaryFollowing1(int *bug, int *goal) {
    int original_bug[3];
    original_bug[0] = bug[0];
    original_bug[1] = bug[1];
    original_bug[2] = bug[2];
    
    bug[2] = (bug[2] + 90) % 360; // 우측으로 방향 전환.

    int *shortest_path = (int *)malloc(2 * sizeof(int));
    // int shortest_path[2] = {bug[0], bug[1]}; // 골과 가장 가까운 지점
    shortest_path[0] = bug[0];
    shortest_path[1] = bug[1];

    while (1) {
        dosclear();
        MAPPlot(MAP);
        if ((goal[0] - bug[0]) * (goal[0] - bug[0]) + (goal[1] - bug[1]) * (goal[1] - bug[1]) < 
            (goal[0] - shortest_path[0]) * (goal[0] - shortest_path[0]) + 
            (goal[1] - shortest_path[1]) * (goal[1] - shortest_path[1])) {
            shortest_path[0] = bug[0];
            shortest_path[1] = bug[1];
        }
        printf("shortest_path: %d, %d\n", shortest_path[0], shortest_path[1]);
        
        // 1-step
        int *prevBug = malloc(3 * sizeof(int));
        prevBug[0] = bug[0];
        prevBug[1] = bug[1];
        prevBug[2] = bug[2];

        int *result = goForward(bug); // 전진
        bug[0] = result[0];
        bug[1] = result[1];

        fprintf(fp, "%d %d\n", bug[0], bug[1]);
        dospause();

        MAP[prevBug[0]][prevBug[1]] = LAND; // update the MAP
        MAP[bug[0]][bug[1]] = BUG;

        // temp_bug를 통해 기존 방향으로 이동 가능한지 확인
        int temp_bug[3] = {bug[0], bug[1], original_bug[2]};
        int *temp_result = goForward(temp_bug);
        if (temp_result[2] == LAND) { // 기존 방향으로 이동 가능하면 
            bug[2] = original_bug[2]; // 그 방향을 바라보게 하고
            original_bug[2] = (original_bug[2] - 90 + 360) % 360; // original_dir 갱신(grid world로, 90도별로 방향이 분리되어 있음)
        }

        if (bug[0] == original_bug[0] && bug[1] == original_bug[1]) { // Boundary Following을 시작한 첫 위치에 도착하면,
            bug[2] = original_bug[2]; // 처음 상태와 동일하게 만듦.
            break;
        }
    }
    
    dosclear();
    MAPPlot(MAP);
    printf("shortest_path: %d, %d\n", shortest_path[0], shortest_path[1]);
    dospause();

    return shortest_path;

}

int boundaryFollowing2(int *bug, int *shortest_path) {
    int original_bug[3];
    original_bug[0] = bug[0];
    original_bug[1] = bug[1];
    original_bug[2] = bug[2];
    
    bug[2] = (bug[2] + 90) % 360; // 우측으로 방향 전환.

    int col=0;

    while (1) {
        // 1-step
        int *prevBug = malloc(3 * sizeof(int));
        prevBug[0] = bug[0];
        prevBug[1] = bug[1];
        prevBug[2] = bug[2];

        int *result = goForward(bug);
        bug[0] = result[0];
        bug[1] = result[1];
        col = result[2];

        MAP[prevBug[0]][prevBug[1]] = LAND;
        MAP[bug[0]][bug[1]] = BUG;

        // temp_bug를 통해 기존 방향으로 이동 가능한지 확인
        int temp_bug[3] = {bug[0], bug[1], original_bug[2]};
        int *temp_result = goForward(temp_bug);
        if (temp_result[2] == LAND) { // 기존 방향으로 이동 가능하면 bug 방향 돌려놓기.
            bug[2] = original_bug[2];
            original_bug[2] = (original_bug[2] - 90 + 360) % 360; // original_dir 갱신
        }

        dosclear();
        MAPPlot(MAP);
        fprintf(fp, "%d %d\n", bug[0], bug[1]);
        printf("shortest_path: %d, %d\n", shortest_path[0], shortest_path[1]);
        dospause();

        if (bug[0] == shortest_path[0] && bug[1] == shortest_path[1]) {
            col = 0;
            break;
        }
    }

    return col;
}

int motionToGo(int *bug, int *goal) {
    int prevBug[3];
    prevBug[0] = bug[0];
    prevBug[1] = bug[1];
    prevBug[2] = bug[2];

    // Goal을 향한 방향 맞추기
    int rel_vec[2] = {goal[0] - bug[0], goal[1] - bug[1]};
    if (abs(rel_vec[0]) > abs(rel_vec[1])) {
        if (rel_vec[0] > 0) {
            bug[2] = 0;
        } else {
            bug[2] = 180;
        }
    } else {
        if (rel_vec[1] > 0) {
            bug[2] = 270;
        } else {
            bug[2] = 90;
        }
    }

    // 전진
    int *result = goForward(bug);
    bug[0] = result[0];
    bug[1] = result[1];
    int col = result[2];

    if (col == OBS) { // Return to prev state.
        bug[0] = prevBug[0];
        bug[1] = prevBug[1];
    } else { // Update the MAP.
        MAP[prevBug[0]][prevBug[1]] = LAND;
        MAP[bug[0]][bug[1]] = BUG;

        dosclear();
        MAPPlot(MAP);
        fprintf(fp, "%d %d\n", bug[0], bug[1]);
        dospause();
    }

    return col;
}

int* goForward(int *bug) {
    int *result = malloc(3 * sizeof(int));

    if (bug[2] == 0) {
        bug[0]++;
    } else if (bug[2] == 90) {
        bug[1]--;
    } else if (bug[2] == 180) {
        bug[0]--;
    } else if (bug[2] == 270) {
        bug[1]++;
    }

    result[0] = bug[0];
    result[1] = bug[1];

    if (MAP[bug[0]][bug[1]] == LAND) {
        result[2] = 0; // LAND
    } else if (MAP[bug[0]][bug[1]] == OBS) {
        result[2] = 1; // OBS
    } else if (MAP[bug[0]][bug[1]] == GOAL) {
        result[2] = 2; // GOAL
    }

    return result;
}