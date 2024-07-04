clc; close all; clear all;

% Environment Settings
% Map(0: 땅, 1: 벽돌, 2: 도착점, 3: 버그)
global LAND OBS GOAL BUG;
LAND = 0;
OBS = 1;
GOAL = 2;
BUG = 3;

mapSize = linspace(1, 5, 5);
map=zeros(length(mapSize));

% obs
obs=[3 3;
    4 3
    2 3];
map(obs(:, 1), obs(:, 2)) = OBS;

% goal
goal = [3, 5];
map(goal(1), goal(2)) = GOAL;

% bug (x, y, theta)
bug = [2 1 270];
map(bug(1), bug(2)) = BUG;


% Bug 1 Algorithm.
col = 0;                % For Check Collision
shortest_path = [0 0];

MapPlot(map);
pause(0.5);

while true
    if col == 0
        disp("Motion To Go 시작!")
        [map, bug, col] = MotionToGo(map, bug, goal);
    end
    
    if col == 1
        disp("Boundary Following 시작!")
        [map, bug, shortest_path] = BoundaryFollowing1(map, bug, goal);
        [map, bug, col] = BoundaryFollowing2(map, bug, shortest_path);
    end
    
    if col == 2
        break
    end

    
end
disp("도착!")


% Functions
function [map, bug, shortest_path] = BoundaryFollowing1(map, bug, goal)
    global LAND BUG
    original_bug = bug;     % 처음 위치 저장.
    bug(3) = mod(bug(3) + 90, 360);             % 우측으로 방향 전환.
    
    shortest_path = bug(1:2);

    % 바운더리 팔로잉 시작.
    while true
        if norm(goal(1:2) - bug(1:2)) < norm(goal(1:2) - shortest_path)
            shortest_path = bug(1:2);
        end

        % 1-step      
        prevBug = bug;
        [bug, col] = GoForward(bug, map);           % 전진.
        map(prevBug(1), prevBug(2)) = LAND;         % Update the Map.
        map(bug(1), bug(2)) = BUG;
    
        % temp_bug를 통해 기존 방향으로 이동 가능한지 확인
        temp_bug = bug;                             
        temp_bug(3) = original_bug(3);
        [temp_bug, col] = GoForward(temp_bug, map);
        if col == 0                                 % 기존 방향으로 이동 가능하면 bug 방향 돌려놓기.
            bug(3) = original_bug(3);
    
            original_bug(3) = original_bug(3) - 90;   % original_dir 갱신
            if original_bug(3) < 0 
                original_bug(3) = 270;
            end
        end

        MapPlot(map);
        pause(0.5);

        if bug(1:2) == original_bug(1:2)        % Boundary Following을 시작한 첫 위치에 도착하면,
            bug(3) = original_bug(3);           % 처음 상태와 동일하게 만듦.
            break;
        end      
    end
end

function [map, bug, col] = BoundaryFollowing2(map, bug, shortest_path)
    global LAND BUG
    original_bug = bug;
    bug(3) = mod(bug(3) + 90, 360);             % 우측으로 방향 전환.
    
    % 바운더리 팔로잉 시작.
    while true
        % 1-step      
        prevBug = bug;
        [bug, col] = GoForward(bug, map);           % 전진.
        map(prevBug(1), prevBug(2)) = LAND;         % Update the Map.
        map(bug(1), bug(2)) = BUG;
    
        % temp_bug를 통해 기존 방향으로 이동 가능한지 확인
        temp_bug = bug;                             
        temp_bug(3) = original_bug(3);
        [temp_bug, col] = GoForward(temp_bug, map);
        if col == 0                                 % 기존 방향으로 이동 가능하면 bug 방향 돌려놓기.
            bug(3) = original_bug(3);
    
            original_bug(3) = original_bug(3) - 90;   % original_dir 갱신
            if original_bug(3) < 0 
                original_bug(3) = 270;
            end
        end

        MapPlot(map);
        pause(0.5);

        if bug(1:2) == shortest_path
            col = 0;
            break;
        end
    end
end

function [bug, col] = GoForward(bug, map)
    global LAND OBS GOAL
    if bug(3) == 0
        bug(1) = bug(1) + 1;
    elseif bug(3) == 90
        bug(2) = bug(2) - 1;
    elseif bug(3) == 180
        bug(1) = bug(1) - 1;
    elseif bug(3) == 270
        bug(2) = bug(2) + 1;
    end

    if map(bug(1), bug(2)) == LAND
        col = 0;
    elseif map(bug(1), bug(2)) == OBS
        col = 1;
    elseif map(bug(1), bug(2)) == GOAL
        col = 2;
    end
end

function [map, bug, col] = MotionToGo(map, bug, goal)
    global LAND OBS GOAL BUG;
    prevBug = bug;                      % 이전 버그 위치
    
    % Goal을 향한 방향 맞추기
    rel_vec = goal(1:2) - bug(1:2);
    if abs(rel_vec(1)) > abs(rel_vec(2))
        if rel_vec(1) > 0
            bug(3) = 0;
        else
            bug(3) = 180;
        end
    else
        if rel_vec(2) > 0
            bug(3) = 270;
        else
            bug(3) = 90;
        end
    end
   

    [bug, col] = GoForward(bug, map);   % 전진

    if col == OBS
        bug = prevBug;                  % Return to prev state.

    elseif col == LAND
        map(prevBug(1), prevBug(2)) = LAND;        % Update the Map.
        map(bug(1), bug(2)) = BUG;

    elseif col == GOAL
        map(prevBug(1), prevBug(2)) = LAND;        % Update the Map.
        map(bug(1), bug(2)) = BUG;
    end

    MapPlot(map);
    pause(0.5);
end

function MapPlot(map)
    map_image = imresize(map, 40, "nearest");
    imshow(map_image, Colormap=jet);
    caxis([0 3])
    xlabel("Y")
    ylabel("X")
end
