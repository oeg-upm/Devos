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



Thing  --> Thing   :theme  

Person  --> Document   :workplaceHomepage  

Agent  --> OnlineAccount   :holdsAccount  

Person  --> Document   :publications  

OnlineAccount  --> Document   :accountServiceHomepage  

Agent  --> Document   :weblog  

Agent  --> Document   :openid  

Person  --> Document   :workInfoHomepage  

Agent  --> Document   :interest  

Thing  --> Document   :page  

Image  --> Thing   :depicts  

Person  --> Thing   :pastProject  

Document  --> Thing   :primaryTopic  

Person  --> Image   :img  

Agent  --> Thing   :made  

Person  --> Thing   :currentProject  

Thing  --> Thing   :logo  

Thing  --> Thing   :fundedBy  

Thing  --> Agent   :maker  

Person  --> Document   :schoolHomepage  

SpatialThing  --> SpatialThing   :based_near  

Image  --> Image   :thumbnail  

SKOSConcept  --> Thing   :focus  

Agent  --> OnlineAccount   :account  

Thing  --> Document   :homepage  

Agent  --> Thing   :mbox  

Document  --> Thing   :topic  

Person  --> Person   :knows  

Agent  --> Document   :tipjar  

Agent  --> Thing   :topic_interest  

Group  --> Agent   :member  

Thing  --> Image   :depiction  

```