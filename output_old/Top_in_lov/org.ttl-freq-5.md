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



Organization  --> ChangeEvent   :changedBy  

Agent  --> Post   :holds  

Organization  --> Site   :hasSite  

Post  --> Agent   :heldBy  

Organization  --> ChangeEvent   :resultedFrom  

Organization  --> Organization   :hasSubOrganization  

Agent  --> Organization   :headOf  

Organization  --> Organization   :linkedTo  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Organization   :transitiveSubOrganizationOf  

Post  --> Organization   :postIn  

Site  --> Organization   :siteOf  

ChangeEvent  --> Organization   :originalOrganization  

Organization  --> Agent   :hasMember  

Agent  --> Organization   :memberOf  

Organization  --> Post   :hasPost  

ChangeEvent  --> Organization   :resultingOrganization  

```