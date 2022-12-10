```mermaid
	classDiagram

    
    class `Variable` {
    
    }

    class `Model` {
    
    }

    class `Linked Variables` {
    
    }

    class `Dataset Structure` {
    
    }

    class `Dataset` {
    
    }

    class `Measure` {
    
    }

    class `n614092c8fd5643d3ba0c626d2dd2cfa0b1` {
    
    }



`Model`  --> `Variable`   :dependentVariable  

`Linked Variables`  --> `Model`   :viaModel  

`Model`  --> `Dataset`   :trainingSet  

`Linked Variables`  --> `Variable`   :firstVariable  

`Model`  --> `Variable`   :independentVariable  

`Model`  --> `Variable`   :controlVariable  

`Dataset`  --> `Dataset Structure`   :datasetStructure  

`Variable`  --> `Measure`   :measuredBy  

`Dataset Structure`  --> `Measure`   :containMeasure  

`Linked Variables`  --> `Variable`   :secondVariable  

```