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



Explanation  --> ExplanationGoal   :SIO000008  

ExplanationCollection  --> Explanation   :SIO000059  

SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> knowledge   :isBasedOn  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

user  --> Explanation   :consumes  

Explanation  --> ExplanationModality   :hasPresentation  

Explanation  --> SIO000085   :addresses  

Explanation  --> SystemRecommendation   :isBasedOn  

```