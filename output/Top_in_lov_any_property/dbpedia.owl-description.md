```mermaid
	classDiagram

    
    class HistoricalSettlement {
    
    }

    class Referee {
    
    }

    class Newspaper {
    
    }

    class InformationAppliance {
    
    }

    class Reference {
    
    }

    class Database {
    
    }

    class BiologicalDatabase {
    
    }

    class Settlement {
    
    }

    class ProgrammingLanguage {
    
    }

    class Language {
    
    }

    class Law {
    
    }



Settlement  --> Settlement   :canton  

Settlement  --> Place   :highestPoint  

PopulatedPlace  --> Language   :regionalLanguage  

Work  --> Language   :originalLanguage  

Newspaper  --> Person   :associateEditor  

Settlement  --> Place   :lowestPoint  

PopulatedPlace  --> Language   :officialLanguage  

Settlement  --> Place   :wilaya  

Settlement  --> Person   :bourgmestre  

Newspaper  --> Newspaper   :sisterNewspaper  

Settlement  --> Settlement   :adjacentSettlement  

Agent  --> Settlement   :hometown  

Settlement  --> Place   :settlementAttached  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Language  --> PopulatedPlace   :spokenIn  

Settlement  --> PoliticalParty   :politicalMajority  

Settlement  --> PopulatedPlace   :federalState  

Settlement  --> PopulatedPlace   :largestMetro  

Legislature  --> Settlement   :meetingCity  

Settlement  --> Place   :daira  

Settlement  --> Settlement   :twinTown  

Settlement  --> PopulatedPlace   :frazioni  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Settlement  --> Population   :agglomerationPopulation  

Settlement  --> Settlement   :mergedSettlement  

Newspaper  --> Person   :managingEditor  

Settlement  --> Group   :minority  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Settlement  --> PopulatedPlace   :jointCommunity  

Settlement  --> PopulatedPlace   :geolocDepartment  

```