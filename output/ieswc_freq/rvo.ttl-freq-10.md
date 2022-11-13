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

    class n4faddac093dd41e58f57522fd375ef94b1 {
    
    }

    class n4faddac093dd41e58f57522fd375ef94b5 {
    
    }

    class n4faddac093dd41e58f57522fd375ef94b13 {
    
    }

    class DataSource {
    
    }



DatasetStructure  --> Measure   :containMeasure  

LinkedVariables  --> LinkType   :linkType  

LinkedVariables  --> Variable   :firstVariable  

LinkedVariables  --> Model   :viaModel  

Model  --> ModelType   :modelType  

DatasetStructure  --> DataSource   :dataSource  

Variable  --> Concept   :operationalize  

Variable  --> Measure   :measuredBy  

LinkedVariables  --> Variable   :secondVariable  

Model  --> Variable   :independentVariable  

Dataset  --> DatasetStructure   :datasetStructure  

Model  --> Variable   :controlVariable  

Model  --> Dataset   :trainingSet  

Model  --> Variable   :dependentVariable  

```