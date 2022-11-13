```mermaid
	classDiagram

    
    class Explanation {
    
    }

    class CounterfactualExplanation {
    
    }

    class SystemRecommendation {
    
    }



Explanation  --> ExplanationGoal   :SIO000008  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> knowledge   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

user  --> Explanation   :consumes  

Explanation  --> ExplanationModality   :hasPresentation  

ExplanationCollection  --> Explanation   :SIO000059  

Explanation  --> SIO000085   :addresses  

```