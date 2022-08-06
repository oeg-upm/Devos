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



Agent  --> Document   :openid  

Agent  --> Document   :tipjar  

Person  --> Document   :workInfoHomepage  

Thing  --> Document   :homepage  

Agent  --> Thing   :made  

Agent  --> OnlineAccount   :account  

Agent  --> Document   :interest  

Thing  --> Thing   :fundedBy  

Thing  --> Thing   :logo  

Document  --> Thing   :primaryTopic  

Person  --> Document   :schoolHomepage  

Thing  --> Document   :page  

Person  --> Document   :publications  

Image  --> Image   :thumbnail  

Thing  --> Agent   :maker  

Agent  --> Thing   :topic_interest  

Person  --> Thing   :currentProject  

Image  --> Thing   :depicts  

Thing  --> Thing   :theme  

SKOSConcept  --> Thing   :focus  

Person  --> Image   :img  

Person  --> Person   :knows  

Document  --> Thing   :topic  

Agent  --> Thing   :mbox  

Thing  --> Image   :depiction  

SpatialThing  --> SpatialThing   :based_near  

Person  --> Document   :workplaceHomepage  

Agent  --> Document   :weblog  

OnlineAccount  --> Document   :accountServiceHomepage  

Agent  --> OnlineAccount   :holdsAccount  

Group  --> Agent   :member  

Person  --> Thing   :pastProject  

```