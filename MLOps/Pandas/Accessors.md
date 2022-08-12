## pandas.Series.str

The pandas.Series.str accessor methods allow you to:

* capitalize
* count
* decode/encode
* extract
* find
* join
* replace
* slice

...and many more operations.  The documentation for strings starts [here](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.capitalize.html#)


```python
import pandas as pd
```


```python
text = "I like cats, dogs and lizards."
data_table = pd.Series(text).str.split().explode().reset_index(drop=False)
data_table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>I</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>like</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>cats,</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>dogs</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>and</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>lizards.</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.Series(text).str.count("like")
```




    0    1
    dtype: int64




```python
# https://docs.python.org/3/library/codecs.html#standard-encodings
ascii_text = pd.Series(text).str.encode('ascii')
ascii_text
```




    0    b'I like cats, dogs and lizards.'
    dtype: object




```python
pd.Series(ascii_text).str.decode('ascii')
```




    0    I like cats, dogs and lizards.
    dtype: object



## pandas.Series.dt

The pandas.Series.dt accessor methods allow you to cut up and work with datetimes in a variety of ways. The documentation for datetime starts [here](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.date.html)


```python
# example
dateseries = pd.Series(pd.date_range("1892-01-01",periods=12, freq='1M'))
dateseries.dt.day_name()
```




    0        Sunday
    1        Monday
    2      Thursday
    3      Saturday
    4       Tuesday
    5      Thursday
    6        Sunday
    7     Wednesday
    8        Friday
    9        Monday
    10    Wednesday
    11     Saturday
    dtype: object



## pandas.Series.cat

The pandas.Series.cat accessor methods allow you to cut up and work with datetimes in a variety of ways, including:

* renaming categories
* reordering categories
* removing categories
* creating unordered categories
* and other operations.

The documentation for datetime starts [here](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.categories.html)


```python
# the dtype must be declared as category
print("Original series setup: ")
catseries = pd.Series(['Mammal','Bird','Bird','Mammal','Reptile','Bird','Reptile'],dtype='category')
print(catseries)
print("Find all category possibilities: ")
catseries.cat.categories
print("Tokenize or rename categories: ")
newnames = catseries.cat.rename_categories({'Bird':1, 'Mammal':2, 'Reptile':0})
print(newnames)
```

    Original series setup: 
    0     Mammal
    1       Bird
    2       Bird
    3     Mammal
    4    Reptile
    5       Bird
    6    Reptile
    dtype: category
    Categories (3, object): ['Bird', 'Mammal', 'Reptile']
    Find all category possibilities: 
    Tokenize or rename categories: 
    0    2
    1    1
    2    1
    3    2
    4    0
    5    1
    6    0
    dtype: category
    Categories (3, int64): [1, 2, 0]


## pandas.Series.sparse

If most of the elements in a matrix, series, or dataframe contain zeros, then it's a sparse matrix.  This is useful for minimizing memory usage in big data.

The pandas.Series.sparse accessor methods allow you to cut up and work with datetimes in a variety of ways, including:

* checking the density, fill value
* looking at the sparse values only
* using the coo format for constructing sparse matricies

The documentation for sparse starts [here](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.npoints.html)


```python
import numpy as np
arr = np.zeros(1000000)
arr[:15] = 1

print(np.unique(arr, return_counts=True))

# dtype must be Sparce
sparseseries = pd.Series(arr, dtype="Sparse[int]")
regularseries = pd.Series(arr)

print("sparseseries memory usage: ",sparseseries.memory_usage())
print("regularseries memory usage: ",regularseries.memory_usage())

print("sparseseries npoints: ",sparseseries.sparse.npoints)
print("sparseseries density: ",sparseseries.sparse.density)
print("sparseseries fill_value: ",sparseseries.sparse.fill_value)
print("sparseseries sp_values: ",sparseseries.sparse.sp_values)
print("sparseseries from_coo: ",sparseseries.sparse.from_coo)
print("sparseseries to_coo: ",sparseseries.sparse.to_coo)
```

    (array([0., 1.]), array([999985,     15]))
    sparseseries memory usage:  308
    regularseries memory usage:  8000128
    sparseseries npoints:  15
    sparseseries density:  1.5e-05
    sparseseries fill_value:  0
    sparseseries sp_values:  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
    sparseseries from_coo:  <bound method SparseAccessor.from_coo of <class 'pandas.core.arrays.sparse.accessor.SparseAccessor'>>
    sparseseries to_coo:  <bound method SparseAccessor.to_coo of <pandas.core.arrays.sparse.accessor.SparseAccessor object at 0x7fd7257d9630>>



```python

```
