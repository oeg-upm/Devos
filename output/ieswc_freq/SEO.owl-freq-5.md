```mermaid
	classDiagram

    
    class OrganisedEvent {
    
    }

    class DCTERMSAgent {
    
    }

    class DCTERMSAgentClass {
    
    }

    class DCTERMSRightsStatement {
    
    }

    class Award {
    
    }



OrganisedEvent  --> EventSeries   :belongsToSeries  

EventSeries  --> OrganisedEvent   :hasEvent  

OrganisedEvent  --> TravelInformation   :providesTravelInformation  

Author  --> Award   :takesAward  

OrganisedEvent  --> Country   :heldInCountry  

OrganisedEvent  --> Award   :offersAward  

OrganisedEvent  --> Registration   :hasRegistration  

Agent  --> OrganisedEvent   :participatesIn  

AcademicEvent  --> DCTERMSAgentClass   :DCTERMSaudience  

Sponsor  --> OrganisedEvent   :isSponsorOf  

OrganisedEvent  --> City   :heldInCity  

OrganisedEvent  --> Keynote   :hasKeynote  

OrganisedEvent  --> Flyer   :hasFlyer  

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

Keynote  --> OrganisedEvent   :keynoteIn  

OrganisedEvent  --> Sponsor   :hasSponsor  

```