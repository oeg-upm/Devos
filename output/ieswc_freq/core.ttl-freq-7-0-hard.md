```mermaid
	classDiagram

    
    class `Configuration Item` {
    
    }

    class `Resource Group` {
    
    }

    class `n138f2aa1334245249f199a3a32ee6c50b7` {
    
    }

    class `n138f2aa1334245249f199a3a32ee6c50b10` {
    
    }

    class `Resource` {
    
    }

    class `Scope` {
    
    }

    class `n138f2aa1334245249f199a3a32ee6c50b20` {
    
    }



`Resource`  --> `Resource Group`   :belongs to resource group  

`Configuration Item`  --> `Scope`   :scope  

`Configuration Item`  --> `Resource Group`   :belongs to resource group  

`Configuration Item`  --> `n138f2aa1334245249f199a3a32ee6c50b20`   :status  

`Configuration Item`  --> `Configuration Item`   :depends on  

`Resource Group`  --> `Resource Group`   :parent Resource Group  

```