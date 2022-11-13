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



Dataset  --> DatasetStructure   :datasetStructure  

LinkedVariables  --> Variable   :secondVariable  

DatasetStructure  --> DataSource   :dataSource  

Model  --> ModelType   :modelType  

Model  --> Variable   :controlVariable  

LinkedVariables  --> Variable   :firstVariable  

Model  --> Variable   :independentVariable  

Model  --> Variable   :dependentVariable  

Model  --> Dataset   :trainingSet  

DatasetStructure  --> Measure   :containMeasure  

LinkedVariables  --> LinkType   :linkType  

Variable  --> Concept   :operationalize  

LinkedVariables  --> Model   :viaModel  

Variable  --> Measure   :measuredBy  

```