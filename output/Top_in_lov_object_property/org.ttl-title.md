```mermaid
	classDiagram

    
    class ChangeEvent {
    
    }

    class FormalOrganization {
    
    }

    class Site {
    
    }

    class OrganizationalCollaboration {
    
    }

    class Organization {
    
    }

    class OrganizationalUnit {
    
    }



Organization  --> ChangeEvent   :resultedFrom  

Organization  --> Post   :hasPost  

Membership  --> Organization   :organization  

Organization  --> Site   :hasPrimarySite  

nbdeb2eb23a114d698dc145315c98cea7b11  --> nbdeb2eb23a114d698dc145315c98cea7b14   :reportsTo  

FormalOrganization  --> Site   :hasRegisteredSite  

Organization  --> Organization   :transitiveSubOrganizationOf  

Agent  --> Organization   :headOf  

Membership  --> Agent   :member  

Organization  --> Site   :hasSite  

Site  --> Organization   :siteOf  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Organization   :linkedTo  

Site  --> Organization   :siteOf  

Organization  --> Post   :hasPost  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Organization  --> ChangeEvent   :changedBy  

Organization  --> Agent   :hasMember  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Agent  --> Organization   :memberOf  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Agent   :hasMember  

Organization  --> Site   :hasPrimarySite  

FormalOrganization  --> Site   :hasRegisteredSite  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Person  --> Site   :basedAt  

Organization  --> Organization   :hasSubOrganization  

Organization  --> ChangeEvent   :resultedFrom  

Person  --> Site   :basedAt  

nbdeb2eb23a114d698dc145315c98cea7b17  --> Role   :role  

Organization  --> SKOSConcept   :classification  

Organization  --> Organization   :hasSubOrganization  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Organization  --> Organization   :transitiveSubOrganizationOf  

Agent  --> Organization   :memberOf  

ChangeEvent  --> Organization   :originalOrganization  

Membership  --> Organization   :organization  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Site   :hasSite  

Post  --> Organization   :postIn  

Agent  --> Organization   :headOf  

ChangeEvent  --> Organization   :resultingOrganization  

```