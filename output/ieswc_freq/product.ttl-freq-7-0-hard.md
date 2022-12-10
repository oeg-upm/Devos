```mermaid
	classDiagram

    
    class `Service Cluster` {
    
    }

    class `Product Offering` {
    
    }

    class `Product Version` {
    
    }

    class `Microservice` {
    
    }

    class `Business Product` {
    
    }

    class `n24012d54884f412d9b0e577cd3da7466b15` {
    
    }

    class `n24012d54884f412d9b0e577cd3da7466b29` {
    
    }



`Microservice`  --> `Service Cluster`   :runs in service cluster  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

`Product Offering`  --> `Product Version`   :has product version  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

`Microservice`  --> `Service Cluster`   :runs in service cluster  

`Microservice`  --> `Service Cluster`   :runs in service cluster  

`Product Offering`  --> `Product Version`   :has product version  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

`Product Offering`  --> `Product Version`   :has product version  

```