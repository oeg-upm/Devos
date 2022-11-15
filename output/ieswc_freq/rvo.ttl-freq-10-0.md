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

    class nabeaa1db450d474ab50f1aaf2699d262b1 {
    
    }

    class nabeaa1db450d474ab50f1aaf2699d262b5 {
    
    }

    class nabeaa1db450d474ab50f1aaf2699d262b13 {
    
    }

    class DataSource {
    
    }



Variable  --> Concept   :operationalize  

Dataset  --> DatasetStructure   :datasetStructure  

DatasetStructure  --> DataSource   :dataSource  

LinkedVariables  --> Model   :viaModel  

Model  --> Variable   :independentVariable  

LinkedVariables  --> Variable   :firstVariable  

Model  --> ModelType   :modelType  

DatasetStructure  --> Measure   :containMeasure  

Model  --> Variable   :controlVariable  

Model  --> Variable   :dependentVariable  

Variable  --> Measure   :measuredBy  

LinkedVariables  --> LinkType   :linkType  

LinkedVariables  --> Variable   :secondVariable  

Model  --> Dataset   :trainingSet  

```