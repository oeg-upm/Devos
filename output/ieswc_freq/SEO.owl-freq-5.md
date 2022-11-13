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



Keynote  --> OrganisedEvent   :keynoteIn  

OrganisedEvent  --> TravelInformation   :providesTravelInformation  

AcademicEvent  --> SubmissionGuidelines   :hasSubmissionGuidelines  

Sponsor  --> OrganisedEvent   :isSponsorOf  

AcademicEvent  --> Person   :hasProgramCommitteeMember  

AcademicEvent  --> SocialEvent   :hasSocialEvent  

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

AcademicEvent  --> Track   :hasTrack  

OrganisedEvent  --> Flyer   :hasFlyer  

OrganisedEvent  --> EventSeries   :belongsToSeries  

OrganisedEvent  --> Country   :heldInCountry  

OrganisedEvent  --> Sponsor   :hasSponsor  

AcademicEvent  --> BestPaperAward   :offersBestPaperAward  

Track  --> Chair   :hasChair  

OrganisedEvent  --> Award   :offersAward  

EventSeries  --> OrganisedEvent   :hasEvent  

Track  --> AcademicEvent   :isTrackOf  

Agent  --> OrganisedEvent   :participatesIn  

AcademicEvent  --> AgentClass   :audience  

AcademicEvent  --> ImportantDates   :hasImportantDates  

OrganisedEvent  --> Keynote   :hasKeynote  

OrganisedEvent  --> City   :heldInCity  

OrganisedEvent  --> Registration   :hasRegistration  

```