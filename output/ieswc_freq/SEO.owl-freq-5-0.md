```mermaid
	classDiagram

    
    class OrganisedEvent {
    
    }

    class AcademicEvent {
    
    }

    class Agent {
    
    }

    class Collection {
    
    }

    class Track {
    
    }



Sponsor  --> OrganisedEvent   :isSponsorOf  

OrganisedEvent  --> Sponsor   :hasSponsor  

OrganisedEvent  --> EventSeries   :belongsToSeries  

AcademicEvent  --> Track   :hasTrack  

AcademicEvent  --> SocialEvent   :hasSocialEvent  

AcademicEvent  --> SubmissionGuidelines   :hasSubmissionGuidelines  

Track  --> Chair   :hasChair  

OrganisedEvent  --> Keynote   :hasKeynote  

OrganisedEvent  --> Award   :offersAward  

OrganisedEvent  --> Country   :heldInCountry  

OrganisedEvent  --> TravelInformation   :providesTravelInformation  

Keynote  --> OrganisedEvent   :keynoteIn  

AcademicEvent  --> Person   :hasProgramCommitteeMember  

OrganisedEvent  --> Flyer   :hasFlyer  

EventSeries  --> OrganisedEvent   :hasEvent  

OrganisedEvent  --> City   :heldInCity  

OrganisedEvent  --> Registration   :hasRegistration  

AcademicEvent  --> AgentClass   :audience  

AcademicEvent  --> ImportantDates   :hasImportantDates  

Agent  --> OrganisedEvent   :participatesIn  

AcademicEvent  --> BestPaperAward   :offersBestPaperAward  

Track  --> AcademicEvent   :isTrackOf  

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

```