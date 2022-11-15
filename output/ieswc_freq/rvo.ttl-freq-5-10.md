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



LinkedVariables  --> Model   :viaModel  

Model  --> Dataset   :trainingSet  

Dataset  --> DatasetStructure   :datasetStructure  

LinkedVariables  --> Variable   :secondVariable  

Model  --> Variable   :dependentVariable  

DatasetStructure  --> Measure   :containMeasure  

Variable  --> Measure   :measuredBy  

Variable  --> Concept   :operationalize  

DatasetStructure  --> DataSource   :dataSource  

```