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



PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalProperty  --> Agent   :hasCataloguingAgency  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

CulturalProperty  --> Agent   :hasRelatedAgency  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

NumismaticProperty  --> ReferenceCoinLegend   :hasReferenceCoinLegend  

NumismaticProperty  --> NumismaticPropertyCategory   :hasNumismaticPropertyCategory  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalProperty  --> TimeIndexedTypedLocation   :hasLocationSubject  

NumismaticPropertyFunctionalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

NumismaticProperty  --> NumismaticSeries   :isCoinMemberOf  

CulturalProperty  --> Subject   :hasSubject  

CulturalProperty  --> Use   :hasUse  

CulturalProperty  --> TypeOfContext   :hasTypeOfContext  

CulturalProperty  --> Title   :hasTitle  

CulturalProperty  --> ProtectiveMeasure   :hasProtectiveMeasure  

CulturalProperty  --> LegalSituation   :hasLegalSituation  

CulturalProperty  --> UrbanPlanningInstrument   :hasUrbanPlanningInstrument  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

MusicHeritage  --> Agent   :hasMusician  

CulturalProperty  --> Intervention   :hasIntervention  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CulturalProperty  --> Documentation   :hasDocumentation  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

CulturalProperty  --> AdditionalForm   :isRelatedToAdditionalForm  

CulturalProperty  --> Orientation   :hasOrientation  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

CulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

CulturalProperty  --> IconographicOrDecorativeApparatus   :hasIconographicOrDecorativeApparatus  

CulturalProperty  --> RelatedWorkSituation   :hasRelatedWorkSituation  

CulturalProperty  --> ConservationStatus   :hasConservationStatus  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

AlternativeMusicalInstrumentClassification  --> Agent   :hasAuthor  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> ExportImportCertification   :hasExportImportCertification  

CulturalProperty  --> Geometry   :hasGeometry  

CulturalProperty  --> CollectionMembership   :isMemberOfCollection  

CulturalProperty  --> DetectionMethod   :hasDetectionMethod  

CulturalProperty  --> AffixedElement   :hasAffixedElement  

CulturalProperty  --> Acquisition   :hasAcquisition  

CulturalProperty  --> FunctionalPurpose   :hasFunctionalPurpose  

CulturalProperty  --> ChangeOfAvailability   :hasChangeOfAvailability  

CulturalProperty  --> TimeIndexedTypedLocation   :hasTimeIndexedTypedLocation  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CulturalProperty  --> DesignationInTime   :hasDesignationInTime  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CulturalProperty  --> Address   :hasCulturalPropertyAddress  

CulturalProperty  --> CulturalPropertyType   :hasCulturalPropertyType  

CulturalProperty  --> InformationForm   :isRelatedToInformationForm  

CulturalProperty  --> CulturalPropertyAccessibility   :hasCulturalPropertyAccessibility  

CulturalProperty  --> AuthorshipAttribution   :hasAuthorshipAttribution  

CulturalProperty  --> CadastralIdentity   :hasCadastralIdentity  

CulturalProperty  --> MeasurementCollection   :hasMeasurementCollection  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CulturalProperty  --> Inventory   :hasInventory  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

CulturalProperty  --> CulturalEntityTechnicalStatus   :hasTechnicalStatus  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

NumismaticProperty  --> CoinIssuance   :hasCoinIssuance  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

CulturalProperty  --> Commission   :hasCommission  

NumismaticPropertyTypologicalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> Bibliography   :hasBibliography  

CulturalProperty  --> Survey   :hasSurvey  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

CulturalProperty  --> CulturalPropertyAvailability   :hasCulturalPropertyAvailability  

CulturalProperty  --> Dating   :hasDating  

```