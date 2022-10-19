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

    class DCTERMSStandard {
    
    }

    class DCTERMSLocationPeriodOrJurisdiction {
    
    }

    class DCTERMSSizeOrDuration {
    
    }

    class DCTERMSMediaTypeOrExtent {
    
    }

    class DCTERMSLinguisticSystem {
    
    }



OrganisedEvent  --> Flyer   :hasFlyer  

Sponsor  --> OrganisedEvent   :isSponsorOf  

Agent  --> OrganisedEvent   :participatesIn  

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

OrganisedEvent  --> TravelInformation   :providesTravelInformation  

OrganisedEvent  --> Keynote   :hasKeynote  

OrganisedEvent  --> Sponsor   :hasSponsor  

EventSeries  --> OrganisedEvent   :hasEvent  

AcademicEvent  --> DCTERMSAgentClass   :DCTERMSaudience  

OrganisedEvent  --> Country   :heldInCountry  

OrganisedEvent  --> Registration   :hasRegistration  

Author  --> Award   :takesAward  

OrganisedEvent  --> EventSeries   :belongsToSeries  

OrganisedEvent  --> Award   :offersAward  

OrganisedEvent  --> City   :heldInCity  

Keynote  --> OrganisedEvent   :keynoteIn  

```