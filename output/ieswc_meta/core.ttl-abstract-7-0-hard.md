```mermaid
	classDiagram

    
    class `Resource Group` {
    
    }

    class `Resource` {
    
    }

    class `Configuration Item` {
    
    }



`Resource`  --> `Resource Group`   :belongs to resource group  

`Resource Group`  --> `Resource Group`   :parent Resource Group  

`Configuration Item`  --> `Resource Group`   :belongs to resource group  

```