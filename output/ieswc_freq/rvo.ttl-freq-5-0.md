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



DatasetStructure  --> Measure   :containMeasure  

Model  --> Variable   :dependentVariable  

LinkedVariables  --> Variable   :secondVariable  

DatasetStructure  --> DataSource   :dataSource  

Model  --> Variable   :controlVariable  

Variable  --> Concept   :operationalize  

LinkedVariables  --> Model   :viaModel  

Model  --> Dataset   :trainingSet  

LinkedVariables  --> LinkType   :linkType  

LinkedVariables  --> Variable   :firstVariable  

Dataset  --> DatasetStructure   :datasetStructure  

Model  --> Variable   :independentVariable  

Variable  --> Measure   :measuredBy  

Model  --> ModelType   :modelType  

```