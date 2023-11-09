import numpy as np
import matplotlib.pyplot as plt
import save_fig as sf

# # Figure: a box-like container holding one or more Axes
# # Axes: actual plots
# # Axis
# # Tick marks, individual lines, legends, text boxes

# fig, _ = plt.subplots()
# # print(type(fig))
# # <class 'matplotlib.figure.Figure'>

# # fig has multiple Axes(a list, for which we take the first element)
# axes = fig.axes[0]
# # print(type(axes))
# # <class 'matplotlib.axes._subplots.AxesSubplot'>

# # Each Axes has a yaxis and axis
# yaxis = axes.yaxis
# # print(type(yaxis))
# # <class 'matplotlib.axis.YAxis'>

# # Each of yaxis, xaxis have a collection of "major ticks"
# # and we grab the first one
# one_tick = yaxis.get_major_ticks()[0]
# # print(type(one_tick))
# # <class 'matplotlib.axis.YTick'>

# # Default to subplots(nrows=1, ncols=1)
# # fig, ax = plt.subplots()
# # Consequently, ax is a single AxesSubplot object
# # print(type(ax))
# # <class 'matplotlib.axes._subplots.AxesSubplot'>




# rng = np.arange(50)
# # Three random time series
# rnd = np.random.randint(0, 10, size=(3, rng.size))
# # 1950 - 2000, x-axis
# yrs = 1950 + rng
# print('rng:\n', rng)
# print('rnd:\n', rnd)
# print('yrs:\n', yrs)

# # One Figure containing one Axes
# fig, ax = plt.subplots(figsize=(5, 3))
# # Call methods of ax directly to create a stacked area chart and to add a legend, title, and y-axis label. Under the object-oriented approach, it's clearly that all of these are attributes of ax.
# ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
# ax.set_title('Combined debt growth over time')
# ax.legend(loc='upper left')
# ax.set_ylabel('Total debt')
# ax.set_xlim(left=yrs[0], right=yrs[-1])
# # Applies to the Figure abject as a whole to clean up whitespace padding
# fig.tight_layout()
# plt.show()






# # Because we'are creating a M x N Figure, now returns a Figure object and a Numpy array of Axes objects
# fig, axs = plt.subplots(nrows=5, ncols=7)
# print(type(axs))
# # <class 'numpy.ndarray'>
# print(axs.shape)
# # (5, 7)
# print(axs)
# [[<matplotlib.axes._subplots.AxesSubplot object at 0x0000026C612039B0>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C61177470>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60DA49E8>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60DCBF60>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60E7B518>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60F64A90>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C61017048>]
#  [<matplotlib.axes._subplots.AxesSubplot object at 0x0000026C6103D588>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C61062B38>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C611190F0>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C6113F668>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60CE7BE0>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60D57198>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60D7E710>]
#  [<matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60DE5C88>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60E14240>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60E3E7B8>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60FA5D30>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60FD52E8>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C60FFB860>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C610A5DD8>]
#  [<matplotlib.axes._subplots.AxesSubplot object at 0x0000026C610D3390>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C610FB908>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C63324E80>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C63353438>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C6337A9B0>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C633A3F28>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C655E34E0>]
#  [<matplotlib.axes._subplots.AxesSubplot object at 0x0000026C6560AA58>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C65633FD0>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C65662588>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C65689B00>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C656BA0B8>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C656E1630>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000026C65709BA8>]]

# ##### Multiple Axes in one figure
# x = np.random.randint(low=1, high=11, size=50)
# y = x + np.random.randint(1, 5, size=x.size)
# data = np.column_stack((x, y))

# # We deal with ax1, ax2 individually
# fig, (ax1, ax2) = plt.subplots(
#     nrows=1, ncols=2,
#     figsize=(8, 4)
# )
# # Remember that multiple Axes can be enclosed in or "belong to" a given figure, `fig.axes` gets us a list of all the Axes objects:
# print(
#     fig.axes[0] is ax1, fig.axes[1] is ax2
# )
# # True True

# # Scatter plot
# ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
# # Support TeX markup, put variables in italics
# ax1.set_title('Scatter: $x$ versus $y$')
# ax1.set_xlabel('$x$')
# ax1.set_ylabel('$y$')

# # Histgram
# ax2.hist(data, bins=np.arange(data.min(), data.max()), label=('x', 'y'))
# ax2.legend(loc=(0.65, 0.8))
# ax2.set_title('Frequencies of $x$ and $y$')
# # Modify the yaxis belonging to the second Axes, placing its ticks and ticklabels to the right
# ax2.yaxis.tick_right()
# # fig.tight_layout()
# plt.show()










# # We now need to call plotting methods on each of these Axes (but not the NumPy array, which is just a container in this case). A common way to address this is to use iterable unpacking after flattening the array to be one-dimensional:
# fig, ax = plt.subplots(
#     nrows=2, ncols=2,
#     figsize=(7, 7)
# )
# ax1, ax2, ax3, ax4 = ax.flatten()
# # Less flexible:
# # ((ax1, ax2), (ax3, ax4)) = ax

















# # More advanced subplot features
# from io import BytesIO
# import tarfile
# from urllib.request import urlopen

# url = 'http://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz'
# b = BytesIO(urlopen(url).read())
# housing = []
# fpath = 'CaliforniaHousing/cal_housing.data'
# with tarfile.open(mode='r', fileobj=b) as archive:
#     housing = np.loadtxt(archive.extractfile(fpath), delimiter=',')

# y = housing[:,-1]
# pop, age = housing[:, [4, 7]].T

# def add_titlebox(ax, text):
#     """
#     a “helper function” that places a text box inside of a plot and acts as an “in-plot title”
#     """
#     ax.text(.55, .8, text,
#         horizontalalignment='center',
#         transform=ax.transAxes,
#         bbox=dict(facecolor='white', alpha=0.6),
#         fontsize=12.5)
#     return ax

# # `gridspec` allows for more subplot customization. `subplot2grid()` interacts with this module nicely. Let's say we want to create a layout like this:
# # =========== ax1 ==========
# # =========== ax1 ==========
# # ==== ax2 ==== ==== ax3 ====
# # What we actually have is a 3x2 grid, ax1 is twice the height and width of ax2/ax3, meaning that it takes up two columns and two rows.

# # The second argument to subplot2grid() is the (row, column) location of the Axes within the grid:
# gridsize = (3, 2)
# fig = plt.figure(figsize=(12, 8))
# ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
# ax2 = plt.subplot2grid(gridsize, (2, 0))
# ax3 = plt.subplot2grid(gridsize, (2, 1))

# # Now we can proceed as normal, modifying each Axis individually:
# ax1.set_title('Home value as a function of home age & area population', fontsize=14)
# sctr = ax1.scatter(x=age, y=pop, c=y, cmap='RdYlGn')
# # colorbar() gets called on the Figure directly, rather than the Axes, the first argument is the result of `ax1.scatter()`, which functions as a mapping of y-values to ColorMap
# plt.colorbar(sctr, ax=ax1, format='$%d')
# ax1.set_yscale('log')
# ax2.hist(age, bins='auto')
# ax3.hist(pop, bins='auto', log=True)

# add_titlebox(ax2, 'Histogram: home age')
# add_titlebox(ax3, 'Histogram: area population (log scl.)')
# plt.show()


















# Methods that get heavy use are inshow() and matshow(), with the latter being a wrapper around the former. There are useful anytime that a raw numerical array can be visualized as a colored grid.

x = np.diag(np.arange(2, 12))[::-1]
x[np.diag_indices_from(x[::-1])] = np.arange(2, 12)
x2 = np.arange(x.size).reshape(x.shape)
print(x2)

# Now we can map these to their image representations. In this specific, we toggle "off" all axis labels and ticks by using a dictionary comprehension and passing the result to `ax.tick_params()`

sides = ('left', 'right', 'top', 'bottom')
nolabels = {s: False for s in sides}
nolabels.update({'label%s' % s: False for s in sides})
# print(nolabels)
# {'left': False, 'right': False, 'top': False, 'bottom': False, 'labelleft': False,
#  'labelright': False, 'labeltop': False, 'labelbottom': False}

from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
with plt.rc_context(rc={'axes.grid': False}):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
    ax1.matshow(x)
    img2 = ax2.matshow(x2, cmap='RdYlGn_r')
    for ax in (ax1, ax2):
        # toggle off all axis labels and ticks
        ax.tick_params(axis='both', which='both', **nolabels)
    # print(x.nonzero())
    for i, j in zip(*x.nonzero()):
        ax1.text(j, i, x[i, j], color='white', ha='center', va='center')
    
    divider = make_axes_locatable(ax2)
    cax = divider.append_axes("right", size='5%', pad=1)
    plt.colorbar(img2, cax=cax, ax=[ax1, ax2])
    fig.suptitle('Heatmaps with `Axes.matshow`', fontsize=16)

plt.show()
# sf.save_to_file('matshow')