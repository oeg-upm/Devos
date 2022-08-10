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

    class Role {
    
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

n0133950bb52246949fce36a2ace5c380b11  --> n0133950bb52246949fce36a2ace5c380b14   :reportsTo  

Organization  --> SKOSConcept   :classification  

n0133950bb52246949fce36a2ace5c380b17  --> Role   :role  

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

Person  --> Site   :basedAt  

ChangeEvent  --> Organization   :resultingOrganization  

Organization  --> Organization   :transitiveSubOrganizationOf  

Organization  --> ChangeEvent   :resultedFrom  

Agent  --> Organization   :memberOf  

Post  --> Agent   :heldBy  

Organization  --> Site   :hasSite  

Organization  --> Agent   :hasMember  

Agent  --> Organization   :headOf  

Organization  --> Site   :hasPrimarySite  

FormalOrganization  --> Site   :hasRegisteredSite  

ChangeEvent  --> Organization   :originalOrganization  

FormalOrganization  --> OrganizationalUnit   :hasUnit  

Organization  --> Post   :hasPost  

Organization  --> SKOSConcept   :classification  

Organization  --> ChangeEvent   :changedBy  

n0133950bb52246949fce36a2ace5c380b17  --> Role   :role  

Membership  --> Organization   :organization  

OrganizationalUnit  --> FormalOrganization   :unitOf  

Organization  --> ChangeEvent   :changedBy  

Site  --> Organization   :siteOf  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Organization   :hasSubOrganization  

Person  --> Site   :basedAt  

Site  --> Organization   :siteOf  

Post  --> Organization   :postIn  

Organization  --> Organization   :linkedTo  

```