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



Variable  --> Concept   :operationalize  

DatasetStructure  --> DataSource   :dataSource  

LinkedVariables  --> Variable   :firstVariable  

Model  --> Variable   :controlVariable  

Model  --> Variable   :independentVariable  

LinkedVariables  --> Variable   :secondVariable  

Model  --> Variable   :dependentVariable  

Dataset  --> DatasetStructure   :datasetStructure  

DatasetStructure  --> Measure   :containMeasure  

ncaa247dcf0f14bdeb87308e331c88396b1  --> Person   :fromExpert  

Variable  --> Measure   :measuredBy  

```