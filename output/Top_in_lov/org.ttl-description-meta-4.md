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



Organization  --> Agent   :hasMember  

Organization  --> Site   :hasSite  

Agent  --> Post   :holds  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Organization   :hasSubOrganization  

Post  --> Organization   :postIn  

Organization  --> Site   :hasPrimarySite  

Organization  --> Post   :hasPost  

Site  --> Organization   :siteOf  

Agent  --> Organization   :memberOf  

Organization  --> Organization   :transitiveSubOrganizationOf  

Post  --> Agent   :heldBy  

Agent  --> Organization   :headOf  

Organization  --> Organization   :linkedTo  

```