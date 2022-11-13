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



NumismaticProperty  --> NumismaticPropertyCategory   :hasNumismaticPropertyCategory  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CulturalProperty  --> Agent   :hasRelatedAgency  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CulturalProperty  --> Agent   :hasCataloguingAgency  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

NumismaticProperty  --> ReferenceCoinLegend   :hasReferenceCoinLegend  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CulturalProperty  --> AdditionalForm   :isRelatedToAdditionalForm  

CulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CulturalProperty  --> FunctionalPurpose   :hasFunctionalPurpose  

CulturalProperty  --> Intervention   :hasIntervention  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

CulturalProperty  --> Commission   :hasCommission  

CulturalProperty  --> UrbanPlanningInstrument   :hasUrbanPlanningInstrument  

NumismaticProperty  --> CoinIssuance   :hasCoinIssuance  

NumismaticPropertyFunctionalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CulturalProperty  --> DesignationInTime   :hasDesignationInTime  

CulturalProperty  --> RelatedWorkSituation   :hasRelatedWorkSituation  

CulturalProperty  --> Title   :hasTitle  

CulturalProperty  --> Dating   :hasDating  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

AlternativeMusicalInstrumentClassification  --> Agent   :hasAuthor  

CulturalProperty  --> Subject   :hasSubject  

CulturalProperty  --> CulturalPropertyAvailability   :hasCulturalPropertyAvailability  

CulturalProperty  --> CulturalPropertyType   :hasCulturalPropertyType  

CulturalProperty  --> Documentation   :hasDocumentation  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

MusicHeritage  --> Agent   :hasMusician  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

CulturalProperty  --> ProtectiveMeasure   :hasProtectiveMeasure  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalProperty  --> InformationForm   :isRelatedToInformationForm  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CulturalProperty  --> Inventory   :hasInventory  

CulturalProperty  --> Use   :hasUse  

CulturalProperty  --> Survey   :hasSurvey  

CulturalProperty  --> AffixedElement   :hasAffixedElement  

CulturalProperty  --> IconographicOrDecorativeApparatus   :hasIconographicOrDecorativeApparatus  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

CulturalProperty  --> ChangeOfAvailability   :hasChangeOfAvailability  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

NumismaticPropertyTypologicalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> MeasurementCollection   :hasMeasurementCollection  

CulturalProperty  --> TypeOfContext   :hasTypeOfContext  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

CulturalProperty  --> DetectionMethod   :hasDetectionMethod  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> Bibliography   :hasBibliography  

CulturalProperty  --> CollectionMembership   :isMemberOfCollection  

CulturalProperty  --> AuthorshipAttribution   :hasAuthorshipAttribution  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CulturalProperty  --> CadastralIdentity   :hasCadastralIdentity  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

CulturalProperty  --> Acquisition   :hasAcquisition  

CulturalProperty  --> CulturalEntityTechnicalStatus   :hasTechnicalStatus  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

CulturalProperty  --> TimeIndexedTypedLocation   :hasTimeIndexedTypedLocation  

CulturalProperty  --> ExportImportCertification   :hasExportImportCertification  

CulturalProperty  --> TimeIndexedTypedLocation   :hasLocationSubject  

CulturalProperty  --> CulturalPropertyAccessibility   :hasCulturalPropertyAccessibility  

CulturalProperty  --> Address   :hasCulturalPropertyAddress  

CulturalProperty  --> Geometry   :hasGeometry  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

NumismaticProperty  --> NumismaticSeries   :isCoinMemberOf  

CulturalProperty  --> ConservationStatus   :hasConservationStatus  

CulturalProperty  --> LegalSituation   :hasLegalSituation  

CulturalProperty  --> Orientation   :hasOrientation  

```