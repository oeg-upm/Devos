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



Person  --> Person   :cousurper  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Place  --> PopulatedPlace   :lowestPlace  

Person  --> Person   :child  

Settlement  --> Settlement   :canton  

Person  --> Person   :seiyu  

Person  --> Person   :opponent  

PopulatedPlace  --> Person   :leaderName  

Settlement  --> Person   :bourgmestre  

PopulatedPlace  --> Person   :viceLeader  

Settlement  --> PopulatedPlace   :jointCommunity  

Place  --> PopulatedPlace   :nearestCity  

Person  --> Person   :relation  

Settlement  --> Settlement   :adjacentSettlement  

Person  --> Person   :spouse  

Place  --> Place   :previousEntity  

Person  --> Person   :sibling  

Person  --> Person   :dubber  

Place  --> Place   :eastPlace  

PopulatedPlace  --> Place   :touristicSite  

Person  --> Person   :parent  

Settlement  --> Place   :daira  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Place  --> Place   :northEastPlace  

Person  --> Person   :friend  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Person  --> Person   :copilote  

Place  --> PopulatedPlace   :district  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Person  --> Person   :usurper  

PopulatedPlace  --> PopulatedPlace   :sheading  

Place  --> Place   :northPlace  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Person  --> Place   :residence  

Settlement  --> PopulatedPlace   :largestMetro  

Place  --> Place   :nextEntity  

Place  --> Place   :supply  

Settlement  --> Settlement   :twinTown  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

PopulatedPlace  --> PopulatedPlace   :borough  

Place  --> Place   :northWestPlace  

Settlement  --> Place   :highestPoint  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Person  --> Place   :announcedFrom  

Place  --> PopulatedPlace   :sovereignCountry  

Place  --> Place   :subregion  

Settlement  --> PopulatedPlace   :federalState  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Place  --> Place   :land  

Settlement  --> Place   :lowestPoint  

Person  --> Person   :colleague  

Place  --> Place   :hasInsidePlace  

Place  --> PopulatedPlace   :regency  

Settlement  --> Settlement   :mergedSettlement  

Place  --> Place   :southEastPlace  

Settlement  --> Place   :settlementAttached  

Settlement  --> PopulatedPlace   :geolocDepartment  

Place  --> Place   :mainIsland  

Place  --> Place   :hasOutsidePlace  

Person  --> Place   :educationPlace  

Person  --> Place   :livingPlace  

Person  --> Person   :relative  

Place  --> Place   :closeTo  

Person  --> Place   :bodyDiscovered  

Place  --> Place   :endPoint  

Person  --> Person   :detractor  

Person  --> Person   :student  

Place  --> Place   :southWestPlace  

Settlement  --> PopulatedPlace   :frazioni  

Place  --> Place   :locatedInArea  

Place  --> PopulatedPlace   :biggestCity  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Place  --> Place   :westPlace  

Person  --> Person   :collaboration  

Settlement  --> Place   :wilaya  


```