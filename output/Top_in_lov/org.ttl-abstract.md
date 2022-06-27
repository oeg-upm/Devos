```mermaid
	classDiagram

    
    class OrganizationalUnit {
    
    }

    class Site {
    
    }

    class n2721a64cd01543a2838301f8936b869ab17 {
    
    }

    class Organization {
    
    }

    class Membership {
    
    }

    class ChangeEvent {
    
    }

    class n2721a64cd01543a2838301f8936b869ab11 {
    
    }

    class Role {
    
    }

    class FormalOrganization {
    
    }

    class n2721a64cd01543a2838301f8936b869ab14 {
    
    }

    class Post {
    
    }

    class OrganizationalCollaboration {
    
    }



Organization  --> ChangeEvent   :changedBy  

Organization  --> SKOSConcept   :classification  

Agent  --> Organization   :memberOf  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Organization   :linkedTo  

Organization  --> Site   :hasPrimarySite  

Organization  --> Agent   :hasMember  

Agent  --> Post   :holds  

Agent  --> Organization   :headOf  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Post  --> Organization   :postIn  

Person  --> Site   :basedAt  

FormalOrganization  --> Site   :hasRegisteredSite  

Organization  --> Organization   :hasSubOrganization  

Organization  --> Organization   :transitiveSubOrganizationOf  

ChangeEvent  --> Organization   :resultingOrganization  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Organization  --> Site   :hasSite  

n2721a64cd01543a2838301f8936b869ab17  --> Role   :role  

ChangeEvent  --> Organization   :originalOrganization  

Site  --> Organization   :siteOf  

Organization  --> Post   :hasPost  

Membership  --> Organization   :organization  

Agent  --> Membership   :hasMembership  

Membership  --> Agent   :member  

Organization  --> ChangeEvent   :resultedFrom  

Post  --> Agent   :heldBy  

```