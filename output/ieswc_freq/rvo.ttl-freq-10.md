```mermaid
	classDiagram

    
    class Variable {
    
    }

    class Measure {
    
    }

    class DataSource {
    
    }

    class DatasetStructure {
    
    }

    class Person {
    
    }

    class LinkType {
    
    }

    class ModelType {
    
    }

    class Concept {
    
    }

    class nd2a534a6414c4856b5890c088e75d1f6b9 {
    
    }

    class Dataset {
    
    }



Variable  --> Concept   :operationalize  

Model  --> Variable   :independentVariable  

LinkedVariables  --> Variable   :secondVariable  

Model  --> Variable   :dependentVariable  

DatasetStructure  --> DataSource   :dataSource  

DatasetStructure  --> Measure   :containMeasure  

Dataset  --> DatasetStructure   :datasetStructure  

nd2a534a6414c4856b5890c088e75d1f6b1  --> Person   :fromExpert  

LinkedVariables  --> LinkType   :linkType  

Model  --> ModelType   :modelType  

Model  --> Variable   :controlVariable  

LinkedVariables  --> Variable   :firstVariable  

Model  --> Dataset   :trainingSet  

Variable  --> Measure   :measuredBy  

```