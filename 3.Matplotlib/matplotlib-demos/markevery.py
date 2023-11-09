import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# define a list of markevery cases to plot
cases = [
    None,
    8,
    (30, 8),
    [16, 24, 30],
    [0, -1],
    slice(100, 200, 3),
    0.1,
    0.3,
    1.5,
    (0.0, 0.1),
    (0.45, 0.1)
]

# define the figure size and grid layout properties
figsize = (10, 8)
cols = 3
gs = gridspec.GridSpec(len(cases) // cols + 1, cols)
gs.update(hspace=0.4)
# define the data for cartesian plots
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta

fig1 = plt.figure(num=1, figsize=figsize)
ax = []
for i, case in enumerate(cases):
    row = (i // cols)
    col = i % cols
    ax.append(fig1.add_subplot(gs[row, col]))
    ax[-1].set_title('markevery=%s' % str(case))
    ax[-1].plot(x, y, 'o', ls='-', ms=4, markevery=case)

import save_fig as sf
sf.save_to_file('markevery')