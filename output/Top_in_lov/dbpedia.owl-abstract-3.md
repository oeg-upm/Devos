```mermaid
	classDiagram

    
    class Person {
    
    }

    class Place {
    
    }

    class PopulatedPlace {
    
    }



Person  --> Person   :seiyu  

Place  --> Place   :supply  

Person  --> Person   :collaboration  

Person  --> Person   :opponent  

Person  --> Person   :usurper  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Place  --> Place   :westPlace  

Place  --> Place   :southWestPlace  

Person  --> Person   :copilote  

PopulatedPlace  --> Person   :leaderName  

Person  --> Place   :bodyDiscovered  

Person  --> Person   :spouse  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> Person   :child  

Person  --> Person   :parent  

Person  --> Person   :sibling  

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

PopulatedPlace  --> PopulatedPlace   :principalArea  

PopulatedPlace  --> Person   :viceLeader  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> Place   :mainIsland  

Person  --> Place   :announcedFrom  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Person  --> Person   :relative  

Person  --> Place   :residence  

Person  --> Place   :livingPlace  

Person  --> Person   :student  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Person  --> Person   :relation  

Place  --> PopulatedPlace   :biggestCity  

Place  --> Place   :northPlace  

Place  --> Place   :land  

Person  --> Person   :cousurper  

Place  --> Place   :closeTo  

PopulatedPlace  --> PopulatedPlace   :largestCity  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Place  --> Place   :southEastPlace  

Place  --> Place   :nextEntity  

Person  --> Person   :colleague  

Place  --> Place   :locatedInArea  

```