function q_output = one_step(q_input)
    global tspan
    %% Phase1 : Unlocked Knee Model
    % input : q0 = [qST qTW qSW dqST dqTW dqSW]'
    % output : q = [qST qTW qSW dqST dqTW dqSW]'
    options=odeset('events',@Event_Kneestrike);
    [t,q] = ode15s(@Dyn_Unlocked_Swing, tspan, q_input, options);
   

    %% Phase2 : Knee Strike
    % input : q0 = [qST qTW qSW dqST dqTW dqSW]'
    % output q_ = [dqST dqSW]'
    q0 = q(end,:);
    q_ = Dyn_Knee_Strike(q0);

    %% Phase3 : Locked Knee Model
    % input : q0 = [qST qSW dqST dqSW]'
    % output : q = [qST qSW dqST dqSW]'
    q0 = [q(end,1), q(end,3), q_(1), q_(2)]';
    options=odeset('events',@Event_Heelstrike);
    [t,q] = ode15s(@Dyn_Locked_Swing, tspan, q0, options);

    %% Phase4 : Heel Strike
    % input : q0 = [qST qSW dqST dqSW]'
    % output : dq_plus = [dqST dqSW vFTx vFTy]'
    q0 = q(end, :);
    dq_plus = Dyn_Heel_Strike(q0);

    %% Swap Leg
    % input : q(end,:) = [qST qSW dqST dqSW]'
    % input : dq_ext = [dqST dqSW vCx vCy]'
    % output : q0 = [qSW qST qST dqSW dqST dqST]'
    q_output = [q(end,2), q(end,1), q(end,1), dq_plus(2), dq_plus(1), dq_plus(1)]';
    
end