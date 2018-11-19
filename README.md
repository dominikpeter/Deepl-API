

```python
from Deepl import Deepl
```


```python
deepl = Deepl.Deepl()
```


```python
sentence = ["Das ist ein Test", "Hallo mein Name ist Hans", "Deepl ist super"]
for i in sentence:
    translation = deepl.translate(i, "EN", lang="DE")
    translation_output = translation.extract_first(log_proba=False)
    print(translation_output)
```

    This is a test
    Hello my name is Hans
    Deepl's great.
    
