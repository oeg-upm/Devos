```mermaid
	classDiagram

    
    class Organization {
    
    }

    class Site {
    
    }

    class Agent {
    
    }

    class ChangeEvent {
    
    }

    class Post {
    
    }



Agent  --> Organization   :memberOf  

Organization  --> Site   :hasSite  

Membership  --> Agent   :member  

Organization  --> Post   :hasPost  

ChangeEvent  --> Organization   :resultingOrganization  

Agent  --> Membership   :hasMembership  

Agent  --> Post   :holds  

Organization  --> ChangeEvent   :changedBy  

Membership  --> Organization   :organization  

Organization  --> Organization   :subOrganizationOf  

Organization  --> ChangeEvent   :resultedFrom  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> SKOSConcept   :classification  

Organization  --> Organization   :linkedTo  

Agent  --> Organization   :headOf  

Post  --> Agent   :heldBy  

Organization  --> Organization   :transitiveSubOrganizationOf  

FormalOrganization  --> Site   :hasRegisteredSite  

Organization  --> Organization   :hasSubOrganization  

Person  --> Site   :basedAt  

Organization  --> Agent   :hasMember  

Site  --> Organization   :siteOf  

Post  --> Organization   :postIn  

Organization  --> Site   :hasPrimarySite  

```