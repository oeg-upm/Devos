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



OrganisedEvent  --> OrganisedEvent   :colocatedWith  

AcademicEvent  --> Track   :hasTrack  

Sponsor  --> OrganisedEvent   :isSponsorOf  

Track  --> AcademicEvent   :isTrackOf  

OrganisedEvent  --> Sponsor   :hasSponsor  

AcademicEvent  --> Submission guidelines   :hasSubmissionGuidelines  

Author  --> Award   :takesAward  

Author  --> N3c42b9f0232542738a393a49b078ead2   :hasRegistrationType  

Track  --> Chair   :hasChair  

Sponsor  --> Sponsorship   :sponsorshipType  

```