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



Explanation  --> SIO000085   :addresses  

SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> ExplanationModality   :hasPresentation  

Explanation  --> knowledge   :isBasedOn  

user  --> Explanation   :consumes  

ExplanationCollection  --> Explanation   :SIO000059  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> ExplanationGoal   :SIO000008  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

```