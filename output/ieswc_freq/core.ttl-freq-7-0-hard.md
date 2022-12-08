```mermaid
	classDiagram

    
    class `Configuration Item` {
    
    }

    class `Resource Group` {
    
    }

    class `ned17e9e1a6044495996b57c68b2fa722b7` {
    
    }

    class `ned17e9e1a6044495996b57c68b2fa722b10` {
    
    }

    class `ned17e9e1a6044495996b57c68b2fa722b20` {
    
    }

    class `Scope` {
    
    }

    class `Resource` {
    
    }



`Configuration Item`  --> `Configuration Item`   :depends on  

`Configuration Item`  --> `Resource Group`   :belongs to resource group  

`Resource Group`  --> `Resource Group`   :parent Resource Group  

`Configuration Item`  --> `ned17e9e1a6044495996b57c68b2fa722b20`   :status  

`Configuration Item`  --> `Scope`   :scope  

`Configuration Item`  --> `Configuration Item`   :depends on  

`Resource Group`  --> `Resource Group`   :parent Resource Group  

`Configuration Item`  --> `Configuration Item`   :depends on  

`Resource Group`  --> `Resource Group`   :parent Resource Group  

`Resource`  --> `Resource Group`   :belongs to resource group  

```