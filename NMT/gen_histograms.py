import matplotlib.pyplot as plt
import numpy as np

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

n_bins = 5

# Generate two normal distributions
Adequancy_1 = [2, 2, 1, 1, 3, 2, 2, 5, 5, 3, 5, 2, 2, 5, 5, 2, 2, 5, 3, 5, 3, 5, 5, 5, 5, 4, 5, 3, 3, 3]
Fluency_1 = [2, 3, 4, 2, 4, 4, 2, 5, 5, 2, 5, 2, 5, 5, 3, 1, 2, 5, 4, 3, 5, 5, 5, 3, 5, 5, 5, 4, 4, 2]
Adequancy_2 = [1, 2, 4, 2, 1, 2, 2, 3, 5, 1, 4, 3, 3, 3, 2, 2, 5, 1, 1, 1, 2, 3, 1, 5, 3, 3, 2, 2, 2, 5]
Fluency_2 = [2, 4, 5, 4, 2, 4, 2, 4, 5, 1, 5, 4, 5, 5, 5, 5, 5, 1, 5, 2, 5, 5, 2, 5, 5, 5, 4, 5, 5, 5]
Adequancy_3 = [5, 5, 1, 3, 2, 5, 3, 3, 2, 2, 3, 4, 2, 4, 2, 3, 1, 1, 1, 3, 1, 2, 2, 3, 2, 3, 1, 2, 2, 5]
Fluency_3 = [5, 5, 1, 3, 5, 5, 4, 5, 2, 2, 5, 5, 2, 5, 5, 5, 1, 4, 3, 3, 5, 3, 2, 5, 3, 2, 2, 5, 5, 5]

all_a = [Adequancy_1, Adequancy_2, Adequancy_3]
all_f = [Fluency_1, Fluency_2, Fluency_3]

for i in range(3):
    Adequacy_n = all_a[i]
    Fluency_n = all_f[i]
    fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

    # We can set the number of bins with the *bins* keyword argument.
    axs[0].hist(Adequacy_n, bins=n_bins)
    axs[1].hist(Fluency_n, bins=n_bins)

    fig, axs = plt.subplots(1, 2, tight_layout=True)

    # Add a title
    plt.title(f"Adequacy & Fluency in Model {i+1}")

    # Axis 2
    # N is the count in each bin, bins is the lower-limit of the bin
    N, bins, patches = axs[0].hist(Adequacy_n, bins=n_bins, density=True)
    axs[0].yaxis.set_major_formatter(PercentFormatter(xmax=1))

    # We'll color code by height, but you could use any scalar
    fracs = N / N.max()

    # we need to normalize the data to 0..1 for the full range of the colormap
    norm = colors.Normalize(fracs.min(), fracs.max())

    # Now, we'll loop through our objects and set the color of each accordingly
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    # Axis 1
    # We can also normalize our inputs by the total number of counts
    N, bins, patches  = axs[1].hist(Fluency_n, bins=n_bins, density=True)
    # Now we format the y-axis to display percentage
    axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

    # We'll color code by height, but you could use any scalar
    fracs = N / N.max()

    # we need to normalize the data to 0..1 for the full range of the colormap
    norm = colors.Normalize(fracs.min(), fracs.max())

    # Now, we'll loop through our objects and set the color of each accordingly
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    # Show
    fig.show()
