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

ExplanationCollection  --> Explanation   :SIO000059  

Explanation  --> ExplanationModality   :hasPresentation  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> ExplanationGoal   :SIO000008  

user  --> Explanation   :consumes  

SystemRecommendation  --> objectrecord   :SIO001277  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

Explanation  --> knowledge   :isBasedOn  

```