"""
attempt to replicate one of the seaborn gallery one-liner plots
"""
import seaborn as sns # we only need this line to get the same data set with which the seaborn plot was created
import matplotlib.pyplot as plt
from scipy.stats import sem
import matplotlib

# Load the seaborn example dataset with long-form data
fmri = sns.load_dataset("fmri") # returns panda dataframe

# sort data in chronological order
fmri_mpl = fmri.sort_values('timepoint')

# create canvas
fig, ax =plt.subplots()

# chose color and linestyle for the different curves
colors = {"parietal":"C0", "frontal":"C1"}
line_styles = {"stim":"solid", "cue":"dashed"}

# plot curves
for event in set(fmri_mpl["event"]):
    # filter for one event
    fmri_mpl_ev = fmri_mpl[fmri_mpl["event"]==event]
    for region in set(fmri_mpl_ev["region"]):
        # filter for one region
        fmri_mpl_re = fmri_mpl_ev[fmri_mpl_ev["region"]==region]
        # calculate mean and 95% confidence interval with scipy stats
        df_mean = fmri_mpl_re.groupby('timepoint').signal.mean()
        df_se = fmri_mpl_re.groupby('timepoint').signal.apply(sem).mul(1.96) # in contrast to seaborn, you see more explicitely, how the confidence interval is calculated
        # plot mean
        ax.plot(df_mean, # time stamps and mean are in one DataFrame
                 color = colors[region], # color according to region
                 ls = line_styles[event]), # linestyle according to event
        # plot confidence interval
        plt.fill_between(df_mean.index, df_mean - df_se, df_mean + df_se, color=colors[region], alpha = 0.2)

# axes labels
ax.set_xlabel('timepoint')
ax.set_ylabel("signal")

# we need some dummy lines to plot the legend (otherwise we have the 4 labels for the four lines)
dummy_lines = []
for event in set(fmri_mpl["event"]):
    dummy_lines.append(ax.plot([],[], c="black", ls = line_styles[event])[0])
lines = ax.get_lines()
# legend regions
legend1 = plt.legend([lines[i] for i in [0, 1]], ["parietal", "frontal"],
                     title = "region",
                     loc="upper right")
# legend events
legend2 = plt.legend([dummy_lines[i] for i in [0,1]], ["stim", "cue"],
                     title = "event",
                     loc="center right",
                     bbox_to_anchor=(1,0.7))

# add the legends to our axes
ax.add_artist(legend1)
ax.add_artist(legend2)

# save figure to file
plt.savefig("mpl.png")
# show in API
plt.show()


