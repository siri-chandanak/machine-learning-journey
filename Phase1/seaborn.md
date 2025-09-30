# Seaborn
Seaborn is a powerful Python visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. Seaborn simplifies the process of creating complex visualizations with less code and offers beautiful default styles.

## Key Features
- **Statistical Plots**: Specialized plots for statistical analysis, including box plots, violin plots, and pair plots.
- **Built-in Themes**: A variety of built-in themes to enhance the aesthetics of your plots.
- **Integration with Pandas**: Seamless integration with Pandas DataFrames for easy data manipulation and visualization.
- **Color Palettes**: A wide range of color palettes to choose from, making it easy to create visually appealing plots.
- **Faceting**: Ability to create multi-plot grids for visualizing data subsets.    
- **Advanced Visualizations**: Support for advanced visualizations like heatmaps, cluster maps, and regression plots.

## Installation
You can install Seaborn using pip or conda. Here are the commands for both methods:
Using pip:
```
pip install seaborn
```
Using conda:
```
conda install seaborn
```

## Functions in Seaborn

Here are some commonly used functions in **Seaborn**:

### Relational Plots

| Function            | Description                                       |
| ------------------- | ------------------------------------------------- |
| `sns.relplot()`     | General-purpose relational plot (scatter or line) |
| `sns.scatterplot()` | Scatter plot of two variables                     |
| `sns.lineplot()`    | Line plot for continuous data                     |

### Categorical Plots

| Function           | Description                                           |
| ------------------ | ----------------------------------------------------- |
| `sns.catplot()`    | General-purpose categorical plot                      |
| `sns.stripplot()`  | Scatter plot for categorical data (jittered points)   |
| `sns.swarmplot()`  | Similar to stripplot but avoids overlapping points    |
| `sns.boxplot()`    | Box-and-whisker plot (showing quartiles and outliers) |
| `sns.violinplot()` | Violin plot (distribution + boxplot)                  |
| `sns.barplot()`    | Bar plot with confidence intervals                    |
| `sns.countplot()`  | Bar plot showing counts of each category              |
| `sns.pointplot()`  | Shows point estimates and confidence intervals        |

### Distribution Plots

| Function         | Description                                   |
| ---------------- | --------------------------------------------- |
| `sns.histplot()` | Histogram                                     |
| `sns.kdeplot()`  | Kernel density estimation plot                |
| `sns.ecdfplot()` | Empirical cumulative distribution function    |
| `sns.displot()`  | Figure-level function for histograms/KDE/ECDF |
| `sns.rugplot()`  | Plot small vertical ticks (rug) along an axis |

### Matrix Plots

| Function           | Description                               |
| ------------------ | ----------------------------------------- |
| `sns.heatmap()`    | Heatmap for 2D data, correlation matrices |
| `sns.clustermap()` | Hierarchical clustering heatmap           |

### Regression Plots

| Function          | Description                             |
| ----------------- | --------------------------------------- |
| `sns.regplot()`   | Scatter plot with linear regression fit |
| `sns.lmplot()`    | Regression plots with multiple facets   |
| `sns.residplot()` | Plot residuals of regression            |

### Multi-Plot Grids

| Function          | Description                                   |
| ----------------- | --------------------------------------------- |
| `sns.FacetGrid()` | Multi-plot grid for data subsets              |
| `sns.PairGrid()`  | Grid for plotting pairwise relationships      |
| `sns.pairplot()`  | Plot pairwise relationships between variables |
| `sns.JointGrid()` | Grid for joint distribution plots             |
| `sns.jointplot()` | Joint distribution with marginal plots        |

### Theming & Aesthetics

| Function              | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| `sns.set()`           | Set default theme and aesthetics                                  |
| `sns.set_style()`     | Set plot style (`dark`, `white`, `ticks`, etc.)                   |
| `sns.set_context()`   | Set context (scales elements for presentation, paper, talk, etc.) |
| `sns.set_palette()`   | Set color palette                                                 |
| `sns.color_palette()` | Return list of colors from palette                                |
| `sns.set_theme()`     | High-level function to set style, palette, context                |

### Color Palettes

| Function                  | Description                      |
| ------------------------- | -------------------------------- |
| `sns.color_palette()`     | Access colors from a palette     |
| `sns.dark_palette()`      | Generate dark color palette      |
| `sns.light_palette()`     | Generate light color palette     |
| `sns.diverging_palette()` | Generate diverging color palette |
| `sns.cubehelix_palette()` | Cubehelix color palette          |
| `sns.set_palette()`       | Set default color palette        |

### Utility Functions

| Function             | Description                                |
| -------------------- | ------------------------------------------ |
| `sns.load_dataset()` | Load sample dataset (e.g., `tips`, `iris`) |
| `sns.despine()`      | Remove top/right spines from plots         |
| `sns.move_legend()`  | Adjust legend position                     |
| `sns.axes_style()`   | Get dictionary of style parameters         |

