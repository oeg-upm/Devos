[![License](https://camo.githubusercontent.com/d6aa9e530d2e113934db4c4c984411041c92b3a120223790c67d37291d373822/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f6d6f7270682d6b67632e737667)](https://github.com/oeg-upm/morph-kgc/blob/main/LICENSE) 

# Ontology-Gister

A tool to generate a gist of the ontology


## Main Features

* In Progress

## Tutorial

* In Progress



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

### Run the experiment (NEW)

#### From Meta data

* To only use `owl:ObjectProperty` when getting the relevant properties to the given meta
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_object_property --object-property```

* To use all properties when getting the relevant properties to the given meta
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_any_property```

#### From Frequency

* Top 5: ```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_freq_5 --object-property --freq --topn 5```

* Top 10: ```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_freq_10 --object-property --freq --topn 10```


### Run the experiment (OLD)

#### From Meta data

* For DBpedia, we use `en` to speed up the process in taking into account only English labels. Note that it take sometime to generate the summary for DBpedia.
```python -m experiments.generate_diagrams -i data/Top_in_lov/dbpedia.owl -o output_old/Top_in_lov -l en```

* Then, the experiment is performed for the rest of ontologies. Note that it will not overwrite generated resources. 
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output_old/Top_in_lov```

#### Only Frequency
Using only frequency

```
python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output_old/Top_in_lov --freq
```

### Evaluation (OLD)

#### META
```
python -m experiments.evaluation -i output_old/Top_in_lov/*meta*.json  -g data/gs_lov.csv -o output_old/Top_in_lov/results-meta.svg
```

#### Frequency
```
python -m experiments.evaluation -i output_old/Top_in_lov/*freq*.json  -g data/gs_lov.csv -o output_old/Top_in_lov/results-freq.svg
```


## Results

![](output_old/Top_in_lov/results-meta.svg)

![](output_old/Top_in_lov/results-freq.svg)

## Authors

- [Ahmad Alobaid](https://github.com/ahmad88me) - (Ontology Engineering Group - UPM)
- [Jhon Toledo](https://github.com/jatoledo) - (Ontology Engineering Group - UPM)

*[Ontology Engineering Group](https://oeg.fi.upm.es/)*, *[Universidad Politécnica de Madrid](https://www.upm.es/internacional)*.

## License

Ontology-Gister is available under the permissive **[Apache License 2.0](https://github.com/oeg-upm/Morph-KGC/blob/main/LICENSE)**.
