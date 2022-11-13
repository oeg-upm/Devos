```mermaid
	classDiagram

    
    class OrganisedEvent {
    
    }

    class AcademicEvent {
    
    }

    class DCTERMSAgent {
    
    }

    class Collection {
    
    }

    class Track {
    
    }



OrganisedEvent  --> Keynote   :hasKeynote  

AcademicEvent  --> Track   :hasTrack  

OrganisedEvent  --> TravelInformation   :providesTravelInformation  

Sponsor  --> OrganisedEvent   :isSponsorOf  

OrganisedEvent  --> DBOCity   :heldInCity  

AcademicEvent  --> DCTERMSAgentClass   :DCTERMSaudience  

OrganisedEvent  --> Sponsor   :hasSponsor  

OrganisedEvent  --> Flyer   :hasFlyer  

AcademicEvent  --> SocialEvent   :hasSocialEvent  

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

Keynote  --> OrganisedEvent   :keynoteIn  

OrganisedEvent  --> EventSeries   :belongsToSeries  

AcademicEvent  --> SubmissionGuidelines   :hasSubmissionGuidelines  

AcademicEvent  --> BestPaperAward   :offersBestPaperAward  

EventSeries  --> OrganisedEvent   :hasEvent  

Agent  --> OrganisedEvent   :participatesIn  

Track  --> Chair   :hasChair  

OrganisedEvent  --> DBOCountry   :heldInCountry  

Track  --> AcademicEvent   :isTrackOf  

OrganisedEvent  --> Registration   :hasRegistration  

OrganisedEvent  --> Award   :offersAward  

AcademicEvent  --> ImportantDates   :hasImportantDates  

AcademicEvent  --> Person   :hasProgramCommitteeMember  

```