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



AcademicEvent  --> Track   :hasTrack  

OrganisedEvent  --> City   :heldInCity  

OrganisedEvent  --> Sponsor   :hasSponsor  

AcademicEvent  --> AgentClass   :audience  

Track  --> Chair   :hasChair  

Track  --> AcademicEvent   :isTrackOf  

```