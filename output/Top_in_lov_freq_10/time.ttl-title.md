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



ProperInterval  --> ProperInterval   :intervalOverlaps  

ProperInterval  --> ProperInterval   :intervalDuring  

Interval  --> Instant   :inside  

ProperInterval  --> ProperInterval   :intervalStarts  

ProperInterval  --> ProperInterval   :intervalBefore  

GeneralDateTimeDescription  --> DayOfWeek   :dayOfWeek  

TemporalEntity  --> TemporalEntity   :before  

TemporalEntity  --> TemporalEntity   :after  

GeneralDateTimeDescription  --> TimeZone   :timeZone  

GeneralDateTimeDescription  --> MonthOfYear   :monthOfYear  

Instant  --> TimePosition   :inTimePosition  

ProperInterval  --> ProperInterval   :intervalFinishes  

ProperInterval  --> ProperInterval   :intervalMetBy  

Instant  --> TemporalPosition   :inTemporalPosition  

TemporalEntity  --> Instant   :hasBeginning  

TemporalEntity  --> TemporalDuration   :hasTemporalDuration  

DateTimeInterval  --> GeneralDateTimeDescription   :hasDateTimeDescription  

n552b1f1b6db24beaa216a374679ad7acb66  --> TRS   :hasTRS  

ProperInterval  --> ProperInterval   :intervalDisjoint  

Instant  --> GeneralDateTimeDescription   :inDateTime  

ProperInterval  --> ProperInterval   :intervalFinishedBy  

ProperInterval  --> ProperInterval   :intervalEquals  

TemporalEntity  --> Instant   :hasEnd  

ProperInterval  --> ProperInterval   :intervalMeets  

ProperInterval  --> ProperInterval   :intervalStartedBy  

ProperInterval  --> ProperInterval   :intervalIn  

ProperInterval  --> ProperInterval   :intervalOverlappedBy  

ProperInterval  --> ProperInterval   :intervalContains  

ProperInterval  --> ProperInterval   :intervalAfter  

```