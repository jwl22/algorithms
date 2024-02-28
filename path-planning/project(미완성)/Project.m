clear; close all; clc;

%% make space
% rot_s = [0 0 0];
% rot_e = [0 0 0];

people1 = collisionBox(1,1,3);
people1.Pose = trvec2tform([-5 -6.5 -3]);
people2 = collisionBox(1,1,3);
people2.Pose = trvec2tform([12 -8.5 -3]);
% startBox.Pose = startBox.Pose*axang2tform([1 0 0 rot_s(1)])*axang2tform([0 1 0 rot_s(2)])*axang2tform([0 0 1 rot_s(3)]);
% endBox = collisionBox(1,1,3);
% endBox.Pose = trvec2tform([8 5 3]);
% endBox.Pose = endBox.Pose*axang2tform([1 0 0 rot_e(1)])*axang2tform([0 1 0 rot_e(2)])*axang2tform([0 0 1 rot_e(3)]);

global walls
walls = [];

createWall(0.3,10,4,[10 -15])
createWall(0.3,15,4,[20 -12.5])
createWall(10,0.3,4,[15 -20])
createWall(4,0.3,4,[18 -10])
createWall(22.5,0.3,4,[1.25 -5])
createWall(5,0.3,4,[17.5 -5])
createWall(12,0.3,4,[6 -10])
createWall(0.3,26,4,[-15 -7])
createWall(0.3,8,4,[-10 -1])
createWall(0.3,9,4,[-10 10.5])
createWall(10,0.3,4,[-15 15])
createWall(5,0.3,4,[-17.5 10])
createWall(5,0.3,4,[-17.5 6])
createWall(0.3,20,4,[17.5 5])
createWall(0.3,20,4,[12.5 5])
createWall(5,0.3,4,[15 15])
createWall(0.3,15,4,[15 2.5])
createWall(3,0.3,4,[-8.5 -10])
createWall(0.3,10,4,[-10 -15])
createWall(0.3,10,4,[-8 -15])
createWall(0.3,10,4,[1 -15])
createWall(0.3,1,4,[-15 9.5])

% samples = [endBox; startBox];
% rot = [rot_s; rot_e];

%% figure   
fig1 = figure;
fig1.Position = [850 100 1000 800];

[~,patchObj] = show(people2);
patchObj.FaceColor = "#FFD0A1";
hold on
view(30,40)
xlim([-20,20]);
ylim([-20,15]);
zlim([-5,5]);
[~,patchObj] = show(people1);
patchObj.FaceColor = "#FFD0A1";

for i=walls
    [~,patchObj] = show(i);
    patchObj.FaceColor = "#FDF5E6";
end

p1_flag = 0.2;
p2_flag = -0.2;
while true
    if people1.Pose(1,4) > 18
        p1_flag = -0.2;
    elseif people1.Pose(1,4) < -13
        p1_flag = 0.2;
    end
    if people2.Pose(1,4) > 18
        p2_flag = -0.2;
    elseif people2.Pose(1,4) < -13
        p2_flag = 0.2;
    end
    hold off
    people1.Pose(1,4) = people1.Pose(1,4) + p1_flag;
    [~,patchObj] = show(people1);
    patchObj.FaceColor = "#FFD0A1";
    hold on
    view(30,40)
    xlim([-20,20]);
    ylim([-20,15]);
    zlim([-5,5]);
    [~,patchObj] = show(people1);
    patchObj.FaceColor = "#FFD0A1";
    
    for i=walls
        [~,patchObj] = show(i);
        patchObj.FaceColor = "#FDF5E6";
    end

    people2.Pose(1,4) = people2.Pose(1,4) + p2_flag;
    [~,patchObj] = show(people2);
    patchObj.FaceColor = "#FFD0A1";

    drawnow
    % pause(0.1)
end


%% wall create function
function createWall(x,y,z, pos)
    global walls

    tmp = collisionBox(x,y,z);
    tmp.Pose = trvec2tform([pos -3]);
    walls = [walls tmp];
end