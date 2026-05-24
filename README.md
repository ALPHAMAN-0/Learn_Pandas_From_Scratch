# Learn Pandas From Scratch 🐼

A complete beginner-friendly Pandas learning repository with **notes**, **examples**, **exercises**, and **mini projects** for Python data analysis.

## Who is this for?

- Beginners who know basic Python and want to start data analysis
- Students preparing for data science roles
- Developers who want practical Pandas practice

## Learning Path

### 1) Notes (`notes/`)
Use short notes to understand core concepts:

- What Pandas is and when to use it
- `Series` and `DataFrame`
- Reading/writing files (`CSV`, `Excel`, `JSON`)
- Indexing (`loc`, `iloc`), filtering, sorting
- Handling missing values
- GroupBy and aggregation
- Merge/join/concat
- Time series basics

### 2) Examples (`examples/`)
Run small examples and modify them:

```python
import pandas as pd

sales = pd.DataFrame({
    "product": ["A", "B", "A", "C"],
    "amount": [100, 200, 150, 120],
    "region": ["East", "West", "East", "West"],
})

# Total sales by product
print(sales.groupby("product")["amount"].sum())
```

### 3) Exercises (`exercises/`)
Practice with guided tasks and expected outputs:

1. Load a CSV and inspect shape, columns, and data types.
2. Filter rows where a numeric column is above a threshold.
3. Create a new derived column.
4. Fill missing values with a strategy you explain.
5. Group by category and compute mean/sum/count.

### 4) Mini Projects (`mini-projects/`)
Build confidence with end-to-end tasks:

- **Sales Dashboard Prep**: clean and summarize retail sales data.
- **Student Performance Analysis**: compare scores by class and subject.
- **Netflix Content Trends**: analyze release years, genres, and countries.
- **Weather Data Insights**: detect seasonal patterns and outliers.

## Suggested Repository Structure

```text
Learn_Pandas_From_Scratch/
├── README.md
├── notes/
├── examples/
├── exercises/
└── mini-projects/
```

## Setup

1. Install Python 3.9+.
2. Create and activate a virtual environment.
3. Install Pandas:

```bash
pip install pandas
```

Optional (recommended for notebooks):

```bash
pip install jupyter matplotlib seaborn
```

## How to Use This Repository

1. Read a note topic.
2. Run the matching example.
3. Solve the exercise without looking at the solution first.
4. Complete one mini project and document your findings.

## Beginner Tips

- Start with small datasets.
- Print intermediate results often.
- Check `df.info()` and `df.head()` before transformations.
- Keep a list of common operations (`groupby`, `merge`, `pivot_table`).

## Next Steps

- Add your own datasets under a `data/` folder.
- Track progress by checking off completed exercises.
- Share your mini project notebooks or scripts.

Happy learning! 🚀
