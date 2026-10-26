# Data Science Library

A personal Python library for collecting reusable data science tools learned
and developed during a course. The project uses a `src/` layout and can be
installed into other projects.

## Install for development

From the repository root:

```bash
python -m pip install -e .
```

## Use in another project

Install the repository or a built distribution in that project's environment,
then import the package:

```python
import data_science_lib

print(data_science_lib.__version__)
```

## Package areas

- `data_science_lib.datasets` — dataset loading and inspection helpers
- `data_science_lib.preprocessing` — data cleaning and transformation helpers
- `data_science_lib.statistics` — statistical utilities
- `data_science_lib.visualization` — plotting helpers

These are starter namespaces; add focused modules and tests as reusable
coursework tools are developed. Optional third-party dependencies should be
added only when a feature needs them.

## Run tests

```bash
python -m pytest
```
