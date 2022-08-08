```mermaid
	classDiagram

    
    class ProperInterval {
    
    }

    class TemporalEntity {
    
    }

    class Instant {
    
    }

    class GeneralDateTimeDescription {
    
    }

    class DayOfWeek {
    
    }

    class Duration {
    
    }

    class GeneralDurationDescription {
    
    }

    class TRS {
    
    }

    class TemporalDuration {
    
    }

    class TemporalPosition {
    
    }



ProperInterval  --> ProperInterval   :intervalStartedBy  

ProperInterval  --> ProperInterval   :intervalEquals  

Interval  --> Instant   :inside  

ProperInterval  --> ProperInterval   :intervalBefore  

TemporalEntity  --> TemporalEntity   :after  

ProperInterval  --> ProperInterval   :intervalDuring  

GeneralDateTimeDescription  --> MonthOfYear   :monthOfYear  

ProperInterval  --> ProperInterval   :intervalDisjoint  

ProperInterval  --> ProperInterval   :intervalMeets  

TemporalEntity  --> TemporalDuration   :hasTemporalDuration  

ProperInterval  --> ProperInterval   :intervalMetBy  

TemporalEntity  --> TemporalEntity   :before  

Instant  --> GeneralDateTimeDescription   :inDateTime  

ProperInterval  --> ProperInterval   :intervalContains  

ProperInterval  --> ProperInterval   :intervalFinishes  

ndf7422624c2d4550b2dc482887e49a52b66  --> TRS   :hasTRS  

TemporalEntity  --> Instant   :hasEnd  

ProperInterval  --> ProperInterval   :intervalOverlaps  

ProperInterval  --> ProperInterval   :intervalOverlappedBy  

DateTimeInterval  --> GeneralDateTimeDescription   :hasDateTimeDescription  

Instant  --> TimePosition   :inTimePosition  

ProperInterval  --> ProperInterval   :intervalIn  

GeneralDateTimeDescription  --> DayOfWeek   :dayOfWeek  

TemporalEntity  --> Instant   :hasBeginning  

Instant  --> TemporalPosition   :inTemporalPosition  

ProperInterval  --> ProperInterval   :intervalFinishedBy  

ProperInterval  --> ProperInterval   :intervalStarts  

GeneralDateTimeDescription  --> TimeZone   :timeZone  

ProperInterval  --> ProperInterval   :intervalAfter  

```