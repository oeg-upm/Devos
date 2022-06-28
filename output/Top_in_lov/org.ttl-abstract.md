```mermaid
	classDiagram

    
    class OrganizationalUnit {
    
    }

    class Membership {
    
    }

    class n1cfcb28c820141e2a1d92a19d17f2230b14 {
    
    }

    class Organization {
    
    }

    class n1cfcb28c820141e2a1d92a19d17f2230b17 {
    
    }

    class Role {
    
    }

    class Site {
    
    }

    class OrganizationalCollaboration {
    
    }

    class ChangeEvent {
    
    }

    class Post {
    
    }

    class n1cfcb28c820141e2a1d92a19d17f2230b11 {
    
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

n1cfcb28c820141e2a1d92a19d17f2230b17  --> Role   :role  

Agent  --> Organization   :headOf  

Organization  --> Organization   :linkedTo  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

```