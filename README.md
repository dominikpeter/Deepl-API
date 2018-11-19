

```python
from Deepl import Deepl
```


```python
deepl = Deepl.Deepl()
```


```python
sentence = "Produkt XY, 50x60"
translation = deepl.translate(sentence, "EN", lang="DE")
output = translation.extract_first(log_proba=False)
output
```




    'Product XY, 50x60'




```python
n_requests = int(1e+06)
sentence = "Produkt XY, 50x60"
for i, j in enumerate(range(n_requests)):
    translation = deepl.translate(sentence, "EN", lang="DE")
    output = translation.extract_first(log_proba=False)
    print("Number of Requests: {}".format(i), end="\r")
```

    Number of Requests: 21
