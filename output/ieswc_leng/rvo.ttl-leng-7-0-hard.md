```mermaid
	classDiagram

    
    class `Model` {
    
    }

    class `Linked Variables` {
    
    }

    class `Variable` {
    
    }

    class `Data Source` {
    
    }

    class `Measure` {
    
    }

    class `Dataset` {
    
    }

    class `Dataset Structure` {
    
    }



`Linked Variables`  --> `Variable`   :firstVariable  

`Dataset Structure`  --> `Measure`   :containMeasure  

`Model`  --> `Variable`   :dependentVariable  

`Linked Variables`  --> `Variable`   :secondVariable  

`Model`  --> `Variable`   :controlVariable  

`Dataset`  --> `Dataset Structure`   :datasetStructure  

`Model`  --> `Variable`   :independentVariable  

`Linked Variables`  --> `Model`   :viaModel  

`Dataset Structure`  --> `Data Source`   :dataSource  

`Model`  --> `Dataset`   :trainingSet  

`Variable`  --> `Measure`   :measuredBy  

```