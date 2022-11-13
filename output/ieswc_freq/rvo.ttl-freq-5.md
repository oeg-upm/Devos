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

Model  --> Variable   :controlVariable  

Model  --> Variable   :dependentVariable  

LinkedVariables  --> Variable   :firstVariable  

LinkedVariables  --> LinkType   :linkType  

Variable  --> Measure   :measuredBy  

LinkedVariables  --> Model   :viaModel  

Model  --> Dataset   :trainingSet  

DatasetStructure  --> Measure   :containMeasure  

DatasetStructure  --> DataSource   :dataSource  

Model  --> Variable   :independentVariable  

Dataset  --> DatasetStructure   :datasetStructure  

Variable  --> Concept   :operationalize  

Model  --> ModelType   :modelType  

```