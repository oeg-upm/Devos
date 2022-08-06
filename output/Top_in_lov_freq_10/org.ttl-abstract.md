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

    class n6d630b9f4d614b96b3e3206c3e3803a9b14 {
    
    }

    class Role {
    
    }



Person  --> Site   :basedAt  

Organization  --> ChangeEvent   :changedBy  

Post  --> Organization   :postIn  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Organization  --> Post   :hasPost  

Organization  --> Organization   :hasSubOrganization  

Organization  --> Agent   :hasMember  

Organization  --> ChangeEvent   :resultedFrom  

Organization  --> Organization   :linkedTo  

Site  --> Organization   :siteOf  

Organization  --> SKOSConcept   :classification  

ChangeEvent  --> Organization   :originalOrganization  

Membership  --> Agent   :member  

n6d630b9f4d614b96b3e3206c3e3803a9b17  --> Role   :role  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Agent  --> Post   :holds  

Post  --> Agent   :heldBy  

Organization  --> Organization   :transitiveSubOrganizationOf  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Site   :hasPrimarySite  

Membership  --> Organization   :organization  

ChangeEvent  --> Organization   :resultingOrganization  

Agent  --> Organization   :headOf  

Agent  --> Membership   :hasMembership  

Organization  --> Site   :hasSite  

Agent  --> Organization   :memberOf  

FormalOrganization  --> Site   :hasRegisteredSite  

```