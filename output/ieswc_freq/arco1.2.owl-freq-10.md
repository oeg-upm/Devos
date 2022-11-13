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



CulturalProperty  --> Agent   :hasCataloguingAgency  

CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

ArchaeologicalMaterialCategory  --> ArchaeologicalMaterial   :isArchaeologicalMaterialCategoryOf  

ComplexCulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

MusicalInstrumentClassification  --> MusicHeritage   :isMusicalInstrumentClassificationOf  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

CulturalPropertyComponent  --> ComplexCulturalProperty   :isCulturalPropertyComponentOf  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

NumismaticProperty  --> NumismaticPropertyCategory   :hasNumismaticPropertyCategory  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

ArchaeologicalMaterial  --> ArchaeologicalMaterialCategory   :hasArchaeologicalMaterialCategory  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

NumismaticProperty  --> ReferenceCoinLegend   :hasReferenceCoinLegend  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

MusicHeritage  --> MusicalInstrumentClassification   :hasMusicalInstrumentClassification  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

CulturalProperty  --> Agent   :hasRelatedAgency  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

CulturalProperty  --> ProtectiveMeasure   :hasProtectiveMeasure  

CulturalProperty  --> RelatedWorkSituation   :hasRelatedWorkSituation  

PhotographicHeritage  --> N111a82d75d5748f5aa6de45a9b23f865   :hasPart  

MusicHeritage  --> MusicalInstrumentClassification   :hasMusicalInstrumentClassification  

AlternativeMusicalInstrumentClassification  --> Agent   :hasAuthor  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

CulturalProperty  --> FunctionalPurpose   :hasFunctionalPurpose  

CulturalProperty  --> LegalSituation   :hasLegalSituation  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalProperty  --> TimeIndexedTypedLocation   :hasLocationSubject  

CulturalProperty  --> CadastralIdentity   :hasCadastralIdentity  

NumismaticPropertyTypologicalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

CulturalProperty  --> InformationForm   :isRelatedToInformationForm  

CulturalProperty  --> Inventory   :hasInventory  

CulturalProperty  --> CulturalPropertyType   :hasCulturalPropertyType  

MusicHeritage  --> Research   :hasResearch  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

MusicHeritage  --> Accessory   :hasAccessory  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

MusicalInstrumentClassification  --> MusicHeritage   :isMusicalInstrumentClassificationOf  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CulturalProperty  --> ChangeOfAvailability   :hasChangeOfAvailability  

CulturalProperty  --> AuthorshipAttribution   :hasAuthorshipAttribution  

CulturalProperty  --> TypeOfContext   :hasTypeOfContext  

CulturalProperty  --> Acquisition   :hasAcquisition  

CulturalProperty  --> Bibliography   :hasBibliography  

CulturalProperty  --> DetectionMethod   :hasDetectionMethod  

CulturalProperty  --> Commission   :hasCommission  

CulturalProperty  --> Survey   :hasSurvey  

PhotographicHeritage  --> PhotographicSeriesMembership   :isMemberOfPhotographicSeries  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

NumismaticPropertyFunctionalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

ArchaeologicalMaterialCategory  --> ArchaeologicalMaterial   :isArchaeologicalMaterialCategoryOf  

CulturalProperty  --> Orientation   :hasOrientation  

CulturalProperty  --> ExportImportCertification   :hasExportImportCertification  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

CulturalProperty  --> AdditionalForm   :isRelatedToAdditionalForm  

CulturalProperty  --> Subject   :hasSubject  

CulturalProperty  --> DesignationInTime   :hasDesignationInTime  

CulturalProperty  --> Title   :hasTitle  

CulturalProperty  --> AffixedElement   :hasAffixedElement  

CulturalProperty  --> CollectionMembership   :isMemberOfCollection  

ArchaeologicalMaterial  --> ArchaeologicalMaterialCategory   :hasArchaeologicalMaterialCategory  

CulturalProperty  --> MeasurementCollection   :hasMeasurementCollection  

CulturalProperty  --> CulturalPropertyAvailability   :hasCulturalPropertyAvailability  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

MusicHeritage  --> Agent   :hasMusician  

MusicHeritage  --> Agent   :hasMusician  

NumismaticProperty  --> CoinIssuance   :hasCoinIssuance  

CulturalProperty  --> Address   :hasCulturalPropertyAddress  

NumismaticProperty  --> NumismaticSeries   :isCoinMemberOf  

CulturalProperty  --> CulturalPropertyAccessibility   :hasCulturalPropertyAccessibility  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalProperty  --> TimeIndexedTypedLocation   :hasTimeIndexedTypedLocation  

CulturalProperty  --> Use   :hasUse  

CulturalProperty  --> Geometry   :hasGeometry  

PhotographicHeritage  --> Responsibility   :hasResponsibility  

CulturalProperty  --> Intervention   :hasIntervention  

CulturalProperty  --> UrbanPlanningInstrument   :hasUrbanPlanningInstrument  

CulturalProperty  --> ConservationStatus   :hasConservationStatus  

CulturalPropertyComponent  --> ComplexCulturalProperty   :isCulturalPropertyComponentOf  

CulturalProperty  --> CulturalEntityTechnicalStatus   :hasTechnicalStatus  

CulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

CulturalProperty  --> IconographicOrDecorativeApparatus   :hasIconographicOrDecorativeApparatus  

CulturalProperty  --> Documentation   :hasDocumentation  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CulturalProperty  --> Dating   :hasDating  

```