```mermaid
	classDiagram

    
    class Explanation {
    
    }

    class CounterfactualExplanation {
    
    }

    class SystemRecommendation {
    
    }



SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> SIO000085   :addresses  

Explanation  --> ExplanationGoal   :SIO000008  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> ExplanationModality   :hasPresentation  

Explanation  --> knowledge   :isBasedOn  

ExplanationCollection  --> Explanation   :SIO000059  

user  --> Explanation   :consumes  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

```