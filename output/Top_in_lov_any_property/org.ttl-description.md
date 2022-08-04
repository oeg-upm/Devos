```mermaid
	classDiagram

    
    class Role {
    
    }

    class FormalOrganization {
    
    }

    class Organization {
    
    }

    class OrganizationalCollaboration {
    
    }

    class Site {
    
    }

    class ChangeEvent {
    
    }

    class OrganizationalUnit {
    
    }



FormalOrganization  --> Site   :hasRegisteredSite  

n6613f7afd2494719b79873490ba3ef20b17  --> Role   :role  

Site  --> Organization   :siteOf  

Agent  --> Organization   :memberOf  

Membership  --> Organization   :organization  

Organization  --> ChangeEvent   :resultedFrom  

Organization  --> Organization   :transitiveSubOrganizationOf  

ChangeEvent  --> Organization   :resultingOrganization  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Organization  --> Post   :hasPost  

Post  --> Organization   :postIn  

Organization  --> Organization   :hasSubOrganization  

Organization  --> Site   :hasPrimarySite  

Person  --> Site   :basedAt  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Organization  --> Site   :hasSite  

Organization  --> Organization   :linkedTo  

Agent  --> Organization   :headOf  

Organization  --> Organization   :subOrganizationOf  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Agent   :hasMember  

Role  --> RDFProperty   :roleProperty  

Organization  --> ChangeEvent   :changedBy  

Organization  --> SKOSConcept   :classification  

```