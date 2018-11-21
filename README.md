

```python
from Deepl import Deepl
```


```python
deepl = Deepl.Deepl(n_trials=5)
```


```python
sentences = ["Das ist ein Test",
             "Hallo mein Name ist Hans",
             "Deepl ist super",
             "Übersetzer ist kein Job mit Zukunft",
             "Künstliche Intelligenz wird die Welt übernehmen"]

for sentence in sentences:
    deepl.translate(sentence, target_lang="EN", lang="DE")
    translation_output = deepl.extract_first(log_proba=False)
    print(translation_output)
```

    This is a test
    Hello my name is Hans
    Deepl's great.
    Translator is not a job with a future
    Artificial intelligence will take over the world
    
