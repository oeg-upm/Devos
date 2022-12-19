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

    class `Tenant` {
    
    }

    class `Product Version` {
    
    }



`Business Product Instance`  --> `Tenant`   :tenant  

`Product Offering`  --> `Product Version`   :has product version  

`Business Product Instance`  --> `Business Product`   :deployed instance of  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

`Product Offering`  --> `Service`   :uses  

`Business Product`  --> `Service`   :uses  

`Product Offering`  --> `Scope`   :offered by  

`Business Product`  --> `Scope`   :offered by  

```