```mermaid
	classDiagram

    
    class Organization {
    
    }

    class Agent {
    
    }

    class Site {
    
    }



Organization  --> Agent   :hasMember  

Organization  --> Site   :hasSite  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Organization   :hasSubOrganization  

Organization  --> Site   :hasPrimarySite  

Site  --> Organization   :siteOf  

Agent  --> Organization   :memberOf  

Organization  --> Organization   :transitiveSubOrganizationOf  

Agent  --> Organization   :headOf  

Organization  --> Organization   :linkedTo  

```