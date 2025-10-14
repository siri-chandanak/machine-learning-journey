# Programming and Foundations
This phase focuses on building a strong foundation in programming, mathematics, and data handling, which are essential for any AI/ML practitioner.

## Required Tools
1. Python 3.x (Anaconda distribution recommended)
2. Jupyter Notebook or any IDE (VSCode, PyCharm)

## Python Core -- PythonCore.ipynb
1. Variables, data types, input/output
2. Data structures: list, dict, set, tuple
3. Loops & conditionals
4. Functions (with arguments, return values)
5. Error handling (try-except)

## Python OOP + Libraries -- PythonOOPS.ipynb
1. Classes & Objects
2. Inheritance, Polymorphism, Encapsulation
3. File handling (with open)
4. Libraries: NumPy (arrays, operations), Pandas (DataFrames), Matplotlib & Seaborn (visualization)

## Math Foundations (Linear Algebra) -- LinearAlgebra.ipynb
1. Scalars, vectors, matrices
2. Matrix operations (addition, multiplication, transpose)
3. Dot product, eigenvalues, eigenvectors

## Math Foundations (Probability & Statistics) -- ProbabilityStatistics.ipynb
1. Mean, median, variance, standard deviation
2. Probability distributions (Normal, Binomial, Poisson)
3. Bayes’ theorem basics

## Math Foundations (Calculus) -- Calculus.ipynb
1. Functions, limits
2. Derivatives & gradients
3. Partial derivatives (multivariable functions)
4. Gradient descent basics

## Databases (SQL + NoSQL) -- Databases.ipynb
1. SQL basics: SELECT, WHERE, GROUP BY, JOIN
2. Subqueries
3. Normalization basics
4. NoSQL: MongoDB basics (collections, documents)

# Starting with Anaconda/Jupyter
Anaconda is a popular distribution for Python and R, which simplifies package management and deployment. Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.

In Conda, the steps are as follows:

Install Anaconda --> Change Path --> Create Environment --> Activate Environment --> Install Libraries --> Install Jupyter Notebook --> Launch Jupyter Notebook

1. Download and install Anaconda from https://www.anaconda.com/products/distribution
2. Create a new environment:
   ```
   conda create -n ai_ml_env python=3.9
   ```
3. Activate the environment:
   ```
   conda activate ai_ml_env
   ```
4. Install essential libraries:
   ```
   conda install numpy pandas matplotlib seaborn scikit-learn
   ```
5. Install Jupyter Notebook:
   ```
   conda install jupyter
   ```
6. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```
7. Deactivate the environment when done:
   ```
   conda deactivate
   ```
8. To remove the environment:
   ```
   conda remove -n ai_ml_env --all
   ```
