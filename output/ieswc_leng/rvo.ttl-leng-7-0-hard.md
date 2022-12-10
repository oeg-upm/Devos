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



`Model`  --> `Variable`   :dependentVariable  

`Dataset`  --> `Dataset Structure`   :datasetStructure  

`Model`  --> `Dataset`   :trainingSet  

`Model`  --> `Variable`   :independentVariable  

`Linked Variables`  --> `Model`   :viaModel  

`Linked Variables`  --> `Variable`   :secondVariable  

`Model`  --> `Variable`   :controlVariable  

`Linked Variables`  --> `Variable`   :firstVariable  

`Variable`  --> `Measure`   :measuredBy  

`Dataset Structure`  --> `Data Source`   :dataSource  

`Dataset Structure`  --> `Measure`   :containMeasure  

```