```mermaid
	classDiagram

    
    class Person {
    
    }

    class Place {
    
    }

    class PopulatedPlace {
    
    }



Person  --> Place   :announcedFrom  

Place  --> Place   :closeTo  

Person  --> Place   :livingPlace  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Person  --> Place   :bodyDiscovered  

Place  --> Place   :northWestPlace  

Place  --> PopulatedPlace   :district  

Place  --> Place   :westPlace  

Place  --> PopulatedPlace   :nearestCity  

Place  --> PopulatedPlace   :regency  

Place  --> Place   :supply  

Place  --> Place   :mainIsland  

Place  --> Place   :previousEntity  

Place  --> Place   :endPoint  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Place  --> PopulatedPlace   :lowestPlace  

Place  --> Place   :northPlace  

Person  --> Person   :parent  

Person  --> Person   :colleague  

Place  --> Place   :northEastPlace  

PopulatedPlace  --> PopulatedPlace   :borough  

Person  --> Person   :sibling  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> Place   :educationPlace  

Person  --> Person   :friend  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

Person  --> Person   :relative  

Person  --> Person   :opponent  

Place  --> Place   :eastPlace  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Person  --> Person   :copilote  

Person  --> Person   :child  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Person  --> Person   :cousurper  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Place  --> PopulatedPlace   :biggestCity  

Place  --> Place   :subregion  

Person  --> Place   :residence  

Place  --> Place   :land  

Place  --> Place   :hasOutsidePlace  

PopulatedPlace  --> Person   :leaderName  

Place  --> Place   :locatedInArea  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

PopulatedPlace  --> Place   :touristicSite  

Person  --> Person   :spouse  

Place  --> Place   :nextEntity  

Person  --> Person   :collaboration  

Person  --> Person   :relation  

Place  --> Place   :hasInsidePlace  

Person  --> Person   :dubber  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Place  --> Place   :southWestPlace  

Person  --> Person   :usurper  

PopulatedPlace  --> Person   :viceLeader  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Person  --> Person   :student  

PopulatedPlace  --> PopulatedPlace   :sheading  

Person  --> Person   :seiyu  

Place  --> Place   :southEastPlace  

Person  --> Person   :detractor  

```