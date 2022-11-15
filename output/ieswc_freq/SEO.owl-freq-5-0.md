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

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

OrganisedEvent  --> TravelInformation   :providesTravelInformation  

OrganisedEvent  --> Country   :heldInCountry  

OrganisedEvent  --> Award   :offersAward  

OrganisedEvent  --> City   :heldInCity  

Track  --> Chair   :hasChair  

OrganisedEvent  --> Keynote   :hasKeynote  

AcademicEvent  --> Person   :hasProgramCommitteeMember  

OrganisedEvent  --> Registration   :hasRegistration  

AcademicEvent  --> ImportantDates   :hasImportantDates  

EventSeries  --> OrganisedEvent   :hasEvent  

Keynote  --> OrganisedEvent   :keynoteIn  

Track  --> AcademicEvent   :isTrackOf  

AcademicEvent  --> SocialEvent   :hasSocialEvent  

OrganisedEvent  --> Flyer   :hasFlyer  

Agent  --> OrganisedEvent   :participatesIn  

AcademicEvent  --> AgentClass   :audience  

OrganisedEvent  --> EventSeries   :belongsToSeries  

OrganisedEvent  --> Sponsor   :hasSponsor  

AcademicEvent  --> BestPaperAward   :offersBestPaperAward  

AcademicEvent  --> SubmissionGuidelines   :hasSubmissionGuidelines  

AcademicEvent  --> Track   :hasTrack  

```