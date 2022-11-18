```mermaid
	classDiagram

    
    class Explanation {
    
    }

    class SystemRecommendation {
    
    }

    class CounterfactualExplanation {
    
    }

    class ScientificKnowledge {
    
    }

    class DeductiveTask {
    
    }



user  --> Explanation   :consumes  

SystemRecommendation  --> objectrecord   :SIO001277  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

Explanation  --> ExplanationModality   :hasPresentation  

```