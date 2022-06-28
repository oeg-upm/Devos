```mermaid
	classDiagram

    
    class Organization {
    
    }

    class Agent {
    
    }

    class Site {
    
    }



Organization  --> Agent   :hasMember  

Agent  --> Organization   :headOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Site   :hasSite  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Organization   :hasSubOrganization  

Organization  --> Organization   :transitiveSubOrganizationOf  

Organization  --> Organization   :linkedTo  

Agent  --> Organization   :memberOf  

Site  --> Organization   :siteOf  

```