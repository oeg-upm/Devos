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



Image  --> Thing   :depicts  

Thing  --> Document   :page  

Document  --> Thing   :topic  

Thing  --> Image   :depiction  

Agent  --> OnlineAccount   :holdsAccount  

Agent  --> Thing   :topic_interest  

Agent  --> Thing   :made  

SKOSConcept  --> Thing   :focus  

Agent  --> Thing   :mbox  

Person  --> Document   :publications  

Document  --> Thing   :primaryTopic  

Image  --> Image   :thumbnail  

Thing  --> Agent   :maker  

Person  --> Document   :workInfoHomepage  

Person  --> Document   :workplaceHomepage  

Thing  --> Thing   :logo  

Person  --> Image   :img  

Thing  --> Document   :homepage  

OnlineAccount  --> Document   :accountServiceHomepage  

Person  --> Document   :schoolHomepage  

Agent  --> OnlineAccount   :account  

Thing  --> Thing   :theme  

Thing  --> Thing   :fundedBy  

Agent  --> Document   :openid  

Agent  --> Document   :tipjar  

Person  --> Thing   :pastProject  

Agent  --> Document   :interest  

Agent  --> Document   :weblog  

Group  --> Agent   :member  

Person  --> Thing   :currentProject  

```