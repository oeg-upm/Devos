```mermaid
	classDiagram

    
    class Site {
    
    }

    class OrganizationalCollaboration {
    
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