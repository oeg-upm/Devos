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



Explanation  --> ExplanationModality   :hasPresentation  

Explanation  --> knowledge   :isBasedOn  

user  --> Explanation   :consumes  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

SystemRecommendation  --> objectrecord   :SIO001277  

ExplanationCollection  --> Explanation   :SIO000059  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

Explanation  --> ExplanationGoal   :SIO000008  

Explanation  --> SIO000085   :addresses  

```