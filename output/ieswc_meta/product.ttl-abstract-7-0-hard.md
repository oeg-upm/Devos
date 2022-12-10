```mermaid
	classDiagram

    
    class `Business Product Instance` {
    
    }

    class `Business Product` {
    
    }

    class `Product Offering` {
    
    }

    class `Scope` {
    
    }

    class `Service` {
    
    }

    class `Tenant` {
    
    }

    class `Product Version` {
    
    }



`Business Product Instance`  --> `Tenant`   :tenant  

`Business Product`  --> `Scope`   :offered by  

`Product Offering`  --> `Product Version`   :has product version  

`Business Product Instance`  --> `Business Product`   :deployed instance of  

`Product Offering`  --> `Service`   :uses  

`Product Offering`  --> `Scope`   :offered by  

`Business Product`  --> `Service`   :uses  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

```