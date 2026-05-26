# Pandas LeetCode Practice Note Guide

This document contains beginner-friendly Pandas LeetCode practice notes. Each problem includes:

- Problem number
- Problem link
- Main Pandas function used
- Solution code
- Easy explanation

---

# Practice List

| No. | Problem | Link | Main Function |
|---|---|---|---|
| 2877 | Create a DataFrame from List | https://leetcode.com/problems/create-a-dataframe-from-list/ | `pd.DataFrame()` |
| 2878 | Get the Size of a DataFrame | https://leetcode.com/problems/get-the-size-of-a-dataframe/ | `df.shape` |
| 2879 | Display the First Three Rows | https://leetcode.com/problems/display-the-first-three-rows/ | `head()` |
| 2880 | Select Data | https://leetcode.com/problems/select-data/ | `.loc[]` |
| 2881 | Create a New Column | https://leetcode.com/problems/create-a-new-column/ | Column assignment |
| 2882 | Drop Duplicate Rows | https://leetcode.com/problems/drop-duplicate-rows/ | `drop_duplicates()` |
| 2883 | Drop Missing Data | https://leetcode.com/problems/drop-missing-data/ | `dropna()` |
| 2884 | Modify Columns | https://leetcode.com/problems/modify-columns/ | Column update |
| 2885 | Rename Columns | https://leetcode.com/problems/rename-columns/ | `rename()` |
| 2886 | Change Data Type | https://leetcode.com/problems/change-data-type/ | `astype()` |
| 2887 | Fill Missing Data | https://leetcode.com/problems/fill-missing-data/ | `fillna()` |
| 2888 | Reshape Data: Concatenate | https://leetcode.com/problems/reshape-data-concatenate/ | `pd.concat()` |
| 2889 | Reshape Data: Pivot | https://leetcode.com/problems/reshape-data-pivot/ | `pivot()` |
| 2890 | Reshape Data: Melt | https://leetcode.com/problems/reshape-data-melt/ | `pd.melt()` |
| 2891 | Method Chaining | https://leetcode.com/problems/method-chaining/ | Filtering + `sort_values()` |

---

# 2877. Create a DataFrame from List

## Problem Link

https://leetcode.com/problems/create-a-dataframe-from-list/

## Main Function Used

```python
pd.DataFrame()
```

## Solution

```python
import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])
```

## Explanation

`pd.DataFrame()` creates a table from list data.

Example list:

```python
[[1, 15], [2, 11], [3, 11], [4, 20]]
```

Output table:

```text
student_id   age
1            15
2            11
3            11
4            20
```

---

# 2878. Get the Size of a DataFrame

## Problem Link

https://leetcode.com/problems/get-the-size-of-a-dataframe/

## Main Function Used

```python
df.shape
```

## Solution

```python
import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows, columns = players.shape
    return [rows, columns]
```

## Explanation

`df.shape` gives the number of rows and columns.

Example:

```python
players.shape
```

Output:

```text
[rows, columns]
```

If the DataFrame has 10 rows and 5 columns, output will be:

```text
[10, 5]
```

---

# 2879. Display the First Three Rows

## Problem Link

https://leetcode.com/problems/display-the-first-three-rows/

## Main Function Used

```python
head()
```

## Solution

```python
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
```

## Explanation

`head(3)` returns the first 3 rows.

```python
employees.head(3)
```

Means:

```text
Show row 1, row 2, and row 3 only.
```

---

# 2880. Select Data

## Problem Link

https://leetcode.com/problems/select-data/

## Main Function Used

```python
.loc[]
```

## Solution

```python
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]
```

## Explanation

This problem asks to find the student whose `student_id` is `101`.

```python
students["student_id"] == 101
```

This checks which row has student id `101`.

```python
["name", "age"]
```

This returns only the `name` and `age` columns.

Full line:

```python
students.loc[students["student_id"] == 101, ["name", "age"]]
```

Means:

```text
Find student_id 101 and show only name and age.
```

---

# 2881. Create a New Column

## Problem Link

https://leetcode.com/problems/create-a-new-column/

## Main Concept Used

```python
df["new_column"] = value
```

## Solution

```python
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees
```

## Explanation

This problem asks to create a new column called `bonus`.

```python
employees["bonus"] = employees["salary"] * 2
```

Means:

```text
Take salary, multiply it by 2, and save it inside a new column named bonus.
```

Example:

```text
salary = 3000
bonus = 3000 * 2 = 6000
```

---

# 2882. Drop Duplicate Rows

## Problem Link

https://leetcode.com/problems/drop-duplicate-rows/

## Main Function Used

```python
drop_duplicates()
```

## Solution

```python
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])
```

## Explanation

This problem asks to remove duplicate email rows.

```python
drop_duplicates(subset=["email"])
```

Means:

```text
If two rows have the same email, keep only the first one.
```

Example:

```text
id   email
1    a@gmail.com
2    b@gmail.com
3    a@gmail.com
```

After removing duplicate email:

```text
id   email
1    a@gmail.com
2    b@gmail.com
```

---

# 2883. Drop Missing Data

## Problem Link

https://leetcode.com/problems/drop-missing-data/

## Main Function Used

```python
dropna()
```

## Solution

```python
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
```

## Explanation

This problem asks to remove rows where the `name` is missing.

```python
dropna(subset=["name"])
```

Means:

```text
Remove rows only if the name column is empty or NaN.
```

Example:

```text
student_id   name
101          Jack
102          NaN
103          Alice
```

After:

```text
student_id   name
101          Jack
103          Alice
```

---

# 2884. Modify Columns

## Problem Link

https://leetcode.com/problems/modify-columns/

## Main Concept Used

Column update.

## Solution

```python
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees
```

## Explanation

This problem asks to multiply every salary by `2`.

```python
employees["salary"] = employees["salary"] * 2
```

Means:

```text
Take the old salary, multiply it by 2, and replace the old salary.
```

Example:

```text
Old salary: 4000
New salary: 8000
```

---

# 2885. Rename Columns

## Problem Link

https://leetcode.com/problems/rename-columns/

## Main Function Used

```python
rename()
```

## Solution

```python
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years"
    })
    return students
```

## Explanation

`rename()` changes column names.

```python
students.rename(columns={
    "id": "student_id"
})
```

Means:

```text
Change column name id to student_id.
```

Rule:

```text
Old column name : New column name
```

---

# 2886. Change Data Type

## Problem Link

https://leetcode.com/problems/change-data-type/

## Main Function Used

```python
astype()
```

## Solution

```python
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students
```

## Explanation

This problem asks to change the `grade` column into integer type.

```python
students["grade"].astype(int)
```

Means:

```text
Convert grade values into integer numbers.
```

Common type changes:

```python
astype(int)      # integer
astype(float)    # decimal number
astype(str)      # text/string
astype(bool)     # true/false
```

---

# 2887. Fill Missing Data

## Problem Link

https://leetcode.com/problems/fill-missing-data/

## Main Function Used

```python
fillna()
```

## Solution

```python
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products
```

## Explanation

This problem asks to fill missing `quantity` values with `0`.

```python
products["quantity"].fillna(0)
```

Means:

```text
If quantity is empty or NaN, replace it with 0.
```

Example:

```text
product   quantity
Pen       10
Book      NaN
Pencil    5
```

After:

```text
product   quantity
Pen       10
Book      0
Pencil    5
```

---

# 2888. Reshape Data: Concatenate

## Problem Link

https://leetcode.com/problems/reshape-data-concatenate/

## Main Function Used

```python
pd.concat()
```

## Solution

```python
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])
```

## Explanation

This problem asks to combine two DataFrames vertically.

```python
pd.concat([df1, df2])
```

Means:

```text
Put df2 under df1.
```

Example:

```text
df1:
student_id   name
1            Jack
2            Alice

df2:
student_id   name
3            Bob
4            Messi
```

After concat:

```text
student_id   name
1            Jack
2            Alice
3            Bob
4            Messi
```

---

# 2889. Reshape Data: Pivot

## Problem Link

https://leetcode.com/problems/reshape-data-pivot/

## Main Function Used

```python
pivot()
```

## Solution

```python
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index="month",
        columns="city",
        values="temperature"
    )
```

## Explanation

This problem asks to make:

```text
Rows = month
Columns = city
Values = temperature
```

Code:

```python
weather.pivot(index="month", columns="city", values="temperature")
```

Meaning:

```text
index="month"
```

Each row becomes a month.

```text
columns="city"
```

Each city becomes a separate column.

```text
values="temperature"
```

Temperature values go inside the table.

Example before:

```text
city      month     temperature
Dhaka     January   25
Dhaka     February  28
Delhi     January   20
Delhi     February  24
```

After pivot:

```text
city      Delhi   Dhaka
month
February  24      28
January   20      25
```

---

# 2890. Reshape Data: Melt

## Problem Link

https://leetcode.com/problems/reshape-data-melt/

## Main Function Used

```python
pd.melt()
```

## Solution

```python
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        report,
        id_vars=["product"],
        var_name="quarter",
        value_name="sales"
    )
```

## Explanation

This problem asks to change wide data into long data.

Before:

```text
product   quarter_1   quarter_2   quarter_3   quarter_4
Pen       100         200         300         400
Book      150         250         350         450
```

After melt:

```text
product   quarter     sales
Pen       quarter_1   100
Book      quarter_1   150
Pen       quarter_2   200
Book      quarter_2   250
Pen       quarter_3   300
Book      quarter_3   350
Pen       quarter_4   400
Book      quarter_4   450
```

Code meaning:

```python
id_vars=["product"]
```

Keep `product` column as it is.

```python
var_name="quarter"
```

Put old quarter column names into a new column called `quarter`.

```python
value_name="sales"
```

Put quarter values into a new column called `sales`.

---

# 2891. Method Chaining

## Problem Link

https://leetcode.com/problems/method-chaining/

## Main Functions Used

```python
filtering
sort_values()
column selection
```

## Solution

```python
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(
        by="weight",
        ascending=False
    )[["name"]]
```

## Explanation

This problem asks to:

1. Find animals with weight more than `100`
2. Sort them by weight from heaviest to lightest
3. Return only the animal names

Code step by step:

```python
animals["weight"] > 100
```

Find animals heavier than `100`.

```python
.sort_values(by="weight", ascending=False)
```

Sort from heaviest to lightest.

```python
[["name"]]
```

Return only the `name` column.

Full code:

```python
animals[animals["weight"] > 100].sort_values(
    by="weight",
    ascending=False
)[["name"]]
```

---

# Important Pandas Functions Summary

| Task | Function / Code |
|---|---|
| Create DataFrame | `pd.DataFrame()` |
| Get rows and columns | `df.shape` |
| Display first rows | `df.head(n)` |
| Select rows and columns | `.loc[]` |
| Create new column | `df["col"] = value` |
| Remove duplicates | `drop_duplicates()` |
| Remove missing rows | `dropna()` |
| Modify column | `df["col"] = df["col"] * 2` |
| Rename columns | `rename(columns={})` |
| Change data type | `astype()` |
| Fill missing values | `fillna()` |
| Concatenate DataFrames | `pd.concat()` |
| Pivot data | `pivot()` |
| Melt data | `pd.melt()` |
| Sort data | `sort_values()` |

---

# Quick Revision Code

```python
df.shape
df.head(3)

df.loc[df["student_id"] == 101, ["name", "age"]]

df["bonus"] = df["salary"] * 2

df.drop_duplicates(subset=["email"])

df.dropna(subset=["name"])

df["salary"] = df["salary"] * 2

df.rename(columns={
    "id": "student_id"
})

df["grade"] = df["grade"].astype(int)

df["quantity"] = df["quantity"].fillna(0)

pd.concat([df1, df2])

df.pivot(
    index="month",
    columns="city",
    values="temperature"
)

pd.melt(
    df,
    id_vars=["product"],
    var_name="quarter",
    value_name="sales"
)

df[df["weight"] > 100].sort_values(
    by="weight",
    ascending=False
)[["name"]]
```

---

# Best Practice Order

```text
2877 → 2878 → 2879 → 2880 → 2881
2882 → 2883 → 2884 → 2885 → 2886
2887 → 2888 → 2889 → 2890 → 2891
```

# Final Memory Trick

```text
Create  → pd.DataFrame()
Size    → shape
First   → head()
Select  → loc[]
Add     → df["new"] = value
Clean   → dropna(), fillna(), drop_duplicates()
Change  → rename(), astype()
Reshape → concat(), pivot(), melt()
Sort    → sort_values()
```


---

If you prefer this content in the main `README.md` instead, tell me and I'll merge it there; otherwise this separate file keeps the README concise and visitor-friendly.
