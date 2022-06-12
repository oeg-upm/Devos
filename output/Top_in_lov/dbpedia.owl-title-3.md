```mermaid
	classDiagram

    
    class Person {
    
    }

    class Place {
    
    }

    class PopulatedPlace {
    
    }



PopulatedPlace  --> PopulatedPlace   :sheading  

Person  --> Person   :colleague  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Place  --> PopulatedPlace   :lowestPlace  

Person  --> Place   :bodyDiscovered  

Person  --> Person   :dubber  

Person  --> Person   :sibling  

Person  --> Place   :educationPlace  

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

Person  --> Person   :cousurper  

Place  --> Place   :nextEntity  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> Place   :livingPlace  

PopulatedPlace  --> Place   :touristicSite  

Person  --> Person   :friend  

Person  --> Person   :seiyu  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> Place   :hasOutsidePlace  

PopulatedPlace  --> PopulatedPlace   :borough  

Person  --> Person   :copilote  

Place  --> Place   :land  

PopulatedPlace  --> Person   :viceLeader  

Place  --> PopulatedPlace   :district  

Person  --> Person   :relative  

PopulatedPlace  --> Person   :leaderName  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Place  --> Place   :previousEntity  

Place  --> Place   :locatedInArea  

Person  --> Person   :collaboration  

Place  --> Place   :northPlace  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Place  --> PopulatedPlace   :biggestCity  

Place  --> Place   :closeTo  

Person  --> Place   :residence  

Person  --> Person   :spouse  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Person  --> Person   :parent  

Place  --> Place   :southEastPlace  

Place  --> Place   :subregion  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Place  --> Place   :endPoint  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Place  --> Place   :northWestPlace  

Place  --> Place   :supply  

Place  --> Place   :northEastPlace  

Person  --> Person   :usurper  

Place  --> Place   :southWestPlace  

Person  --> Person   :detractor  

Place  --> Place   :hasInsidePlace  

Place  --> Place   :eastPlace  


```