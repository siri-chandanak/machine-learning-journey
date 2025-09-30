# NumPy
NumPy is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and a wide range of mathematical functions to operate on these data structures.
## Key Features
- **N-Dimensional Arrays**: Efficient storage and manipulation of large datasets.
- **Broadcasting**: Automatic expansion of arrays with different shapes during arithmetic operations.
- **Vectorization**: Elimination of explicit loops for array operations, leading to more concise and faster code.
- **Integration with Other Libraries**: Works seamlessly with libraries like SciPy, Pandas, and Matplotlib.
## Installation
You can install NumPy using pip or conda:
```bash
pip install numpy
```
or
```bash
conda install numpy
```
# Functions in NumPy

Here are some commonly used functions in NumPy:

### Array Creation

| Function | Description |
|----------|-------------|
| `np.array()` | Create an array from a list or tuple |
| `np.zeros()` | Create an array filled with zeros |
| `np.ones()` | Create an array filled with ones |
| `np.empty()` | Create an empty array (uninitialized) |
| `np.arange()` | Create an array with a range of numbers |
| `np.linspace()` | Create evenly spaced numbers over a specified interval |
| `np.logspace()` | Create numbers spaced evenly on a log scale |
| `np.eye()` / `np.identity()` | Create an identity matrix |
| `np.full()` | Create an array filled with a specific value |
| `np.random.rand()` | Uniformly distributed random numbers |
| `np.random.randn()` | Normally distributed random numbers |
| `np.random.randint()` | Random integers |
| `np.random.choice()` | Random selection from array |

### Array Inspection

| Function | Description |
|----------|-------------|
| `np.shape()` | Get shape of an array |
| `np.size()` | Number of elements |
| `np.ndim()` | Number of dimensions |
| `np.dtype()` | Data type of array elements |
| `np.itemsize()` | Size in bytes of each element |
| `np.size()` | Total number of elements |

### Array Manipulation

| Function | Description |
|----------|-------------|
| `np.reshape()` | Change shape of an array |
| `np.flatten()` | Flatten array to 1D |
| `np.ravel()` | Flatten array (returns view if possible) |
| `np.transpose()` | Transpose array |
| `np.swapaxes()` | Swap two axes |
| `np.concatenate()` | Join arrays along an axis |
| `np.vstack()` / `np.hstack()` | Stack arrays vertically/horizontally |
| `np.split()` | Split array into multiple sub-arrays |
| `np.resize()` | Return a resized array |

### Mathematical Functions

| Function | Description |
|----------|-------------|
| `np.add()` / `+` | Element-wise addition |
| `np.subtract()` / `-` | Element-wise subtraction |
| `np.multiply()` / `*` | Element-wise multiplication |
| `np.divide()` / `/` | Element-wise division |
| `np.power()` / `**` | Element-wise exponentiation |
| `np.sqrt()` | Square root |
| `np.exp()` | Exponential |
| `np.log()` / `np.log10()` | Natural log / base-10 log |
| `np.sin()`, `np.cos()`, `np.tan()` | Trigonometric functions |
| `np.arcsin()`, `np.arccos()`, `np.arctan()` | Inverse trigonometric functions |
| `np.sum()` | Sum of array elements |
| `np.mean()` | Mean value |
| `np.median()` | Median value |
| `np.std()` | Standard deviation |
| `np.var()` | Variance |
| `np.min()` / `np.max()` | Minimum / Maximum |
| `np.argmin()` / `np.argmax()` | Index of min/max |

### Linear Algebra (`numpy.linalg`)

| Function | Description |
|----------|-------------|
| `np.dot()` | Dot product |
| `np.matmul()` | Matrix multiplication |
| `np.vdot()` | Vector dot product |
| `np.cross()` | Cross product |
| `np.linalg.inv()` | Inverse of matrix |
| `np.linalg.det()` | Determinant |
| `np.linalg.eig()` | Eigenvalues and eigenvectors |
| `np.linalg.solve()` | Solve linear equations |
| `np.linalg.norm()` | Vector/matrix norm |

### Statistics

| Function | Description |
|----------|-------------|
| `np.mean()` | Mean of elements |
| `np.median()` | Median |
| `np.std()` | Standard deviation |
| `np.var()` | Variance |
| `np.percentile()` | Percentiles |
| `np.corrcoef()` | Correlation coefficient |
| `np.histogram()` | Histogram of data |

### Random Numbers (`numpy.random`)

| Function | Description |
|----------|-------------|
| `np.random.seed()` | Seed for reproducibility |
| `np.random.rand()` | Uniform random numbers |
| `np.random.randn()` | Normal random numbers |
| `np.random.randint()` | Random integers |
| `np.random.choice()` | Random sample from array |
| `np.random.shuffle()` | Shuffle array elements |

### Fourier Transform (`numpy.fft`)

| Function | Description |
|----------|-------------|
| `np.fft.fft()` | Fast Fourier Transform |
| `np.fft.ifft()` | Inverse FFT |
| `np.fft.fft2()` | 2D FFT |
| `np.fft.ifft2()` | Inverse 2D FFT |
| `np.fft.fftfreq()` | Frequencies corresponding to FFT |

### Polynomials (`numpy.polynomial`)

| Function | Description |
|----------|-------------|
| `np.polyval()` | Evaluate a polynomial |
| `np.polyfit()` | Fit a polynomial to data |
| `np.roots()` | Find polynomial roots |
| `np.polyder()` | Derivative of polynomial |
| `np.polyint()` | Integral of polynomial |

### Other Useful Functions

| Function | Description |
|----------|-------------|
| `np.unique()` | Unique elements of array |
| `np.sort()` | Sort array |
| `np.argsort()` | Indices that would sort array |
| `np.where()` | Conditional selection |
| `np.clip()` | Limit values within bounds |
| `np.isnan()` | Check for NaN |
| `np.isfinite()` | Check for finite values |
| `np.copy()` | Copy array |
| `np.tile()` | Repeat array |
| `np.repeat()` | Repeat elements |
