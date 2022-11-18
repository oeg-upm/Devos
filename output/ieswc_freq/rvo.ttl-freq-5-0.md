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



Model  --> Variable   :controlVariable  

Model  --> Variable   :dependentVariable  

LinkedVariables  --> Variable   :firstVariable  

Model  --> ModelType   :modelType  

LinkedVariables  --> Model   :viaModel  

DatasetStructure  --> DataSource   :dataSource  

Model  --> Dataset   :trainingSet  

DatasetStructure  --> Measure   :containMeasure  

Variable  --> Concept   :operationalize  

Variable  --> Measure   :measuredBy  

Dataset  --> DatasetStructure   :datasetStructure  

LinkedVariables  --> Variable   :secondVariable  

Model  --> Variable   :independentVariable  

LinkedVariables  --> LinkType   :linkType  

```