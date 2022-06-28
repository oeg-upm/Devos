```mermaid
	classDiagram

    
    class Person {
    
    }

    class Place {
    
    }

    class PopulatedPlace {
    
    }



PopulatedPlace  --> PopulatedPlace   :sheading  

Person  --> Person   :relative  

Place  --> Place   :mainIsland  

Place  --> Place   :endPoint  

Person  --> Person   :collaboration  

Person  --> Person   :relation  

Place  --> Place   :locatedInArea  

Person  --> Person   :seiyu  

Person  --> Person   :copilote  

PopulatedPlace  --> Place   :touristicSite  

Place  --> Place   :hasOutsidePlace  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

Place  --> PopulatedPlace   :district  

Person  --> Person   :detractor  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Person  --> Person   :friend  

Person  --> Person   :colleague  

Place  --> Place   :supply  

Place  --> Place   :northPlace  

Person  --> Person   :dubber  

Place  --> Place   :land  

PopulatedPlace  --> PopulatedPlace   :borough  

Place  --> Place   :eastPlace  

Person  --> Person   :spouse  

Person  --> Person   :child  

Place  --> Place   :subregion  

Place  --> Place   :southWestPlace  

Person  --> Person   :usurper  

Place  --> Place   :northWestPlace  

Place  --> Place   :previousEntity  

Person  --> Place   :educationPlace  

Person  --> Place   :announcedFrom  

Place  --> PopulatedPlace   :sovereignCountry  

Place  --> Place   :southEastPlace  

PopulatedPlace  --> Person   :viceLeader  

Person  --> Person   :sibling  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Place  --> Place   :northEastPlace  

Person  --> Place   :livingPlace  

PopulatedPlace  --> Person   :leaderName  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Place  --> Place   :nextEntity  

Person  --> Person   :student  

Person  --> Place   :bodyDiscovered  

Place  --> Place   :hasInsidePlace  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Place  --> PopulatedPlace   :regency  

Place  --> PopulatedPlace   :biggestCity  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Person  --> Person   :cousurper  

Person  --> Person   :opponent  

Place  --> PopulatedPlace   :nearestCity  

Place  --> Place   :westPlace  

Place  --> PopulatedPlace   :lowestPlace  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> Place   :closeTo  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Person  --> Person   :parent  

Person  --> Place   :residence  

```