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



Person  --> Document   :workplaceHomepage  

Document  --> Thing   :primaryTopic  

Image  --> Thing   :depicts  

SKOSConcept  --> Thing   :focus  

SpatialThing  --> SpatialThing   :based_near  

Person  --> Thing   :currentProject  

Thing  --> Document   :page  

Agent  --> Document   :interest  

Person  --> Person   :knows  

Agent  --> Document   :tipjar  

Person  --> Document   :workInfoHomepage  

Agent  --> Document   :weblog  

Agent  --> Thing   :topic_interest  

Thing  --> Image   :depiction  

Person  --> Document   :publications  

Thing  --> Agent   :maker  

Agent  --> Document   :openid  

Thing  --> Thing   :theme  

Agent  --> OnlineAccount   :account  

Thing  --> Thing   :logo  

Agent  --> Thing   :made  

Person  --> Image   :img  

Thing  --> Thing   :fundedBy  

Person  --> Thing   :pastProject  

Image  --> Image   :thumbnail  

Document  --> Thing   :topic  

Agent  --> OnlineAccount   :holdsAccount  

Agent  --> Thing   :mbox  

Person  --> Document   :schoolHomepage  

OnlineAccount  --> Document   :accountServiceHomepage  

Thing  --> Document   :homepage  

Group  --> Agent   :member  

```