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



Organization  --> ChangeEvent   :resultedFrom  

Membership  --> Organization   :organization  

Site  --> Organization   :siteOf  

Organization  --> Agent   :hasMember  

Agent  --> Organization   :memberOf  

Agent  --> Post   :holds  

ChangeEvent  --> Organization   :resultingOrganization  

Post  --> Organization   :postIn  

Organization  --> SKOSConcept   :classification  

Person  --> Site   :basedAt  

Membership  --> Agent   :member  

Agent  --> Membership   :hasMembership  

Organization  --> Post   :hasPost  

Organization  --> ChangeEvent   :changedBy  

Agent  --> Organization   :headOf  

Organization  --> Site   :hasPrimarySite  

Post  --> Agent   :heldBy  

Organization  --> Organization   :hasSubOrganization  

FormalOrganization  --> Site   :hasRegisteredSite  

Organization  --> Site   :hasSite  

Organization  --> Organization   :subOrganizationOf  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Organization   :linkedTo  

Organization  --> Organization   :transitiveSubOrganizationOf  

```