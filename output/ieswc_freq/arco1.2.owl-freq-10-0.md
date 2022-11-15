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

    class SubjectDiscipline {
    
    }

    class ArchaeologicalMaterial {
    
    }

    class ComplexCulturalProperty {
    
    }

    class MusicHeritage {
    
    }

    class PhotographicHeritage {
    
    }



CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

MusicalInstrumentClassification  --> MusicHeritage   :isMusicalInstrumentClassificationOf  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

ArchaeologicalMaterialCategory  --> ArchaeologicalMaterial   :isArchaeologicalMaterialCategoryOf  

CulturalProperty  --> Agent   :hasRelatedAgency  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

ComplexCulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

ArchaeologicalMaterial  --> ArchaeologicalMaterialCategory   :hasArchaeologicalMaterialCategory  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CulturalPropertyComponent  --> ComplexCulturalProperty   :isCulturalPropertyComponentOf  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

NumismaticProperty  --> ReferenceCoinLegend   :hasReferenceCoinLegend  

MusicHeritage  --> MusicalInstrumentClassification   :hasMusicalInstrumentClassification  

NumismaticProperty  --> NumismaticPropertyCategory   :hasNumismaticPropertyCategory  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CulturalProperty  --> Agent   :hasCataloguingAgency  

CulturalProperty  --> Inventory   :hasInventory  

CulturalProperty  --> Subject   :hasSubject  

CulturalProperty  --> Acquisition   :hasAcquisition  

MusicHeritage  --> Accessory   :hasAccessory  

PhotographicHeritage  --> N33cff92add8b4dad9390de4a093a9c81   :hasPart  

CulturalProperty  --> AuthorshipAttribution   :hasAuthorshipAttribution  

CulturalProperty  --> Intervention   :hasIntervention  

CulturalProperty  --> Dating   :hasDating  

CulturalProperty  --> TimeIndexedTypedLocation   :hasLocationSubject  

CulturalProperty  --> ProtectiveMeasure   :hasProtectiveMeasure  

CulturalProperty  --> Address   :hasCulturalPropertyAddress  

CulturalProperty  --> MeasurementCollection   :hasMeasurementCollection  

NumismaticPropertyTypologicalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

ArchaeologicalMaterialCategory  --> ArchaeologicalMaterial   :isArchaeologicalMaterialCategoryOf  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CulturalProperty  --> CulturalEntityTechnicalStatus   :hasTechnicalStatus  

CulturalProperty  --> Orientation   :hasOrientation  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CulturalProperty  --> AffixedElement   :hasAffixedElement  

CulturalProperty  --> InformationForm   :isRelatedToInformationForm  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> CulturalPropertyType   :hasCulturalPropertyType  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

CulturalProperty  --> Use   :hasUse  

CulturalProperty  --> AdditionalForm   :isRelatedToAdditionalForm  

CulturalProperty  --> Survey   :hasSurvey  

CulturalProperty  --> RelatedWorkSituation   :hasRelatedWorkSituation  

CulturalProperty  --> CulturalPropertyAccessibility   :hasCulturalPropertyAccessibility  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CulturalPropertyComponent  --> ComplexCulturalProperty   :isCulturalPropertyComponentOf  

CulturalProperty  --> IconographicOrDecorativeApparatus   :hasIconographicOrDecorativeApparatus  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

NumismaticProperty  --> CoinIssuance   :hasCoinIssuance  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CulturalProperty  --> Title   :hasTitle  

CulturalProperty  --> TimeIndexedTypedLocation   :hasTimeIndexedTypedLocation  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

MusicHeritage  --> Agent   :hasMusician  

MusicHeritage  --> Agent   :hasMusician  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

CulturalProperty  --> CulturalPropertyAvailability   :hasCulturalPropertyAvailability  

CulturalProperty  --> Commission   :hasCommission  

CulturalProperty  --> Geometry   :hasGeometry  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CulturalProperty  --> UrbanPlanningInstrument   :hasUrbanPlanningInstrument  

CulturalProperty  --> TypeOfContext   :hasTypeOfContext  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

ArchaeologicalMaterial  --> ArchaeologicalMaterialCategory   :hasArchaeologicalMaterialCategory  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CulturalProperty  --> FunctionalPurpose   :hasFunctionalPurpose  

AlternativeMusicalInstrumentClassification  --> Agent   :hasAuthor  

CulturalProperty  --> DetectionMethod   :hasDetectionMethod  

PhotographicHeritage  --> PhotographicSeriesMembership   :isMemberOfPhotographicSeries  

MusicHeritage  --> Research   :hasResearch  

MusicalInstrumentClassification  --> MusicHeritage   :isMusicalInstrumentClassificationOf  

CulturalProperty  --> CadastralIdentity   :hasCadastralIdentity  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

CulturalProperty  --> LegalSituation   :hasLegalSituation  

PhotographicHeritage  --> Responsibility   :hasResponsibility  

CulturalProperty  --> ExportImportCertification   :hasExportImportCertification  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

CulturalProperty  --> ChangeOfAvailability   :hasChangeOfAvailability  

NumismaticProperty  --> NumismaticSeries   :isCoinMemberOf  

CulturalProperty  --> Documentation   :hasDocumentation  

CulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

NumismaticPropertyFunctionalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> ConservationStatus   :hasConservationStatus  

MusicHeritage  --> MusicalInstrumentClassification   :hasMusicalInstrumentClassification  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalProperty  --> Bibliography   :hasBibliography  

CulturalProperty  --> CollectionMembership   :isMemberOfCollection  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CulturalProperty  --> DesignationInTime   :hasDesignationInTime  

```