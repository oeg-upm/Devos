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

    class OrganizationalUnit {
    
    }

    class FormalOrganization {
    
    }

    class SKOSConcept {
    
    }

    class n4545bd71152047e8b5baf416906bafd0b14 {
    
    }

    class Role {
    
    }



OrganizationalUnit  --> FormalOrganization   :unitOf  

Membership  --> Agent   :member  

ChangeEvent  --> Organization   :originalOrganization  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Post  --> Agent   :heldBy  

Site  --> Organization   :siteOf  

Agent  --> Organization   :memberOf  

Organization  --> ChangeEvent   :resultedFrom  

Organization  --> Organization   :linkedTo  

Organization  --> Site   :hasSite  

Post  --> Organization   :postIn  

Organization  --> Site   :hasPrimarySite  

Organization  --> Organization   :subOrganizationOf  

Agent  --> Organization   :headOf  

Organization  --> Organization   :transitiveSubOrganizationOf  

Organization  --> ChangeEvent   :changedBy  

Organization  --> SKOSConcept   :classification  

ChangeEvent  --> Organization   :resultingOrganization  

FormalOrganization  --> Site   :hasRegisteredSite  

Agent  --> Membership   :hasMembership  

Organization  --> Agent   :hasMember  

Person  --> Site   :basedAt  

n4545bd71152047e8b5baf416906bafd0b17  --> Role   :role  

Organization  --> Post   :hasPost  

Organization  --> Organization   :hasSubOrganization  

Agent  --> Post   :holds  

Membership  --> Organization   :organization  

```