```mermaid
	classDiagram

    
    class OrganizationalUnit {
    
    }

    class Membership {
    
    }

    class Organization {
    
    }

    class Site {
    
    }

    class Role {
    
    }

    class OrganizationalCollaboration {
    
    }

    class ChangeEvent {
    
    }

    class n6b40eb1d2d2145d8b2892f162afe80acb14 {
    
    }

    class n6b40eb1d2d2145d8b2892f162afe80acb17 {
    
    }

    class Post {
    
    }

    class n6b40eb1d2d2145d8b2892f162afe80acb11 {
    
    }

    class FormalOrganization {
    
    }



Organization  --> Agent   :hasMember  

Agent  --> Membership   :hasMembership  

Organization  --> SKOSConcept   :classification  

Organization  --> Site   :hasSite  

Agent  --> Post   :holds  

Organization  --> Organization   :subOrganizationOf  

Organization  --> ChangeEvent   :resultedFrom  

FormalOrganization  --> Site   :hasRegisteredSite  

Organization  --> Organization   :hasSubOrganization  

Post  --> Organization   :postIn  

n6b40eb1d2d2145d8b2892f162afe80acb17  --> Role   :role  

Membership  --> Organization   :organization  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Post   :hasPost  

Organization  --> ChangeEvent   :changedBy  

ChangeEvent  --> Organization   :resultingOrganization  

Membership  --> Agent   :member  

ChangeEvent  --> Organization   :originalOrganization  

Site  --> Organization   :siteOf  

Agent  --> Organization   :memberOf  

Organization  --> Organization   :transitiveSubOrganizationOf  

Post  --> Agent   :heldBy  

Person  --> Site   :basedAt  

Agent  --> Organization   :headOf  

Organization  --> Organization   :linkedTo  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

```