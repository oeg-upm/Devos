```mermaid
	classDiagram

    
    class OrganizationalUnit {
    
    }

    class Site {
    
    }

    class Organization {
    
    }

    class Membership {
    
    }

    class n82b216db468d41afa742054788fdc5a4b17 {
    
    }

    class ChangeEvent {
    
    }

    class n82b216db468d41afa742054788fdc5a4b11 {
    
    }

    class n82b216db468d41afa742054788fdc5a4b14 {
    
    }

    class Role {
    
    }

    class FormalOrganization {
    
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

n82b216db468d41afa742054788fdc5a4b17  --> Role   :role  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Post  --> Organization   :postIn  

Person  --> Site   :basedAt  

FormalOrganization  --> Site   :hasRegisteredSite  

Organization  --> Organization   :hasSubOrganization  

Organization  --> Organization   :transitiveSubOrganizationOf  

ChangeEvent  --> Organization   :resultingOrganization  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Organization  --> Site   :hasSite  

ChangeEvent  --> Organization   :originalOrganization  

Site  --> Organization   :siteOf  

Organization  --> Post   :hasPost  

Membership  --> Organization   :organization  

Agent  --> Membership   :hasMembership  

Membership  --> Agent   :member  

Organization  --> ChangeEvent   :resultedFrom  

Post  --> Agent   :heldBy  

```