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

    class Author {
    
    }

    class Sponsor {
    
    }

    class AgentClass {
    
    }

    class Publication {
    
    }

    class Person {
    
    }



Publication  --> Nf586d3da102443e288029d1fa3dd44ae   :hasAppendix  

AcademicEvent  --> AgentClass   :audience  

OrganisedEvent  --> Award   :offersAward  

Author  --> AuthorRegistration   :registeredAs  

Person  --> Ndabce7e4590141838343451ae9fc4736   :participatesAs  

Sponsor  --> OrganisedEvent   :isSponsorOf  

Track  --> Chair   :hasChair  

```