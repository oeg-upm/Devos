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

Agent  --> Organization   :headOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Site   :hasSite  

Post  --> Organization   :postIn  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Post   :hasPost  

Post  --> Agent   :heldBy  

Organization  --> Organization   :hasSubOrganization  

Organization  --> Organization   :transitiveSubOrganizationOf  

Organization  --> Organization   :linkedTo  

Agent  --> Organization   :memberOf  

Site  --> Organization   :siteOf  

Agent  --> Post   :holds  

```