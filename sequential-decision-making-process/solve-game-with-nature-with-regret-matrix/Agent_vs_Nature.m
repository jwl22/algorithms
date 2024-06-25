close all; clc; clear

P_theta = [1/5 1/5 3/5];

nonD_samples = randsample([1 -1 0], 1000, true, [1/5 1/5 3/5]);
prob_samples = randsample([-1 2 -2], 1000, true, [1/5 1/5 3/5]);

cum_nonD = [nonD_samples(1)];
cum_prob = [prob_samples(1)];
for i=2:1000
    cum_nonD(i) = cum_nonD(i-1) + nonD_samples(i);
    cum_prob(i) = cum_prob(i-1) + prob_samples(i);
end

figure
xlabel('trial')
ylabel('cumulative cost')
hold on
plot(1:1000, cum_nonD, 'Color','b')
plot(1:1000, cum_prob, 'Color','r')
legend({'Non-Deterministic', 'Probabilistic'})