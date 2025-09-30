# Matplotlib
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used in data science and machine learning for data visualization.
## Key Features 
- **Versatile Plotting**: Supports a wide range of plot types including line plots, bar charts, histograms, scatter plots, and more.
- **Customization**: Highly customizable with options for colors, labels, legends, and styles.  
- **Integration**: Works well with other libraries like NumPy and Pandas for seamless data visualization.
- **Interactive Plots**: Can create interactive plots that can be embedded in web applications.
- **Publication Quality**: Capable of producing high-quality figures suitable for publication.
## Installation
You can install Matplotlib using pip or conda. Here are the commands for both methods:
Using pip:
```
pip install matplotlib
```
Using conda:
```
conda install matplotlib
```
## Functions in Matplotlib
Here are some commonly used functions in Matplotlib:

### **Creating Figures & Axes**

| Function                           | Description                                         |
| ---------------------------------- | --------------------------------------------------- |
| `plt.figure()`                     | Create a new figure                                 |
| `plt.subplot(nrows, ncols, index)` | Create a subplot in a figure                        |
| `plt.subplots()`                   | Create a figure with multiple subplots              |
| `fig.add_subplot()`                | Add a subplot to an existing figure                 |
| `fig.add_axes()`                   | Add axes at specific position [x, y, width, height] |

### **Basic Plotting**

| Function                        | Description              |
| ------------------------------- | ------------------------ |
| `plt.plot(x, y)`                | Line plot                |
| `plt.scatter(x, y)`             | Scatter plot             |
| `plt.bar(x, height)`            | Vertical bar plot        |
| `plt.barh(y, width)`            | Horizontal bar plot      |
| `plt.hist(data, bins=10)`       | Histogram                |
| `plt.boxplot(data)`             | Box plot                 |
| `plt.pie(sizes, labels=labels)` | Pie chart                |
| `plt.stackplot(x, y1, y2, ...)` | Stack plot               |
| `plt.fill_between(x, y1, y2)`   | Fill area between curves |

### **Customizing Plots**

| Function                      | Description                             |
| ----------------------------- | --------------------------------------- |
| `plt.title('Title')`          | Set plot title                          |
| `plt.xlabel('X-axis')`        | Set X-axis label                        |
| `plt.ylabel('Y-axis')`        | Set Y-axis label                        |
| `plt.xlim(min, max)`          | Set X-axis limits                       |
| `plt.ylim(min, max)`          | Set Y-axis limits                       |
| `plt.xticks([vals])`          | Set X-axis tick positions               |
| `plt.yticks([vals])`          | Set Y-axis tick positions               |
| `plt.legend()`                | Show legend                             |
| `plt.grid(True)`              | Show grid                               |
| `plt.style.use('style_name')` | Apply style (e.g., 'ggplot', 'seaborn') |
| `plt.tight_layout()`          | Adjust layout to prevent overlap        |

### **Line & Marker Styles**

| Parameter                 | Description                         |
| ------------------------- | ----------------------------------- |
| `color='r'`               | Line color (red)                    |
| `linestyle='--'`          | Line style (dashed, dotted, etc.)   |
| `linewidth=2`             | Line width                          |
| `marker='o'`              | Marker style (circle, square, etc.) |
| `markersize=5`            | Marker size                         |
| `markerfacecolor='blue'`  | Marker fill color                   |
| `markeredgecolor='black'` | Marker edge color                   |

Example:

```python
plt.plot(x, y, color='r', linestyle='--', marker='o', markersize=5)
```

### **Multiple Plots**

| Function                                   | Description                       |
| ------------------------------------------ | --------------------------------- |
| `plt.plot(x1, y1, label='Line1')`          | Add first line                    |
| `plt.plot(x2, y2, label='Line2')`          | Add second line                   |
| `plt.scatter(x, y, c='r', label='Points')` | Add scatter points                |
| `plt.bar(x, height, label='Bars')`         | Add bar plot                      |
| `plt.legend()`                             | Display legend for multiple plots |

### **Saving & Displaying Plots**

| Function                      | Description          |
| ----------------------------- | -------------------- |
| `plt.show()`                  | Display plot         |
| `plt.savefig('filename.png')` | Save figure to file  |
| `plt.close()`                 | Close current figure |
| `plt.clf()`                   | Clear current figure |
| `plt.cla()`                   | Clear current axes   |

### **Advanced Features**

| Function                                                              | Description                                  |
| --------------------------------------------------------------------- | -------------------------------------------- |
| `plt.subplot2grid((rows, cols), (row, col))`                          | Create subplot at specific grid location     |
| `plt.errorbar(x, y, yerr=errors)`                                     | Plot with error bars                         |
| `plt.annotate('text', xy=(x, y), xytext=(x2, y2), arrowprops=dict())` | Add annotation with arrow                    |
| `plt.text(x, y, 'text')`                                              | Add text at specified position               |
| `plt.xscale('log')`                                                   | Set X-axis scale (linear, log, symlog, etc.) |
| `plt.yscale('log')`                                                   | Set Y-axis scale                             |
| `plt.hexbin(x, y, gridsize=30, cmap='Blues')`                         | Hexbin plot for density                      |
| `plt.contour(X, Y, Z)`                                                | Contour plot                                 |
| `plt.contourf(X, Y, Z)`                                               | Filled contour plot                          |
| `plt.imshow(image)`                                                   | Display image (2D array)                     |
| `plt.colorbar()`                                                      | Add colorbar for images or contour plots     |

### **Style & Theme**

| Function                                 | Description               |
| ---------------------------------------- | ------------------------- |
| `plt.style.available`                    | List all available styles |
| `plt.style.use('seaborn-dark')`          | Apply a style             |
| `plt.rcParams['font.size'] = 12`         | Set default font size     |
| `plt.rcParams['figure.figsize'] = (8,6)` | Set default figure size   |
