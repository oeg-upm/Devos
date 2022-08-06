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



Organization  --> Organization   :linkedTo  

Membership  --> Organization   :organization  

Post  --> Organization   :postIn  

Membership  --> Agent   :member  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Post   :hasPost  

Organization  --> Site   :hasSite  

Agent  --> Organization   :headOf  

Organization  --> Organization   :transitiveSubOrganizationOf  

Organization  --> Organization   :subOrganizationOf  

Agent  --> Post   :holds  

Agent  --> Membership   :hasMembership  

Organization  --> SKOSConcept   :classification  

Person  --> Site   :basedAt  

Organization  --> Organization   :hasSubOrganization  

Organization  --> ChangeEvent   :resultedFrom  

Organization  --> ChangeEvent   :changedBy  

ChangeEvent  --> Organization   :resultingOrganization  

Organization  --> Agent   :hasMember  

FormalOrganization  --> Site   :hasRegisteredSite  

Agent  --> Organization   :memberOf  

Organization  --> Site   :hasPrimarySite  

Site  --> Organization   :siteOf  

Post  --> Agent   :heldBy  

```