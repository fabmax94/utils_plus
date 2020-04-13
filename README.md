# Utils Plus

A set of auxiliary functions that are subdivided into:


### Decorator

This module is responsible for grouping the decorator functions.
There are decorators to use lazy load, notifications, timeout, measure time and prevent exception.

```python
from utils_plus.decorators import timeout

@timeout(20)
def process_test():
    # process
```


### Parser

This module is responsible for grouping the parser functions.
There are functions to parser xml, json and images.

```python
from utils_plus.parser import convert_list_to_dict

list_data = [{"name": "Fabio"}, {"age": "26"}, {"company": "SIDIA"}]
result = {}
convert_list_to_dict(result, list_data)
print(result)
>> {"name": "Fabio", "age": "26", "company": "SIDIA"}
```


### Utility

This module is responsible for grouping the utility functions.
There are functions to logging config, prints and threads.

```python
from utils_plus.utility import waiting

tasks = []

tasks.append(threading.Thread(target=process_1))
tasks.append(threading.Thread(target=process_2))
tasks.append(threading.Thread(target=process_3))

waiting(tasks)

```
