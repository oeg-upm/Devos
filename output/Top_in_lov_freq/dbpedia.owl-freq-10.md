```mermaid
	classDiagram

    
    class Person {
    
    }

    class PopulatedPlace {
    
    }

    class Place {
    
    }

    class SportsTeam {
    
    }

    class Award {
    
    }

    class Organisation {
    
    }

    class MeanOfTransportation {
    
    }

    class Country {
    
    }

    class Species {
    
    }

    class Agent {
    
    }



Settlement  --> PopulatedPlace   :administrativeCollectivity  

Person  --> Place   :residence  

River  --> Country   :sourceConfluenceCountry  

Settlement  --> Place   :lowestPoint  

MusicalWork  --> Person   :lyrics  

PopulatedPlace  --> PopulatedPlace   :sheading  

Actor  --> Award   :laurenceOlivierAward  

WrittenWork  --> Person   :prefaceBy  

Film  --> Person   :cinematography  

AdministrativeRegion  --> Person   :landeshauptmann  

Person  --> RadioStation   :radio  

Aircraft  --> Organisation   :aircraftUser  

Work  --> Person   :chiefEditor  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Film  --> Person   :editing  

Place  --> Place   :westPlace  

Ship  --> Place   :homeport  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

MilitaryUnit  --> MeanOfTransportation   :aircraftTrainer  

Athlete  --> Country   :sportCountry  

Organisation  --> Person   :superintendent  

Place  --> River   :river  

Actor  --> Award   :screenActorsGuildAward  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

Artist  --> Award   :academyAward  

Saint  --> Person   :canonizedBy  

Person  --> Tournament   :olympicGames  

GrandPrix  --> SportsTeam   :secondTeam  

Place  --> PopulatedPlace   :biggestCity  

SportsTeam  --> Person   :manager  

Organisation  --> Person   :secretaryGeneral  

Athlete  --> SportsTeam   :juniorTeam  

Place  --> PopulatedPlace   :district  

ArchitecturalStructure  --> Organisation   :tenant  

Athlete  --> SportsTeam   :club  

Agent  --> Artist   :artPatron  

Place  --> Sea   :sea  

Artist  --> Award   :tonyAward  

AdministrativeRegion  --> Place   :administrativeCenter  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

Place  --> Species   :bird  

Mountain  --> Person   :firstAscentPerson  

PopulatedPlace  --> Place   :touristicSite  

Person  --> SKOSConcept   :mastersWins  

Actor  --> Award   :naacpImageAward  

Person  --> Person   :detractor  

Person  --> Person   :colleague  

Island  --> PopulatedPlace   :governmentRegion  

Person  --> Person   :relative  

Person  --> SKOSConcept   :world  

Island  --> PopulatedPlace   :lowestRegion  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

Place  --> PopulatedPlace   :lowestPlace  

Person  --> SKOSConcept   :endReign  

SoccerClub  --> Place   :ground  

Agent  --> Event   :roleInEvent  

Island  --> PopulatedPlace   :managementRegion  

Person  --> CareerStation   :careerStation  

FigureSkater  --> Person   :currentPartner  

Canal  --> Person   :principalEngineer  

Place  --> Province   :province  

Country  --> Continent   :continent  

PopulatedPlace  --> Population   :population  

LegalCase  --> Person   :solicitorGeneral  

PopulatedPlace  --> Agglomeration   :agglomeration  

Saint  --> Person   :beatifiedBy  

Man  --> Person   :son  

Person  --> Person   :cousurper  

Settlement  --> Person   :bourgmestre  

Athlete  --> SportsTeam   :currentTeam  

Athlete  --> SportsTeam   :oldTeamCoached  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Athlete  --> Person   :trainer  

VideoGame  --> Person   :gameArtist  

Person  --> SKOSConcept   :startReign  

Organisation  --> City   :locationCity  

Person  --> Organisation   :federation  

Film  --> Person   :specialEffects  

Person  --> SKOSConcept   :britishWins  

MilitaryUnit  --> MeanOfTransportation   :aircraftFighter  

Place  --> Place   :mainIsland  

River  --> PopulatedPlace   :mouthDistrict  

Athlete  --> SportsTeam   :coachClub  

Actor  --> Award   :iftaAward  

Place  --> Place   :hasInsidePlace  

Person  --> SportsTeam   :currentTeamManager  

Place  --> PopulatedPlace   :regency  

Saint  --> Organisation   :veneratedIn  

MusicalWork  --> PopulatedPlace   :recordedIn  

Olympics  --> Person   :officialOpenedBy  

Settlement  --> PopulatedPlace   :jointCommunity  

Person  --> SportsTeam   :teamManager  

Canal  --> Place   :originalStartPoint  

Athlete  --> SportsTeam   :youthClub  

Family  --> Person   :headOfFamily  

Broadcaster  --> PopulatedPlace   :broadcastArea  

Work  --> Agent   :producer  

MilitaryUnit  --> MeanOfTransportation   :aircraftPatrol  

Person  --> Person   :spouse  

Actor  --> Award   :goldenCalfAward  

MilitaryUnit  --> MeanOfTransportation   :aircraftTransport  

GrandPrix  --> Person   :secondDriver  

Place  --> Place   :southWestPlace  

Man  --> Person   :brother  

Settlement  --> Place   :highestPoint  

Person  --> Tournament   :worldTournament  

EducationalInstitution  --> Person   :dean  

Politician  --> Person   :prefect  

Sport  --> Person   :footedness  

Place  --> Place   :hasOutsidePlace  

MilitaryUnit  --> MeanOfTransportation   :aircraftRecon  

Island  --> Country   :governmentCountry  

Department  --> PopulatedPlace   :subprefecture  

PopulatedPlace  --> PopulatedPlace   :principalArea  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

Album  --> Person   :compiler  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Settlement  --> Place   :settlementAttached  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

SkiResort  --> Place   :massif  

Scientist  --> Person   :doctoralAdvisor  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Organisation  --> City   :foundationPlace  

SoccerPlayer  --> SportsTeam   :trainerClub  

GrandPrix  --> Person   :firstDriver  

Place  --> Altitude   :lowestAltitude  

Island  --> Place   :subdivisionName  

Place  --> Place   :eastPlace  

Artist  --> Award   :gaudiAward  

YearInSpaceflight  --> Country   :countryWithFirstAstronaut  

Cartoon  --> Agent   :animator  

Person  --> Person   :sibling  

Organisation  --> Organisation   :mergedWith  

Work  --> Person   :mainCharacter  

Person  --> Place   :educationPlace  

PopulatedPlace  --> Saint   :saint  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Athlete  --> SportsTeam   :debutTeam  

Actor  --> Award   :arielAward  

Agent  --> Ideology   :ideology  

Restaurant  --> Person   :chef  

Organisation  --> PopulatedPlace   :headquarter  

Rocket  --> Country   :countryOrigin  

MilitaryUnit  --> MeanOfTransportation   :aircraftBomber  

FictionalCharacter  --> Species   :enemy  

Person  --> Place   :livingPlace  

Person  --> MilitaryService   :militaryService  

TelevisionShow  --> Person   :coExecutiveProducer  

FigureSkater  --> Person   :formerCoach  

Place  --> Place   :locatedInArea  

School  --> Person   :nobelLaureates  

Food  --> Person   :creatorOfDish  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

Work  --> Person   :translator  

Artist  --> Award   :goldenGlobeAward  

MilitaryUnit  --> MeanOfTransportation   :aircraftInterceptor  

Family  --> Person   :lastFamilyMember  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Artist  --> Award   :cesarAward  

Person  --> Person   :dubber  

Scientist  --> Person   :doctoralStudent  

Magazine  --> Person   :previousEditor  

Artist  --> Award   :emmyAward  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Place  --> Mountain   :lowestMountain  

Man  --> Person   :father  

Saint  --> PopulatedPlace   :beatifiedPlace  

Species  --> Species   :subTribus  

Comedian  --> Award   :olivierAward  

Organisation  --> Person   :chairperson  

Species  --> Taxon   :superFamily  

Person  --> Country   :stateOfOrigin  

Island  --> PopulatedPlace   :highestRegion  

MilitaryUnit  --> Person   :notableCommander  

Place  --> Place   :subregion  

SportsTeam  --> TeamMember   :currentTeamMember  

Woman  --> Person   :daughter  

PopulatedPlace  --> PopulatedPlace   :borough  

Comedian  --> Award   :britishComedyAwards  

Country  --> Country   :twinCountry  

LegalCase  --> Person   :attorneyGeneral  

PopulatedPlace  --> Demographics   :previousDemographics  

FictionalCharacter  --> Species   :entourage  

Person  --> Contest   :contest  

Place  --> Species   :tree  

EducationalInstitution  --> Person   :principal  

Olympics  --> Person   :olympicOathSwornBy  

Species  --> Species   :tribus  

Species  --> Taxon   :subFamily  

Person  --> Person   :child  

Athlete  --> SportsTeam   :formerTeam  

Person  --> Project   :project  

FigureSkater  --> Person   :formerChoreographer  

FigureSkater  --> Person   :choreographer  

Species  --> Species   :superTribus  

PopulatedPlace  --> Person   :viceLeader  

Athlete  --> SportsTeam   :ncaaTeam  

Person  --> Tournament   :continentalTournament  

Person  --> Place   :bodyDiscovered  

MilitaryUnit  --> Person   :fourthCommander  

WrittenWork  --> Person   :illustrator  

EducationalInstitution  --> Person   :rector  

Man  --> Person   :uncle  

SportsEvent  --> Person   :medalist  

Artist  --> Award   :filmFareAward  

Athlete  --> SportsTeam   :stateOfOriginTeam  

Person  --> Person   :relation  

River  --> PopulatedPlace   :mouthRegion  

EducationalInstitution  --> Person   :actingHeadteacher  

Person  --> Diploma   :diploma  

ResearchProject  --> Organisation   :fundedBy  

Work  --> Person   :writer  

Settlement  --> Place   :wilaya  

Person  --> Work   :debutWork  

Country  --> TopLevelDomain   :topLevelDomain  

Person  --> SportsEvent   :competitionTitle  

PopulatedPlace  --> Department   :department  

PopulatedPlace  --> Language   :officialLanguage  

Person  --> EthnicGroup   :ethnicity  

Person  --> Work   :created  

Agent  --> TermOfOffice   :regionalCouncil  

School  --> Person   :executiveHeadteacher  

Actor  --> Award   :goldenRaspberryAward  

Organisation  --> Person   :ceo  

TelevisionShow  --> Person   :creativeDirector  

Person  --> Person   :copilote  

Work  --> Agent   :publisher  

Person  --> Person   :usurper  

Place  --> Place   :endPoint  

ResearchProject  --> Organisation   :projectCoordinator  

Athlete,_CareerStation  --> SportsTeam   :leadTeam  

Species  --> Species   :fossil  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> EducationalInstitution   :college  

Place  --> SpatialThing   :lowestPosition  

Stream  --> Country   :sourceCountry  

TermOfOffice  --> Person   :presidentGeneralCouncil  

Person  --> Person   :opponent  

PopulatedPlace  --> Person   :leaderName  

Place  --> Place   :northPlace  

Artwork  --> Person   :painter  

Island  --> PopulatedPlace   :governmentPlace  

PopulatedPlace  --> Area   :agglomerationArea  

Newspaper  --> Person   :associateEditor  

Person  --> Person   :parent  

Organisation  --> Organisation   :childOrganisation  

PopulatedPlace  --> Legislature   :legislature  

Organisation  --> Person   :chaplain  

Organisation  --> PersonFunction   :leaderFunction  

Settlement  --> PopulatedPlace   :geolocDepartment  

Monarch  --> Person   :heir  

Place  --> Province   :provinceLink  

Athlete  --> SportsTeam   :nflTeam  

Place  --> Altitude   :altitude  

Place  --> Place   :northEastPlace  

Island  --> PopulatedPlace   :lowestState  

Person  --> Tournament   :nationalTournament  

Person  --> Person   :friend  

Artist  --> Award   :afiAward  

GrandPrix  --> Country   :fastestDriverCountry  

Olympics  --> Person   :torchBearer  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Place  --> Place   :northWestPlace  

Place  --> Place   :closeTo  

Person  --> Film   :movie  

Organisation  --> Person   :administrator  

Work  --> Place   :releaseLocation  

Place  --> Species   :flower  

SportsTeam  --> Person   :currentMember  

Person  --> EducationalInstitution   :almaMater  

WrittenWork  --> Agent   :firstPublisher  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Place  --> Organisation   :governingBody  

MeanOfTransportation  --> MeanOfTransportation   :relatedMeanOfTransportation  

Film  --> Person   :director  

GrandPrix  --> Country   :secondDriverCountry  

Woman  --> Person   :sister  

Woman  --> Person   :mother  

Island  --> PopulatedPlace   :capitalDistrict  

Language  --> PopulatedPlace   :spokenIn  

Island  --> PopulatedPlace   :capitalPlace  

Person  --> SKOSConcept   :usopenWins  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterObservation  

Band  --> Person   :bandMember  

PublicTransitSystem  --> MeanOfTransportation   :vehiclesInFleet  

Species  --> Species   :family  

University  --> Person   :officerInCharge  

Agent  --> Settlement   :hometown  

TelevisionEpisode  --> Person   :guest  

Settlement  --> PopulatedPlace   :largestMetro  

Artist  --> Award   :grammyAward  

Person  --> Sport   :sportDiscipline  

Place  --> Place   :nextEntity  

Agent  --> Thing   :owns  

River  --> PopulatedPlace   :mouthState  

Settlement  --> Place   :daira  

School  --> Person   :vicePrincipal  

Band  --> Person   :formerBandMember  

Person  --> Person   :collaboration  

TelevisionShow  --> Person   :storyEditor  

Animal  --> Place   :birthPlace  

Place  --> Area   :wholeArea  

PopulatedPlace  --> Language   :regionalLanguage  

Settlement  --> PopulatedPlace   :federalState  

Actor  --> Award   :nationalFilmAward  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterTransport  

Person  --> Person   :student  

TelevisionShow  --> Person   :presenter  

ResearchProject  --> Organisation   :projectParticipant  

MilitaryUnit  --> Person   :secondCommander  

Film  --> Person   :setDesigner  

Athlete,_CareerStation  --> SportsTeam   :amateurTeam  

EducationalInstitution  --> Person   :custodian  

Organisation  --> Place   :regionServed  

Athlete  --> SportsTeam   :managerClub  

TelevisionShow  --> Person   :showJudge  

Place  --> RouteStop   :isRouteStop  

Agent  --> TermOfOffice   :generalCouncil  

Work  --> Person   :composer  

RouteOfTransportation  --> Place   :routeStartLocation  

SpaceMission  --> MeanOfTransportation   :lunarRover  

YearInSpaceflight  --> Country   :countryWithFirstSatelliteLaunched  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterAttack  

SportsTeam  --> Person   :generalManager  

HistoricBuilding  --> Person   :pastor  

Species  --> Species   :species  

Canal  --> Place   :originalEndPoint  

Animal  --> Place   :deathPlace  

Musical  --> Person   :musicBy  

PopulatedPlace  --> Population   :previousPopulation  

Person  --> Place   :announcedFrom  

Place  --> Depth   :depths  

River  --> PopulatedPlace   :sourceConfluenceState  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueWinner  

River  --> Place   :sourceConfluenceRegion  

Person  --> PersonFunction   :otherOccupation  

Saint  --> PopulatedPlace   :canonizedPlace  

SportsEvent  --> Person   :bronzeMedalist  

Place  --> Place   :land  

Place  --> PopulatedPlace   :nearestCity  

Place  --> Place   :southEastPlace  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopter  

Place  --> Place   :supply  

MilitaryUnit  --> PopulatedPlace   :garrison  

Work  --> Person   :author  

Place  --> Place   :previousEntity  

EducationalInstitution  --> Person   :alumni  

Road  --> PopulatedPlace   :ruralMunicipality  

Person  --> Person   :seiyu  

Organisation  --> Person   :trustee  

Settlement  --> PopulatedPlace   :frazioni  

Olympics  --> Person   :olympicOathSwornByJudge  

Race  --> Person   :recentWinner  

Person  --> SportsLeague   :leagueManager  

Person  --> List   :relatedFunctions  

MilitaryUnit  --> MeanOfTransportation   :aircraftElectronic  

GrandPrix  --> Country   :firstDriverCountry  

Scientist  --> Person   :academicAdvisor  

Scientist  --> Person   :notableStudent  

Race  --> Person   :firstWinner  

PoliticalParty  --> Person   :spokesperson  

Actor  --> Award   :geminiAward  

GrandPrix  --> SportsTeam   :fastestDriverTeam  

Person  --> Organisation   :employer  

MilitaryUnit  --> MeanOfTransportation   :aircraftHelicopterMultirole  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueRelegated  

GrandPrix  --> Person   :thirdDriver  

PopulatedPlace  --> City   :capital  

Sport  --> Agent   :currentWorldChampion  

Newspaper  --> Person   :managingEditor  

Island  --> PopulatedPlace   :capitalRegion  

Work  --> Person   :coverArtist  

Film  --> Person   :makeupArtist  

MusicalWork  --> Agent   :artist  

Athlete  --> SportsTeam   :teamCoached  

Restaurant  --> Person   :headChef  

School  --> Person   :headteacher  

Athlete,_CareerStation  --> SportsTeam   :proTeam  

Place  --> PersonFunction   :politicalLeader  

RouteOfTransportation  --> Place   :routeEndLocation  

GrandPrix  --> Person   :fastestDriver  

Person  --> SpatialThing   :restingPlacePosition  

Person  --> Country   :nationality  

Family  --> Person   :primogenitor  

```