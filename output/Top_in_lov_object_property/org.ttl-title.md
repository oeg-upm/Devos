```mermaid
	classDiagram

    
    class OrganizationalUnit {
    
    }

    class Site {
    
    }

    class ChangeEvent {
    
    }

    class Organization {
    
    }

    class OrganizationalCollaboration {
    
    }

    class FormalOrganization {
    
    }



FormalOrganization  --> OrganizationalUnit   :hasUnit  

Organization  --> Organization   :hasSubOrganization  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Organization  --> Organization   :linkedTo  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Post   :hasPost  

Organization  --> SKOSConcept   :classification  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Organization   :transitiveSubOrganizationOf  

Membership  --> Organization   :organization  

Organization  --> Agent   :hasMember  

Agent  --> Organization   :memberOf  

Agent  --> Organization   :headOf  

Membership  --> Agent   :member  

Organization  --> Site   :hasSite  

FormalOrganization  --> Site   :hasRegisteredSite  

Organization  --> ChangeEvent   :resultedFrom  

n16ececc9993845c786ecbb034b2712c4b17  --> Role   :role  

Person  --> Site   :basedAt  

ChangeEvent  --> Organization   :resultingOrganization  

Organization  --> Organization   :transitiveSubOrganizationOf  

Organization  --> ChangeEvent   :resultedFrom  

Agent  --> Organization   :memberOf  

Organization  --> Site   :hasSite  

Organization  --> Agent   :hasMember  

Agent  --> Organization   :headOf  

Organization  --> Site   :hasPrimarySite  

FormalOrganization  --> Site   :hasRegisteredSite  

ChangeEvent  --> Organization   :originalOrganization  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Organization  --> Post   :hasPost  

Membership  --> Organization   :organization  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Organization  --> ChangeEvent   :changedBy  

Site  --> Organization   :siteOf  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Organization   :hasSubOrganization  

Person  --> Site   :basedAt  

Site  --> Organization   :siteOf  

n16ececc9993845c786ecbb034b2712c4b11  --> n16ececc9993845c786ecbb034b2712c4b14   :reportsTo  

Post  --> Organization   :postIn  

```