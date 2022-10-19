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



EventSeries  --> OrganisedEvent   :hasEvent  

AcademicEvent  --> DCTERMSAgentClass   :DCTERMSaudience  

Sponsor  --> OrganisedEvent   :isSponsorOf  

Keynote  --> OrganisedEvent   :keynoteIn  

OrganisedEvent  --> Flyer   :hasFlyer  

OrganisedEvent  --> Keynote   :hasKeynote  

OrganisedEvent  --> TravelInformation   :providesTravelInformation  

Author  --> Award   :takesAward  

OrganisedEvent  --> Award   :offersAward  

OrganisedEvent  --> Sponsor   :hasSponsor  

OrganisedEvent  --> City   :heldInCity  

OrganisedEvent  --> Country   :heldInCountry  

OrganisedEvent  --> Registration   :hasRegistration  

OrganisedEvent  --> EventSeries   :belongsToSeries  

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

Agent  --> OrganisedEvent   :participatesIn  

```