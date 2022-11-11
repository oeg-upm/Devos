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



CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CulturalProperty  --> Agent   :hasCataloguingAgency  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalProperty  --> Agent   :hasRelatedAgency  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

h  --> s   :a  

i  --> R   :s  

h  --> s   :a  

h  --> s   :a  

i  --> P   :s  

h  --> s   :a  

h  --> s   :a  

i  --> M   :s  

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

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> C   :s  

h  --> s   :a  

i  --> C   :s  

i  --> C   :s  

h  --> s   :a  

i  --> R   :s  

h  --> s   :a  

i  --> T   :s  

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

h  --> s   :a  

h  --> s   :a  

i  --> M   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> P   :s  

i  --> C   :s  

h  --> s   :a  

h  --> s   :a  

```