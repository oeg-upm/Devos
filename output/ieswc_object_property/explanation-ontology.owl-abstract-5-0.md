```mermaid
	classDiagram

    
    class SystemRecommendation {
    
    }

    class CounterfactualExplanation {
    
    }

    class Explanation {
    
    }



SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

Explanation  --> SIO000085   :addresses  

Explanation  --> ExplanationGoal   :SIO000008  

Explanation  --> knowledge   :isBasedOn  

SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

user  --> Explanation   :consumes  

Explanation  --> ExplanationModality   :hasPresentation  

ExplanationCollection  --> Explanation   :SIO000059  

```