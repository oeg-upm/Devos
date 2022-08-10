```mermaid
	classDiagram

    
    class Site {
    
    }

    class OrganizationalCollaboration {
    
    }

    class Role {
    
    }

    class OrganizationalUnit {
    
    }

    class Organization {
    
    }

    class ChangeEvent {
    
    }

    class FormalOrganization {
    
    }



ChangeEvent  --> Organization   :resultingOrganization  

Organization  --> Agent   :hasMember  

Person  --> Site   :basedAt  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Organization   :subOrganizationOf  

Site  --> Organization   :siteOf  

Organization  --> SKOSConcept   :classification  

Organization  --> Post   :hasPost  

nfe96903dd2ea4374ac2da5aeaeb73444b17  --> Role   :role  

Organization  --> ChangeEvent   :changedBy  

Post  --> Organization   :postIn  

Agent  --> Organization   :headOf  

Membership  --> Organization   :organization  

Organization  --> Organization   :hasSubOrganization  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Organization  --> Organization   :linkedTo  

Organization  --> Organization   :transitiveSubOrganizationOf  

Role  --> RDFProperty   :roleProperty  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Agent  --> Organization   :memberOf  

FormalOrganization  --> Site   :hasRegisteredSite  

Organization  --> ChangeEvent   :resultedFrom  

Organization  --> Site   :hasPrimarySite  

Organization  --> Site   :hasSite  

```