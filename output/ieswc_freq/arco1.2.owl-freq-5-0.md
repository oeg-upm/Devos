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



CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

NumismaticProperty  --> NumismaticPropertyCategory   :hasNumismaticPropertyCategory  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

CulturalProperty  --> Agent   :hasCataloguingAgency  

CulturalProperty  --> Agent   :hasRelatedAgency  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

NumismaticProperty  --> ReferenceCoinLegend   :hasReferenceCoinLegend  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

CulturalProperty  --> Acquisition   :hasAcquisition  

CulturalProperty  --> DetectionMethod   :hasDetectionMethod  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CulturalProperty  --> TimeIndexedTypedLocation   :hasLocationSubject  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

CulturalProperty  --> FunctionalPurpose   :hasFunctionalPurpose  

AlternativeMusicalInstrumentClassification  --> Agent   :hasAuthor  

CulturalProperty  --> TypeOfContext   :hasTypeOfContext  

CulturalProperty  --> Bibliography   :hasBibliography  

CulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

NumismaticProperty  --> CoinIssuance   :hasCoinIssuance  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CulturalProperty  --> CulturalPropertyAvailability   :hasCulturalPropertyAvailability  

CulturalProperty  --> MeasurementCollection   :hasMeasurementCollection  

CulturalProperty  --> AdditionalForm   :isRelatedToAdditionalForm  

CulturalProperty  --> CollectionMembership   :isMemberOfCollection  

CulturalProperty  --> Geometry   :hasGeometry  

CulturalProperty  --> Documentation   :hasDocumentation  

CulturalProperty  --> InformationForm   :isRelatedToInformationForm  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CulturalProperty  --> Commission   :hasCommission  

MusicHeritage  --> Agent   :hasMusician  

CulturalProperty  --> ExportImportCertification   :hasExportImportCertification  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalProperty  --> DesignationInTime   :hasDesignationInTime  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

CulturalProperty  --> ProtectiveMeasure   :hasProtectiveMeasure  

CulturalProperty  --> Orientation   :hasOrientation  

CulturalProperty  --> Intervention   :hasIntervention  

CulturalProperty  --> ChangeOfAvailability   :hasChangeOfAvailability  

CulturalProperty  --> AffixedElement   :hasAffixedElement  

CulturalProperty  --> LegalSituation   :hasLegalSituation  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

NumismaticPropertyTypologicalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

CulturalProperty  --> ConservationStatus   :hasConservationStatus  

CulturalProperty  --> CadastralIdentity   :hasCadastralIdentity  

CulturalProperty  --> CulturalPropertyType   :hasCulturalPropertyType  

CulturalProperty  --> Address   :hasCulturalPropertyAddress  

CulturalProperty  --> Title   :hasTitle  

NumismaticPropertyFunctionalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CulturalProperty  --> CulturalPropertyAccessibility   :hasCulturalPropertyAccessibility  

CulturalProperty  --> Use   :hasUse  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

CulturalProperty  --> IconographicOrDecorativeApparatus   :hasIconographicOrDecorativeApparatus  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CulturalProperty  --> Dating   :hasDating  

CulturalProperty  --> CulturalEntityTechnicalStatus   :hasTechnicalStatus  

NumismaticProperty  --> NumismaticSeries   :isCoinMemberOf  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalProperty  --> Subject   :hasSubject  

CulturalProperty  --> Survey   :hasSurvey  

CulturalProperty  --> UrbanPlanningInstrument   :hasUrbanPlanningInstrument  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CulturalProperty  --> RelatedWorkSituation   :hasRelatedWorkSituation  

CulturalProperty  --> Inventory   :hasInventory  

CulturalProperty  --> TimeIndexedTypedLocation   :hasTimeIndexedTypedLocation  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

CulturalProperty  --> AuthorshipAttribution   :hasAuthorshipAttribution  

```