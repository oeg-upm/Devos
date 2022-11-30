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

    class n8a97ca6142844c90934656223ad1fbb6b1 {
    
    }



LinkedVariables  --> Model   :viaModel  

Model  --> Variable   :dependentVariable  

Variable  --> Measure   :measuredBy  

Model  --> Variable   :independentVariable  

Model  --> Dataset   :trainingSet  

DatasetStructure  --> Measure   :containMeasure  

LinkedVariables  --> Variable   :firstVariable  

Dataset  --> DatasetStructure   :datasetStructure  

LinkedVariables  --> Variable   :secondVariable  

DatasetStructure  --> DataSource   :dataSource  

```