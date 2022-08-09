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



Thing  --> Thing   :theme  

Agent  --> Document   :openid  

Image  --> Thing   :depicts  

Person  --> Document   :workplaceHomepage  

Person  --> Thing   :pastProject  

Agent  --> Thing   :mbox  

Agent  --> OnlineAccount   :account  

Document  --> Thing   :primaryTopic  

Person  --> Thing   :currentProject  

Person  --> Document   :schoolHomepage  

Document  --> Thing   :topic  

Thing  --> Document   :homepage  

Person  --> Image   :img  

OnlineAccount  --> Document   :accountServiceHomepage  

Agent  --> OnlineAccount   :holdsAccount  

Person  --> Document   :workInfoHomepage  

Agent  --> Document   :interest  

Group  --> Agent   :member  

Agent  --> Document   :tipjar  

SKOSConcept  --> Thing   :focus  

Thing  --> Document   :page  

Thing  --> Thing   :fundedBy  

Thing  --> Thing   :logo  

Thing  --> Image   :depiction  

Person  --> Document   :publications  

Agent  --> Thing   :made  

Image  --> Image   :thumbnail  

Agent  --> Document   :weblog  

Thing  --> Agent   :maker  

Agent  --> Thing   :topic_interest  

```