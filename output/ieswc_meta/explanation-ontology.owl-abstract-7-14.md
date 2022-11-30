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



ExplanationCollection  --> Explanation   :SIO000059  

Explanation  --> Knowledge   :is based on  

Explanation  --> Explanation Goal   :SIO000008  

Explanation  --> Explanation Modality   :has presentation  

System Recommendation  --> Object Record   :SIO001277  

Explanation  --> System Recommendation   :is based on  

System Recommendation  --> AI Method   :SIO000232  

```