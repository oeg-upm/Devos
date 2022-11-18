```mermaid
	classDiagram

    
    class Variable {
    
    }

    class Model {
    
    }

    class LinkedVariables {
    
    }

    class DatasetStructure {
    
    }

    class Dataset {
    
    }



LinkedVariables  --> Variable   :secondVariable  

Model  --> Variable   :dependentVariable  

LinkedVariables  --> Variable   :firstVariable  

Model  --> Dataset   :trainingSet  

Model  --> Variable   :independentVariable  

Dataset  --> DatasetStructure   :datasetStructure  

Model  --> Variable   :controlVariable  

DatasetStructure  --> Measure   :containMeasure  

DatasetStructure  --> DataSource   :dataSource  

```