```mermaid
	classDiagram

    
    class `Business Product Instance` {
    
    }

    class `Business Product` {
    
    }

    class `Product Offering` {
    
    }

    class `Service` {
    
    }

    class `Scope` {
    
    }

    class `Site` {
    
    }

    class `Service Instance` {
    
    }



`Business Product Instance`  --> `Site`   :site  

`Business Product Instance`  --> `Service Instance`   :uses  

`Business Product`  --> `Service`   :uses  

`Business Product Instance`  --> `Business Product`   :deployed instance of  

`Product Offering`  --> `Service`   :uses  

`Product Offering`  --> `Scope`   :offered by  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

`Business Product`  --> `Scope`   :offered by  

```