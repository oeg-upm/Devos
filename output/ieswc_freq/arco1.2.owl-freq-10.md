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

    class NumismaticProperty {
    
    }

    class ArchaeologicalMaterialCategory {
    
    }

    class CartographicSymbol {
    
    }

    class CartographicTheme {
    
    }

    class CulturalPropertyCataloguingCategory {
    
    }



ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

ArchaeologicalMaterialCategory  --> ArchaeologicalMaterial   :isArchaeologicalMaterialCategoryOf  

NumismaticProperty  --> NumismaticPropertyCategory   :hasNumismaticPropertyCategory  

CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

CulturalProperty  --> Agent   :hasCataloguingAgency  

ArchaeologicalMaterial  --> ArchaeologicalMaterialCategory   :hasArchaeologicalMaterialCategory  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CulturalProperty  --> Agent   :hasRelatedAgency  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

NumismaticProperty  --> ReferenceCoinLegend   :hasReferenceCoinLegend  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

h  --> s   :a  

i  --> C   :s  

h  --> s   :a  

i  --> C   :s  

i  --> C   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> R   :s  

h  --> s   :a  

i  --> R   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> M   :s  

h  --> s   :a  

i  --> C   :s  

i  --> P   :s  

i  --> C   :s  

h  --> s   :a  

i  --> R   :s  

h  --> s   :a  

i  --> P   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> A   :s  

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

i  --> T   :s  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

h  --> s   :a  

i  --> N   :s  

h  --> s   :a  

i  --> C   :s  

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

```