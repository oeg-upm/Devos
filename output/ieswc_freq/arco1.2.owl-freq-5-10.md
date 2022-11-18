```mermaid
	classDiagram

    
    class CulturalProperty {
    
    }

    class CartographicClassification {
    
    }

    class Agent {
    
    }

    class NumismaticProperty {
    
    }

    class PhotographicHeritageClassification {
    
    }



CulturalProperty  --> Agent   :hasRelatedAgency  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

NumismaticProperty  --> NumismaticPropertyCategory   :hasNumismaticPropertyCategory  

```