```mermaid
	classDiagram

    
    class `Scope` {
    
    }

    class `Tenant` {
    
    }

    class `Site` {
    
    }

    class `Organisation` {
    
    }

    class `n4a3af5fa52124069a7d67ac77f6de253b1` {
    
    }

    class `n4a3af5fa52124069a7d67ac77f6de253b5` {
    
    }

    class `n4a3af5fa52124069a7d67ac77f6de253b11` {
    
    }



`Site`  --> `Tenant`   :accessible to tenant  

`Scope`  --> `n4a3af5fa52124069a7d67ac77f6de253b11`   :scope type  

`Tenant`  --> `n4a3af5fa52124069a7d67ac77f6de253b5`   :tenant type  

`Scope`  --> `Organisation`   :managed by  

`Tenant`  --> `Scope`   :scope  

`Scope`  --> `n4a3af5fa52124069a7d67ac77f6de253b1`   :scope type  

```