```mermaid
	classDiagram

    
    class OrganizationalUnit {
    
    }

    class n56397b272ee44bd6941ab08c8d16f31fb14 {
    
    }

    class n56397b272ee44bd6941ab08c8d16f31fb11 {
    
    }

    class Membership {
    
    }

    class Organization {
    
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

    class FormalOrganization {
    
    }

    class n56397b272ee44bd6941ab08c8d16f31fb17 {
    
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

n56397b272ee44bd6941ab08c8d16f31fb17  --> Role   :role  

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