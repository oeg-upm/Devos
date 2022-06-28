```mermaid
	classDiagram

    
    class Organization {
    
    }

    class Agent {
    
    }

    class Site {
    
    }



Organization  --> Site   :hasSite  

Organization  --> Organization   :hasSubOrganization  

Agent  --> Organization   :headOf  

Organization  --> Organization   :linkedTo  

Organization  --> Organization   :subOrganizationOf  

Organization  --> Site   :hasPrimarySite  

Organization  --> Organization   :transitiveSubOrganizationOf  

Site  --> Organization   :siteOf  

Organization  --> Agent   :hasMember  

Agent  --> Organization   :memberOf  

```