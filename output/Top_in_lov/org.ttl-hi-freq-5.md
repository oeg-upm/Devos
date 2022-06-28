```mermaid
	classDiagram

    
    class Organization {
    
    }

    class Agent {
    
    }

    class Site {
    
    }

    class Post {
    
    }

    class ChangeEvent {
    
    }



Organization  --> Agent   :hasMember  

Organization  --> ChangeEvent   :resultedFrom  

Agent  --> Organization   :headOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Site   :hasSite  

Post  --> Organization   :postIn  

Organization  --> ChangeEvent   :changedBy  

Organization  --> Organization   :subOrganizationOf  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Post   :hasPost  

Post  --> Agent   :heldBy  

Organization  --> Organization   :hasSubOrganization  

Organization  --> Organization   :transitiveSubOrganizationOf  

Organization  --> Organization   :linkedTo  

Agent  --> Organization   :memberOf  

ChangeEvent  --> Organization   :resultingOrganization  

Site  --> Organization   :siteOf  

Agent  --> Post   :holds  

```