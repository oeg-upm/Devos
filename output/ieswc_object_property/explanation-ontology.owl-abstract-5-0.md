```mermaid
	classDiagram

    
    class Explanation {
    
    }

    class SystemRecommendation {
    
    }

    class CounterfactualExplanation {
    
    }



Explanation  --> ExplanationModality   :hasPresentation  

Explanation  --> knowledge   :isBasedOn  

user  --> Explanation   :consumes  

SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> ExplanationGoal   :SIO000008  

Explanation  --> SIO000085   :addresses  

ExplanationCollection  --> Explanation   :SIO000059  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

```