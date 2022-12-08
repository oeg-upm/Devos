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

    class `nb6871623afe848d0a7b518a678063830b15` {
    
    }

    class `nb6871623afe848d0a7b518a678063830b29` {
    
    }



`Product Offering`  --> `Product Version`   :has product version  

`Microservice`  --> `Service Cluster`   :runs in service cluster  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

`Microservice`  --> `Service Cluster`   :runs in service cluster  

`Product Offering`  --> `Product Version`   :has product version  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

`Product Offering`  --> `Product Version`   :has product version  

`Microservice`  --> `Service Cluster`   :runs in service cluster  

`Business Product`  --> `Product Offering`   :A Business Product may have a number of commercial product offerings, which are usually made available in a product catalogue  

```