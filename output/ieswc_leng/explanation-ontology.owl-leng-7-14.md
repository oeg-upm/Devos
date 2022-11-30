```mermaid
	classDiagram

    
    class Explanation {
    
    }

    class System Recommendation {
    
    }

    class Counterfactual Explanation {
    
    }

    class Scientific Knowledge {
    
    }

    class Named Individual {
    
    }

    class Object Property {
    
    }

    class Datatype Property {
    
    }



Explanation  --> SIO_000085   :addresses  

Explanation  --> Knowledge   :is based on  

Explanation  --> System Recommendation   :is based on  

System Recommendation  --> Object Record   :SIO001277  

```