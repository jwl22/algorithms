clear vars; close all; clc;

%% make space
global wall1 wall2 wall3 wall4 maxX minX maxY minY maxZ minZ;

rot_s = [0 0 0];
rot_e = [0 0 0];

startBox = collisionBox(1,1,3);
startBox.Pose = trvec2tform([-8 0 0]);
startBox.Pose = startBox.Pose*axang2tform([1 0 0 rot_s(1)])*axang2tform([0 1 0 rot_s(2)])*axang2tform([0 0 1 rot_s(3)]);
endBox = collisionBox(1,1,3);
endBox.Pose = trvec2tform([8 5 3]);
endBox.Pose = endBox.Pose*axang2tform([1 0 0 rot_e(1)])*axang2tform([0 1 0 rot_e(2)])*axang2tform([0 0 1 rot_e(3)]);
wall1 = collisionBox(0.3,20,4);
wall1.Pose = trvec2tform([0 0 3]);
wall2 = collisionBox(0.3,20,4);
wall2.Pose = trvec2tform([0 0 -3]);
wall3 = collisionBox(0.3,9,5);
wall3.Pose = trvec2tform([0 6 0]);
wall4 = collisionBox(0.3,9,5);
wall4.Pose = trvec2tform([0 -6 0]);
maxZ = collisionBox(20,20,0.1);
maxZ.Pose = trvec2tform([0 0 5]);
minZ = collisionBox(20,20,0.1);
minZ.Pose = trvec2tform([0 0 -5]);
maxX = collisionBox(0.1,20,20);
maxX.Pose = trvec2tform([-10 0 0]);
minX = collisionBox(0.1,20,20);
minX.Pose = trvec2tform([10 0 0]);
maxY = collisionBox(20,0.1,20);
maxY.Pose = trvec2tform([0 10 0]);
minY = collisionBox(20,0.1,20);
minY.Pose = trvec2tform([0 -10 0]);

samples = [startBox; endBox];
rot = [rot_s; rot_e];

%% figure
figure;
view(-10, 30)
xlim([-10,10]);
ylim([-10,10]);
zlim([-5,5]);
xlabel('X');
ylabel('Y');
zlabel('Z');
hold on
grid on;

[~,patchObj] = show(startBox);
patchObj.FaceColor = 'g';
[~,patchObj] = show(endBox);
patchObj.FaceColor = 'r';
show(wall1)
show(wall2)
show(wall3)
show(wall4)

% node = [];
n1 = [];
n2 = [];
weights = [];

%% sampling
idx = 3;
while true
    samx=(rand-0.5)*20;
    samy=(rand-0.5)*20;
    samz=(rand-0.5)*10;
    samyaw=rand*2*pi;
    sampitch=rand*2*pi;
    samroll=rand*2*pi;

    sample = collisionBox(1,1,3);
    sample.Pose = trvec2tform([samx samy samz])*axang2tform([1 0 0 samroll])*axang2tform([0 1 0 sampitch])*axang2tform([0 0 1 samyaw]);

    if colchk(sample)
        delete(sample)
        continue
    else
        % node = [node; sample.Pose(1) sample.Pose(2) sample.Pose(3)];
        nodenum = 1;
        for i=1:length(samples)
            chk_sam = sample.copy;
            div_count = 20;
            betx = (samples(i).Pose(1,4) - chk_sam.Pose(1,4))/div_count;
            bety = (samples(i).Pose(2,4) - chk_sam.Pose(2,4))/div_count;
            betz = (samples(i).Pose(3,4) - chk_sam.Pose(3,4))/div_count;
            betyaw = (rot(i,3) - samyaw)/div_count;
            betpitch = (rot(i,2) - sampitch)/div_count;
            betroll = (rot(i,1) - samroll)/div_count;

            flag = 0;
            for j=1:div_count
                chk_sam.Pose = trvec2tform([chk_sam.Pose(1,4)+betx chk_sam.Pose(2,4)+bety chk_sam.Pose(3,4)+betz]);
                chk_sam.Pose = chk_sam.Pose*axang2tform([1 0 0 samroll+j*betroll])*axang2tform([0 1 0 sampitch+j*betpitch])*axang2tform([0 0 1 samyaw+j*betyaw]);
                % chk_sam.Pose(1,4) = chk_sam.Pose(1,4) + betx;
                % chk_sam.Pose(2,4) = chk_sam.Pose(2,4) + bety;
                % chk_sam.Pose(3,4) = chk_sam.Pose(3,4) + betz;
                % chk_sam.Pose = chk_sam.Pose*axang2tform([1 0 0 betroll])*axang2tform([0 1 0 betpitch])*axang2tform([0 0 1 betyaw]);
                if colchk(chk_sam)
                    flag = 1;
                    break
                end
            end
            if flag==0
                n1 = [n1 idx];
                n2 = [n2 nodenum];
                weights = [weights norm(sample.Pose(:,4)-samples(i).Pose(:,4))];

                sampleipos = [samples(i).Pose(1,4), samples(i).Pose(2,4), samples(i).Pose(3,4)];
                samplepos = [sample.Pose(1,4), sample.Pose(2,4), sample.Pose(3,4)];
                sampleline = [samplepos; sampleipos];
                plot3(sampleline(:,1), sampleline(:,2), sampleline(:,3), 'b')
                drawnow
            end
            delete(chk_sam)
            nodenum = nodenum + 1;
        end
        samples = [samples; sample];
        rot = [rot; samroll sampitch samyaw];

        % [~,patchObj] = show(sample);
        % patchObj.FaceColor = 'g';
        idx = idx + 1;
    end
    G = graph(n1,n2,weights);
    P = shortestpath(G,1,2);
    if P
        cla;
        [~,patchObj] = show(startBox);
        patchObj.FaceColor = 'g';
        [~,patchObj] = show(endBox);
        patchObj.FaceColor = 'r';
        show(wall1)
        show(wall2)
        show(wall3)
        show(wall4)
        break
    end
end

smooth = div_count;
for i=2:length(P)
    cur_idx = i-1;
    betx = (samples(P(i)).Pose(1,4) - samples(P(cur_idx)).Pose(1,4))/smooth;
    bety = (samples(P(i)).Pose(2,4) - samples(P(cur_idx)).Pose(2,4))/smooth;
    betz = (samples(P(i)).Pose(3,4) - samples(P(cur_idx)).Pose(3,4))/smooth;
    betroll = (rot(P(i),1) - rot(P(cur_idx),1))/smooth;
    betpitch = (rot(P(i),2) - rot(P(cur_idx),2))/smooth;
    betyaw = (rot(P(i),3) - rot(P(cur_idx),3))/smooth;

    startBox.Pose = trvec2tform([samples(P(cur_idx)).Pose(1,4) samples(P(cur_idx)).Pose(2,4) samples(P(cur_idx)).Pose(3,4)]);
    % rot(P(cur_idx),3) + betyaw*smooth
    for j=1:smooth
        startBox.Pose = trvec2tform([startBox.Pose(1,4)+betx startBox.Pose(2,4)+bety startBox.Pose(3,4)+betz]);
        startBox.Pose = startBox.Pose*axang2tform([1 0 0 rot(P(cur_idx),1)+j*betroll])*axang2tform([0 1 0 rot(P(cur_idx),2)+j*betpitch])*axang2tform([0 0 1 rot(P(cur_idx),3)+j*betyaw]);
        % startBox.Pose(1,4) = startBox.Pose(1,4) + betx;
        % startBox.Pose(2,4) = startBox.Pose(2,4) + bety;
        % startBox.Pose(3,4) = startBox.Pose(3,4) + betz;
        % startBox.Pose = startBox.Pose*axang2tform([1 0 0 betroll])*axang2tform([0 1 0 betpitch])*axang2tform([0 0 1 betyaw]);
        [~,patchObj] = show(startBox);
        patchObj.FaceColor = 'g';
        patchObj.FaceAlpha = 0.3;
        drawnow
        pause(0.1)
    end
end

function re = colchk(sample)
    global wall1 wall2 wall3 wall4 maxX maxY maxZ minX minY minZ;

    if ~checkCollision(sample, wall1) && ~checkCollision(sample, wall2) && ~checkCollision(sample, wall3) && ~checkCollision(sample, wall4)...
            && ~checkCollision(sample, maxZ) && ~checkCollision(sample, minZ) && ~checkCollision(sample, maxX) && ~checkCollision(sample, minX)...
            && ~checkCollision(sample, maxY) && ~checkCollision(sample, minY)
        re = false;
    else
        re = true;
    end
end