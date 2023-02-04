

# Devos Experimentation

# Preprocessing 
We perform ontology enrichment by adding labels from class names for the classes that do not
have labels.

## IESWC (ISWC and ESWC)
```
python -m experiments.enrich -i data/ieswc/* -o data/ieswc_enriched
;
python -m experiments.enrich -i data/ieswc/devops/* -o data/ieswc_enriched/devops
```




# Run the experiment

## From Ontology Meta data (OntMet)

* To only use `owl:ObjectProperty` when getting the relevant properties to the given meta

### Top in Lov
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_object_property --object-property```

* To use all properties when getting the relevant properties to the given meta
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_any_property```


### IESWC (ISWC and ESWC)
* Top 7 classes: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_meta --object-property --topn 7```

```python -m experiments.generate_diagrams -i data/ieswc_enriched/devops/* -o output/ieswc_meta --object-property --topn 7```


* Top 7 classes 14 references: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_meta --object-property --topn 7 --topr 14```



## From Frequency

### Top in Lov


* Top 5: ```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_freq --object-property --freq --topn 5```

* Top 10: ```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_freq --object-property --freq --topn 10```


### IESWC (ISWC and ESWC)

* Top 7 classes: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_freq --object-property --freq --topn 7```

 Top 7 classes from devops: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/devops/* -o output/ieswc_freq --object-property --freq --topn 7```

* Top 7 classes and 14 relations: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_freq --object-property --freq --topn 7 --topr 14```

* Top 10 classes: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_freq --object-property --freq --topn 10```

[//]: # "* Top 10 classes and 10 relations: ```python -m experiments.generate_diagrams -i data/ieswc/* -o output/ieswc_freq --object-property --freq --topn 10 --topr 10```"


## Label Length
##### IESWC (ISWC and ESWC)

* Top 7 classes: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_leng --leng --topn 7```

Top 7 classes from devops: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/devops/* -o output/ieswc_leng --leng --topn 7```

* Top 7 classes and 14 relations: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_leng --leng --topn 7 --topr 14```


* Top 10: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_leng --leng --topn 10```



# Generate Statistics
About the number of classes properties to `stats.csv`
```
python -m experiments.analytics
```