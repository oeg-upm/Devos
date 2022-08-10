```mermaid
	classDiagram

    
    class Newspaper {
    
    }

    class Reference {
    
    }

    class InformationAppliance {
    
    }

    class Referee {
    
    }

    class Settlement {
    
    }

    class BiologicalDatabase {
    
    }

    class HistoricalSettlement {
    
    }

    class Database {
    
    }

    class Law {
    
    }



PublicTransitSystem  --> Station   :importantStation  

Settlement  --> Settlement   :mergedSettlement  

PopulatedPlace  --> Legislature   :legislature  

Settlement  --> PoliticalParty   :politicalMajority  

Settlement  --> Place   :settlementAttached  

Settlement  --> Population   :agglomerationPopulation  

Settlement  --> Place   :daira  

Work  --> Place   :releaseLocation  

Person  --> Work   :created  

Newspaper  --> Person   :associateEditor  

Settlement  --> Place   :lowestPoint  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Newspaper  --> Person   :managingEditor  

Agent  --> Settlement   :hometown  

Settlement  --> PopulatedPlace   :geolocDepartment  

Settlement  --> Place   :settlementAttached  

Work  --> Person   :translator  

Settlement  --> Place   :highestPoint  

Newspaper  --> Newspaper   :sisterNewspaper  

Settlement  --> PopulatedPlace   :largestMetro  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Settlement  --> Group   :minority  

Legislature  --> Settlement   :meetingCity  

Mountain  --> MountainRange   :alpsMajorSector  

Settlement  --> Settlement   :canton  

Settlement  --> Person   :bourgmestre  

Settlement  --> Settlement   :mergedSettlement  

Municipality  --> FormerMunicipality   :hasAbsorbedMunicipality  

Settlement  --> Settlement   :twinTown  

Settlement  --> Settlement   :adjacentSettlement  

Settlement  --> PopulatedPlace   :federalState  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Newspaper  --> Newspaper   :sisterNewspaper  

Settlement  --> PopulatedPlace   :jointCommunity  

Settlement  --> Place   :wilaya  

Settlement  --> Settlement   :adjacentSettlement  

Settlement  --> PopulatedPlace   :frazioni  

Film  --> Person   :setDesigner  

Weapon  --> MilitaryConflict   :usedInWar  

```