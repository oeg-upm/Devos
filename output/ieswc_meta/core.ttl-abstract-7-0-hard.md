```mermaid
	classDiagram

    
    class `Resource` {
    
    }

    class `Resource Group` {
    
    }

    class `Configuration Item` {
    
    }



`Configuration Item`  --> `Resource Group`   :belongs to resource group  

`Resource`  --> `Resource Group`   :belongs to resource group  

`Resource Group`  --> `Resource Group`   :parent Resource Group  

```