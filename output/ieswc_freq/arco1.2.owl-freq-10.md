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



CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CartographicTheme  --> CartographicClassification   :isCartographicThemeOf  

CulturalProperty  --> Agent   :hasCataloguingAgency  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CulturalProperty  --> CulturalPropertyInventoryCategory   :hasCulturalPropertyInventoryCategory  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> Agent   :hasHeritageProtectionAgency  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

MusicHeritage  --> MusicalInstrumentClassification   :hasMusicalInstrumentClassification  

CulturalProperty  --> SubjectDiscipline   :hasAlternativeDiscipline  

NumismaticProperty  --> ReferenceCoinLegend   :hasReferenceCoinLegend  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

ComplexCulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

Agent  --> CulturalProperty   :isRelatedAgencyOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

CulturalProperty  --> MibacScopeOfProtection   :hasMibacScopeOfProtection  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CulturalProperty  --> SubjectDiscipline   :hasMainDiscipline  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalPropertyComponent  --> ComplexCulturalProperty   :isCulturalPropertyComponentOf  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

Agent  --> CulturalProperty   :isCataloguingAgencyOf  

Agent  --> CulturalProperty   :isHeritageProtectionAgencyOf  

NumismaticProperty  --> NumismaticPropertyCategory   :hasNumismaticPropertyCategory  

MusicalInstrumentClassification  --> MusicHeritage   :isMusicalInstrumentClassificationOf  

SubjectDiscipline  --> CulturalProperty   :isMainDisciplineOf  

CulturalProperty  --> CulturalPropertyCategory   :hasCulturalPropertyCategory  

CulturalProperty  --> Agent   :hasRelatedAgency  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

ArchaeologicalMaterialCategory  --> ArchaeologicalMaterial   :isArchaeologicalMaterialCategoryOf  

CulturalProperty  --> CulturalPropertyCataloguingCategory   :hasCulturalPropertyCataloguingCategory  

ArchaeologicalMaterial  --> ArchaeologicalMaterialCategory   :hasArchaeologicalMaterialCategory  

CulturalProperty  --> CartographicClassification   :hasCartographicClassification  

SubjectDiscipline  --> CulturalProperty   :isAlternativeDisciplineOf  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CulturalProperty  --> DetectionMethod   :hasDetectionMethod  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

PhotographicHeritageClassification  --> PhotographicHeritage   :isPhotographicHeritageClassificationOf  

MusicHeritage  --> Research   :hasResearch  

PhotographicHeritage  --> PhotographicSeriesMembership   :isMemberOfPhotographicSeries  

CulturalProperty  --> IconographicOrDecorativeApparatus   :hasIconographicOrDecorativeApparatus  

PhotographicHeritageClassification  --> PhotographicHeritageClassificationType   :hasPhotographicHeritageClassificationType  

CulturalProperty  --> Orientation   :hasOrientation  

CulturalProperty  --> Bibliography   :hasBibliography  

CulturalProperty  --> TypeOfContext   :hasTypeOfContext  

CulturalProperty  --> MeasurementCollection   :hasMeasurementCollection  

CartographicSymbol  --> CartographicClassification   :isCartographicSymbolOf  

MusicalInstrumentClassification  --> MusicHeritage   :isMusicalInstrumentClassificationOf  

CulturalProperty  --> Subject   :hasSubject  

CulturalProperty  --> Dating   :hasDating  

PhotographicHeritageClassificationType  --> PhotographicHeritageClassification   :isPhotographicHeritageClassificationTypeOf  

CulturalProperty  --> AdditionalForm   :isRelatedToAdditionalForm  

NumismaticPropertyTypologicalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> FunctionalPurpose   :hasFunctionalPurpose  

ReferenceCoinLegend  --> NumismaticProperty   :isReferenceCoinLegendOf  

MusicHeritage  --> Accessory   :hasAccessory  

CulturalPropertyResidual  --> CulturalProperty   :isCulturalPropertyResidualOf  

MusicHeritage  --> MusicalInstrumentClassification   :hasMusicalInstrumentClassification  

CulturalProperty  --> CulturalPropertyType   :hasCulturalPropertyType  

CulturalProperty  --> TimeIndexedTypedLocation   :hasLocationSubject  

ThematicCategory  --> CartographicClassification   :isThematicCategoryOf  

AlternativeMusicalInstrumentClassification  --> Agent   :hasAuthor  

NumismaticPropertyFunctionalCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

CulturalProperty  --> UrbanPlanningInstrument   :hasUrbanPlanningInstrument  

CulturalProperty  --> Intervention   :hasIntervention  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CulturalPropertyCategory  --> CulturalProperty   :isCulturalPropertyCategoryOf  

CartographicClassification  --> CulturalProperty   :isCartographicClassificationOf  

CulturalProperty  --> Address   :hasCulturalPropertyAddress  

CulturalProperty  --> Use   :hasUse  

CulturalProperty  --> RelatedWorkSituation   :hasRelatedWorkSituation  

CulturalProperty  --> CadastralIdentity   :hasCadastralIdentity  

CulturalPropertyInventoryCategory  --> CulturalProperty   :isCulturalPropertyInventoryCategoryOf  

CulturalProperty  --> CulturalEntityTechnicalStatus   :hasTechnicalStatus  

CulturalPropertyCataloguingCategory  --> CulturalProperty   :isCulturalPropertyCataloguingCategoryOf  

CulturalProperty  --> Inventory   :hasInventory  

CulturalProperty  --> Acquisition   :hasAcquisition  

MibacScopeOfProtection  --> CulturalProperty   :isMibacScopeOfProtectionOf  

CulturalPropertyComponent  --> ComplexCulturalProperty   :isCulturalPropertyComponentOf  

CulturalProperty  --> AffixedElement   :hasAffixedElement  

CulturalProperty  --> CollectionMembership   :isMemberOfCollection  

CulturalProperty  --> CulturalPropertyComponent   :hasCulturalPropertyComponent  

PhotographicHeritage  --> Responsibility   :hasResponsibility  

ArchaeologicalMaterialCategory  --> ArchaeologicalMaterial   :isArchaeologicalMaterialCategoryOf  

CulturalProperty  --> ConservationStatus   :hasConservationStatus  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

NumismaticPropertyCategory  --> NumismaticProperty   :isNumismaticPropertyCategoryOf  

MusicHeritage  --> Agent   :hasMusicalEnsemble  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CulturalProperty  --> CulturalPropertyAvailability   :hasCulturalPropertyAvailability  

PhotographicHeritage  --> PhotographicHeritageClassification   :hasPhotographicHeritageClassification  

CulturalProperty  --> Survey   :hasSurvey  

CulturalProperty  --> CulturalPropertyAccessibility   :hasCulturalPropertyAccessibility  

CulturalProperty  --> ExportImportCertification   :hasExportImportCertification  

CulturalProperty  --> InformationForm   :isRelatedToInformationForm  

MusicHeritage  --> Agent   :hasMusician  

MusicHeritage  --> Agent   :hasMusician  

NumismaticProperty  --> NumismaticSeries   :isCoinMemberOf  

CartographicClassification  --> ThematicCategory   :hasThematicCategory  

CulturalProperty  --> DesignationInTime   :hasDesignationInTime  

CulturalProperty  --> ChangeOfAvailability   :hasChangeOfAvailability  

CulturalProperty  --> TimeIndexedTypedLocation   :hasTimeIndexedTypedLocation  

CulturalProperty  --> Documentation   :hasDocumentation  

NumismaticProperty  --> CoinIssuance   :hasCoinIssuance  

PhotographicHeritage  --> N3aaacc667ea744e4be32dc69d6325572   :hasPart  

CulturalProperty  --> Title   :hasTitle  

CulturalProperty  --> Commission   :hasCommission  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

NumismaticProperty  --> NumismaticProperty   :hasNumismaticPropertyCategory  

CulturalProperty  --> ProtectiveMeasure   :hasProtectiveMeasure  

CulturalProperty  --> CulturalPropertyResidual   :hasCulturalPropertyResidual  

ArchaeologicalMaterial  --> ArchaeologicalMaterialCategory   :hasArchaeologicalMaterialCategory  

CulturalProperty  --> Geometry   :hasGeometry  

CartographicClassification  --> CartographicSymbol   :hasCartographicSymbol  

CartographicClassification  --> CartographicTheme   :hasCartographicTheme  

CulturalProperty  --> LegalSituation   :hasLegalSituation  

CulturalProperty  --> AuthorshipAttribution   :hasAuthorshipAttribution  

```