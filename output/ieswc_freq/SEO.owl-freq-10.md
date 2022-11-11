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



OrganisedEvent  --> Country   :heldInCountry  

OrganisedEvent  --> Registration   :hasRegistration  

OrganisedEvent  --> Flyer   :hasFlyer  

Author  --> Award   :takesAward  

EventSeries  --> OrganisedEvent   :hasEvent  

Agent  --> OrganisedEvent   :participatesIn  

AcademicEvent  --> DCTERMSAgentClass   :DCTERMSaudience  

OrganisedEvent  --> TravelInformation   :providesTravelInformation  

OrganisedEvent  --> Award   :offersAward  

OrganisedEvent  --> Sponsor   :hasSponsor  

OrganisedEvent  --> City   :heldInCity  

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

OrganisedEvent  --> EventSeries   :belongsToSeries  

Sponsor  --> OrganisedEvent   :isSponsorOf  

OrganisedEvent  --> Keynote   :hasKeynote  

Keynote  --> OrganisedEvent   :keynoteIn  

```