```mermaid
	classDiagram

    
    class CulturalProperty {
    
    }

    class CartographicClassification {
    
    }

    class Agent {
    
    }

    class SubjectDiscipline {
    
    }

    class PhotographicHeritageClassification {
    
    }



CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

CulturalProperty  --> Agent   :hasCataloguingAgency  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CulturalProperty  --> Agent   :hasRelatedAgency  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

h  --> s   :a  

i  --> R   :s  

i  --> C   :s  

h  --> s   :a  

h  --> s   :a  

i  --> M   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> T   :s  

h  --> s   :a  

h  --> s   :a  

i  --> P   :s  

h  --> s   :a  

h  --> s   :a  

i  --> P   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> C   :s  

h  --> s   :a  

i  --> M   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> R   :s  

h  --> s   :a  

h  --> s   :a  

i  --> C   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> C   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> C   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> C   :s  

```