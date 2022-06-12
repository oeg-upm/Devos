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



PopulatedPlace  --> PopulatedPlace   :sheading  

Settlement  --> Place   :highestPoint  

Person  --> Person   :colleague  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Settlement  --> PopulatedPlace   :frazioni  

Place  --> PopulatedPlace   :lowestPlace  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Person  --> Place   :bodyDiscovered  

Person  --> Person   :dubber  

Person  --> Person   :sibling  

Person  --> Place   :educationPlace  

Settlement  --> Settlement   :adjacentSettlement  

Settlement  --> PopulatedPlace   :federalState  

Person  --> Place   :announcedFrom  

Place  --> Place   :westPlace  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

Place  --> PopulatedPlace   :regency  

Person  --> Person   :child  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Place  --> PopulatedPlace   :nearestCity  

Person  --> Person   :relation  

Person  --> Person   :student  

Place  --> Place   :mainIsland  

Person  --> Person   :opponent  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Person  --> Person   :cousurper  

Place  --> Place   :nextEntity  

Settlement  --> Settlement   :twinTown  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> Place   :livingPlace  

PopulatedPlace  --> Place   :touristicSite  

Settlement  --> PopulatedPlace   :jointCommunity  

Person  --> Person   :friend  

Person  --> Person   :seiyu  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> Place   :hasOutsidePlace  

PopulatedPlace  --> PopulatedPlace   :borough  

Settlement  --> Person   :bourgmestre  

Settlement  --> Place   :wilaya  

Person  --> Person   :copilote  

Place  --> Place   :land  

PopulatedPlace  --> Person   :viceLeader  

Place  --> PopulatedPlace   :district  

Person  --> Person   :relative  

PopulatedPlace  --> Person   :leaderName  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Place  --> Place   :previousEntity  

Settlement  --> Place   :daira  

Place  --> Place   :locatedInArea  

Person  --> Person   :collaboration  

Place  --> Place   :northPlace  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Settlement  --> Settlement   :mergedSettlement  

Place  --> PopulatedPlace   :biggestCity  

Settlement  --> Settlement   :canton  

Place  --> Place   :closeTo  

Person  --> Place   :residence  

Person  --> Person   :spouse  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Person  --> Person   :parent  

Settlement  --> PopulatedPlace   :geolocDepartment  

Place  --> Place   :southEastPlace  

Place  --> Place   :subregion  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Place  --> Place   :endPoint  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Place  --> Place   :northWestPlace  

Place  --> Place   :supply  

Place  --> Place   :northEastPlace  

Settlement  --> Place   :lowestPoint  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Settlement  --> Place   :settlementAttached  

Person  --> Person   :usurper  

Place  --> Place   :southWestPlace  

Person  --> Person   :detractor  

Place  --> Place   :hasInsidePlace  

Place  --> Place   :eastPlace  

Settlement  --> PopulatedPlace   :largestMetro  


```