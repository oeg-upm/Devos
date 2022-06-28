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



Agent  --> Post   :holds  

Organization  --> Site   :hasSite  

Post  --> Agent   :heldBy  

Organization  --> Organization   :hasSubOrganization  

Agent  --> Organization   :headOf  

Organization  --> Organization   :linkedTo  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Organization   :transitiveSubOrganizationOf  

Post  --> Organization   :postIn  

Site  --> Organization   :siteOf  

Organization  --> Agent   :hasMember  

Agent  --> Organization   :memberOf  

Organization  --> Post   :hasPost  

```