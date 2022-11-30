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

    class Measure {
    
    }

    class n1bfc4bafb14e489ba2267f776df6c349b1 {
    
    }



Model  --> Dataset   :trainingSet  

Model  --> Variable   :independentVariable  

DatasetStructure  --> Measure   :containMeasure  

Model  --> Variable   :dependentVariable  

Dataset  --> DatasetStructure   :datasetStructure  

Model  --> Variable   :controlVariable  

DatasetStructure  --> DataSource   :dataSource  

LinkedVariables  --> Link Type   :linkType  

Variable  --> Concept   :operationalize  

Variable  --> Measure   :measuredBy  

LinkedVariables  --> Variable   :firstVariable  

LinkedVariables  --> Model   :viaModel  

LinkedVariables  --> Variable   :secondVariable  

Model  --> ModelType   :modelType  

```