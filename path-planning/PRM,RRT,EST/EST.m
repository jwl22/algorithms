clear vars; close all; clc;

%% make space
global wall1 wall2 wall3 wall4 maxX minX maxY minY maxZ minZ scan_range;

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
wall3 = collisionBox(0.3,9,2.5);
wall3.Pose = trvec2tform([0 6 0]);
wall4 = collisionBox(0.3,9,2.5);
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

samples = [endBox; startBox];
samples_init = [startBox];
samples_end = [endBox];
rot = [rot_e; rot_s];
rot_init = [rot_s];
rot_end = [rot_e];
near_init = [0];
near_end = [0];

%% figure
[~,patchObj] = show(startBox);
patchObj.FaceColor = 'g';
hold on
grid on;
view(-10, 30)
xlim([-10,10]);
ylim([-10,10]);
zlim([-5,5]);
xlabel('X');
ylabel('Y');
zlabel('Z');

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
idxs_init = [2];
idxs_end = [1];
threshold = 2;
scan_range = 3;
isend = false;
if norm(startBox.Pose(:,4) - endBox.Pose(:,4)) < scan_range
    near_init = [1];
    near_end = [1];
end

while ~isend
    [~,q_selected_init] = min(near_init);
    [~,q_selected_end] = min(near_end);
    
    % start point tree
    samx=samples_init(q_selected_init).Pose(1,4) + (rand-0.5)*scan_range*2;
    samy=samples_init(q_selected_init).Pose(2,4) + (rand-0.5)*scan_range*2;
    samz=samples_init(q_selected_init).Pose(3,4) + (rand-0.5)*scan_range*2;
    samyaw=rand*2*pi;
    sampitch=rand*2*pi;
    samroll=rand*2*pi;

    Qrand = collisionBox(1,1,3);
    Qrand.Pose = trvec2tform([samx samy samz])*axang2tform([1 0 0 samroll])*axang2tform([0 1 0 sampitch])*axang2tform([0 0 1 samyaw]);

    while norm(Qrand.Pose(:,4) - samples_init(q_selected_init).Pose(:,4)) > scan_range
        samx=samples_init(q_selected_init).Pose(1,4) + (rand-0.5)*scan_range*2;
        samy=samples_init(q_selected_init).Pose(2,4) + (rand-0.5)*scan_range*2;
        samz=samples_init(q_selected_init).Pose(3,4) + (rand-0.5)*scan_range*2;
        Qrand.Pose = trvec2tform([samx samy samz])*axang2tform([1 0 0 samroll])*axang2tform([0 1 0 sampitch])*axang2tform([0 0 1 samyaw]);
    end

    div_count = max(ceil(norm(Qrand.Pose(:,4) - samples_init(q_selected_init).Pose(:,4))) , 1);
    
    betx = (samx-samples_init(q_selected_init).Pose(1,4))/div_count;
    bety = (samy-samples_init(q_selected_init).Pose(2,4))/div_count;
    betz = (samz-samples_init(q_selected_init).Pose(3,4))/div_count;
    betyaw = (samyaw-rot_init(q_selected_init,3))/div_count;
    betpitch = (sampitch-rot_init(q_selected_init,2))/div_count;
    betroll = (samroll-rot_init(q_selected_init,1))/div_count;

    chk_sam = collisionBox(1,1,3);
    tmp = [0 0 0];
    flag = 0;
    for j=1:div_count
        chk_sam.Pose = trvec2tform([samples_init(q_selected_init).Pose(1,4)+j*betx samples_init(q_selected_init).Pose(2,4)+j*bety samples_init(q_selected_init).Pose(3,4)+j*betz]);
        chk_sam.Pose = chk_sam.Pose*axang2tform([1 0 0 rot_init(q_selected_init,1)+j*betroll])*axang2tform([0 1 0 rot_init(q_selected_init,2)+j*betpitch])*axang2tform([0 0 1 rot_init(q_selected_init,3)+j*betyaw]);
        tmp(1) = rot_init(q_selected_init,1)+j*betroll;
        tmp(2) = rot_init(q_selected_init,2)+j*betpitch;
        tmp(3) = rot_init(q_selected_init,3)+j*betyaw;
        if colchk(chk_sam)
            flag = 1;
            break
        end
    end
    if flag ~= 1
        near_count = 0;
        for j=1:length(samples_init)
            if norm(samples_init(j).Pose(:,4) - chk_sam.Pose(:,4))<scan_range
                near_init(j) = near_init(j) + 1;
                near_count = near_count + 1;
            end
        end
        samples_init = [samples_init; chk_sam];
        rot_init = [rot_init; tmp];
        rot = [rot; tmp];
        near_init = [near_init; near_count];
        n1 = [n1; idxs_init(q_selected_init)];
        n2 = [n2; idx];
        weights = [weights; norm(samples_init(j).Pose(:,4) - chk_sam.Pose(:,4))];
        idxs_init = [idxs_init idx];
        
        sampleipos = [chk_sam.Pose(1,4), chk_sam.Pose(2,4), chk_sam.Pose(3,4)];
        samplepos = [samples_init(q_selected_init).Pose(1,4), samples_init(q_selected_init).Pose(2,4), samples_init(q_selected_init).Pose(3,4)];
        sampleline = [samplepos; sampleipos];
        plot3(sampleline(:,1), sampleline(:,2), sampleline(:,3), 'b')
        drawnow

        for i=1:length(samples_end)
            Q = chk_sam.copy;
            div_count = max(ceil(norm(samples_end(i).Pose(:,4) - Q.Pose(:,4))) , 1);
            
            betx = (samples_end(i).Pose(1,4)-Q.Pose(1,4))/div_count;
            bety = (samples_end(i).Pose(2,4)-Q.Pose(2,4))/div_count;
            betz = (samples_end(i).Pose(3,4)-Q.Pose(3,4))/div_count;
            betroll = (rot_end(i,1)-tmp(1))/div_count;
            betpitch = (rot_end(i,2)-tmp(2))/div_count;
            betyaw = (rot_end(i,3)-tmp(3))/div_count;
        
            flag = 0;
            for j=1:div_count
                Q.Pose = trvec2tform([chk_sam.Pose(1,4)+j*betx chk_sam.Pose(2,4)+j*bety chk_sam.Pose(3,4)+j*betz]);
                Q.Pose = Q.Pose*axang2tform([1 0 0 rot_end(i,1)+j*betroll])*axang2tform([0 1 0 rot_end(i,2)+j*betpitch])*axang2tform([0 0 1 rot_end(i,3)+j*betyaw]);
                if colchk(Q)
                    flag = 1;
                    break
                end
            end
            if flag == 0
                sampleipos = [chk_sam.Pose(1,4), chk_sam.Pose(2,4), chk_sam.Pose(3,4)];
                samplepos = [samples_end(i).Pose(1,4), samples_end(i).Pose(2,4), samples_end(i).Pose(3,4)];
                sampleline = [samplepos; sampleipos];
                plot3(sampleline(:,1), sampleline(:,2), sampleline(:,3), 'b')

                n1 = [n1; idxs_end(i)];
                n2 = [n2; idx];
                weights = [weights; norm(samples_end(i).Pose(:,4) - chk_sam.Pose(:,4))];

                drawnow
                
                isend = true;
                break
            end
        end
        
        idx = idx + 1;
        samples = [samples; chk_sam];
    end
    if isend == true
        break
    end
    % end potint tree
    samx=samples_end(q_selected_end).Pose(1,4) + (rand-0.5)*scan_range*2;
    samy=samples_end(q_selected_end).Pose(2,4) + (rand-0.5)*scan_range*2;
    samz=samples_end(q_selected_end).Pose(3,4) + (rand-0.5)*scan_range*2;
    samroll=rand*2*pi;
    sampitch=rand*2*pi;
    samyaw=rand*2*pi;

    Qrand = collisionBox(1,1,3);
    Qrand.Pose = trvec2tform([samx samy samz])*axang2tform([1 0 0 samroll])*axang2tform([0 1 0 sampitch])*axang2tform([0 0 1 samyaw]);

    while norm(Qrand.Pose(:,4) - samples_end(q_selected_end).Pose(:,4)) > scan_range
        samx=samples_end(q_selected_end).Pose(1,4) + (rand-0.5)*scan_range*2;
        samy=samples_end(q_selected_end).Pose(2,4) + (rand-0.5)*scan_range*2;
        samz=samples_end(q_selected_end).Pose(3,4) + (rand-0.5)*scan_range*2;
        Qrand.Pose = trvec2tform([samx samy samz])*axang2tform([1 0 0 samroll])*axang2tform([0 1 0 sampitch])*axang2tform([0 0 1 samyaw]);
    end
    
    div_count = max(ceil(norm(Qrand.Pose(:,4) - samples_end(q_selected_end).Pose(:,4))) , 1);
    
    betx = (samx-samples_end(q_selected_end).Pose(1,4))/div_count;
    bety = (samy-samples_end(q_selected_end).Pose(2,4))/div_count;
    betz = (samz-samples_end(q_selected_end).Pose(3,4))/div_count;
    betyaw = (samyaw-rot_end(q_selected_end,3))/div_count;
    betpitch = (sampitch-rot_end(q_selected_end,2))/div_count;
    betroll = (samroll-rot_end(q_selected_end,1))/div_count;

    chk_sam = collisionBox(1,1,3);
    tmp = [0 0 0];
    flag = 0;
    for j=1:div_count
        chk_sam.Pose = trvec2tform([samples_end(q_selected_end).Pose(1,4)+j*betx samples_end(q_selected_end).Pose(2,4)+j*bety samples_end(q_selected_end).Pose(3,4)+j*betz]);
        chk_sam.Pose = chk_sam.Pose*axang2tform([1 0 0 rot_end(q_selected_end,1)+j*betroll])*axang2tform([0 1 0 rot_end(q_selected_end,2)+j*betpitch])*axang2tform([0 0 1 rot_end(q_selected_end,3)+j*betyaw]);
        tmp(1) = rot_end(q_selected_end,1)+j*betroll;
        tmp(2) = rot_end(q_selected_end,2)+j*betpitch;
        tmp(3) = rot_end(q_selected_end,3)+j*betyaw;
        if colchk(chk_sam)
            flag = 1;
            break
        end
    end
    if flag ~= 1
        near_count = 0;
        for j=1:length(samples_end)
            if norm(samples_end(j).Pose(:,4) - chk_sam.Pose(:,4))<scan_range
                near_end(j) = near_end(j) + 1;
                near_count = near_count + 1;
            end
        end
        samples_end = [samples_end; chk_sam];
        rot_end = [rot_end; tmp];
        rot = [rot; tmp];
        near_end = [near_end; near_count];
        n1 = [n1; idxs_end(q_selected_end)];
        n2 = [n2; idx];
        weights = [weights; norm(samples_end(j).Pose(:,4) - chk_sam.Pose(:,4))];
        idxs_end = [idxs_end idx];
    
        sampleipos = [chk_sam.Pose(1,4), chk_sam.Pose(2,4), chk_sam.Pose(3,4)];
        samplepos = [samples_end(q_selected_end).Pose(1,4), samples_end(q_selected_end).Pose(2,4), samples_end(q_selected_end).Pose(3,4)];
        sampleline = [samplepos; sampleipos];
        plot3(sampleline(:,1), sampleline(:,2), sampleline(:,3), 'b')
        drawnow
        
        for i=1:length(samples_init)
            Q = chk_sam.copy;
            div_count = max(ceil(norm(samples_init(i).Pose(:,4) - Q.Pose(:,4)))*2 , 1);
            
            betx = (samples_init(i).Pose(1,4)-Q.Pose(1,4))/div_count;
            bety = (samples_init(i).Pose(2,4)-Q.Pose(2,4))/div_count;
            betz = (samples_init(i).Pose(3,4)-Q.Pose(3,4))/div_count;
            betroll = (rot_init(i,1)-tmp(1))/div_count;
            betpitch = (rot_init(i,2)-tmp(2))/div_count;
            betyaw = (rot_init(i,3)-tmp(3))/div_count;
        
            flag = 0;
            for j=1:div_count
                Q.Pose = trvec2tform([chk_sam.Pose(1,4)+j*betx chk_sam.Pose(2,4)+j*bety chk_sam.Pose(3,4)+j*betz]);
                Q.Pose = Q.Pose*axang2tform([1 0 0 rot_init(i,1)+j*betroll])*axang2tform([0 1 0 rot_init(i,2)+j*betpitch])*axang2tform([0 0 1 rot_init(i,3)+j*betyaw]);
                if colchk(Q)
                    flag = 1;
                    break
                end
            end
            if flag == 0
                sampleipos = [chk_sam.Pose(1,4), chk_sam.Pose(2,4), chk_sam.Pose(3,4)];
                samplepos = [samples_init(i).Pose(1,4), samples_init(i).Pose(2,4), samples_init(i).Pose(3,4)];
                sampleline = [samplepos; sampleipos];
                plot3(sampleline(:,1), sampleline(:,2), sampleline(:,3), 'b')

                n1 = [n1; idxs_init(i)];
                n2 = [n2; idx];
                weights = [weights; norm(samples_init(i).Pose(:,4) - chk_sam.Pose(:,4))];

                drawnow

                isend = true;
            end
        end
        idx = idx+1;
        samples = [samples; chk_sam];
    end
end
G = graph(n1,n2, weights);
P = shortestpath(G,2,1);
hold off
[~,patchObj] = show(startBox);
patchObj.FaceColor = 'g';
hold on
grid on;
view(-10, 30)
xlim([-10,10]);
ylim([-10,10]);
zlim([-5,5]);
xlabel('X');
ylabel('Y');
zlabel('Z');

[~,patchObj] = show(endBox);
patchObj.FaceColor = 'r';
show(wall1)
show(wall2)
show(wall3)
show(wall4)

smooth = 10;
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

% function m = chk_near(samples, nears)
% % 매번 계산하지 말고 배열에 저장해뒀다가 인근 노드 생성시마다 +1로 업데이트하면 최적화 가능
%     global scan_range
% 
%     [~,idx] = min(nears);
% 
%     q_selected = -1;
%     q_selected_near = length(samples);
% 
%     for i=1:length(samples)
%         near_nodes = 0;
%         for j=1:length(samples)
%             if i == j
%                 continue
%             end
%             if norm(samples(j).Pose(:,4) - samples(i).Pose(:,4)) <= scan_range
%                 near_nodes = near_nodes + 1;
%             end
%         end
%         if near_nodes <= q_selected_near
%             q_selected = i;
%             q_selected_near = near_nodes;
%         end
%     end
%     m = q_selected;
% end