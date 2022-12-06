```mermaid
	classDiagram

    
    class Explanation {
    
    }

    class Counterfactual Explanation {
    
    }

    class Ontology {
    
    }

    class System Recommendation {
    
    }

    class Explanation Modality {
    
    }

    class Explanation {
    
    }

    class System Recommendation {
    
    }



Explanation  --> Explanation Modality   :has presentation  

Explanation  --> System Recommendation   :is based on  

Explanation  --> System Recommendation   :is based on  

Explanation  --> Knowledge   :is based on  

Explanation  --> Explanation Goal   :SIO000008  

Explanation  --> SIO_000085   :addresses  

User  --> Explanation   :is consumer of  

System Recommendation  --> Object Record   :SIO001277  

ExplanationCollection  --> Explanation   :SIO000059  

System Recommendation  --> AI Method   :SIO000232  

```