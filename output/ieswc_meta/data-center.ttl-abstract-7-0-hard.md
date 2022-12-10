```mermaid
	classDiagram

    
    class `Data Center Connection` {
    
    }

    class `Data Center` {
    
    }

    class `Resource Group` {
    
    }

    class `Network Segment` {
    
    }

    class `Location` {
    
    }

    class `n7196aebe1b1948969e5dfe724e84966ab9` {
    
    }

    class `n7196aebe1b1948969e5dfe724e84966ab34` {
    
    }



`Data Center`  --> `Network Segment`   :offers Network Segment  

`Data Center Connection`  --> `Data Center`   :endInternetDataCenter  

`Data Center`  --> `Data Center Connection`   :allows connection via  

`Data Center`  --> `Location`   :located In  

`Data Center`  --> `n7196aebe1b1948969e5dfe724e84966ab9`   :hosts  

`Data Center`  --> `n7196aebe1b1948969e5dfe724e84966ab34`   :hosts  

`Data Center Connection`  --> `Data Center`   :startInternetDataCenter  

```