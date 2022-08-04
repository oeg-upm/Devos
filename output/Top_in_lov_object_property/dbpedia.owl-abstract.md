```mermaid
	classDiagram

    
    class Referee {
    
    }

    class HistoricalSettlement {
    
    }

    class Newspaper {
    
    }

    class Settlement {
    
    }

    class Database {
    
    }

    class InformationAppliance {
    
    }

    class BiologicalDatabase {
    
    }

    class Reference {
    
    }

    class Law {
    
    }



Settlement  --> PopulatedPlace   :administrativeDistrict  

PopulatedPlace  --> Legislature   :legislature  

Work  --> Person   :translator  

Settlement  --> PopulatedPlace   :largestMetro  

Settlement  --> PopulatedPlace   :jointCommunity  

Settlement  --> Place   :settlementAttached  

Newspaper  --> Newspaper   :sisterNewspaper  

Settlement  --> Population   :agglomerationPopulation  

Municipality  --> FormerMunicipality   :hasAbsorbedMunicipality  

Settlement  --> Place   :settlementAttached  

Settlement  --> Person   :bourgmestre  

Settlement  --> Settlement   :adjacentSettlement  

Settlement  --> Place   :wilaya  

Settlement  --> Settlement   :adjacentSettlement  

Settlement  --> Place   :daira  

Newspaper  --> Person   :associateEditor  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Agent  --> Settlement   :hometown  

Settlement  --> Group   :minority  

Settlement  --> PopulatedPlace   :federalState  

Settlement  --> Settlement   :mergedSettlement  

Settlement  --> PoliticalParty   :politicalMajority  

Settlement  --> Settlement   :mergedSettlement  

Settlement  --> Place   :highestPoint  

Settlement  --> Settlement   :twinTown  

Person  --> Work   :created  

Settlement  --> PopulatedPlace   :geolocDepartment  

Newspaper  --> Person   :managingEditor  

Legislature  --> Settlement   :meetingCity  

Settlement  --> PopulatedPlace   :frazioni  

Work  --> Place   :releaseLocation  

Newspaper  --> Newspaper   :sisterNewspaper  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

PublicTransitSystem  --> Station   :importantStation  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Settlement  --> Place   :lowestPoint  

Settlement  --> Settlement   :canton  

Weapon  --> MilitaryConflict   :usedInWar  

Film  --> Person   :setDesigner  

Mountain  --> MountainRange   :alpsMajorSector  

```