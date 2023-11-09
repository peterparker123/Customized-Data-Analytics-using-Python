# -introduction-to-data-visualization-with-matplotlib




This chapter introduces the Matplotlib visualization library and demonstrates how to use it with data...


Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:


```
import matplotlib.pyplot as plt

# Run in command prompt : 

```

Now the Pyplot package can be referred to as plt.

```

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

```
Output : 

![image](https://user-images.githubusercontent.com/77969007/236448783-3165bce3-45d1-4b0d-9f93-76ef518623e7.png)

