```mermaid
	classDiagram

    
    class Person {
    
    }

    class Place {
    
    }

    class PopulatedPlace {
    
    }

    class Settlement {
    
    }



Person  --> Person   :seiyu  

Place  --> Place   :supply  

Person  --> Person   :collaboration  

Person  --> Person   :opponent  

Settlement  --> Person   :bourgmestre  

Person  --> Person   :usurper  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Settlement  --> Place   :settlementAttached  

Place  --> Place   :westPlace  

Settlement  --> Place   :wilaya  

Place  --> Place   :southWestPlace  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Person  --> Person   :copilote  

PopulatedPlace  --> Person   :leaderName  

Person  --> Place   :bodyDiscovered  

Person  --> Person   :spouse  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> Person   :child  

Person  --> Person   :parent  

Person  --> Person   :sibling  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Place  --> Place   :northWestPlace  

Place  --> Place   :northEastPlace  

Place  --> PopulatedPlace   :district  

PopulatedPlace  --> PopulatedPlace   :borough  

Place  --> Place   :hasOutsidePlace  

Person  --> Place   :educationPlace  

Place  --> PopulatedPlace   :nearestCity  

Place  --> Place   :hasInsidePlace  

Person  --> Person   :friend  

PopulatedPlace  --> Place   :touristicSite  

Place  --> Place   :eastPlace  

Person  --> Person   :dubber  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

PopulatedPlace  --> PopulatedPlace   :sheading  

Place  --> Place   :previousEntity  

Place  --> Place   :endPoint  

Person  --> Person   :detractor  

Place  --> PopulatedPlace   :regency  

Place  --> PopulatedPlace   :lowestPlace  

Place  --> Place   :subregion  

Settlement  --> PopulatedPlace   :federalState  

PopulatedPlace  --> PopulatedPlace   :principalArea  

PopulatedPlace  --> Person   :viceLeader  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> Place   :mainIsland  

Settlement  --> PopulatedPlace   :geolocDepartment  

Person  --> Place   :announcedFrom  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Settlement  --> Place   :daira  

Settlement  --> Settlement   :mergedSettlement  

Person  --> Person   :relative  

Settlement  --> Settlement   :canton  

Person  --> Place   :residence  

Settlement  --> PopulatedPlace   :largestMetro  

Settlement  --> PopulatedPlace   :frazioni  

Settlement  --> PopulatedPlace   :jointCommunity  

Person  --> Place   :livingPlace  

Person  --> Person   :student  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Person  --> Person   :relation  

Settlement  --> Place   :lowestPoint  

Settlement  --> Settlement   :twinTown  

Place  --> PopulatedPlace   :biggestCity  

Place  --> Place   :northPlace  

Place  --> Place   :land  

Person  --> Person   :cousurper  

Place  --> Place   :closeTo  

PopulatedPlace  --> PopulatedPlace   :largestCity  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Place  --> Place   :southEastPlace  

Settlement  --> Settlement   :adjacentSettlement  

Settlement  --> Place   :highestPoint  

Place  --> Place   :nextEntity  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Person  --> Person   :colleague  

Place  --> Place   :locatedInArea  

```