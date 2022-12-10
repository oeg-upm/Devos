```mermaid
	classDiagram

    
    class `Resource Group` {
    
    }

    class `Resource` {
    
    }

    class `Configuration Item` {
    
    }

    class `Concept Scheme` {
    
    }

    class `Scope` {
    
    }

    class `Concept` {
    
    }

    class `nf534fec15c384d4784a5febdfb5dd745b20` {
    
    }



`Configuration Item`  --> `Scope`   :scope  

`Configuration Item`  --> `Configuration Item`   :depends on  

`Configuration Item`  --> `nf534fec15c384d4784a5febdfb5dd745b20`   :status  

`Configuration Item`  --> `Resource Group`   :belongs to resource group  

`Resource`  --> `Resource Group`   :belongs to resource group  

`Resource Group`  --> `Resource Group`   :parent Resource Group  

```