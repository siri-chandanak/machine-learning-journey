# Pandas
Pandas is a powerful library for data manipulation and analysis in Python. It provides data structures like Series and DataFrame that make it easy to work with structured data.
## Installation
You can install Pandas using pip or conda. Here are the commands for both methods:
Using pip:
```
pip install pandas
```
Using conda:
```
conda install pandas
```

## Functions in Pandas

Here are some commonly used functions in **Pandas**:

### DataFrame & Series Creation

| Function            | Description                                     |
| ------------------- | ----------------------------------------------- |
| `pd.DataFrame()`    | Create a DataFrame from lists, dicts, or arrays |
| `pd.Series()`       | Create a Series from a list, dict, or array     |
| `pd.read_csv()`     | Read CSV file into DataFrame                    |
| `pd.read_excel()`   | Read Excel file into DataFrame                  |
| `pd.read_json()`    | Read JSON file into DataFrame                   |
| `pd.read_sql()`     | Read SQL query or database table into DataFrame |
| `pd.read_html()`    | Read HTML tables into DataFrame                 |
| `pd.read_parquet()` | Read Parquet file into DataFrame                |
| `pd.read_pickle()`  | Read pickled object into DataFrame              |

### Data Inspection

| Function            | Description                               |
| ------------------- | ----------------------------------------- |
| `df.head(n)`        | First n rows of DataFrame                 |
| `df.tail(n)`        | Last n rows of DataFrame                  |
| `df.shape`          | Dimensions of DataFrame (rows, columns)   |
| `df.info()`         | Summary of DataFrame including data types |
| `df.describe()`     | Statistical summary of numeric columns    |
| `df.columns`        | Column labels                             |
| `df.index`          | Row index labels                          |
| `df.dtypes`         | Data types of columns                     |
| `df.memory_usage()` | Memory usage of DataFrame                 |

### Selection & Indexing

| Function                            | Description                              |
| ----------------------------------- | ---------------------------------------- |
| `df['column']`                      | Select a column (Series)                 |
| `df[['col1', 'col2']]`              | Select multiple columns                  |
| `df.loc[row_indexer, col_indexer]`  | Label-based selection                    |
| `df.iloc[row_indexer, col_indexer]` | Position-based selection                 |
| `df.at[row_label, col_label]`       | Access a single value by label           |
| `df.iat[row_pos, col_pos]`          | Access a single value by position        |
| `df.query('condition')`             | Query DataFrame using a string condition |
| `df[df['col'] > value]`             | Boolean indexing                         |

### Data Manipulation

| Function                               | Description                        |
| -------------------------------------- | ---------------------------------- |
| `df.drop(columns='col')`               | Drop column(s)                     |
| `df.drop(index=0)`                     | Drop row(s)                        |
| `df.rename(columns={'old':'new'})`     | Rename columns                     |
| `df.sort_values(by='col')`             | Sort by column values              |
| `df.sort_index()`                      | Sort by index                      |
| `df.reset_index()`                     | Reset index                        |
| `df.set_index('col')`                  | Set column as index                |
| `df.append(df2)`                       | Append rows from another DataFrame |
| `df.merge(df2, on='col', how='inner')` | Merge DataFrames (SQL-like join)   |
| `df.join(df2)`                         | Join DataFrames by index           |
| `df.concat([df1, df2])`                | Concatenate DataFrames             |

### Handling Missing Data

| Function                      | Description                               |
| ----------------------------- | ----------------------------------------- |
| `df.isna()` / `df.isnull()`   | Detect missing values                     |
| `df.notna()` / `df.notnull()` | Detect non-missing values                 |
| `df.dropna()`                 | Drop rows with missing values             |
| `df.fillna(value)`            | Fill missing values with a specific value |
| `df.interpolate()`            | Fill missing values using interpolation   |

### Aggregation & Grouping

| Function                 | Description                         |
| ------------------------ | ----------------------------------- |
| `df.groupby('col')`      | Group data by column(s)             |
| `df.agg({'col':'mean'})` | Aggregate using function(s)         |
| `df.sum()`               | Sum of columns/rows                 |
| `df.mean()`              | Mean of columns/rows                |
| `df.median()`            | Median of columns/rows              |
| `df.min()` / `df.max()`  | Min / Max values                    |
| `df.count()`             | Count of non-NA values              |
| `df.value_counts()`      | Frequency of unique values (Series) |

### String Operations

| Function                             | Description                      |
| ------------------------------------ | -------------------------------- |
| `df['col'].str.lower()`              | Convert to lowercase             |
| `df['col'].str.upper()`              | Convert to uppercase             |
| `df['col'].str.strip()`              | Remove leading/trailing spaces   |
| `df['col'].str.replace('old','new')` | Replace substring                |
| `df['col'].str.contains('pattern')`  | Boolean mask for substring       |
| `df['col'].str.startswith('prefix')` | Boolean mask for starting string |
| `df['col'].str.endswith('suffix')`   | Boolean mask for ending string   |

### Date & Time Functions

| Function                    | Description                |
| --------------------------- | -------------------------- |
| `pd.to_datetime(df['col'])` | Convert column to datetime |
| `df['col'].dt.year`         | Extract year from datetime |
| `df['col'].dt.month`        | Extract month              |
| `df['col'].dt.day`          | Extract day                |
| `df['col'].dt.weekday`      | Extract day of the week    |
| `df['col'].dt.hour`         | Extract hour               |
| `df['col'].dt.minute`       | Extract minute             |

### Pivoting & Reshaping

| Function                                                                     | Description                                |
| ---------------------------------------------------------------------------- | ------------------------------------------ |
| `df.pivot(index='col1', columns='col2', values='col3')`                      | Pivot table                                |
| `df.pivot_table(values='col', index='col1', columns='col2', aggfunc='mean')` | Pivot table with aggregation               |
| `df.melt()`                                                                  | Unpivot DataFrame from wide to long format |
| `df.stack()`                                                                 | Stack columns into rows                    |
| `df.unstack()`                                                               | Unstack rows into columns                  |

### Other Useful Functions

| Function               | Description                   |
| ---------------------- | ----------------------------- |
| `df.copy()`            | Copy DataFrame                |
| `df.duplicated()`      | Identify duplicate rows       |
| `df.drop_duplicates()` | Remove duplicate rows         |
| `df.corr()`            | Correlation matrix            |
| `df.cov()`             | Covariance matrix             |
| `df.apply(func)`       | Apply function along axis     |
| `df.applymap(func)`    | Apply function element-wise   |
| `df.astype(dtype)`     | Change data type of column(s) |
| `df.sample(n)`         | Random sample of rows         |

