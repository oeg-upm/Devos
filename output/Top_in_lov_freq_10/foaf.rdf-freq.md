```mermaid
	classDiagram

    
    class Thing {
    
    }

    class Document {
    
    }

    class Image {
    
    }

    class Agent {
    
    }

    class OnlineAccount {
    
    }

    class SpatialThing {
    
    }

    class Person {
    
    }



Group  --> Agent   :member  

Agent  --> OnlineAccount   :account  

Thing  --> Thing   :theme  

Thing  --> Document   :homepage  

Person  --> Document   :workplaceHomepage  

Agent  --> Thing   :topic_interest  

SpatialThing  --> SpatialThing   :based_near  

Person  --> Person   :knows  

OnlineAccount  --> Document   :accountServiceHomepage  

Person  --> Document   :schoolHomepage  

Person  --> Thing   :pastProject  

Person  --> Image   :img  

Thing  --> Document   :page  

Person  --> Thing   :currentProject  

SKOSConcept  --> Thing   :focus  

Agent  --> Thing   :mbox  

Image  --> Image   :thumbnail  

Thing  --> Thing   :fundedBy  

Agent  --> OnlineAccount   :holdsAccount  

Person  --> Document   :workInfoHomepage  

Agent  --> Thing   :made  

Document  --> Thing   :primaryTopic  

Document  --> Thing   :topic  

Thing  --> Agent   :maker  

Agent  --> Document   :interest  

Image  --> Thing   :depicts  

Thing  --> Thing   :logo  

Thing  --> Image   :depiction  

Agent  --> Document   :openid  

Person  --> Document   :publications  

Agent  --> Document   :tipjar  

Agent  --> Document   :weblog  

```