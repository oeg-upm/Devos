```mermaid
	classDiagram

    
    class CounterfactualExplanation {
    
    }

    class Explanation {
    
    }

    class SystemRecommendation {
    
    }



Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> ExplanationGoal   :SIO000008  

SystemRecommendation  --> objectrecord   :SIO001277  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

user  --> Explanation   :consumes  

ExplanationCollection  --> Explanation   :SIO000059  

Explanation  --> SystemRecommendation   :isBasedOn  

```