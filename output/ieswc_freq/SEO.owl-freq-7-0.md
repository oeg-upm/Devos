```mermaid
	classDiagram

    
    class OrganisedEvent {
    
    }

    class AcademicEvent {
    
    }

    class Agent {
    
    }

    class Author {
    
    }

    class Track {
    
    }

    class Collection {
    
    }

    class Sponsor {
    
    }



Keynote speech  --> OrganisedEvent   :keynoteIn  

AcademicEvent  --> Submission guidelines   :hasSubmissionGuidelines  

AcademicEvent  --> SocialEvent   :hasSocialEvent  

Author  --> Award   :takesAward  

OrganisedEvent  --> Travel information   :providesTravelInformation  

AcademicEvent  --> Person   :hasProgramCommitteeMember  

Sponsor  --> OrganisedEvent   :isSponsorOf  

Author  --> Author registration   :registeredAs  

OrganisedEvent  --> Award   :offersAward  

OrganisedEvent  --> Keynote speech   :hasKeynote  

OrganisedEvent  --> Sponsor   :hasSponsor  

AcademicEvent  --> Important dates   :hasImportantDates  

AcademicEvent  --> Track   :hasTrack  

Track  --> AcademicEvent   :isTrackOf  

OrganisedEvent  --> EventSeries   :belongsToSeries  

OrganisedEvent  --> Flyer   :hasFlyer  

AcademicEvent  --> Best paper award   :offersBestPaperAward  

OrganisedEvent  --> OrganisedEvent   :colocatedWith  

Track  --> Chair   :hasChair  

Sponsor  --> Sponsorship   :sponsorshipType  

EventSeries  --> OrganisedEvent   :hasEvent  

AcademicEvent  --> Agent Class   :audience  

OrganisedEvent  --> Country   :heldInCountry  

Agent  --> OrganisedEvent   :participatesIn  

Author  --> Ndc5078e914214c17a08c6e5934dc0179   :hasRegistrationType  

OrganisedEvent  --> Registration   :hasRegistration  

OrganisedEvent  --> City   :heldInCity  

```