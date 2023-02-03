[![License](https://camo.githubusercontent.com/d6aa9e530d2e113934db4c4c984411041c92b3a120223790c67d37291d373822/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f6d6f7270682d6b67632e737667)](https://github.com/oeg-upm/morph-kgc/blob/main/LICENSE) [![DOI](https://camo.githubusercontent.com/cb4ada9b60b4ebbede3565b01c9b8aace5283e8fa6eda21d0d9c46abf4d53cc2/68747470733a2f2f7a656e6f646f2e6f72672f62616467652f3331313935363236302e7376673f7374796c653d666c6174)](https://zenodo.org/record/7456085#.Y9vBhnZBzGI) 

# DeVoS
Depicting Vocabulary Summaries(**DeVoS**) is a tool that generates a visual summary from a given ontology. DeVoS is built on top of [Mermaid](https://mermaid.js.org/) syntax which is a Markdown-inspired tool that renders text in diagrams and it uses **[SPARQL](https://www.w3.org/TR/rdf-sparql-query/) Query Language** over the ontology generating a visual summary. It's based on three approaches.

1. Ontology Meta Data 
2. Classes frequencies
3. Label Length technique


## Main Features
* Generate summary diagrams.
  * Allows the user to use the summarisation technique (e.g., using meta data, class frequency, or label length)
* Enrich ontologies with labels for the classes that are missing them.

## Tutorial

1. Use meta data as the signal for importance
```
python -m devos.gister -i data/ieswc/cocoon.ttl --freq
python -m devos.gister -i data/ieswc_enriched/ck.ttl -t -d -a  


python -m devos.gister -i data/ieswc_enriched/explanation-ontology.owl  -t -d -a --topn 7


python -m devos.gister -i data/ieswc_enriched/devops/core.ttl   --freq --topn 7

python -m devos.gister -i data/ieswc_enriched/devops/core.ttl   --freq --topn 7
```





**Example**:


```mermaid
	classDiagram

Agent  --> Document   :interest  

Person  --> Document   :publications  

Thing  --> Document   :page  


Agent  --> Thing   :topic_interest  

Thing  --> Agent   :maker  

Group  --> Agent   :member  
```

## Experiment

### Preprocessing 
We perform ontology enrichment by adding labels from class names for the classes that do not
have labels.

#### IESWC (ISWC and ESWC)
```
python -m experiments.enrich -i data/ieswc/* -o data/ieswc_enriched
;
python -m experiments.enrich -i data/ieswc/devops/* -o data/ieswc_enriched/devops
```




### Run the experiment

#### From Ontology Meta data (OntMet)

* To only use `owl:ObjectProperty` when getting the relevant properties to the given meta

##### Top in Lov
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_object_property --object-property```

* To use all properties when getting the relevant properties to the given meta
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_any_property```


##### IESWC (ISWC and ESWC)
* Top 7 classes: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_meta --object-property --topn 7```

```python -m experiments.generate_diagrams -i data/ieswc_enriched/devops/* -o output/ieswc_meta --object-property --topn 7```


* Top 7 classes 14 references: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_meta --object-property --topn 7 --topr 14```



#### From Frequency

##### Top in Lov


* Top 5: ```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_freq --object-property --freq --topn 5```

* Top 10: ```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_freq --object-property --freq --topn 10```


##### IESWC (ISWC and ESWC)

* Top 7 classes: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_freq --object-property --freq --topn 7```

 Top 7 classes from devops: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/devops/* -o output/ieswc_freq --object-property --freq --topn 7```

* Top 7 classes and 14 relations: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_freq --object-property --freq --topn 7 --topr 14```

* Top 10 classes: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_freq --object-property --freq --topn 10```

[//]: # "* Top 10 classes and 10 relations: ```python -m experiments.generate_diagrams -i data/ieswc/* -o output/ieswc_freq --object-property --freq --topn 10 --topr 10```"


#### Label Length
##### IESWC (ISWC and ESWC)

* Top 7 classes: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_leng --leng --topn 7```

Top 7 classes from devops: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/devops/* -o output/ieswc_leng --leng --topn 7```

* Top 7 classes and 14 relations: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_leng --leng --topn 7 --topr 14```


* Top 10: ```python -m experiments.generate_diagrams -i data/ieswc_enriched/* -o output/ieswc_leng --leng --topn 10```



### Generate Statistics
About the number of classes properties to `stats.csv`
```
python -m experiments.analytics
```


## Tests
To run unit tests
```
python -m unittest discover tests 
```

## Authors

- [Ahmad Alobaid](https://github.com/ahmad88me) - (Ontology Engineering Group - UPM)
- [Jhon Toledo](https://github.com/jatoledo) - (Ontology Engineering Group - UPM)
- [María Poveda Villalón] - (Ontology Engineering Group - UPM)
- [Oscar Corcho] - (Ontology Engineering Group - UPM)

*[Ontology Engineering Group](https://oeg.fi.upm.es/)*, *[Universidad Politécnica de Madrid](https://www.upm.es/internacional)*.

## License

DeVoS is available under the permissive **[Apache License 2.0](https://github.com/oeg-upm/Morph-KGC/blob/main/LICENSE)**.
