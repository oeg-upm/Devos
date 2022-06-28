```mermaid
	classDiagram

    
    class Person {
    
    }

    class Place {
    
    }

    class PopulatedPlace {
    
    }



Person  --> Person   :colleague  

Place  --> Place   :land  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Place  --> Place   :eastPlace  

Person  --> Place   :livingPlace  

Person  --> Person   :dubber  

PopulatedPlace  --> Place   :touristicSite  

Place  --> Place   :nextEntity  

Place  --> Place   :northEastPlace  

Person  --> Person   :cousurper  

Place  --> Place   :locatedInArea  

Place  --> PopulatedPlace   :district  

Place  --> Place   :subregion  

PopulatedPlace  --> PopulatedPlace   :sheading  

PopulatedPlace  --> Person   :leaderName  

Person  --> Person   :parent  

Place  --> Place   :closeTo  

PopulatedPlace  --> Person   :viceLeader  

Person  --> Person   :sibling  

Person  --> Place   :bodyDiscovered  

Person  --> Person   :usurper  

Place  --> Place   :endPoint  

Place  --> Place   :northWestPlace  

Place  --> Place   :supply  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Place  --> Place   :mainIsland  

Place  --> Place   :previousEntity  

Place  --> Place   :southEastPlace  

Person  --> Person   :collaboration  

Person  --> Person   :friend  

Place  --> Place   :westPlace  

Person  --> Place   :educationPlace  

Place  --> Place   :southWestPlace  

Place  --> Place   :hasInsidePlace  

Place  --> Place   :northPlace  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Place  --> PopulatedPlace   :sovereignCountry  

Place  --> PopulatedPlace   :biggestCity  

PopulatedPlace  --> PopulatedPlace   :borough  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Person  --> Person   :relation  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Person  --> Place   :announcedFrom  

Person  --> Person   :child  

Person  --> Person   :detractor  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Person  --> Person   :relative  

Person  --> Person   :student  

Person  --> Person   :copilote  

Place  --> PopulatedPlace   :nearestCity  

Person  --> Person   :opponent  

Person  --> Person   :spouse  

Place  --> Place   :hasOutsidePlace  

Person  --> Place   :residence  

Place  --> PopulatedPlace   :regency  

Person  --> Person   :seiyu  

Place  --> PopulatedPlace   :lowestPlace  

```