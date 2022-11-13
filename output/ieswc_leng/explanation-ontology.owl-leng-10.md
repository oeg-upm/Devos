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



user  --> Explanation   :consumes  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> SystemRecommendation   :isBasedOn  

Explanation  --> ExplanationModality   :hasPresentation  

ExplanationCollection  --> Explanation   :SIO000059  

Explanation  --> SIO000085   :addresses  

SystemRecommendation  --> objectrecord   :SIO001277  

Explanation  --> knowledge   :isBasedOn  

Explanation  --> ExplanationGoal   :SIO000008  

SystemRecommendation  --> ArtificialIntelligenceMethod   :SIO000232  

```