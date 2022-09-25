# CS-555
Shared CS 555 repository


# Project Sprint Report
Link to excel sheet with team: https://docs.google.com/spreadsheets/d/1vpMHk346ppo99FykLNff3ib_xNGSePcU/edit?usp=sharing&ouid=100857675956622681414&rtpof=true&sd=true 
## Team Information 
| Initials |	First |	Last| Email |	GitHub Username|
| -------- | ------ | ----- | ----- |	-------------- |			
| SM | Sanjana | Madhu | smadhu@stevens.edu | smadhu247
| DD | Danielle | Dauphinais | ddauphin@stevens.edu | DanielleDauphinais
| LJ | Lasya | Josyula | ljosyula@stevens.edu | lkjosyula
| BG | Brianna | Garland | bgarland@stevens.edu | BriannaPGarland
				
GitHub Repository:	https://github.com/smadhu247/CS-555

## Backlog 

Sprint	Story ID	Story Name	Owner	Status
1	US01	Dates before current date	Lasya	
1	US02	Birth before marriage	Lasya	
1	US03	Birth before death	Danielle	
1	US04	Marriage before divorce	Danielle	
1	US05	Marriage before death	Sanjana	
1	US06	Divorce before death	Sanjana	
1	US07	Less then 150 years old	Bri	
1	US08	Birth before marriage of parents	Bri	
2	US09	Birth before death of parents	Lasya	
2	US10	Marriage after 14	Lasya	
2	US11	No bigamy	Danielle	
2	US12	Parents not too old	Danielle	
2	US13	Siblings spacing	Sanjana	
2	US14	Multiple births <= 5	Sanjana	
2	US15	Fewer than 15 siblings	Bri	
2	US16	Male last names	Bri	
3	US17	No marriages to descendants	Lasya	
3	US18	Siblings should not marry	Lasya	
3	US19	First cousins should not marry	Danielle	
3	US20	Aunts and uncles	Danielle	
3	US21	Correct gender for role	Sanjana	
3	US22	Unique IDs	Sanjana	
3	US23	Unique name and birth date	Bri	
3	US24	Unique families by spouses	Bri	
4	US25	Unique first names in families	Lasya	
4	US26	Corresponding entries	Lasya	
4	US27	Include individual ages	Danielle	
4	US28	Order siblings by age	Danielle	
4	US29	List deceased	Sanjana	
4	US30	List living married	Sanjana	
4	US31	List living single	Bri	
4	US32	List multiple births	Bri	

## Burndown 

Sprint	Date	Remaining Stories	Story Velocity	LOC	Min	Code Velocity
Start	9/20/2022	32		0

## Sprint 1

Story ID	Story Name	Owner	Status	Est Size	Est Time	Act Size	Act Time	Completed
US01	Dates before current date	Lasya	coding	10	30 minutes			
US02	Birth before marriage	Lasya	coding	50	45 minutes			
US03	Birth before death	Danielle	coding	10	30 minutes			
US04	Marriage before divorce	Danielle	coding	20	40 minutes			
US05	Marriage before death	Sanjana	coding	30	20 minutes			
US06	Divorce before death	Sanjana	coding	15	40 minutes			
US07	Less then 150 years old	Bri	coding	15	30 minutes			
US08	Birth before marriage of parents	Bri	coding	20	20 minutes			
								
								
								
								
	Review Results							
								
	Keep doing:							
								
								
								
	Avoid:							
	
## Sprint 2

Story ID	Story Name	Owner	Status	Est Size	Est Time	Act Size	Act Time	Completed
US09	Birth before death of parents	Lasya	coding	5	20 minutes			
US10	Marriage after 14	Lasya	coding	20	45 minutes			
US11	No bigamy	Danielle	coding	20	45 minutes			
US12	Parents not too old	Danielle	coding	20	40 minutes			
US13	Siblings spacing	Sanjana	coding	20	40 minutes			
US14	Multiple births <= 5	Sanjana	coding	5	15 minutes			
US15	Fewer than 15 siblings	Bri	coding	15	15 minutes			
US16	Male last names	Bri	coding	20	25 minutes			

## Sprint 3

Story ID	Story Name	Owner	Status	Est Size	Est Time	Act Size	Act Time	Completed
US17	No marriages to descendants	Lasya	coding	20	45 minutes			
US18	Siblings should not marry	Lasya	coding	10	20 minutes			
US19	First cousins should not marry	Danielle	coding	15	30 minutes			
US20	Aunts and uncles	Danielle	coding	25	45 minutes			
US21	Correct gender for role	Sanjana	coding	5	15 minutes			
US22	Unique IDs	Sanjana	coding	15	40 minutes			
US23	Unique name and birth date	Bri	coding	15	45 minutes			
US24	Unique families by spouses	Bri	coding	20	30 minutes			

# Spring 4 

Story ID	Story Name	Owner	Status	Est Size	Est Time	Act Size	Act Time	Completed
US25	Unique first names in families	Lasya	coding	10	30 minutes			
US26	Corresponding entries	Lasya	coding	50	45 minutes			
US27	Include individual ages	Danielle	coding	10	30 minutes			
US28	Order siblings by age	Danielle	coding	20	40 minutes			
US29	List deceased	Sanjana	coding	30	20 minutes			
US30	List living married	Sanjana	coding	15	40 minutes			
US31	List living single	Bri	coding	15	30 minutes			
US32	List multiple births	Bri	coding	20	20 minutes			
								
# Stories 

Story ID	Story Name	Story Description
US01	Dates before current date	Dates (birth, marriage, divorce, death) should not be after the current date
US02	Birth before marriage	Birth should occur before marriage of an individual
US03	Birth before death	Birth should occur before death of an individual
US04	Marriage before divorce	Marriage should occur before divorce of spouses, and divorce can only occur after marriage
US05	Marriage before death	Marriage should occur before death of either spouse
US06	Divorce before death	Divorce can only occur before death of both spouses
US07	Less then 150 years old	Death should be less than 150 years after birth for dead people, and current date should be less than 150 years after birth for all living people
US08	Birth before marriage of parents	Children should be born after marriage of parents (and not more than 9 months after their divorce)
US09	Birth before death of parents	Child should be born before death of mother and before 9 months after death of father
US10	Marriage after 14	Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
US11	No bigamy	Marriage should not occur during marriage to another spouse
US12	Parents not too old	Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
US13	Siblings spacing	Birth dates of siblings should be more than 8 months apart or less than 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
US14	Multiple births <= 5	No more than five siblings should be born at the same time
US15	Fewer than 15 siblings	There should be fewer than 15 siblings in a family
US16	Male last names	All male members of a family should have the same last name
US17	No marriages to descendants	Parents should not marry any of their descendants
US18	Siblings should not marry	Siblings should not marry one another
US19	First cousins should not marry	First cousins should not marry one another
US20	Aunts and uncles	Aunts and uncles should not marry their nieces or nephews
US21	Correct gender for role	Husband in family should be male and wife in family should be female
US22	Unique IDs	All individual IDs should be unique and all family IDs should be unique
US23	Unique name and birth date	No more than one individual with the same name and birth date should appear in a GEDCOM file
US24	Unique families by spouses	No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
US25	Unique first names in families	No more than one child with the same name and birth date should appear in a family
US26	Corresponding entries	All family roles (spouse, child) specified in an individual record should have corresponding entries in the corresponding family records. Likewise, all individual roles (spouse, child) specified in family records should have corresponding entries in the corresponding  individual's records.  I.e. the information in the individual and family records should be consistent.
US27	Include individual ages	Include person's current age when listing individuals
US28	Order siblings by age	List siblings in families by decreasing age, i.e. oldest siblings first
US29	List deceased	List all deceased individuals in a GEDCOM file
US30	List living married	List all living married people in a GEDCOM file
US31	List living single	List all living people over 30 who have never been married in a GEDCOM file
US32	List multiple births	List all multiple births in a GEDCOM file
US33	List orphans	List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
US34	List large age differences	List all couples who were married when the older spouse was more than twice as old as the younger spouse
US35	List recent births	List all people in a GEDCOM file who were born in the last 30 days
US36	List recent deaths	List all people in a GEDCOM file who died in the last 30 days
US37	List recent survivors	List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days
US38	List upcoming birthdays	List all living people in a GEDCOM file whose birthdays occur in the next 30 days
US39	List upcoming anniversaries	List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
US40	Include input line numbers	List line numbers from GEDCOM source file when reporting errors
US41	Include partial dates	Accept and use dates without days or without days and months
US42	Reject illegitimate dates	All dates should be legitimate dates for the months specified (e.g., 2/30/2015 is not legitimate)
