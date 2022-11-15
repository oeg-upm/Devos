```mermaid
	classDiagram

    
    class SystemRecommendation {
    
    }

    class Explanation {
    
    }

    class CounterfactualExplanation {
    
    }



SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> ExplanationModality   :hasPresentation  

ExplanationCollection  --> Explanation   :SIO000059  

user  --> Explanation   :consumes  

Explanation  --> SIO000085   :addresses  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> knowledge   :isBasedOn  

Explanation  --> ExplanationGoal   :SIO000008  

Explanation  --> SystemRecommendation   :isBasedOn  

```