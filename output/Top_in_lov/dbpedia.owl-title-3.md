```mermaid
	classDiagram

    
    class Person {
    
    }

    class Place {
    
    }

    class PopulatedPlace {
    
    }



Person  --> Person   :cousurper  

Place  --> PopulatedPlace   :lowestPlace  

Person  --> Person   :child  

Person  --> Person   :seiyu  

Person  --> Person   :opponent  

PopulatedPlace  --> Person   :leaderName  

PopulatedPlace  --> Person   :viceLeader  

Place  --> PopulatedPlace   :nearestCity  

Person  --> Person   :relation  

Person  --> Person   :spouse  

Place  --> Place   :previousEntity  

Person  --> Person   :sibling  

Person  --> Person   :dubber  

Place  --> Place   :eastPlace  

PopulatedPlace  --> Place   :touristicSite  

Person  --> Person   :parent  

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

Place  --> Place   :nextEntity  

Place  --> Place   :supply  

PopulatedPlace  --> PopulatedPlace   :borough  

Place  --> Place   :northWestPlace  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Person  --> Place   :announcedFrom  

Place  --> PopulatedPlace   :sovereignCountry  

Place  --> Place   :subregion  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Place  --> Place   :land  

Person  --> Person   :colleague  

Place  --> Place   :hasInsidePlace  

Place  --> PopulatedPlace   :regency  

Place  --> Place   :southEastPlace  

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

Place  --> Place   :locatedInArea  

Place  --> PopulatedPlace   :biggestCity  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Place  --> Place   :westPlace  

Person  --> Person   :collaboration  


```