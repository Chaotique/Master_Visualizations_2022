"""
plot a plot from the seaborn gallery.
Later try to replicate it with matplotlib (then_plot_with_matplotlib.py)
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

# set plotting style
#sns.set_theme(style="darkgrid")

# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)

# save figure to file
plt.savefig("sb_wo_dark.png")

# show in API
plt.show()

