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

    class Characteristic {
    
    }

    class Foil {
    
    }

    class Fact {
    
    }



Explanation  --> SIO000085   :addresses  

Explanation  --> knowledge   :isBasedOn  

Explanation  --> ExplanationModality   :hasPresentation  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

user  --> Explanation   :consumes  

ExplanationCollection  --> Explanation   :SIO000059  

SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> ExplanationGoal   :SIO000008  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

```