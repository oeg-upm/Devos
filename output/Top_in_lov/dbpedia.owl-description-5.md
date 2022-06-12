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

    class Athlete {
    
    }



Settlement  --> PopulatedPlace   :administrativeDistrict  

Place  --> Place   :northEastPlace  

Place  --> Place   :locatedInArea  

PopulatedPlace  --> PopulatedPlace   :sheading  

Settlement  --> PopulatedPlace   :frazioni  

PopulatedPlace  --> Person   :leaderName  

Person  --> Person   :usurper  

Person  --> Place   :livingPlace  

PopulatedPlace  --> PopulatedPlace   :borough  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Settlement  --> PopulatedPlace   :largestMetro  

Settlement  --> Person   :bourgmestre  

Settlement  --> Place   :highestPoint  

Person  --> Person   :spouse  

Place  --> Place   :northPlace  

Place  --> Place   :mainIsland  

Person  --> Place   :residence  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Person  --> Person   :collaboration  

Athlete  --> Person   :trainer  

Settlement  --> Place   :wilaya  

Settlement  --> Settlement   :twinTown  

Settlement  --> PopulatedPlace   :federalState  

Settlement  --> Place   :daira  

Settlement  --> Settlement   :canton  

Person  --> Place   :educationPlace  

Place  --> Place   :closeTo  

Person  --> Person   :parent  

Settlement  --> Settlement   :mergedSettlement  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Person  --> Place   :announcedFrom  

Place  --> Place   :southWestPlace  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> Place   :bodyDiscovered  

Person  --> Person   :friend  

Place  --> PopulatedPlace   :biggestCity  

Person  --> Person   :seiyu  

Settlement  --> Place   :settlementAttached  

Settlement  --> PopulatedPlace   :jointCommunity  

Place  --> Place   :endPoint  

Place  --> Place   :hasOutsidePlace  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

Person  --> Person   :student  

Place  --> Place   :westPlace  

Person  --> Person   :opponent  

Person  --> Person   :child  

Settlement  --> Place   :lowestPoint  

Place  --> Place   :land  

Person  --> Person   :cousurper  

Person  --> Person   :detractor  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> PopulatedPlace   :nearestCity  

Place  --> PopulatedPlace   :regency  

Place  --> PopulatedPlace   :lowestPlace  

PopulatedPlace  --> PopulatedPlace   :principalArea  

PopulatedPlace  --> Place   :touristicSite  

PopulatedPlace  --> Person   :viceLeader  

Person  --> Person   :sibling  

Person  --> Person   :relation  

Place  --> Place   :nextEntity  

Settlement  --> Settlement   :adjacentSettlement  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Place  --> Place   :subregion  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Place  --> Place   :previousEntity  

Person  --> Person   :colleague  

Person  --> Person   :relative  

Settlement  --> PopulatedPlace   :geolocDepartment  

Person  --> Person   :copilote  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Person  --> Person   :dubber  

Place  --> Place   :hasInsidePlace  

Place  --> Place   :northWestPlace  

Place  --> PopulatedPlace   :district  

Place  --> Place   :eastPlace  

Place  --> Place   :southEastPlace  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Place  --> Place   :supply  


```