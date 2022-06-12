```mermaid
	classDiagram

    
    class Site {
    
    }

    class FormalOrganization {
    
    }

    class Organization {
    
    }

    class Post {
    
    }

    class nbf745b56d64248d3b99e6ffa38d08592b17 {
    
    }

    class nbf745b56d64248d3b99e6ffa38d08592b14 {
    
    }

    class Role {
    
    }

    class OrganizationalCollaboration {
    
    }

    class nbf745b56d64248d3b99e6ffa38d08592b11 {
    
    }

    class ChangeEvent {
    
    }

    class OrganizationalUnit {
    
    }

    class Membership {
    
    }



Organization  --> SKOSConcept   :classification  

Membership  --> Organization   :organization  

FormalOrganization  --> Site   :hasRegisteredSite  

ChangeEvent  --> Organization   :resultingOrganization  

Agent  --> Organization   :headOf  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Membership  --> Agent   :member  

Agent  --> Organization   :memberOf  

Agent  --> Membership   :hasMembership  

Organization  --> ChangeEvent   :changedBy  

Person  --> Site   :basedAt  

nbf745b56d64248d3b99e6ffa38d08592b17  --> Role   :role  

Organization  --> Post   :hasPost  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Organization   :linkedTo  

Organization  --> ChangeEvent   :resultedFrom  

Organization  --> Site   :hasSite  

Organization  --> Site   :hasPrimarySite  

Organization  --> Organization   :hasSubOrganization  

Site  --> Organization   :siteOf  

Post  --> Agent   :heldBy  

Organization  --> Organization   :subOrganizationOf  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Organization  --> Agent   :hasMember  

Agent  --> Post   :holds  

Organization  --> Organization   :transitiveSubOrganizationOf  

Post  --> Organization   :postIn  

```