# Database Systems - Design, Implementation, and Management (9th Edition).pdf

## Page 1



## Page 2

A_C7046_FM.4c 10/23/09 4:28 PM Page i
DATABASE S YSTEMS
DESIGN, IMPLEMENTATION, AND MANAGEMENT
CARLOS CORONEL • STEVEN MORRIS • PETER ROB
Australia • Brazil • Japan • Korea • Mexico • Singapore • Spain • United Kingdom • United States
Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part.

## Page 3

Database Systems: Design, Implementation, © 2011Cengage Learning
and Management, Ninth Edition ALL RIGHTS RESERVED. No part of this work covered by the copyright herein may be
Carlos Coronel, Steven Morris, and Peter Rob
reproduced, transmitted, stored or used in any form or by any means graphic, electronic,
or mechanical, including but not limited to photocopying, recording, scanning, digitiz-
Vice President of Editorial, Business: Jack W. Calhoun
ing, taping, Web distribution, information networks, or information storage and retrieval
Publisher: Joe Sabatino systems, except as permitted under Section 107or 108of the 1976United States
Senior Acquisitions Editor: Charles McCormick, Jr. Copyright Act, without the prior written permission of the publisher.
Senior Product Manager: Kate Mason
Development Editor: Deb Kaufmann For product information and technology assistance, contact us at
Cengage Learning Customer &Sales Support, 1-800-354-9706
Editorial Assistant: Nora Heink
For permission to use material from this text or product, submit all
Senior Marketing Communications Manager:
requests online at www.cengage.com/permissions
LibbyShipp
Further permissions questions can be emailed to
Marketing Coordinator: Suellen Ruttkay permissionrequest@cengage.com
Content Product Manager: Matthew Hutchinson
Senior Art Director: Stacy Jenkins Shirley Library of Congress Control Number:2009936830
Cover Designer: Itzhack Shelomi
Student Edition Package
Cover Image: iStock Images
ISBN-13:978-0-538-46968-5
Media Editor: Chris Valentine
ISBN-10:0-538-46968-4
Manufacturing Coordinator: Julio Esperas
Copyeditor: Andrea Schein Student Edition (Book Only)
Proofreader: Foxxe Editorial ISBN-13:978-0-538-74884-1
Indexer: Elizabeth Cunningham ISBN-10:0-538-74884-2
Composition: GEX Publishing Services
Instructor Edition
ISBN-13: 978-0-538-46806-0
ISBN-10: 0-538-46806-8
Cengage Learning
20 Channel Center Street
Boston, MA 02210
USA
Cengage Learning is a leading provider of customized learning solutions with office loca-
tions around the globe, including Singapore, the United Kingdom, Australia, Mexico,
Brazil, and Japan. Locate your local office at:
international.cengage.com/region
Cengage Learning products are represented in Canada by Nelson Education, Ltd.
To learn more about Course Technology, visit www.cengage.com/coursetechnology
To learn more about Cengage Learning, visit www.cengage.com.
Purchase any of our products at your local college store or at our preferred online store
www.ichapters.com
Printed in the United States of America
1 2 3 4 5 6 7 17 16 15 14 13 12 11

## Page 4

D
edication
To the treasures in my life:To Victoria,for 20 wonderful years.Thank you for your unending
support, for being my angel, my sweetie and most importantly, my best friend.To Carlos
Anthony whose intelligence and wit is matched only by your good looks;you show us the way.
Thank you for your words of wisdom,contagious happiness and for bringing us shining days.
You are still young;your best times are still to come.To Gabriela Victoria who is the image of
brilliance,beauty,and faithfulness.Thank you for being the sunshine in my cloudy days.To
Christian Javier whose endless energy and delightful smiles keep us going every day.Thank you
for being the youthful reminder of life’s simple beauties.To my parents,Sarah and Carlos,thank
you for your sacrifice and example.To all of you,you are all my inspiration.“TQTATA.”
Carlos Coronel
To Pamela,from high school sweetheart through 20 years of marriage,the beautiful love of
my life who has supported,encouraged,and inspired me.More than anyone else,you are
responsible for whatever successes I have achieved.To my son,Alexander Logan,whose
depth of character is without measure.You are my pride and joy.To my daughter,Lauren
Elizabeth,whose beauty and intensity take my breath away.You are my heart and soul.
Thank you all for the sacrifices that you have made that enabled me to pursue this dream.
I love you so much more than I can express.To my mother,Florence Maryann,and to the
memory of my father,Alton Lamar,who together instilled in me the desire to learn and the
passion to achieve.To my mother-in-law,Connie Duke,and to the memory of my father-in-
law,Wayne Duke,who taught me to find joy in all things.To all of you,with all my love,
I dedicate this book.
Steven Morris
To Anne,who remains my best friend after 48 years of marriage.To our son,Peter William,
who turned out to be the man we hoped he would be and who proved his wisdom by
making Sheena our treasured daughter-in-law.To Sheena,who stole our hearts so many
years ago.To our grandsons, Adam Lee and Alan Henri,who are growing up to be the fine
human beings their parents are.To my mother-in-law,Nini Fontein,and to the memory of
my father-in-law,Henri Fontein—their life experiences in Europe and SoutheastAsia would
fill a history book and they enriched my life by entrusting me with their daughter’s future.
To the memory of my parents,Hendrik and Hermine Rob,who rebuilt their lives after
World War II’s horrors,who did it again after a failed insurgency in Indonesia,and who
finally found their promised land in these United States. And to the memory of Heinz,who
taught me daily lessons about loyalty,uncritical acceptance,and boundless understanding.
I dedicate this book to you,with love.
Peter Rob
D
E
D
I
C
A
T
I
O
N

## Page 5



## Page 6

BRIEF CONTENTS
PART I: Database Concepts
Chapter 1: Database Systems
Chapter 2: Data Models
PART II: Design Concepts
Chapter 3: The Relational Database Model
Chapter 4: Entity Relationship (ER) Modeling
Chapter 5: Advanced Data Modeling
Chapter 6: Normalization of Database Tables
PART III: Advanced Design and Implementation
Chapter 7: Introduction to Structured Query Language (SQL)
Chapter 8: Advanced SQL
Chapter 9: Database Design
PART IV: Advanced Database Concepts
Chapter 10: Transaction Management and Concurrency Control
Chapter 11: Database Performance Tuning and Query Optimization
Chapter 12: Distributed Database Management Systems
Chapter 13: Business Intelligence and Data Warehouses
PART V: Databases and the Internet
Chapter 14: Database Connectivity and Web Technologies
PART VI: Database Administration
Chapter 15: Database Administration and Security
GLOSSARY
INDEX
IV

## Page 7

BRIEF CONTENTS
The following appendixes and answers to selected questions and problems are included in the Premium Website for
this text, found at cengage.com/mis/coronel.
Appendix A: Designing Databases with Visio Professional: A Tutorial
Appendix B: The University Lab: Conceptual Design
Appendix C: The University Lab: Conceptual Design Verification, Logical
Design, and Implementation
Appendix D: Converting an ER Model into a Database Structure
Appendix E: Comparison of ER Model Notations
Appendix F: Client/Server Systems
Appendix G: Object-Oriented Databases
Appendix H: Unified Modeling Language (UML)
Appendix I: Databases in Electronic Commerce
Appendix J: Web Database Development with ColdFusion
Appendix K: The Hierarchical Database Model
Appendix L: The Network Database Model
® ®
Appendix M: Microsoft Access Tutorial
Appendix N: Creating a New Database Using Oracle 11g
Answers to Selected Questions and Problems
V

## Page 8

TABLE OF CONTENTS
PART I DATABASE CONCEPTS
Business Vignette:The Relational Revolution 3
Chapter 1 Database Systems 4
1.1 Why Databases? 5
1.2 Data vs.Information 5
1.3 Introducing the Database 7
1.3.1 Role and Advantages of the DBMS 7
1.3.2 Types of Databases 9
1.4 Why Database Design is Important 10
1.5 Evolution of File System Data Processing 11
1.5.1 Manual File Systems 11
1.5.2 Computerized File Systems 11
1.5.3 File System Redux:Modern End-User Productivity Tools 14
1.6 Problems with File System Data Processing 14
1.6.1 Structural and Data Dependence 15
1.6.2 Data Redundancy 16
1.6.3 Lack of Design and Data-Modeling Skills 17
1.7 Database Systems 17
1.7.1 The Database System Environment 18
1.7.2 DBMS Functions 20
1.7.3 Managing the Database System: A Shift in Focus 23
Summary 25
Key Terms 25
Review Questions 26
Problems 26
Chapter 2 Data Models 29
2.1 Data Modeling and Data Models 30
2.2 The Importance of Data Models 30
2.3 Data Model Basic Building Blocks 31
2.4 Business Rules 32
2.4.1 Discovering Business Rules 33
2.4.2 Translating Business Rules into Data Model Components 33
2.4.3 Naming Conventions 34
2.5 The Evolution of Data Models 34
2.5.1 Hierarchical and Network Models 35
2.5.2 The Relational Model 36
2.5.3 The Entity Relationship Model 38
2.5.4 The Object-Oriented (OO) Model 40
2.5.5 Newer Data Models:Object/Relational and XML 42
2.5.6 The Future of Data Models 43
2.5.7 Data Models: A Summary 43
2.6 Degrees of Data Abstraction 46
2.6.1 The External Model 46
2.6.2 The Conceptual Model 48
2.6.3 The Internal Model 49
2.6.4 The Physical Model 49
VI

## Page 9

TABLE OF CONTENTS
Summary 51
Key Terms 51
Review Questions 52
Problems 53
PART II DESIGN CONCEPTS
Business Vignette:BP’s Data Modeling Initiative 61
Chapter 3 The Relational Database Model 58
3.1 A Logical View of Data 59
3.1.1 Tables and Their Characteristics 59
3.2 Keys 62
3.3 Integrity Rules 66
3.4 Relational Set Operators 68
3.5 The Data Dictionary and the System Catalog 74
3.6 Relationships within the Relational Database 76
3.6.1 The 1:M Relationship 76
3.6.2 The 1:1 Relationship 78
3.6.3 The M:N Relationship 78
3.7 Data Redundancy Revisited 84
3.8 Indexes 86
3.9 Codd’s Relational Database Rules 88
Summary 89
Key Terms 89
Review Questions 90
Problems 92
Chapter 4 Entity Relationship (ER) Modeling 99
4.1 The Entity Relationship Model (ERM) 100
4.1.1 Entities 100
4.1.2 Attributes 101
4.1.3 Relationships 105
4.1.4 Connectivity and Cardinality 107
4.1.5 Existence Dependence 108
4.1.6 Relationship Strength 108
4.1.7 Weak Entities 110
4.1.8 Relationship Participation 113
4.1.9 Relationship Degree 116
4.1.10 Recursive Relationships 117
4.1.11 Associative (Composite) Entities 121
4.2 Developing an ER Diagram 123
4.3 Database Design Challenges:Conflicting Goals 128
Summary 134
Key Terms 134
Review Questions 135
Problems 137
Cases 140
VII

## Page 10

TABLE OF CONTENTS
Chapter 5 Advanced Data Modeling 147
5.1 The Extended Entity Relationship Model 148
5.1.1 Entity Supertypes and Subtypes 148
5.1.2 Specialization Hierarchy 149
5.1.3 Inheritance 150
5.1.4 Subtype Discriminator 151
5.1.5 Disjoint and Overlapping Constraints 151
5.1.6 Completeness Constraint 153
5.1.7 Specialization and Generalization 154
5.2 Entity Clustering 154
5.3 Entity Integrity:Selecting Primary Keys 155
5.3.1 Natural Keys and Primary Keys 156
5.3.2 Primary Key Guidelines 156
5.3.3 When to Use Composite Primary Keys 157
5.3.4 When to Use Surrogate Primary Keys 158
5.4 Design Cases:Learning Flexible Database Design 159
5.4.1 Design Case #1:Implementing 1:1 Relationships 160
5.4.2 Design Case #2:Maintaining History of Time-Variant Data 161
5.4.3 Design Case #3:Fan Traps 162
5.4.4 Design Case #4:Redundant Relationships 164
Summary 165
Key Terms 165
Review Questions 166
Problems 167
Cases 168
Chapter 6 Normalization of Database Tables 174
6.1 Database Tables and Normalization 175
6.2 The Need for Normalization 175
6.3 The Normalization Process 179
6.3.1 Conversion to First Normal Form 181
6.3.2 Conversion to Second Normal Form 184
6.3.3 Conversion to Third Normal Form 185
6.4 Improving the Design 187
6.5 Surrogate Key Considerations 191
6.6 Higher-Level Normal Forms 192
6.6.1 The Boyce-Codd Normal Form (BCNF) 192
6.6.2 Fourth Normal Form (4NF) 196
6.7 Normalization and Database Design 197
6.8 Denormalization 200
6.9 Data-Modeling Checklist 204
Summary 206
Key Terms 206
Review Questions 207
Problems 208
VIII

## Page 11

TABLE OF CONTENTS
PART III ADVANCED DESIGN AND IMPLEMENTATION
Business Vignette:The Many Benefits of BI 219
Chapter 7 Introduction to Structured Query Language (SQL) 220
7.1 Introduction to SQL 221
7.2 Data Definition Commands 223
7.2.1 The Database Model 223
7.2.2 Creating the Database 225
7.2.3 The Database Schema 225
7.2.4 Data Types 226
7.2.5 Creating Table Structures 229
7.2.6 SQL Constraints 232
7.2.7 SQL Indexes 235
7.3 Data Manipulation Commands 237
7.3.1 Adding Table Rows 237
7.3.2 Saving Table Changes 238
7.3.3 Listing Table Rows 238
7.3.4 Updating Table Rows 240
7.3.5 Restoring Table Contents 240
7.3.6 Deleting Table Rows 241
7.3.7 Inserting Table Rows with a Select Subquery 242
7.4 SELECT Queries 242
7.4.1 Selecting Rows with Conditional Restrictions 242
7.4.2 Arithmetic Operators:The Rule of Precedence 247
7.4.3 Logical Operators: AND,OR,and NOT 247
7.4.4 Special Operators 249
7.5 Additional Data Definition Commands 253
7.5.1 Changing a Column’s Data Type 253
7.5.2 Changing a Column’s Data Characteristics 254
7.5.3 Adding a Column 254
7.5.4 Dropping a Column 255
7.5.5 Advanced Data Updates 255
7.5.6 Copying Parts of Tables 257
7.5.7 Adding Primary and Foreign Key Designations 258
7.5.8 Deleting a Table from the Database 259
7.6 Additional SELECT Query Keywords 259
7.6.1 Ordering a Listing 259
7.6.2 Listing Unique Values 261
7.6.3 Aggregate Functions 261
7.6.4 Grouping Data 266
7.7 Virtual Tables:Creating a View 269
7.8 Joining Database Tables 270
7.8.1 Joining Tables with an Alias 273
7.8.2 Recursive Joins 273
7.8.3 Outer Joins 274
Summary 276
Key Terms 277
Review Questions 277
Problems 278
Cases 287
IX

## Page 12

TABLE OF CONTENTS
Chapter 8 Advanced SQL 297
8.1 Relational Set Operators 298
8.1.1 UNION 299
8.1.2 UNION ALL 300
8.1.3 INTERSECT 300
8.1.4 MINUS 301
8.1.5 Syntax Alternatives 303
8.2 SQL Join Operators 305
8.2.1 Cross Join 306
8.2.2 Natural Join 307
8.2.3 Join USING Clause 307
8.2.4 JOIN ON Clause 308
8.2.5 Outer Joins 309
8.3 Subqueries and Correlated Queries 312
8.3.1 WHERE Subqueries 314
8.3.2 IN Subqueries 315
8.3.3 HAVING Subqueries 316
8.3.4 Multirow Subquery Operators: ANY and ALL 317
8.3.5 FROM Subqueries 318
8.3.6 Attribute List Subqueries 319
8.3.7 Correlated Subqueries 321
8.4 SQL Functions 324
8.4.1 Date and Time Functions 324
8.4.2 Numeric Functions 327
8.4.3 String Functions 327
8.4.4 Conversion Functions 328
8.5 Oracle Sequences 330
8.6 Updatable Views 333
8.7 Procedural SQL 336
8.7.1 Triggers 341
8.7.2 Stored Procedures 350
8.7.3 PL/SQL Processing with Cursors 354
8.7.4 PL/SQL Stored Functions 357
8.8 Embedded SQL 358
Summary 363
Key Terms 364
Review Questions 364
Problems 365
Cases 369
Chapter 9 Database Design 372
9.1 The Information System 373
9.2 The Systems Development Life Cycle (SDLC) 375
9.2.1 Planning 376
9.2.2 Analysis 376
9.2.3 Detailed Systems Design 377
9.2.4 Implementation 377
9.2.5 Maintenance 377
9.3 The Database Life Cycle (DBLC) 378
9.3.1 The Database Initial Study 378
9.3.2 Database Design 382
X

## Page 13

TABLE OF CONTENTS
9.3.3 Implementation and Loading 384
9.3.4 Testing and Evaluation 386
9.3.5 Operation 389
9.3.6 Maintenance and Evolution 389
9.4 Conceptual Design 390
9.4.1 Data Analysis and Requirements 391
9.4.2 Entity Relationship Modeling and Normalization 393
9.4.3 Data Model Verification 396
9.4.4 Distributed Database Design 399
9.5 DBMS Software Selection 399
9.6 Logical Design 400
9.6.1 Map the Conceptual Model to the Logical Model 400
9.6.2 Validate the Logical Model Using Normalization 402
9.6.3 Validate Logical Model Integrity Constraints 402
9.6.4 Validate the Logical Model against User Requirements 403
9.7 Physical Design 403
9.7.1 Define Data Storage Organization 403
9.7.2 Define Integrity and Security Measures 404
9.7.3 Determine Performance Measures 404
9.8 Database Design Strategies 405
9.9 Centralized vs.Decentralized Design 406
Summary 409
Key Terms 409
Review Questions 410
Problems 410
PART IV ADVANCED DATABASE CONCEPTS
Business Vignette: Combating Data Explosion 413
Chapter 10 Transaction Management and Concurrency Control 414
10.1 What Is a Transaction? 415
10.1.1 Evaluating Transaction Results 416
10.1.2 Transaction Properties 419
10.1.3 Transaction Management with SQL 419
10.1.4 The Transaction Log 420
10.2 Concurrency Control 421
10.2.1 Lost Updates 422
10.2.2 Uncommitted Data 423
10.2.3 Inconsistent Retrievals 424
10.2.4 The Scheduler 425
10.3 Concurrency Control with Locking Methods 426
10.3.1 Lock Granularity 427
10.3.2 Lock Types 430
10.3.3 Two-Phase Locking to Ensure Serializability 431
10.3.4 Deadlocks 432
10.4 Concurrency Control with Time Stamping Methods 433
10.4.1 Wait/Die and Wound/Wait Schemes 434
XI

## Page 14

TABLE OF CONTENTS
10.5 Concurrency Control with Optimistic Methods 435
10.6 Database Recovery Management 435
10.6.1 Transaction Recovery 436
Summary 440
Key Terms 441
Review Questions 441
Problems 442
Chapter 11 Database Performance Tuning and Query Optimization 445
11.1 Database Performance-Tuning Concepts 446
11.1.1 Performance Tuning:Client and Server 447
11.1.2 DBMS Architecture 447
11.1.3 Database Statistics 449
11.2 Query Processing 451
11.2.1 SQL Parsing Phase 452
11.2.2 SQL Execution Phase 453
11.2.3 SQL Fetching Phase 453
11.2.4 Query Processing Bottlenecks 453
11.3 Indexes and Query Optimization 454
11.4 Optimizer Choices 456
11.4.1 Using Hints to Affect Optimizer Choices 458
11.5 SQL Performance Tuning 459
11.5.1 Index Selectivity 459
11.5.2 Conditional Expressions 460
11.6 Query Formulation 462
11.7 DBMS Performance Tuning 463
11.8 Query Optimization Example 465
Summary 474
Key Terms 475
Review Questions 475
Problems 476
Chapter 12 Distributed Database Management Systems 480
12.1 The Evolution of Distributed Database Management Systems 481
12.2 DDBMS Advantages and Disadvantages 483
12.3 Distributed Processing and Distributed Databases 484
12.4 Characteristics of Distributed Database Management Systems 485
12.5 DDBMS Components 486
12.6 Levels of Data and Process Distribution 488
12.6.1 Single-Site Processing,Single-Site Data (SPSD) 488
12.6.2 Multiple-Site Processing,Single-Site Data (MPSD) 489
12.6.3 Multiple-Site Processing,Multiple-Site Data (MPMD) 490
12.7 Distributed Database Transparency Features 491
12.8 Distribution Transparency 492
12.9 Transaction Transparency 494
12.9.1 Distributed Requests and Distributed Transactions 494
12.9.2 Distributed Concurrency Control 498
12.9.3 Two-Phase Commit Protocol 498
XII

## Page 15

TABLE OF CONTENTS
12.10 Performance Transparency and Query Optimization 499
12.11 Distributed Database Design 501
12.11.1 Data Fragmentation 501
12.11.2 Data Replication 504
12.11.3 Data Allocation 506
12.12 Client/Server vs.DDBMS 507
12.13 C.J.Date’s Twelve Commandments for Distributed Databases 508
Summary 509
Key Terms 510
Review Questions 510
Problems 511
Chapter 13 Business Intelligence and Data Warehouses 514
13.1 The Need for Data Analysis 515
13.2 Business Intelligence 515
13.3 Business Intelligence Architecture 517
13.4 Decision Support Data 521
13.4.1 Operational Data vs.Decision Support Data 521
13.4.2 Decision Support Database Requirements 523
13.5 The Data Warehouse 526
13.5.1 Twelve Rules that Define a Data Warehouse 528
13.5.2 Decision Support Architectural Styles 529
13.6 Online Analytical Processing 529
13.6.1 Multidimensional Data Analysis Techniques 529
13.6.2 Advanced Database Support 533
13.6.3 Easy-to-Use End-User Interface 533
13.6.4 Client/Server Architecture 533
13.6.5 OLAP Architecture 533
13.6.6 Relational OLAP 537
13.6.7 Multidimensional OLAP 539
13.6.8 Relational vs.Multidimensional OLAP 540
13.7 Star Schemas 541
13.7.1 Facts 541
13.7.2 Dimensions 542
13.7.3 Attributes 542
13.7.4 Attribute Hierarchies 544
13.7.5 Star Schema Representation 545
13.7.6 Performance-Improving Techniques for the Star Schema 548
13.8 Implementing a Data Warehouse 551
13.8.1 The Data Warehouse as an Active Decision Support Framework 551
13.8.2 A Company-Wide Effort that Requires User Involvement 552
13.8.3 Satisfy the Trilogy:Data,Analysis,and Users 552
13.8.4 Apply Database Design Procedures 552
13.9 Data Mining 553
13.10 SQL Extensions for OLAP 556
13.10.1 The ROLLUP Extension 557
13.10.2 The CUBE Extension 558
13.10.3 Materialized Views 559
Summary 564
Key Terms 565
Review Questions 565
Problems 566
XIII

## Page 16

TABLE OF CONTENTS
PART V DATABASES AND THE INTERNET
Business Vignette: KBB Transforms with Innovative Web Services 573
Chapter 14 Database Connectivity and Web Technologies 574
14.1 Database Connectivity 575
14.1.1 Native SQL Connectivity 575
14.1.2 ODBC,DAO,and RDO 575
14.1.3 OLE-DB 579
14.1.4 ADO.NET 581
14.1.5 Java Database Connectivity (JDBC) 583
14.2 Internet Databases 585
14.2.1 Web-to-Database Middleware:Server-Side Extensions 586
14.2.2 Web Server Interfaces 588
14.2.3 The Web Browser 589
14.2.4 Client-Side Extensions 590
14.2.5 Web Application Servers 591
14.3 Extensible Markup Language (XML) 592
14.3.1 Document Type Definitions (DTD) and XML Schemas 594
14.3.2 XML Presentation 596
14.3.3 XML Applications 597
14.4 SQL Data Services 600
Summary 602
Key Terms 603
Review Questions 603
Problems 604
PART VI DATABASE ADMINISTRATION
Business Vignette:The Rising SQL Injection Threat 607
Chapter 15 Database Administration and Security 608
15.1 Data as a Corporate Asset 609
15.2 The Need for and Role of a Database in an Organization 610
15.3 Introduction of a Database:Special Considerations 612
15.4 The Evolution of the Database Administration Function 613
15.5 The Database Environment’s Human Component 616
15.5.1 The DBA’s Managerial Role 618
15.5.2 The DBA’s Technical Role 623
15.6 Security 629
15.6.1 Security Policies 629
15.6.2 Security Vulnerabilities 630
15.6.3 Database Security 631
15.7 Database Administration Tools 633
15.7.1 The Data Dictionary 633
15.7.2 CASE Tools 635
XIV

## Page 17

TABLE OF CONTENTS
15.8 Developing a Data Administration Strategy 637
15.9 The DBA at Work:Using Oracle for Database Administration 639
15.9.1 Oracle Database Administration Tools 640
15.9.2 The Default Login 640
15.9.3 Ensuring an Automatic RDBMS Start 641
15.9.4 Creating Tablespaces and Datafiles 642
15.9.5 Managing the Database Objects:Tables,Views,Triggers,and Procedures 643
15.9.6 Managing Users and Establishing Security 644
15.9.7 Customizing the Database Initialization Parameters 647
Summary 648
Key Terms 649
Review Questions 649
Glossary 653
Index 672
IN THE PREMIUM WEBSITE
The Premium Website can be found atcengage.com/mis/coronel.Locate your premium access card in the front of each new
book purchase,and click “Create My Account” to begin the registration process.If you’ve purchased a used book,please
search forDatabase Systems,Ninth Edition atwww.ichapters.com where you can purchase instant access.
Appendix A Designing Databases with Visio Professional: A Tutorial
Appendix B The University Lab: Conceptual Design
Appendix C The University Lab: Conceptual Design Verification, Logical Design,
andImplementation
Appendix D Converting an ER Model into a Database Structure
Appendix E Comparison of ER Model Notations
Appendix F Client/Server Systems
Appendix G Object-Oriented Databases
Appendix H Unified Modeling Language (UML)
Appendix I Databases in Electronic Commerce
Appendix J Web Database Development with ColdFusion
Appendix K The Hierarchical Database Model
Appendix L The Network Database Model
Appendix M Microsoft® Access® Tutorial
Appendix N Creating a New Database with Oracle 11g
Answers to Selected Questions and Problems
XV

## Page 18

PREFACE
This database systems book has been successful through eight editions because the authors,editors,and the publisher
paid attention to the impact of technology and to adopter questions and suggestions.We believe that this ninth edition
successfully reflects the same attention to such stimuli.Furthermore this ninth edition marks the addition of a new
co-author,Steven Morris.Steven brings his wealth of knowledge,teaching experience,and expertise to this work.
In many respects,rewriting a book is more difficult than writing it the first time.If the book is successful,as this one is,
a major concern is that the updates,inserts,and deletions will adversely affect writing style and continuity of coverage.
Fortunately,this edition benefits from the incorporation of a new co-author with fresh ideas and perspectives balanced
by the experience of the original authors to ensure continuity of writing style and quality of presentation.In addition,the
efforts of a combination of superb reviewers and editors,plus a wealth of feedback from adopters and students of the
previous editions,helped provide the guidance that make this new edition the best yet.
XVI

## Page 19

PREFACE
CHANGES TO THE NINTH EDITION
In this ninth edition, we have added some new features and we have reorganized some of the coverage to provide a
better flow of material. Aside from enhancing the already strong database design coverage, we have made other
improvements in the topical coverage. Here are a few of the highlights:
• Updated Business Vignettes showing the impact of database technologies in the real world.
• Strengthened the database design contents by more clearly differentiating among the conceptual, logi-
cal, and physical design stages.
• Streamlined and modernized the coverage of database evolution and the importance of database design
skills.
• Enhanced the coverage of data models by shifting the focus from a historical perspective to emerging
data technologies.
• Expanded end-of-chapter review questions and problems and introduced a new Cases section to
selected chapters.
• Formalized and improved consistency of normalization concepts.
• Improved readability and overall visual appeal of the book.
• Created a database design process guide and a data modeling checklist as cover inserts.
This ninth edition continues to provide a solid and practical foundation for the design, implementation, and manage-
ment of database systems. This foundation is built on the notion that, while databases are very practical things, their
successful creation depends on understanding the important concepts that define them. It’s not easy to come up with
the proper mix of theory and practice, but we are grateful that the previously mentioned feedback suggests that we
largely succeeded in our quest to maintain the proper balance.
THE APPROACH: A CONTINUED EMPHASIS ON DESIGN
As the title suggests, Database Systems: Design, Implementation, and Management covers three broad aspects of
database systems. However, for several important reasons, special attention is given to database design.
• The availability of excellent database software enables even database-inexperienced people to create
databases and database applications. Unfortunately, the “create without design” approach usually
paves the road to any number of database disasters. In our experience, many, if not most, database sys-
tem failures are traceable to poor design and cannot be solved with the help of even the best program-
mers and managers. Nor is better DBMS software likely to overcome problems created or magnified by
poor design. Using an analogy, even the best bricklayers and carpenters can’t create a good building
from a bad blueprint.
• Most of the vexing database system management problems seem to be triggered by poorly designed data-
bases. It hardly seems worthwhile to use scarce resources to develop excellent and extensive database sys-
tem management skills in order to exercise them on crises induced by poorly designed databases.
• Design provides an excellent means of communication. Clients are more likely to get what they need
when database system design is approached carefully and thoughtfully. In fact, clients may discover
how their organizations really function once a good database design is completed.
XVII

## Page 20

PREFACE
• Familiarity with database design techniques promotes one’s understanding of current database tech-
nologies. For example, because data warehouses derive much of their data from operational databases,
data warehouse concepts, structures, and procedures make more sense when the operational data-
base’s structure and implementation are understood.
Because the practical aspects of database design are stressed, we have covered design concepts and procedures in
detail, making sure that the numerous end-of-chapter problems and cases are sufficiently challenging so students can
develop real and useful design skills. We also make sure that students understand the potential and actual conflicts
between database design elegance, information requirements, and transaction processing speed. For example, it
makes little sense to design databases that meet design elegance standards while they fail to meet end-user information
requirements. Therefore, we explore the use of carefully defined trade-offs to ensure that the databases are capable of
meeting end-user requirements while conforming to high design standards.
TOPICAL COVERAGE
The Systems View
The book’s title begins with Database Systems. Therefore, we examine the
database and design concepts covered in Chapters 1–6 as part of a larger
whole by placing them within the systems analysis framework of Chapter 9.
We believe that database designers who fail to understand that the database
is part of a larger system are likely to overlook important database design
requirements. In fact, Chapter 9, Database Design, provides the map for
the advanced database design developed in Appendixes B and C. Within
the larger systems framework, we can also explore issues such as transac-
tion management and concurrency control (Chapter 10), distributed data-
base management systems (Chapter 12), business intelligence and data
warehouses (Chapter 13), database connectivity and Web technologies
(Chapter 14), and database administration and security (Chapter 15).
Database Design
The first item in the
book’s subtitle is Design,
and our examination of
database design is com-
prehensive. For example, Chapters 1 and 2 examine the development
and future of databases and data models and illustrate the need for
design. Chapter 3 examines the details of the relational database
model; Chapter 4 provides extensive, in-depth, and practical database
design coverage; and Chapter 5 explores advanced database design
topics. Chapter 6 is devoted to critical normalization issues that affect
database efficiency and effectiveness. Chapter 9 examines database
design within the systems framework and maps the activities required
to successfully design and implement the complex real-world database
XVIII

## Page 21

PREFACE
developed in Appendixes B and C. Appendix A, Designing Databases with Visio Professional: A Tutorial, provides a
good introductory tutorial for the use of a database design tool.
Because database design is affected by real-world transactions, the way data are distributed, and ever-increasing
information requirements, we examine major database features that must be supported in current-generation data-
bases and models. For example, Chapter 10, Transaction Management and Concurrency Control, focuses on the
characteristics of database transactions and how they affect database integrity and consistency. Chapter 11,
Database Performance Tuning and Query Optimization, illustrates the need for query efficiency in a real world that
routinely generates and uses terabyte-sized databases and tables with millions of records. Chapter 12, Distributed
Database Management Systems, focuses on data distribution, replication, and allocation. In Chapter 13, Business
Intelligence and Data Warehouses, we explore the characteristics of the databases that are used in decision support
and online analytical processing. Chapter 14, Database Connectivity and Web Technologies, covers the basic data-
base connectivity issues encountered in a Web-based data world, and it shows the development of Web-based data-
base front ends.
Implementation
The second portion of the subtitle is Implementation. We use Structured
Query Language (SQL) in Chapters 7 and 8 to show how databases are
implemented and managed. Appendix M, Microsoft Access Tutorial, pro-
vides a quick but comprehensive guide to MS Access database implemen-
tation. Appendixes B and C demonstrate the design of a database that was
fully implemented and they illustrate a wide range of implementation
issues. We had to deal with conflicting design goals: design elegance, infor-
mation requirements, and operational speed. Therefore, we carefully
audited the initial design (Appendix B) to check its ability to meet end-user
needs and to establish appropriate implementation protocols. The result of
this audit yielded the final, implementable design developed in Appendix
C. The special issues encountered in an Internet database environment are
addressed in Chapter 14, Database Connectivity and Web Technologies,
and in Appendix J, Web
Database Development
with ColdFusion.
Management
The final portion of the subtitle is Management. We deal with database
management issues in Chapter 10, Transaction Management and
Concurrency Control; Chapter 12, Distributed Database Management
Systems; and Chapter 15, Database Administration and Security.
Chapter 11, Database Performance Tuning and Query Optimization, is
a valuable resource that illustrates how a DBMS manages the data
retrieval operations. In addition, Appendix N, Creating a New Database
Using Oracle 11g, walks you through the process of setting up a new
database.
XIX

## Page 22

PREFACE
TEACHING DATABASE: A MATTER OF FOCUS
Given the wealth of detailed coverage, instructors can “mix and match” chapters to produce the desired coverage.
Depending on where database courses fit into the curriculum, instructors may choose to emphasize database design or
database management. (See Figure 1.)
The hands-on nature of database design lends itself particularly well to class projects for which students use instructor-
selected software to prototype a student-designed system for the end user. Several of the end-of-chapter problems are
sufficiently complex to serve as projects, or an instructor may work with local businesses to give students hands-on
experience. Note that some elements of the database design track are also found in the database management track.
This is because it is difficult to manage database technologies that are not understood.
The options shown in Figure 1 serve only as a starting point. Naturally, instructors will tailor their coverage based on
their specific course requirements. For example, an instructor may decide to make Appendix I an outside reading
assignment and Appendix A a self-taught tutorial, then use that time to cover client/server systems or object-oriented
databases. The latter choice would serve as a gateway to UML coverage.
FIGURE
1
Core Coverage
(1) Database Systems
(2) Data Models
(3) The Relational Database Model
(4) Entity Relationship (ER) Modeling
(6) Normalization of Database Tables
(7) Introduction to Structured Query Language (SQL)
Database Design and Implementation Focus Database Management Focus
(5) Advanced Data Modeling (10) Transaction Management and Concurrency Control
(8) Advanced SQL (11) Database Performance Tuning and Query Optimization
(9) Database Design (12) Distributed Database Management Systems
(D) Converting an ER Model into a Database Structure (13) The Data Warehouse
(E) Comparison of ER Model Notations (15) Database Administration
(H) Unified Modeling Language (UML) (F) Client/Server Systems
(11) Database Performance Tuning and Query Optimization (G) Object-Oriented Databases
(14) Database Connectivity and Web Development (I) Databases in Electronic Commerce
(J) Web Database Development with ColdFusion
Supplementary Reading Supplementary Reading
(A) Designing Databases with Visio Professional: A Tutorial (9) Database Design
(B) The University Lab: Conceptual Design (A) Designing Databases with Visio Professional: A Tutorial
(C) The University Lab: Conceptual Design Verification, (D) Converting an ER Model into a Database Structure
Logical Design, and Implementation (E) Comparison of ER Model Notations
(F) Client/Server Systems (K) The Hierarchical Database Model
(L) The Network Database Model (L) The Network Database Model
(M) Microsoft Access Tutorial (N) Creating a New Database Using Oracle 11g
XX

## Page 23

TEXT FEATURES
TheRelationalRevolution
B
Today,wetakeforgrantedthebenefitsbroughttousbyrelationaldatabases:theability
tostore,access,andchangedataquicklyandeasilyonlow-costcomputers.Yet,untilthe usiness
late1970s,databasesstoredlargeamountsofdatainahierarchicalstructurethatwas Vignette
difficulttonavigateandinflexible.Programmersneededtoknowwhatclientswantedto
Business Vignettes dowiththedatabeforethedatabasewasdesigned.Addingorchangingthewaythedata
highlight part topics in wasanalyzedwasatime-consumingandexpensiveprocess.Asaresult,yousearched
throughhugecardcatalogstofindalibrarybook,youusedroadmapsthatdidntshow
areal-life setting. changesmadeinthelastyear,andyouhadtobuyanewspaperto findinformationon
stockprices.
In1970,Edgar“Ted”Codd,amathematicianemployedbyIBM,wroteanarticlethat
wouldchangeallthat.Atthetime,nobodyrealizedthatCodd’sobscuretheorieswould
Online Content
Online Content boxes
ThedatabasesusedineachchapterareavailableinthePremiumWebsiteforthisbook.Throughoutthebook,
draw attention to material OnlineContentboxeshighlightmaterialrelatedtochaptercontentlocatedinthePremiumWebsite.
in the Premium Website
for this text and provide
ideas for incorporating Note
this content into the course.
Datathatdisplaydatainconsistencyarealsoreferredtoasdatathatlackdataintegrity.Dataintegrityisdefined
astheconditioninwhichallofthedatainthedatabaseareconsistentwiththereal-worldeventsandconditions.
Inotherwords,dataintegritymeansthat:
•Dataareaccurate—therearenodatainconsistencies.
•Dataareverifiable—thedatawillalwaysyieldconsistentresults.
Noteshighlight impor-
tant facts about the con-
cepts introduced in the FIGURE Illustrating data storage management with Oracle
1.9
chapter.
Database Name: ORALAB.MTSU.EDU
A variety of four-color
figures, including ER
models and implementa-
tions, tables, and illustra-
tions, clearly illustrate
difficult concepts.
The ORALAB database is The Oracle DBA Studio
actually stored in nine Management interface also
datafiles located on the C: shows the amount of space
drive of the database server used by each of the datafiles
computer. that constitute the single
logical database.
The Oracle DBA Studio Administrator GUI shows the data storage
management characteristics for the ORALAB database.
XXI

## Page 24

TEXT FEATURES
S u m m a r y
TheERMusesERDstorepresenttheconceptualdatabaseasviewedbytheenduser.TheERM’smaincomponents A robust Summaryat
areentities,relationships,andattributes.TheERDalsoincludesconnectivityandcardinalitynotations.AnERDcan
the end of each chap-
also show relationship strength, relationship participation (optional or mandatory), and degree of relationship
(unary,binary,ternary,etc.). ter ties together the
Connectivitydescribestherelationshipclassification(1:1,1:M,orM:N).Cardinalityexpressesthespecificnumber major concepts and
ofentityoccurrencesassociatedwithanoccurrenceofarelatedentity.Connectivitiesandcardinalitiesareusually serves as a quick
basedonbusinessrules.
review for students.
IntheERM,aM:Nrelationshipisvalidattheconceptuallevel.However,whenimplementingtheERMina
relationaldatabase,theM:Nrelationshipmustbemappedtoasetof1:Mrelationshipsthroughacompositeentity.
K e y T e r m s
binaryrelationship,118 identifyingrelationship,112 relationshipdegree,118
An alphabetic list of
cardinality,109 iterativeprocess,124 simpleattribute,106
Key Termspoints to
compositeattribute,105 mandatoryparticipation,116 single-valuedattribute,106
compositekey,105 multivaluedattribute,106 strongrelationship,112 the pages where terms
derivedattribute,107 non-identifyingrelationship,111 ternaryrelationship,118 are first explained.
existence-dependent,110 optionalparticipation,116 unaryrelationship,118
R e v i e w Q u e s t i o n s
1. Whattwoconditionsmustbemetbeforeanentitycanbeclassifiedasaweakentity?Giveanexampleofa
Review Questions
weakentity.
2. Whatisastrong(oridentifying)relationship,andhowisitdepictedinaCrow’sFootERD? challenge students to
3. Giventhebusinessrule“anemployeemayhavemanydegrees,”discussitseffectonattributes,entities,and apply the skills learned
relationships.(Hint:Rememberwhatamultivaluedattributeisandhowitmightbeimplemented.)
in each chapter.
4. Whatisacompositeentity,andwhenisitused?
5. SupposeyouareworkingwithintheframeworkoftheconceptualmodelinFigureQ4.5.
P r o b l e m s
1. Giventhefollowingbusinessrules,createtheappropriateCrow’sFootERD.
Problemsbecome
a. Acompanyoperatesmanydepartments.
b. Eachdepartmentemploysoneormoreemployees. progressively more
c. Eachoftheemployeesmayormaynothaveoneormoredependents. complex as students
d. Eachemployeemayormaynothaveanemploymenthistory. draw on the lessons
2. TheHudsonEngineeringGroup(HEG)hascontactedyoutocreateaconceptualmodelwhoseapplicationwill
learned from the com-
meettheexpecteddatabaserequirementsforthecompany’strainingprogram.TheHEGadministratorgivesyou
pletion of preceding
problems.
XXII

## Page 25

ADDITIONAL FEATURES
PREMIUM WEBSITE
Single Sign On (SSO) provides a central location from which you can access Cengage Learning’s online learning solu-
tions with convenience and flexibility. You can:
• Gain access to online resources including robust Premium Website.
• Simplify your coursework by reducing human error and the need to keep track of multiple passwords.
See the insert card at the front of this book for instructions on how to access this text’s SSO site.
This Web resource, which you will find referenced throughout the book in the Online Content boxes, includes the fol-
lowing features:
Appendixes
Fourteen appendixes provide additional material on a variety of important areas, such as using Microsoft®Visio®and
Microsoft® Access®, ER model notations, UML, object-oriented databases, databases and electronic commerce, and
Adobe®ColdFusion®.
Answers to Selected Questions and Problems
The authors have provided answers to selected Review Questions and Problems from each chapter to help students
check their comprehension of chapter content and database skills.
Database, SQL Script, and ColdFusion Files
The Premium Website for this book includes all of the database structures and table contents used in the text. For students
™
using Oracle®and Microsoft SQL Server , the SQL scripts to create and load all tables used in the SQL chapters (7 and 8)
are included. In addition, all ColdFusion scripts used to develop the Web interfaces shown Appendix J are included.
Video Tutorials
Custom-made video tutorials by Peter Rob and Carlos Coronel, exclusive to this textbook, provide clear explanations
of the essential concepts presented in the book. These unique tutorials will help the user gain a better understanding of
topics such as SQL, Oracle, ERDs, and ColdFusion.
Test Yourself on Database Systems
Brand new quizzes, created specifically for this site, allow users to test themselves on the content of each chapter and
immediately see what answers they answered right and wrong. For each question answered incorrectly, users are pro-
vided with the correct answer and the page in the text where that information is covered. Special testing software ran-
domly compiles a selection of questions from a large database, so students can take quizzes multiple times on a given
chapter, with some new questions each time.
®
Microsoft PowerPoint Slides
Direct access is offered to the book’s PowerPoint presentations that cover the key points from each chapter. These
presentations are a useful study tool.
Useful Web Links
Students can access a chapter-by-chapter repository of helpful and relevant links for further research.
Glossary of Key Terms
Students can view a PDF file of the glossary from the book. They can also search for keywords and terms in this file;
it’s quick and easy to use!
Q & A
Helpful question-and-answer documents are available for download. Here you will find supporting material in areas
such as Data Dependency/Structural Dependency and Weak Entities/Strong Relationships.
XXIII

## Page 26

ADDITIONAL FEATURES
INSTRUCTOR RESOURCES
Database Systems: Design, Implementation, and Management, Ninth Edition, includes teaching tools to support
instructors in the classroom. The ancillaries that accompany the textbook are listed below. Most of the teaching tools
available with this book are provided to the instructor on a single CD-ROM; they are also available on the Web at
www.cengage.com/mis/coronel.
Instructor’s Manual
The authors have created this manual to help instructors make their classes informative and interesting. Because the
authors tackle so many problems in depth, instructors will find the Instructor’s Manualespecially useful. The details of
the design solution process are shown in detail in the Instructor’s Manual as well as notes about alternative
approaches that may be used to solve a particular problem. Finally, the book’s questions and problems together with
their answers and solutions are included.
SQL Script Files for Instructors
The authors have provided teacher’s SQL script files to create and delete users. They have also provided SQL scripts
to let instructors cut and paste the SQL code into the SQL windows. (Scripts are provided for Oracle as well as for MS
SQL Server.) The SQL scripts, which have all been tested by Course Technology, are a major convenience for instruc-
tors. You won’t have to type in the SQL commands and the use of the scripts eliminates errors due to “typos” that are
sometimes difficult to trace.
ColdFusion Files for Instructors
The ColdFusion Web development solutions are provided. Instructors have access to a menu-driven system that lets
teachers show the code as well as the execution of that code.
Databases
Microsoft®Access®Instructor databases are available for many chapters that include features not found in the student
databases. For example, the databases that accompany Chapters 7 and 8 include many of the queries that produce the
problem solutions. Other Access databases, such as the ones accompanying Chapters 3, 4, 5, and 6, include the
implementation of the design problem solutions to let instructors illustrate the effect of design decisions. All the MS
Access files are in the Access 2000 format so that students can use them regardless of what version they have installed
on their computers. In addition, instructors have access to all the script files for both Oracle and MS SQL Server so that
all the databases and their tables can be converted easily and precisely.
XXIV

## Page 27

ADDITIONAL FEATURES
Solutions
Instructors are provided with solutions to all Review Questions and Problems. Intermediate solution steps for the more
complex problems are shown to make the instructor’s job easier. Solutions may also be found on the Course
Technology Web site at www.cengage.com/mis/coronel. The solutions are password-protected.
®
ExamView
This objective-based test generator lets the instructor create paper, LAN, or Web-based tests from test banks designed
specifically for this Course Technology text. Instructors can use the QuickTest Wizard to create tests in fewer than five
minutes by taking advantage of Course Technology’s question banks, or instructors can create customized exams.
®
PowerPoint Presentations
Microsoft PowerPoint slides are included for each chapter. Instructors can use the slides in a variety of ways; for exam-
ple, as teaching aids during classroom presentations or as printed handouts for classroom distribution. Instructors can
modify the slides provided or include slides of their own for additional topics introduced to the class.
Figure Files
Figure files for solutions presented in the Instructor’s Manual allow instructors to create their own presentations.
Instructors can also manipulate these files to meet their particular needs.
WebTutor™
Whether you want to Web-enable your class or teach entirely online, WebTutor provides customizable, rich, text-spe-
cific content that can be used with both WebCT®and BlackBoard®. WebTutor allows instructors to easily blend, add,
edit, reorganize, or delete content. Each WebTutor product provides media assets, quizzing, Web links, discussion top-
ics, and more.
XXV

## Page 28

ACKNOWLEDGMENTS
Regardless of how many editions of this book are published, they will always rest on the solid foundation created by the first
edition. We remain convinced that our work has become successful because that first edition was guided by Frank Ruggirello,
a former Wadsworth senior editor and publisher. Aside from guiding the book’s development, Frank also managed to solicit
the great Peter Keen’s evaluation (thankfully favorable) and subsequently convinced PK to write the foreword for the first edi-
tion. Although we sometimes found Frank to be an especially demanding taskmaster, we also found him to be a superb pro-
fessional and a fine friend. We suspect Frank will still see his fingerprints all over our current work. Many thanks.
A difficult task in rewriting a book is deciding what new approaches, topical coverage, and depth of coverage changes
can or cannot fit into a book that has successfully weathered the test of the marketplace. The comments and sugges-
tions made by the book’s adopters, students, and reviewers play a major role in deciding what coverage is desirable and
how that coverage is to be treated.
Some adopters became extraordinary reviewers, providing incredibly detailed and well-reasoned critiques even as they
praised the book’s coverage and style. Dr. David Hatherly, a superb database professional who is a senior lecturer in the
School of Information Technology, Charles Sturt University–Mitchell, Bathhurst, Australia, made sure that we knew precisely
what issues led to his critiques. Even better for us, he provided the suggestions that made it much easier for us to improve
the topical coverage in earlier editions. Dr. Hatherly’s recommendations continue to be reflected in this ninth edition. All of
his help was given freely and without prompting on our part. His efforts are much appreciated, and our thanks are heartfelt.
We also owe a debt of gratitude to Professor Emil T. Cipolla, who teaches at St. Mary College. Professor Cipolla’s wealth
of IBM experience turned out to be a valuable resource when we tackled the embedded SQL coverage in Chapter 8.
Every technical book receives careful scrutiny by several groups of reviewers selected by the publisher. We were fortu-
nate to face the scrutiny of reviewers who were superbly qualified to offer their critiques, comments, and suggestions—
many of which were used to strengthen this edition. While holding them blameless for any remaining shortcomings, we
owe these reviewers many thanks for their contributions:
Amita G. Chin, Virginia Commonwealth University
Samuel Conn, Regis University
Bill Hochstettler, Franklin University
Lionel M. Holguin, Jr., Athens State University
Larry Molloy, Oakland Community College
Bruce Myers, Austin Peay State University
Steven Robinett, Allegany College of Maryland
Ioulia Rytikova, George Mason University
Samuel Sambasivam, Azusa Pacific University
Kevin Scheibe, Iowa State University
Ganesan Shankaranarayanan, Boston University
Xingzhong (Frank) Shi, New Jersey Institute of Technology
Yingbing Yu, Austin Peay State Univeristy
XXVI

## Page 29

ACKNOWLEDGMENTS
Because this ninth edition is build solidly on the foundation of the previous editions, we would also like to thank the
following reviewers for their efforts in helping to make the previous editions successful: Dr. Reza Barkhi, Pamplin
College of Business, Virginia Polytechnic Institute and State University; Dr. Vance Cooney, Xavier University; Harpal
S. Dillion, Southwestern Oklahoma State University; Janusz Szczypula, Carnegie Mellon University; Dr. Ahmad
Abuhejleh, University of Wisconsin, River Falls; Dr. Terence M. Baron, University of Toledo; Dr. Juan Estava, Eastern
Michigan University; Dr. Kevin Gorman, University of North Carolina, Charlotte; Dr. Jeff Hedrington, University of
Wisconsin, Eau Claire; Dr. Herman P. Hoplin, Syracuse University; Dr. Sophie Lee, University of Massachusetts,
Boston; Dr. Michael Mannino, University of Washington; Dr. Carol Chrisman, Illinois State University; Dr. Timothy
Heintz, Marquette University; Dr. Herman Hoplin, Syracuse University; Dr. Dean James, Embry-Riddle University;
Dr. Constance Knapp, Pace University; Dr. Mary Ann Robbert, Bentley College; Dr. Francis J. Van Wetering,
University of Nebraska; Dr. Joseph Walls, University of Southern California; Dr. Stephen C. Solosky, Nassau
Community College; Dr. Robert Chiang, Syracuse University; Dr. Crist Costa, Rhode Island College; Dr. Sudesh M.
Duggal, Northern Kentucky University; Dr. Chang Koh, University of North Carolina, Greensboro; Paul A. Seibert,
North Greenville College; Neil Dunlop, Vista Community College; Ylber Ramadani, George Brown College; Samuel
Sambasivam, Azusa Pacific University; Arjan Sadhwani, San Jose State University; Genard Catalano, Columbia
College; Craig Shaw, Central Community College; Lei-da Chen, Creighton University; Linda K. Lau, Longwood
University; Anita Lee-Post, University of Kentucky; Lenore Horowitz, Schenectady County Community College;
Dr. Scott L. Schneberger, Georgia State University; Tony Pollard, University of Western Sydney; Lejla Vrazalic,
University of Wollongong; and David Witzany, Parkland College.
In some respects, writing books resembles building construction: When 90 percent of the work seems done, 90 per-
cent of the work remains to be done. Fortunately for us, we had a great team on our side.
• How can we possibly pay sufficient homage to Deb Kaufmann’s many contributions? Even our best
superlatives don’t begin to paint a proper picture of our professional relationship with Deb
Kaufmann, our developmental editor since the fifth edition. Deb has that magic combination of good
judgment, intelligence, technical skill, and the rare ability to organize and sharpen an author’s writ-
ing without affecting its intent or its flow. And she does it all with style, class, and humor. She is the
best of the best.
• After writing so many books and eight editions of thisbook, we know just how difficult it can be to
transform the authors’ work into an attractive book. The production team, both at Course
Technology (Matt Hutchinson) and GEX Publishing Services (Louise Capulli and Marisa Taylor),
have done an excellent job.
• We also owe Kate Mason, our product manager, special thanks for her ability to guide this book to a
successful conclusion. Kate’s work touched all of the publication bases, and her managerial skills pro-
tected us from those publishing gremlins that might have become a major nuisance. Not to mention the
fact that her skills in dealing with occasionally cranky authors far exceed those of any diplomat we can
think of. And did we mention that Kate is, quite simply, a delightful person?
• Many thanks to Andrea Schein, our copyeditor. Given her ability to spot even the smallest discrepan-
cies, we suspect that her middle name is “Thorough.” We can only imagine the level of mental disci-
pline required to perform her job and we salute her.
XXXXVVIIII

## Page 30

ACKNOWLEDGMENTS
We also thank our students for their comments and suggestions. They are the reason for writing this book in the first
place. One comment stands out in particular: “I majored in systems for four years, and I finally discovered why when I
took your course.” And one of our favorite comments by a former student was triggered by a question about the chal-
lenges created by a real-world information systems job: “Doc, it’s just like class, only easier. You really prepared me
well. Thanks!”
Last, and certainly not least, we thank our families for the solid home support. They graciously accepted the fact that
during more than a year’s worth of rewriting, there would be no free weekends, rare free nights, and even rarer free
days. We owe you much, and the dedication we wrote to you is but a small reflection of the important space you
occupy in our hearts.
Carlos Coronel, Steven Morris, and Peter Rob
XXVIII

## Page 31

This page intentionally left blank

## Page 32

PART
I
DATABASE CONCEPTS
1
Database Systems
2
Data Models

## Page 33

The Relational Revolution
B
Today,we take for granted the benefits brought to us by relational databases:the ability
tostore,access,andchangedataquicklyandeasilyonlow-costcomputers.Yet,untilthe usiness
late 1970s,databases stored large amounts of data in a hierarchical structure that was V
ignette
difficulttonavigateandinflexible.Programmersneededtoknowwhatclientswantedto
dowiththedatabeforethedatabasewasdesigned.Addingorchangingthewaythedata
was analyzed was a time-consuming and expensive process.As a result, you searched
through huge card catalogs to find a library book,you used road maps that didn’t show
changes made in the last year,and you had to buy a newspaper to find information on
stock prices.
In 1970, Edgar “Ted” Codd, a mathematician employed by IBM, wrote an article that
wouldchangeallthat. Atthetime,nobodyrealizedthatCodd’sobscuretheorieswould
sparkatechnologicalrevolutiononparwiththedevelopmentofpersonalcomputersand
the Internet.Don Chamberlin,coinventor of SQL,the most popular computer language
used by database systems today,explains,“There was this guyTed Codd who had some
kindofstrangemathematicalnotation,butnobodytookitveryseriously.”ThenTedCodd
organizedasymposium,andChamberlinlistenedasCoddreducedcomplicatedfive-page
programs to one line.“And I said,‘Wow,’” Chamberlin recalls.
The symposium convinced IBM to fund System R, a research project that built a
prototypeofarelationaldatabaseandthatwouldeventuallyleadtothecreationofSQL
andDB2.IBM,however,keptSystemRonthebackburnerforanumberofcrucialyears.
ThecompanyhadavestedinterestinIMS,areliable,high-enddatabasesystemthathad
comeoutin1968.Unawareofthemarketpotentialofthisresearch,IBMalloweditsstaff
to publish these papers publicly.
Among those reading these papers was Larry Ellison, who had just founded a small
company.RecruitingprogrammersfromSystemRandtheUniversityofCalifornia,Ellison
was able to market the first SQL-based relational database in 1979,well before IBM.By
1983, the company had released a portable version of the database, grossed over
$5,000,000 annually,and changed its name to Oracle.Spurred on by competition,IBM
finally released SQL/DS,its first relational database,in 1980.
IBMhasyettocatchup.By2007,globalsalesofrelationaldatabasemanagementsystems
rose to $18.8 billion.Oracle captured 48.6% of the market share,more than its two
closest competitors,IBM and Microsoft,combined.

## Page 34

1
Database Systems
In this chapter, you will learn:
(cid:1) The difference between data and information
(cid:1) What a database is, the various types of databases, and why they are valuable assets for
decision making
(cid:1) The importance of database design
(cid:1) How modern databases evolved from file systems
(cid:1) About flaws in file system data management
(cid:1) The main components of the database system
(cid:1) The main functions of a database management system (DBMS)
Gooddecisionsrequiregoodinformationthatisderivedfromrawfacts.Theserawfactsare
known as data.Data are likely to be managed most efficiently when they are stored in a
database.In this chapter,you will learn what a database is,what it does,and why it yields
P
betterresultsthanotherdatamanagementmethods.Youwillalsolearnaboutvarioustypes
of databases and why database design is so important. review
Databases evolved from computer file systems.Although file system data management is
now largely outmoded, understanding the characteristics of file systems is important
becausefilesystemsarethesourceofseriousdatamanagementlimitations.Inthischapter,
you will also learn how the database system approach helps eliminate most of the
shortcomings of file system data management.
E
N
O

## Page 35

DATABASE SYSTEMS 5
1.1 WHY DATABASES?
Imaginetryingtooperateabusinesswithoutknowingwhoyourcustomersare,whatproductsyouareselling,whois
workingforyou,whoowesyoumoney,andwhomyouowemoney.Allbusinesseshavetokeepthistypeofdataand
muchmore;andjustasimportantly,theymusthavethosedataavailabletodecisionmakerswhentheyneedthem.It
can be argued that the ultimate purpose of all business information systems is to help businesses use information as
anorganizationalresource.Attheheartofallofthesesystemsarethecollection,storage,aggregation,manipulation,
dissemination, and management of data.
Dependingonthetypeofinformationsystemandthecharacteristicsofthebusiness,thesedatacouldvaryfromafew
megabytesonjustoneortwotopicstoterabytescoveringhundredsoftopicswithinthebusiness’sinternalandexternal
environment.TelecommunicationscompaniessuchasSprintandAT&Tareknowntohavesystemsthatkeepdataon
trillions of phone calls, with new data being added to the system at speeds up to 70,000 calls per second!1 Not only
dothesecompanieshavetostoreandmanagetheseimmensecollectionsofdata,theyhavetobeabletofindanygiven
factinthatdataquickly.ConsiderthecaseofInternetsearchstapleGoogle.WhileGoogleisreluctanttodisclosemany
detailsaboutitsdatastoragespecifications,itisestimatedthatthecompanyrespondstoover91millionsearchesper
dayacrossacollectionofdatathatisseveralterabytesinsize.Impressively,theresultsofthesesearchesareavailable
nearly instantly.
How can these businesses process this much data? How can they store it all, and then quickly retrieve just the facts
thatdecisionmakerswanttoknow,justwhentheywanttoknowit?Theansweristhattheyusedatabases.Databases,
as explained in detail throughout this book, are specialized structures that allow computer-based systems to store,
manage, and retrieve data very quickly. Virtually all modern business systems rely on databases; therefore, a good
understanding of how these structures are created and their proper use is vital for any information systems
professional. Even if your career does not take you down the amazing path of database design and development,
databaseswillbeakeycomponentunderpinningthesystemsthatyouworkwith.Inanycase,itisverylikelythat,in
your career, you will be making decisions based on information generated from data. Thus, it is important that you
know the difference between data and information.
1.2 DATA VS. INFORMATION
Tounderstandwhatdrivesdatabasedesign,youmustunderstandthedifferencebetweendataandinformation.Data
arerawfacts.Thewordrawindicatesthatthefactshavenotyetbeenprocessedtorevealtheirmeaning.Forexample,
suppose that you want to know what the users of a computer lab think of its services. Typically, you would begin by
surveying users to assess the computer lab’s performance. Figure 1.1, Panel A, shows the Web survey form that
enablesuserstorespondtoyourquestions.Whenthesurveyformhasbeencompleted,theform’srawdataaresaved
to a data repository, such as the one shown in Figure 1.1, Panel B. Although you now have the facts in hand, they
are not particularly useful in this format—reading page after page of zeros and ones is not likely to provide much
insight.Therefore,youtransformtherawdataintoadatasummaryliketheoneshowninFigure1.1,PanelC.Now
it’s possible to get quick answers to questions such as “What is the composition of our lab’s customer base?” In this
case, you can quickly determine that most of your customers are juniors (24.59%) and seniors (53.01%). Because
graphics can enhance your ability to quickly extract meaning from data, you show the data summary bar graph in
Figure 1.1, Panel D.
Informationistheresultofprocessingrawdatatorevealitsmeaning.Dataprocessingcanbeassimpleasorganizing
data to reveal patterns or as complex as making forecasts or drawing inferences using statistical modeling. To reveal
meaning,informationrequirescontext.Forexample,anaveragetemperaturereadingof105degreesdoesnotmean
1“TopTenLargestDatabasesintheWorld,”BusinessIntelligenceLowdown,February15,2007,http://www.businessintelligencelowdown.com/
2007/02/top_10_largest_.html

## Page 36

6 CHAPTER 1
FIGURE Transforming raw data into information
1.1
a) Initial Survey Screen b) Raw Data
c) Information in Summary Format d) Information in Graphic Format
muchunlessyoualsoknowitscontext:IsthisindegreesFahrenheitorCelsius?Isthisamachinetemperature,abody
temperature, or an outside air temperature? Information can be used as the foundation for decision making. For
example, the data summary for each question on the survey form can point out the lab’s strengths and weaknesses,
helping you to make informed decisions to better meet the needs of lab customers.
Keep in mind that raw data must be properly formatted for storage, processing, and presentation. For example, in
PanelCofFigure1.1,thestudentclassificationisformattedtoshowtheresultsbasedontheclassificationsFreshman,
Sophomore, Junior, Senior, and Graduate Student. The respondents’ yes/no responses might need to be converted
toaY/Nformatfordatastorage.Morecomplexformattingisrequiredwhenworkingwithcomplexdatatypes,such
as sounds, videos, or images.
Inthis“informationage,”productionofaccurate,relevant,andtimelyinformationisthekeytogooddecisionmaking.
In turn, good decision making is the key to business survival in a global market. We are now said to be entering the

## Page 37

DATABASE SYSTEMS 7
“knowledgeage.”2Dataarethefoundationofinformation,whichisthebedrockofknowledge—thatis,thebodyof
information and facts about a specific subject. Knowledge implies familiarity, awareness, and understanding of
informationasitappliestoanenvironment.Akeycharacteristicofknowledgeisthat“new”knowledgecanbederived
from “old” knowledge.
Let’s summarize some key points:
(cid:2) Data constitute the building blocks of information.
(cid:2) Information is produced by processing data.
(cid:2) Information is used to reveal the meaning of data.
(cid:2) Accurate, relevant, and timely information is the key to good decision making.
(cid:2) Good decision making is the key to organizational survival in a global environment.
Timely and useful information requires accurate data. Such data must be properly generated and stored in a format
thatiseasytoaccessandprocess.And,likeanybasicresource,thedataenvironmentmustbemanagedcarefully.Data
management is a discipline that focuses on the proper generation, storage, and retrieval of data. Given the crucial
role that data play, it should not surprise you that data management is a core activity for any business, government
agency, service organization, or charity.
1.3 INTRODUCING THE DATABASE
Efficient data management typically requires the use of a computer database. A database is a shared, integrated
computer structure that stores a collection of:
(cid:2) End-user data, that is, raw facts of interest to the end user.
(cid:2) Metadata, or data about data, through which the end-user data are integrated and managed.
The metadata provide a description of the data characteristics and the set of relationships that links the data found
withinthedatabase.Forexample,themetadatacomponentstoresinformationsuchasthenameofeachdataelement,
the type of values (numeric, dates, or text) stored on each data element, whether or not the data element can be left
empty, and so on. The metadata provide information that complements and expands the value and use of the data.
Inshort,metadatapresentamorecompletepictureofthedatainthedatabase.Giventhecharacteristicsofmetadata,
you might hear a database described as a “collection of self-describing data.”
A database management system (DBMS) is a collection of programs that manages the database structure and
controls access to the data stored in the database. In a sense, a database resembles a very well-organized electronic
filing cabinet in which powerful software, known as a database management system, helps manage the cabinet’s
contents.
1.3.1 Role and Advantages of the DBMS
TheDBMSservesastheintermediarybetweentheuserandthedatabase.Thedatabasestructureitselfisstoredasa
collectionoffiles,andtheonlywaytoaccessthedatainthosefilesisthroughtheDBMS.Figure1.2emphasizesthe
point that the DBMS presents the end user (or application program) with a single, integrated view of the data in the
database.TheDBMSreceivesallapplicationrequestsandtranslatesthemintothecomplexoperationsrequiredtofulfill
thoserequests.TheDBMShidesmuchofthedatabase’sinternalcomplexityfromtheapplicationprogramsandusers.
TheapplicationprogrammightbewrittenbyaprogrammerusingaprogramminglanguagesuchasVisualBasic.NET,
Java, or C#, or it might be created through a DBMS utility program.
2Peter Drucker coined the phrase “knowledge worker” in 1959 in his book Landmarks of Tomorrow. In 1994, Ms. Esther Dyson, Mr. George
Keyworth,andDr.AlvinTofflerintroducedtheconceptofthe“knowledgeage.”

## Page 38

8 CHAPTER 1
FIGURE The DBMS manages the interaction between the end user and the database
1.2
End users
Database structure
Application Metadata
Data
request
Customers
http:// DBMS Single
Database View of Data Invoices End-user
Management System Integrated data
End users
Application Products
Data
request
Having a DBMS between the end user’s applications and the database offers some important advantages. First, the
DBMS enables the data in the database to be shared among multiple applications or users. Second, the DBMS
integrates the many different users’ views of the data into a single all-encompassing data repository.
Becausedataarethecrucialrawmaterialfromwhichinformationisderived,youmusthaveagoodmethodtomanage
suchdata.Asyouwilldiscoverinthisbook,theDBMShelpsmakedatamanagementmoreefficientandeffective.In
particular, a DBMS provides advantages such as:
(cid:2) Improved data sharing. The DBMS helps create an environment in which end users have better access to
more and better-managed data. Such access makes it possible for end users to respond quickly to changes in
their environment.
(cid:2) Improved data security. The more users access the data, the greater the risks of data security breaches.
Corporations invest considerable amounts of time, effort, and money to ensure that corporate data are used
properly. A DBMS provides a framework for better enforcement of data privacy and security policies.
(cid:2) Betterdataintegration.Wideraccesstowell-manageddatapromotesanintegratedviewoftheorganization’s
operations and a clearer view of the big picture. It becomes much easier to see how actions in one segment
of the company affect other segments.
(cid:2) Minimizeddatainconsistency.Datainconsistencyexistswhendifferentversionsofthesamedataappear
in different places. For example, data inconsistency exists when a company’s sales department stores a sales
representative’s name as “Bill Brown” and the company’s personnel department stores that same person’s
name as “William G. Brown,” or when the company’s regional sales office shows the price of a product as
$45.95 and its national sales office shows the same product’s price as $43.95. The probability of data
inconsistency is greatly reduced in a properly designed database.
(cid:2) Improved data access. The DBMS makes it possible to produce quick answers to ad hoc queries. From a
database perspective, a query is a specific request issued to the DBMS for data manipulation—for example,
toreadorupdatethedata.Simplyput,aqueryisaquestion,andanadhocqueryisaspur-of-the-moment
question.TheDBMSsendsbackananswer(calledthequeryresultset)totheapplication.Forexample,end

## Page 39

DATABASE SYSTEMS 9
users,whendealingwithlargeamountsofsalesdata,mightwantquickanswerstoquestions(adhocqueries)
such as:
- What was the dollar volume of sales by product during the past six months?
- What is the sales bonus figure for each of our salespeople during the past three months?
- How many of our customers have credit balances of $3,000 or more?
(cid:2) Improved decision making. Better-managed data and improved data access make it possible to generate
better-quality information, on which better decisions are based. The quality of the information generated
depends on the quality of the underlying data. Data quality is a comprehensive approach to promoting the
accuracy, validity, and timeliness of the data. While the DBMS does not guarantee data quality, it provides a
frameworktofacilitatedataqualityinitiatives.DataqualityconceptswillbecoveredinmoredetailinChapter
15, Database Administration and Security.
(cid:2) Increased end-user productivity. The availability of data, combined with the tools that transform data into
usable information, empowers end users to make quick, informed decisions that can make the difference
between success and failure in the global economy.
TheadvantagesofusingaDBMSarenotlimitedtothefewjustlisted.Infact,youwilldiscovermanymoreadvantages
as you learn more about the technical details of databases and their proper design.
1.3.2 Types of Databases
ADBMScansupportmanydifferenttypesofdatabases.Databasescanbeclassifiedaccordingtothenumberofusers,
the database location(s), and the expected type and extent of use.
The number of users determines whether the database is classified as single-user or multiuser. A single-user
databasesupportsonlyoneuseratatime.Inotherwords,ifuserAisusingthedatabase,usersBandCmustwait
until user A is done. A single-user database that runs on a personal computer is called a desktop database. In
contrast, a multiuser database supports multiple users at the same time. When the multiuser database supports a
relatively small number of users (usually fewer than 50) or a specific department within an organization, it is called a
workgroupdatabase.Whenthedatabaseisusedbytheentireorganizationandsupportsmanyusers(morethan50,
usually hundreds) across many departments, the database is known as an enterprise database.
Location might also be used to classify the database. For example, a database that supports data located at a single
siteiscalledacentralizeddatabase.Adatabasethatsupportsdatadistributedacrossseveraldifferentsitesiscalled
a distributed database. The extent to which a database can be distributed and the way in which such distribution
is managed are addressed in detail in Chapter 12, Distributed Database Management Systems.
The most popular way of classifying databases today, however, is based on how they will be used and on the time
sensitivity of the information gathered from them. For example, transactions such as product or service sales,
payments, and supply purchases reflect critical day-to-day operations. Such transactions must be recorded accurately
and immediately. A database that is designed primarily to support a company’s day-to-day operations is classified as
anoperationaldatabase(sometimesreferredtoasatransactionalorproductiondatabase).Incontrast,adata
warehouse focuses primarily on storing data used to generate information required to make tactical or strategic
decisions. Such decisions typically require extensive “data massaging” (data manipulation) to extract information to
formulate pricing decisions, sales forecasts, market positioning, and so on. Most decision support data are based on
dataobtainedfromoperationaldatabasesovertimeandstoredindatawarehouses.Additionally,thedatawarehouse
canstoredataderivedfrommanysources.Tomakeiteasiertoretrievesuchdata,thedatawarehousestructureisquite
different from that of an operational or transactional database. The design, implementation, and use of data
warehouses are covered in detail in Chapter 13, Business Intelligence and Data Warehouses.
Databases can also be classified to reflect the degree to which the data are structured. Unstructured data are data
thatexistintheiroriginal(raw)state,thatis,intheformatinwhichtheywerecollected.Therefore,unstructureddata
existinaformatthatdoesnotlenditselftotheprocessingthatyieldsinformation.Structureddataaretheresultof

## Page 40

10 CHAPTER 1
taking unstructured data and formatting (structuring) such data to facilitate storage, use, and the generation of
information. You apply structure (format) based on the type of processing that you intend to perform on the data.
Some data might not be ready (unstructured) for some types of processing, but they might be ready (structured) for
other types of processing. For example, the data value 37890 might refer to a zip code, a sales value, or a product
code. If this value represents a zip code or a product code and is stored as text, you cannot perform mathematical
computations with it. On the other hand, if this value represents a sales transaction, it is necessary to format it as
numeric.
Tofurtherillustratethestructureconcept,imagineastackofprintedpaperinvoices.Ifyouwanttomerelystorethese
invoicesasimagesforfutureretrievalanddisplay,youcanscanthemandsavetheminagraphicformat.Ontheother
hand, if you want to derive information such as monthly totals and average sales, such graphic storage would not be
useful. Instead, you could store the invoice data in a (structured) spreadsheet format so that you can perform the
requisitecomputations.Actually,mostdatayouencounterarebestclassifiedassemistructured.Semistructureddata
are data that have already been processed to some extent. For example, if you look at a typical Web page, the data
are presented to you in a prearranged format to convey some information.
The database types mentioned thus far focus on the storage and management of highly structured data. However,
corporations are not limited to the use of structured data. They also use semistructured and unstructured data. Just
thinkoftheveryvaluableinformationthatcanbefoundoncompanye-mails,memos,documentssuchasprocedures
and rules, Web pages, and so on. Unstructured and semistructured data storage and management needs are being
addressedthroughanewgenerationofdatabasesknownasXMLdatabases.ExtensibleMarkupLanguage(XML)
isaspeciallanguageusedtorepresentandmanipulatedataelementsinatextualformat.AnXMLdatabasesupports
the storage and management of semistructured XML data.
Table 1.1 compares the features of several well-known database management systems.
TABLE Types of Databases
1.1
NUMBEROFUSERS DATALOCATION DATAUSAGE XML
PRODUCT SINGLE MULTIUSER DATA
USER WORKGROUP ENTERPRISE CENTRALIZED DISTRIBUTED OPERATIONAL WAREHOUSE
MSAccess X X X X
MSSQL X3 X X X X X X X
Server
IBMDB2 X3 X X X X X X X
MySQL X X X X X X X X*
Oracle X3 X X X X X X X
RDBMS
*SupportsXMLfunctionsonly.XMLdataarestoredinlargetextobjects.
1.4 WHY DATABASE DESIGN IS IMPORTANT
Database design refers to the activities that focus on the design of the database structure that will be used to store
and manage end-user data. A database that meets all user requirements does not just happen; its structure must be
designed carefully. In fact, database design is such a crucial aspect of working with databases that most of this book
is dedicated to the development of good database design techniques. Even a good DBMS will perform poorly with a
badly designed database.
Proper database design requires the designer to identify precisely the database’s expected use. Designing a
transactional database emphasizes accurate and consistent data and operational speed. Designing a data warehouse
database emphasizes the use of historical and aggregated data. Designing a database to be used in a centralized,
3Vendorofferssingle-user/personalDBMSversion.

## Page 41

DATABASE SYSTEMS 11
single-userenvironmentrequiresadifferentapproachfromthatusedinthedesignofadistributed,multiuserdatabase.
This book emphasizes the design of transactional, centralized, single-user, and multiuser databases. Chapters 12 and
13 also examine critical issues confronting the designer of distributed and data warehouse databases.
Designingappropriatedatarepositoriesofintegratedinformationusingthetwo-dimensionaltablestructuresfoundin
mostdatabasesisaprocessofdecomposition.Theintegrateddatamustbedecomposedproperlyintoitsconstituent
parts, with each part stored in its own table. Further, the relationships between these tables must be carefully
consideredandimplementedsothattheintegratedviewofthedatacanbere-createdlaterasinformationfortheend
user.Awell-designeddatabasefacilitatesdatamanagementandgeneratesaccurateandvaluableinformation.Apoorly
designed database is likely to become a breeding ground for difficult-to-trace errors that may lead to bad decision
making—andbaddecisionmakingcanleadtothefailureofanorganization.Databasedesignissimplytooimportant
to be left to luck. That’s why college students study database design, why organizations of all types and sizes send
personnel to database design seminars, and why database design consultants often make an excellent living.
1.5 EVOLUTION OF FILE SYSTEM DATA PROCESSING
Understanding what a database is, what it does, and the proper way to use it can be clarified by considering what a
databaseisnot.Abriefexplanationoftheevolutionoffilesystemdataprocessingcanbehelpfulinunderstandingthe
data access limitations that databases attempt to overcome. Understanding these limitations is relevant to database
designersanddevelopersbecausedatabasetechnologiesdonotmaketheseproblemsmagicallydisappear—database
technologiessimplymakeiteasiertocreatesolutionsthatavoidtheseproblems.Creatingdatabasedesignsthatavoid
thepitfallsofearliersystemsrequiresthatthedesignerunderstandwhattheproblemsoftheearliersystemswereand
howtoavoidthem,orelsethedatabasetechnologiesarenobetter(potentiallyevenworse!)thanthetechnologiesand
techniques that they have replaced.
1.5.1 Manual File Systems
In order to be successful, an organization must come up with systems for handling core business tasks. Historically,
suchsystemswereoftenmanual,paper-and-pencilsystems.Thepaperswithinthesesystemswereorganizedinorder
to facilitate the expected use of the data. Typically, this was accomplished through a system of file folders and filing
cabinets. As long as a data collection was relatively small and an organization’s business users had few reporting
requirements, the manual system served its role well as a data repository. However, as organizations grew and as
reporting requirements became more complex, keeping track of data in a manual file system became more difficult.
Therefore, companies looked to computer technology for help.
1.5.2 Computerized File Systems
Generating reports from manual file systems was slow and cumbersome. In fact, some business managers faced
government-imposed reporting requirements that required weeks of intensive effort each quarter, even when a
well-designed manual system was used. Therefore, a data processing (DP) specialist was hired to create a
computer-based system that would track data and produce required reports.
Initially,thecomputerfileswithinthefilesystemweresimilartothemanualfiles.Asimpleexampleofacustomerdatafile
forasmallinsurancecompanyisshowninFigure1.3.(YouwilldiscoverlaterthatthefilestructureshowninFigure1.3,
although typically found in early file systems, is unsatisfactory for a database.)
Thedescriptionofcomputerfilesrequiresaspecializedvocabulary.Everydisciplinedevelopsitsownjargontoenable
its practitioners to communicate clearly. The basic file vocabulary shown in Table 1.2 will help you to understand
subsequent discussions more easily.

## Page 42

12 CHAPTER 1
FIGURE Contents of the CUSTOMER file
1.3
C_NAME = Customer name A_NAME = Agent name
C_PHONE = Customer phone A_PHONE = Agent phone
C_ADDRESS = Customer address TP = Insurance type
C_ZIP = Customer zip code AMT = Insurance policy amount, in thousands of $
REN = Insurance renewal date
O n l i n e C o n t e n t
ThedatabasesusedineachchapterareavailableinthePremiumWebsiteforthisbook.Throughoutthebook,
OnlineContentboxeshighlightmaterialrelatedtochaptercontentlocatedinthePremiumWebsite.
TABLE Basic File Terminology
1.2
TERM DEFINITION
Data “Raw”facts,suchasatelephonenumber,abirthdate,acustomername,andayear-to-date(YTD)
salesvalue.Datahavelittlemeaningunlesstheyhavebeenorganizedinsomelogicalmanner.
Field Acharacterorgroupofcharacters(alphabeticornumeric)thathasaspecificmeaning.Afieldis
usedtodefineandstoredata.
Record Alogicallyconnectedsetofoneormorefieldsthatdescribesaperson,place,orthing.Forexample,
thefieldsthatconstitutearecordforacustomermightconsistofthecustomer’sname,address,
phonenumber,dateofbirth,creditlimit,andunpaidbalance.
File Acollectionofrelatedrecords.Forexample,afilemightcontaindataaboutthestudentscurrently
enrolledatGiganticUniversity.
UsingtheproperfileterminologygiveninTable1.2,youcanidentifythefilecomponentsshowninFigure1.3.The
CUSTOMER file shown in Figure 1.3 contains 10 records. Each record is composed of nine fields: C_NAME,
C_PHONE,C_ADDRESS,C_ZlP,A_NAME,A_PHONE,TP,AMT,andREN.The10recordsarestoredinanamed
file. Because the file in Figure 1.3 contains customer data for the insurance company, its filename is CUSTOMER.
Whenbusinessuserswanteddatafromthecomputerizedfile,theysentrequestsforthedatatotheDPspecialist.Foreach
request,theDPspecialisthadtocreateprogramstoretrievethedatafromthefile,manipulateitinwhatevermannerthe
userhadrequested,andpresentitasaprintedreport.Ifarequestwasforareportthathadbeenpreviouslyrun,theDP
specialist could rerun the existing program and provide the printed results to the user. As other business users saw the
newandinnovativewaysthatthecustomerdatawerebeingreported,theywantedtobeabletoviewtheirdatainsimilar
fashions. This generated more requests for the DP specialist to create more computerized files of other business data,
which in turn meant that more data management programs had to be created, and more requests for reports. For
example, the sales department at the insurance company created a file named SALES, which helped track daily sales

## Page 43

DATABASE SYSTEMS 13
efforts.Thesalesdepartment’ssuccesswassoobviousthatthepersonneldepartmentmanagerdemandedaccesstothe
DPspecialisttoautomatepayrollprocessingandotherpersonnelfunctions.Consequently,theDPspecialistwasasked
tocreatetheAGENTfileshowninFigure1.4.ThedataintheAGENTfilewereusedtowritechecks,keeptrackoftaxes
paid, and summarize insurance coverage, among other tasks.
FIGURE Contents of the AGENT file
1.4
A_NAME = Agent name YTD_PAY = Year-to-date pay
A_PHONE = Agent phone YTD_FIT = Year-to-date federal income tax paid
A_ADDRESS = Agent address YTD_FICA = Year-to-date Social Security taxes paid
ZIP = Agent zip code YTD_SLS = Year-to-date sales
HIRED = Agent date of hire DEP = Number of dependents
As more and more computerized files were developed, the problems with this type of file system became apparent.
While these problems are explored in detail in the next section, briefly, the problems centered on having lots of data
files that contained related, often overlapping, data with no means of controlling or managing the data consistently
across all of the files. As shown in Figure 1.5, each file in the system used its own application program to store,
retrieve,andmodifydata.Andeachfilewasownedbytheindividualorthedepartmentthatcommissioneditscreation.
FIGURE A simple file system
1.5
Sales department Personnel department
SALES
file
File File File File
Management Report Management Report
Programs Programs Programs Programs
CUSTOMER AGENT
file file
The advent of computer files to store company data was significant; it not only established a landmark in the use of
computertechnologiesbutalsorepresentedahugestepforwardinabusiness’sabilitytoprocessdata.Previously,users
had direct, hands-on access to all of the business data. But they didn’t have the tools to convert those data into the
information that they needed. The creation of computerized file systems gave them improved tools for manipulating
the company data that allowed them to create new information. However, it had the additional effect of introducing

## Page 44

14 CHAPTER 1
a schism between the end users and their data. The desire to close the gap between the end users and the data
influenced the development of all types of computer technologies, system designs, and uses (and misuse) of many
technologies and techniques. However, such developments also created a split between the ways DP specialists and
end users viewed the data.
(cid:2) FromtheDPspecialist’sperspective,thecomputerfileswithinthefilesystemwerecreatedtobesimilartothe
manual files. Data management programs were created to add to, update, and delete data from the file.
(cid:2) From the end user’s perspective, the systems separated the users from the data. As the users’ competitive
environment pushed them to make more and more decisions in less and less time, the delay from when the
usersconceivedofanewwaytocreateinformationfromthedatatowhentheDPspecialistcouldcreatethe
programs to generate that information was a source of great frustration.
1.5.3 File System Redux: Modern End-User Productivity Tools
Theusers’desirefordirect,hands-onaccesstothedatahelpedtofueltheadoptionofpersonalcomputersforbusiness
use. Although not directly related to file system evolution, the ubiquitous use of personal productivity tools can
introduce the same problems as the old file systems.
PersonalcomputerspreadsheetprogramssuchasMicrosoftExcelarewidelyusedbybusinessusers,andallowtheuser
toenterdatainaseriesofrowsandcolumnssothatthedatacanbemanipulatedusingawiderangeoffunctions.The
popularity of spreadsheet applications has enabled users to conduct sophisticated analysis of data that has greatly
enhancedtheirabilitytounderstandthedataandmakebetterdecisions.Unfortunately,asintheoldadage“Whenthe
only tool you have is a hammer, every problem looks like a nail,” users have become so adept at working with
spreadsheets, they tend to use them to complete tasks for which spreadsheets are not appropriate.
One of the common misuses of spreadsheets is as a substitute for a database. Interestingly, end users often take the
limiteddatatowhichtheyhavedirectaccessandplaceitinaspreadsheetinaformatsimilartothatofthetraditional,
manual data storage systems—which is precisely what the early DP specialists did when creating computerized data
files.Duetothelargenumberofuserswithspreadsheets,eachmakingseparatecopiesofthedata,theresulting“file
system”ofspreadsheetssuffersfromthesameproblemsasthefilesystemscreatedbytheearlyDPspecialists,which
are outlined in the next section.
1.6 PROBLEMS WITH FILE SYSTEM DATA PROCESSING
Thefilesystemmethodoforganizingandmanagingdatawasadefiniteimprovementoverthemanualsystem,andthe
filesystemservedausefulpurposeindatamanagementforovertwodecades—averylongtimeinthecomputerera.
Nonetheless, many problems and limitations became evident in this approach. A critique of the file system method
serves two major purposes:
(cid:2) Understanding the shortcomings of the file system enables you to understand the development of modern
databases.
(cid:2) Many of the problems are not unique to file systems. Failure to understand such problems is likely to lead to
their duplication in a database environment, even though database technology makes it easy to avoid them.
The following problems associated with file systems, whether created by DP specialists or through a series of
spreadsheets,severelychallengethetypesofinformationthatcanbecreatedfromthedataaswellastheaccuracyof
the information:
(cid:2) Lengthy development times. The first and most glaring problem with the file system approach is that even
thesimplestdata-retrievaltaskrequiresextensiveprogramming.Withtheolderfilesystems,programmershad
to specify what must be done and how it was to be done. As you will learn in upcoming chapters, modern
databasesuseanonproceduraldatamanipulationlanguagethatallowstheusertospecifywhatmustbedone
without specifying how it must be done.

## Page 45

DATABASE SYSTEMS 15
(cid:2) Difficultyofgettingquickanswers.The need to write programs to produce even the simplest reports makes
ad hoc queries impossible. Harried DP specialists who work with mature file systems often receive numerous
requestsfornewreports.Theyareoftenforcedtosaythatthereportwillbeready“nextweek”oreven“next
month.”Ifyouneedtheinformationnow,gettingitnextweekornextmonthwillnotserveyourinformation
needs.
(cid:2) Complexsystemadministration.Systemadministrationbecomesmoredifficultasthenumberoffilesinthe
system expands. Even a simple file system with a few files requires creating and maintaining several file
management programs (each file must have its own file management programs that allow the user to add,
modify, and delete records; to list the file contents; and to generate reports). Because ad hoc queries are not
possible, the file reporting programs can multiply quickly. The problem is compounded by the fact that each
department in the organization “owns” its data by creating its own files.
(cid:2) Lackofsecurityandlimiteddatasharing. Anotherfaultofafilesystemdatarepositoryisalackofsecurity
and limited data sharing. Data sharing and security are closely related. Sharing data among multiple
geographically dispersed users introduces a lot of security risks. In terms of spreadsheet data, while many
spreadsheetprogramsproviderudimentarysecurityoptions,theyarenotalwaysused,andevenwhentheyare
used, they are insufficient for robust data sharing among users. In terms of the creation of data management
and reporting programs, security and data-sharing features are difficult to program and are, therefore, often
omittedinafilesystemenvironment.Suchfeaturesincludeeffectivepasswordprotection,theabilitytolockout
partsoffilesorpartsofthesystemitself,andothermeasuresdesignedtosafeguarddataconfidentiality.Even
whenanattemptismadetoimprovesystemanddatasecurity,thesecuritydevicestendtobelimitedinscope
and effectiveness.
(cid:2) Extensiveprogramming.Making changes to an existing file structure can be difficult in a file system environ-
ment. For example, changing just one field in the original CUSTOMER file would require a program that:
1. Reads a record from the original file.
2. Transforms the original data to conform to the new structure’s storage requirements.
3. Writes the transformed data into the new file structure.
4. Repeats steps 2 to 4 for each record in the original file.
In fact, any change to a file structure, no matter how minor, forces modifications in all of the programs that use the
datainthatfile.Modificationsarelikelytoproduceerrors(bugs),andadditionaltimeisspentusingadebuggingprocess
to find those errors. Those limitations, in turn, lead to problems of structural and data dependence.
1.6.1 Structural and Data Dependence
A file system exhibits structural dependence, which means that access to a file is dependent on its structure. For
example,addingacustomerdate-of-birthfieldtotheCUSTOMERfileshowninFigure1.3wouldrequirethefoursteps
described in the previous section. Given this change, none of the previous programs will work with the new
CUSTOMER file structure. Therefore, all of the file system programs must be modified to conform to the new file
structure.Inshort,becausethefilesystemapplicationprogramsareaffectedbychangeinthefilestructure,theyexhibit
structural dependence. Conversely, structural independence exists when it is possible to make changes in the file
structure without affecting the application program’s ability to access the data.
Evenchangesinthecharacteristicsofdata,suchaschangingafieldfromintegertodecimal,requirechangesinallthe
programs that access the file. Because all data access programs are subject to change when any of the file’s data
storage characteristics change (that is, changing the data type), the file system is said to exhibit data dependence.
Conversely,dataindependenceexistswhenitispossibletomakechangesinthedatastoragecharacteristicswithout
affecting the application program’s ability to access the data.
The practical significance of data dependence is the difference between the logical data format (how the human
beingviewsthedata)andthephysicaldataformat(howthecomputermustworkwiththedata).Anyprogramthat
accesses a file system’s file must tell the computer not only what to do but also how to do it. Consequently, each

## Page 46

16 CHAPTER 1
program must contain lines that specify the opening of a specific file type, its record specification, and its field
definitions. Data dependence makes the file system extremely cumbersome from the point of view of a programmer
and database manager.
1.6.2 Data Redundancy
Thefilesystem’sstructuremakesitdifficulttocombinedatafrommultiplesources,anditslackofsecurityrendersthe
file system vulnerable to security breaches. The organizational structure promotes the storage of the same basic data
indifferentlocations.(Databaseprofessionalsusethetermislandsofinformationforsuchscattereddatalocations.)
The dispersion of data is exacerbated by the use of spreadsheets to store data. In a file system, the entire sales
departmentwouldshareaccesstotheSALESdatafilethroughthedatamanagementandreportingprogramscreated
by the DP specialist. With the use of spreadsheets, it is possible for each member of the sales department to create
hisorherowncopyofthesalesdata.Becauseitisunlikelythatdatastoredindifferentlocationswillalwaysbeupdated
consistently,theislandsofinformationoftencontaindifferentversionsofthesamedata.Forexample,inFigures1.3
and 1.4, the agent names and phone numbers occur in both the CUSTOMER and the AGENT files. You only need
onecorrectcopyoftheagentnamesandphonenumbers.Havingthemoccurinmorethanoneplaceproducesdata
redundancy. Data redundancy exists when the same data are stored unnecessarily at different places.
Uncontrolled data redundancy sets the stage for:
(cid:2) Poor data security. Having multiple copies of data increases the chances for a copy of the data to be
susceptibletounauthorizedaccess.Chapter15,DatabaseAdministrationandSecurity,explorestheissuesand
techniques associated with securing data.
(cid:2) Datainconsistency.Datainconsistencyexistswhendifferentandconflictingversionsofthesamedataappear
indifferentplaces.Forexample,supposeyouchangeanagent’sphonenumberoraddressintheAGENTfile.
If you forget to make corresponding changes in the CUSTOMER file, the files contain different data for the
same agent. Reports will yield inconsistent results that depend on which version of the data is used.
Note
Datathatdisplaydatainconsistencyarealsoreferredtoasdatathatlackdataintegrity.Dataintegrityisdefined
astheconditioninwhichallofthedatainthedatabaseareconsistentwiththereal-worldeventsandconditions.
Inotherwords,dataintegritymeansthat:
• Dataareaccurate—therearenodatainconsistencies.
• Dataareverifiable—thedatawillalwaysyieldconsistentresults.
Data entry errors are more likely to occur when complex entries (such as 10-digit phone numbers) are made
in several different files and/or recur frequently in one or more files. In fact, the CUSTOMER file shown in
Figure1.3containsjustsuchanentryerror:thethirdrecordintheCUSTOMERfilehasatransposeddigitin
the agent’s phone number (615-882-2144 rather than 615-882-1244).
It is possible to enter a nonexistent sales agent’s name and phone number into the CUSTOMER file, but
customers are not likely to be impressed if the insurance agency supplies the name and phone number of an
agent who does not exist. Should the personnel manager allow a nonexistent agent to accrue bonuses and
benefits? In fact, a data entry error such as an incorrectly spelled name or an incorrect phone number yields
the same kind of data integrity problems.
(cid:2) Dataanomalies.Thedictionarydefinesanomalyas“anabnormality.”Ideally,afieldvaluechangeshouldbe
made in only a single place. Data redundancy, however, fosters an abnormal condition by forcing field value
changesinmanydifferentlocations.LookattheCUSTOMERfileinFigure1.3.IfagentLeahF.Hahndecides
togetmarriedandmove,theagentname,address,andphonenumberarelikelytochange.Insteadofmaking
justasinglenameand/orphone/addresschangeinasinglefile(AGENT),youmustalsomakethechangeeach
time that agent’s name, phone number, and address occur in the CUSTOMER file. You could be faced with

## Page 47

DATABASE SYSTEMS 17
theprospectofmakinghundredsofcorrections,oneforeachofthecustomersservedbythatagent!Thesame
problem occurs when an agent decides to quit. Each customer served by that agent must be assigned a new
agent.Anychangeinanyfieldvaluemustbecorrectlymadeinmanyplacestomaintaindataintegrity.Adata
anomalydevelopswhennotalloftherequiredchangesintheredundantdataaremadesuccessfully.Thedata
anomalies found in Figure 1.3 are commonly defined as follows:
- Updateanomalies.IfagentLeahF.Hahnhasanewphonenumber,thatnumbermustbeenteredineach
of the CUSTOMER file records in which Ms. Hahn’s phone number is shown. In this case, only three
changes must be made. In a large file system, such a change might occur in hundreds or even thousands
of records. Clearly, the potential for data inconsistencies is great.
- Insertionanomalies.IfonlytheCUSTOMERfileexisted,toaddanewagent,youwouldalsoaddadummy
customerdataentrytoreflectthenewagent’saddition.Again,thepotentialforcreatingdatainconsistencies
would be great.
- Deletionanomalies.IfyoudeletethecustomersAmyB.O’Brian,GeorgeWilliams,andOletteK.Smith,
you will also delete John T. Okon’s agent data. Clearly, this is not desirable.
1.6.3 LACK OF DESIGN AND DATA-MODELING SKILLS
Anewproblemthathasevolvedwiththeuseofpersonalproductivitytools(suchasspreadsheetanddesktopdatabases)
is that users typically lack the knowledge of proper design and data-modeling skills.People naturally have an integrated
viewofthedataintheirenvironment.Forexample,considerastudent’sclassschedule.Thescheduleprobablycontains
thestudent’sidentificationnumberandname,classcode,classdescription,classcredithours,thenameoftheinstructor
teachingtheclass,theclassmeetingdaysandtimes,andtheclassroomnumber.Inthemindofthestudent,thesevarious
data items compose a single unit. If a student organization wanted to keep a record of the schedules of all of the
organizationmembers,anendusermightmakeaspreadsheettostorethescheduleinformation.Evenifthestudentmakes
aforayintotherealmofdesktopdatabases,heorsheislikelytocreateastructurecomposedofasingletablethatmimics
the structure of the schedule.As you will learn in the coming chapters, forcing this type of integrated data into a single
two-dimensional table structure is a poor data design that leads to a large degree of redundancy for several data items.
Data-modelingskillsarealsoavitalpartofthedesignprocess.Itisimportantthatthedesignthatiscreatedbeproperly
documented. Design documentation is necessary to facilitate communication among the database designer, the end
user,andthedeveloper.Datamodeling,asintroducedlaterinthistext,isthemostcommonmethodofdocumenting
databasedesigns.Usingastandardizeddata-modelingtechniqueensuresthatthedatamodelfulfillsitsroleinfacilitating
communication among the designer, user, and developer. The data model also provides an invaluable resource when
maintainingormodifyingadatabaseasbusinessrequirementschange.Thedatadesignscreatedbyendusersarerarely
documentedandneverwithanappropriatestandardizeddata-modelingtechnique.Onapositivenote,however,ifyou
arereadingthisbook,thenyouareengagedinthetypeoftrainingthatisnecessarytodeveloptheskillsindatabase
designanddatamodelingthatittakestosuccessfullydesignadatabasethatensuresconsistencyofthedata,enforces
integrity, and provides a stable and flexible platform for providing users with timely, accurate information.
1.7 DATABASE SYSTEMS
The problems inherent in file systems make using a database system very desirable. Unlike the file system, with its
manyseparateandunrelatedfiles,thedatabasesystemconsistsoflogicallyrelateddatastoredinasinglelogicaldata
repository.(The“logical”labelreflectsthefactthat,althoughthedatarepositoryappearstobeasingleunittotheend
user,itscontentsmayactuallybephysicallydistributedamongmultipledatastoragefacilitiesand/orlocations.)Because
thedatabase’sdatarepositoryisasinglelogicalunit,thedatabaserepresentsamajorchangeinthewayend-userdata
arestored,accessed,andmanaged.Thedatabase’sDBMS,showninFigure1.6,providesnumerousadvantagesover
file system management, shown in Figure 1.5, by making it possible to eliminate most of the file system’s data
inconsistency,dataanomaly,datadependence,andstructuraldependenceproblems.Betteryet,thecurrentgeneration

## Page 48

18 CHAPTER 1
of DBMS software stores not only the data structures, but also the relationships between those structures and the
access paths to those structures—all in a central location. The current generation of DBMS software also takes care
of defining, storing, and managing all required access paths to those components.
FIGURE Contrasting database and file systems
1.6
A Database System
Personnel dept.
Database
Employees
DBMS Customers
Sales dept.
Sales
Inventory
Accounts
Accounting dept.
A File System
Personnel dept. Sales dept. Accounting dept.
Employees Customers Sales Accounts
Remember that the DBMS is just one of several crucial components of a database system. The DBMS may even be
referredtoasthedatabasesystem’sheart.However,justasittakesmorethanahearttomakeahumanbeingfunction,
ittakesmorethanaDBMStomakeadatabasesystemfunction.Inthesectionsthatfollow,you’lllearnwhatadatabase
system is, what its components are, and how the DBMS fits into the database system picture.
1.7.1 The Database System Environment
Thetermdatabasesystemreferstoanorganizationofcomponentsthatdefineandregulatethecollection,storage,
management,anduseofdatawithinadatabaseenvironment.Fromageneralmanagementpointofview,thedatabase
system is composed of the five major parts shown in Figure 1.7: hardware, software, people, procedures, and data.
Let’s take a closer look at the five components shown in Figure 1.7:
(cid:2) Hardware.Hardwarereferstoallofthesystem’sphysicaldevices;forexample,computers(PCs,workstations,
servers,andsupercomputers),storagedevices,printers,networkdevices(hubs,switches,routers,fiberoptics),
and other devices (automated teller machines, ID readers, and so on).

## Page 49

DATABASE SYSTEMS 19
FIGURE The database system environment
1.7
writes
Procedures
and
and standards supervises
enforces
Database System
Database administrator administrator
Analysts
designer manages
designs
Hardware
End users Programmers
Application
DBMS utilities
use programs write
DBMS
access
Data
(cid:2) Software. Although the most readily identified software is the DBMS itself, to make the database system
functionfully,threetypesofsoftwareareneeded:operatingsystemsoftware,DBMSsoftware,andapplication
programs and utilities.
- Operatingsystemsoftwaremanagesallhardwarecomponentsandmakesitpossibleforallothersoftware
to run on the computers. Examples of operating system software include Microsoft Windows, Linux, Mac
OS, UNIX, and MVS.
- DBMS software manages the database within the database system. Some examples of DBMS software
include Microsoft’s SQL Server, Oracle Corporation’s Oracle, Sun’s MySQL, and IBM’s DB2.
- Application programs and utility software are used to access and manipulate data in the DBMS and to
manage the computer environment in which data access and manipulation take place. Application
programs are most commonly used to access data found within the database to generate reports,
tabulations,andotherinformationtofacilitatedecisionmaking.Utilitiesarethesoftwaretoolsusedtohelp
manage the database system’s computer components. For example, all of the major DBMS vendors now
provide graphical user interfaces (GUIs) to help create database structures, control database access, and
monitor database operations.
(cid:2) People.Thiscomponentincludesallusersofthedatabasesystem.Onthebasisofprimaryjobfunctions,five
typesofuserscanbeidentifiedinadatabasesystem:systemadministrators,databaseadministrators,database
designers,systemanalystsandprogrammers,andendusers.Eachusertype,describedbelow,performsboth
unique and complementary functions.
- System administrators oversee the database system’s general operations.
- Database administrators, also known as DBAs, manage the DBMS and ensure that the database is
functioningproperly.TheDBA’sroleissufficientlyimportanttowarrantadetailedexplorationinChapter
15, Database Administration and Security.
- Database designers design the database structure. They are, in effect, the database architects. If the
database design is poor, even the best application programmers and the most dedicated DBAs cannot
produce a useful database environment. Because organizations strive to optimize their data resources, the
database designer’s job description has expanded to cover new dimensions and growing responsibilities.

## Page 50

20 CHAPTER 1
- System analysts and programmers design and implement the application programs. They design and
createthedataentryscreens,reports,andproceduresthroughwhichendusersaccessandmanipulatethe
database’s data.
- Endusersarethepeoplewhousetheapplicationprogramstoruntheorganization’sdailyoperations.For
example, salesclerks, supervisors, managers, and directors are all classified as end users. High-level end
usersemploytheinformationobtainedfromthedatabasetomaketacticalandstrategicbusinessdecisions.
(cid:2) Procedures.Proceduresaretheinstructionsandrulesthatgovernthedesignanduseofthedatabasesystem.
Procedures are a critical, although occasionally forgotten, component of the system. Procedures play an
important role in a company because they enforce the standards by which business is conducted within the
organizationandwithcustomers.Proceduresarealsousedtoensurethatthereisanorganizedwaytomonitor
and audit both the data that enter the database and the information that is generated through the use of
those data.
(cid:2) Data. The word data covers the collection of facts stored in the database. Because data are the raw material
fromwhichinformationisgenerated,thedeterminationofwhatdataaretobeenteredintothedatabaseand
how those data are to be organized is a vital part of the database designer’s job.
A database system adds a new dimension to an organization’s management structure. Just how complex this
managerialstructureisdependsontheorganization’ssize,itsfunctions,anditscorporateculture.Therefore,database
systemscanbecreatedandmanagedatdifferentlevelsofcomplexityandwithvaryingadherencetoprecisestandards.
Forexample,comparealocalmovierentalsystemwithanationalinsuranceclaimssystem.Themovierentalsystem
maybemanagedbytwopeople,thehardwareusedisprobablyasinglePC,theproceduresareprobablysimple,and
the data volume tends to be low. The national insurance claims system is likely to have at least one systems
administrator, several full-time DBAs, and many designers and programmers; the hardware probably includes several
servers at multiple locations throughout the United States; the procedures are likely to be numerous, complex, and
rigorous; and the data volume tends to be high.
Inadditiontothedifferentlevelsofdatabasesystemcomplexity,managersmustalsotakeanotherimportantfactinto
account: database solutions must be cost-effective as well as tactically and strategically effective. Producing a
million-dollarsolutiontoathousand-dollarproblemishardlyanexampleofgooddatabasesystemselectionorofgood
databasedesignandmanagement.Finally,thedatabasetechnologyalreadyinuseislikelytoaffecttheselectionofa
database system.
1.7.2 DBMS Functions
ADBMSperformsseveralimportantfunctionsthatguaranteetheintegrityandconsistencyofthedatainthedatabase.
Mostofthosefunctionsaretransparenttoendusers,andmostcanbeachievedonlythroughtheuseofaDBMS.They
include data dictionary management, data storage management, data transformation and presentation, security
management, multiuser access control, backup and recovery management, data integrity management, database
access languages and application programming interfaces, and database communication interfaces. Each of these
functions is explained below.
(cid:2) Data dictionary management. The DBMS stores definitions of the data elements and their relationships
(metadata)inadatadictionary.Inturn,allprogramsthataccessthedatainthedatabaseworkthroughthe
DBMS. The DBMS uses the data dictionary to look up the required data component structures and
relationships,thusrelievingyoufromhavingtocodesuchcomplexrelationshipsineachprogram.Additionally,
anychangesmadeinadatabasestructureareautomaticallyrecordedinthedatadictionary,therebyfreeingyou
from having to modify all of the programs that access the changed structure. In other words, the DBMS
provides data abstraction, and it removes structural and data dependence from the system. For example,
Figure 1.8 shows how Microsoft SQL Server Express presents the data definition for the CUSTOMER table.
(cid:2) Datastoragemanagement.TheDBMScreatesandmanagesthecomplexstructuresrequiredfordatastorage,
thus relieving you from the difficult task of defining and programming the physical data characteristics. A

## Page 51

DATABASE SYSTEMS 21
FIGURE Illustrating metadata with Microsoft SQL Server Express
1.8
Metadata
modern DBMS provides storage not only for the data, but also for related data entry forms or screen
definitions, report definitions, data validation rules, procedural code, structures to handle video and picture
formats, and so on. Data storage management is also important for database performance tuning.
Performance tuning relates to the activities that make the database perform more efficiently in terms of
storageandaccessspeed.Althoughtheuserseesthedatabaseasasingledatastorageunit,theDBMSactually
stores the database in multiple physical data files. (See Figure 1.9.) Such data files may even be stored on
different storage media. Therefore, the DBMS doesn’t have to wait for one disk request to finish before the
nextonestarts.Inotherwords,theDBMScanfulfilldatabaserequestsconcurrently.Datastoragemanagement
and performance tuning issues are addressed in Chapter 11, Database Performance Tuning and Query
Optimization.
(cid:2) Data transformation and presentation. The DBMS transforms entered data to conform to required data
structures. The DBMS relieves you of the chore of making a distinction between the logical data format and
the physical data format. That is, the DBMS formats the physically retrieved data to make it conform to the
user’slogicalexpectations.Forexample,imagineanenterprisedatabaseusedbyamultinationalcompany.An
end user in England would expect to enter data such as July 11, 2010, as “11/07/2010.” In contrast, the
same date would be entered in the United States as “07/11/2010.” Regardless of the data presentation
format, the DBMS must manage the date in the proper format for each country.
(cid:2) Security management. The DBMS creates a security system that enforces user security and data privacy.
Security rules determine which users can access the database, which data items each user can access, and
which data operations (read, add, delete, or modify) the user can perform. This is especially important in

## Page 52

22 CHAPTER 1
FIGURE Illustrating data storage management with Oracle
1.9
Database Name: ORALAB.MTSU.EDU
The ORALAB database is The Oracle DBA Studio
actually stored in nine Management interface also
datafiles located on the C: shows the amount of space
drive of the database server used by each of the datafiles
computer. that constitute the single
logical database.
The Oracle DBA Studio Administrator GUI shows the data storage
management characteristics for the ORALAB database.
multiuser database systems. Chapter 15, Database Administration and Security, examines data security and
privacyissuesingreaterdetail.AlldatabaseusersmaybeauthenticatedtotheDBMSthroughausernameand
passwordorthroughbiometricauthenticationsuchasafingerprintscan.TheDBMSusesthisinformationto
assign access privileges to various database components such as queries and reports.
(cid:2) Multiuser access control. To provide data integrity and data consistency, the DBMS uses sophisticated
algorithms to ensure that multiple users can access the database concurrently without compromising the
integrity of the database. Chapter 10, Transaction Management and Concurrency Control, covers the details
of the multiuser access control.
(cid:2) Backupandrecoverymanagement.TheDBMSprovidesbackupanddatarecoverytoensuredatasafetyand
integrity. Current DBMS systems provide special utilities that allow the DBA to perform routine and special
backupandrestoreprocedures.Recoverymanagementdealswiththerecoveryofthedatabaseafterafailure,
such as a bad sector in the disk or a power failure. Such capability is critical to preserving the database’s
integrity. Chapter 15 covers backup and recovery issues.
(cid:2) Data integrity management. The DBMS promotes and enforces integrity rules, thus minimizing data
redundancyandmaximizingdataconsistency.Thedatarelationshipsstoredinthedatadictionaryareusedto
enforcedataintegrity.Ensuringdataintegrityisespeciallyimportantintransaction-orienteddatabasesystems.
Data integrity and transaction management issues are addressed in Chapter 7, Introduction to Structured
Query Language (SQL), and Chapter 10.
(cid:2) Databaseaccesslanguagesandapplicationprogramminginterfaces.TheDBMSprovidesdataaccessthrough
aquerylanguage.Aquerylanguageisanonprocedurallanguage—onethatletstheuserspecifywhatmust
bedonewithouthavingtospecifyhowitistobedone.StructuredQueryLanguage(SQL)isthedefacto

## Page 53

DATABASE SYSTEMS 23
querylanguageanddataaccessstandardsupportedbythemajorityofDBMSvendors.Chapter7,Introduction
toStructuredQueryLanguage(SQL),andChapter8,AdvancedSQL,addresstheuseofSQL.TheDBMSalso
provides application programming interfaces to procedural languages such as COBOL, C, Java, Visual
Basic.NET,andC#.Inaddition,theDBMSprovidesadministrativeutilitiesusedbytheDBAandthedatabase
designer to create, implement, monitor, and maintain the database.
(cid:2) Database communication interfaces. Current-generation DBMSs accept end-user requests via multiple,
differentnetworkenvironments.Forexample,theDBMSmightprovideaccesstothedatabaseviatheInternet
through the use of Web browsers such as Mozilla Firefox or Microsoft Internet Explorer. In this environment,
communications can be accomplished in several ways:
- EnduserscangenerateanswerstoqueriesbyfillinginscreenformsthroughtheirpreferredWebbrowser.
- The DBMS can automatically publish predefined reports on a Website.
- The DBMS can connect to third-party systems to distribute information via e-mail or other productivity
applications.
DatabasecommunicationinterfacesareexaminedingreaterdetailinChapter12,DistributedDatabaseManagement
Systems, in Chapter 14, Database Connectivity and Web Technologies, and in Appendix I, Databases in Electronic
Commerce. (Appendixes are found in the Premium Website.)
NOTE
WhyaSpreadsheetIsNotaDatabase
Whileaspreadsheetallowsforthecreationofmultipletables,itdoesnotsupporteventhemostbasicdatabase
functionalitysuchassupportforself-documentationthroughmetadata,enforcementofdatatypesordomains
to ensure consistency of data within a column, defined relationships among tables, or constraints to ensure
consistencyofdataacrossrelatedtables.Mostuserslackthenecessarytrainingtorecognizethelimitationsof
spreadsheetsforthesetypesoftasks.
1.7.3 Managing the Database System: A Shift in Focus
The introduction of a database system over the file system provides a framework in which strict procedures and
standards can be enforced. Consequently, the role of the human component changes from an emphasis on
programming(inthefilesystem)toafocusonthebroaderaspectsofmanagingtheorganization’sdataresourcesand
on the administration of the complex database software itself.
Thedatabasesystemmakesitpossibletotacklefarmoresophisticatedusesofthedataresources,aslongasthedatabase
isdesignedtomakeuseofthatavailablepower.Thekindsofdatastructurescreatedwithinthedatabaseandtheextent
of the relationships among them play a powerful role in determining the effectiveness of the database system.
Although the database system yields considerable advantages over previous data management approaches, database
systems do carry significant disadvantages. For example:
(cid:2) Increased costs. Database systems require sophisticated hardware and software and highly skilled personnel.
The cost of maintaining the hardware, software, and personnel required to operate and manage a database
system can be substantial. Training, licensing, and regulation compliance costs are often overlooked when
database systems are implemented.
(cid:2) Managementcomplexity.Databasesystemsinterfacewithmanydifferenttechnologiesandhaveasignificant
impact on a company’s resources and culture. The changes introduced by the adoption of a database system
must be properly managed to ensure that they help advance the company’s objectives. Given the fact that
database systems hold crucial company data that are accessed from multiple sources, security issues must be
assessed constantly.

## Page 54

24 CHAPTER 1
(cid:2) Maintainingcurrency.Tomaximizetheefficiencyofthedatabasesystem,youmustkeepyoursystemcurrent.
Therefore, you must perform frequent updates and apply the latest patches and security measures to all
components. Because database technology advances rapidly, personnel training costs tend to be significant.
(cid:2) Vendor dependence. Given the heavy investment in technology and personnel training, companies might be
reluctant to change database vendors. As a consequence, vendors are less likely to offer pricing point
advantages to existing customers, and those customers might be limited in their choice of database system
components.
(cid:2) Frequent upgrade/replacement cycles. DBMS vendors frequently upgrade their products by adding new
functionality.Suchnewfeaturesoftencomebundledinnewupgradeversionsofthesoftware.Someofthese
versionsrequirehardwareupgrades.Notonlydotheupgradesthemselvescostmoney,butitalsocostsmoney
to train database users and administrators to properly use and manage the new features.
Now that we have considered what a database and DBMS are, and why they are necessary, it is natural for our
thoughts to turn to developing the skills of database design. However, before we can create a design, we must know
what tools are at our disposal. Throughout this chapter, we have generalized the discussion of database technology
suchthatitappearsthatthereisasingle,commonapproachtodatabasedesign.Asadatabasedesigneranddeveloper,
however, you need to understand that there are different approaches, and you need to know how these approaches
influence the designs that you can create and how those designs are modeled.

## Page 55

DATABASE SYSTEMS 25
S u m m a r y
◗
Dataarerawfacts.Informationistheresultofprocessingdatatorevealitsmeaning.Accurate,relevant,andtimely
informationisthekeytogooddecisionmaking,andgooddecisionmakingisthekeytoorganizationalsurvivalin
a global environment.
◗
Data are usually stored in a database. To implement a database and to manage its contents, you need a database
management system (DBMS). The DBMS serves as the intermediary between the user and the database. The
database contains the data you have collected and “data about data,” known as metadata.
◗
Database design defines the database structure. A well-designed database facilitates data management and
generatesaccurateandvaluableinformation.Apoorlydesigneddatabasecanleadtobaddecisionmaking,andbad
decision making can lead to the failure of an organization.
◗
Databasesevolvedfrommanualandthencomputerizedfilesystems.Inafilesystem,dataarestoredinindependent
files, each requiring its own data management programs. Although this method of data management is largely
outmoded, understanding its characteristics makes database design easier to comprehend.
◗
Somelimitationsoffilesystemdatamanagementarethatitrequiresextensiveprogramming,systemadministration
canbecomplexanddifficult,makingchangestoexistingstructuresisdifficult,andsecurityfeaturesarelikelytobe
inadequate. Also, independent files tend to contain redundant data, leading to problems of structural and data
dependence.
◗
Database management systems were developed to address the file system’s inherent weaknesses. Rather than
depositingdatainindependentfiles,aDBMSpresentsthedatabasetotheenduserasasingledatarepository.This
arrangementpromotesdatasharing,thuseliminatingthepotentialproblemofislandsofinformation.Inaddition,
the DBMS enforces data integrity, eliminates redundancy, and promotes data security.
K e y T e r ms
ad hoc query, 8 database system, 18 query, 8
centralized database, 9 desktop database, 9 query language, 22
data, 5 distributed database, 9 query result set, 8
data anomaly, 17 enterprise database, 9 record, 12
data dependence, 15 Extensible Markup semistructured data, 10
data dictionary, 20 Language (XML), 10 single-user database, 9
data inconsistency, 8 field, 12 structural dependence, 15
data independence, 15 file, 12 structural independence, 15
data integrity, 16 information, 5 structured data, 9
data management, 7 islands of information, 16 Structured Query
data processing (DP) specialist, 11 knowledge, 7 Language (SQL), 22
data quality, 9 logical data format, 15 transactional database, 9
data redundancy, 16 metadata, 7 unstructured data, 9
data warehouse, 9 multiuser database, 9 workgroup database, 9
database, 7 operational database, 9 XML database, 10
database design, 10 performance tuning, 21
database management physical data format, 15
system (DBMS), 7 production database, 9

## Page 56

26 CHAPTER 1
O n l i n e C o n t e n t
AnswerstoselectedReviewQuestionsandProblemsforthischapterarecontainedinthePremiumWebsitefor
thisbook.
R e v ie w Q u e st i o ns
1. Define each of the following terms:
a. data
b. field
c. record
d. file
2. What is data redundancy, and which characteristics of the file system can lead to it?
3. What is data independence, and why is it lacking in file systems?
4. What is a DBMS, and what are its functions?
5. What is structural independence, and why is it important?
6. Explain the difference between data and information.
7. What is the role of a DBMS, and what are its advantages? What are its disadvantages?
8. List and describe the different types of databases.
9. What are the main components of a database system?
10. What are metadata?
11. Explain why database design is important.
12. What are the potential costs of implementing a database system?
13. Use examples to compare and contrast unstructured and structured data. Which type is more prevalent in a
typical business environment?
14. What are some basic database functions that a spreadsheet cannot perform?
15. Whatcommonproblemsdoesacollectionofspreadsheetscreatedbyenduserssharewiththetypicalfilesystem?
16. Explain the significance of the loss of direct, hands-on access to business data that end users experienced with
the advent of computerized data repositories.
P r o b le m s
O n l i n e C o n t e n t
ThefilestructuresyouseeinthisproblemsetaresimulatedinaMicrosoftAccessdatabasenamed
Ch01_Problems,availableinthePremiumWebsiteforthisbook.

## Page 57

DATABASE SYSTEMS 27
FIGURE The file structure for Problems 1–4
P1.1
Given the file structure shown in Figure P1.1, answer Problems 1−4.
1. How many records does the file contain? How many fields are there per record?
2. Whatproblemwouldyouencounterifyouwantedtoproducealistingbycity?Howwouldyousolvethisproblem
by altering the file structure?
3. Ifyouwantedtoproducealistingofthefilecontentsbylastname,areacode,city,state,orzipcode,howwould
you alter the file structure?
4. What data redundancies do you detect? How could those redundancies lead to anomalies?
FIGURE The file structure for Problems 5–8
P1.5
5. Identify and discuss the serious data redundancy problems exhibited by the file structure shown in Figure P1.5.
6. LookingattheEMP_NAMEandEMP_PHONEcontentsinFigureP1.5,whatchange(s)wouldyourecommend?
7. Identify the various data sources in the file you examined in Problem 5.
8. GivenyouranswertoProblem7,whatnewfilesshouldyoucreatetohelpeliminatethedataredundanciesfound
in the file shown in Figure P1.5?

## Page 58

28 CHAPTER 1
FIGURE The file structure for Problems 9–10
P1.9
9. Identify and discuss the serious data redundancy problems exhibited by the file structure shown in Figure P1.9.
(The file is meant to be used as a teacher class assignment schedule. One of the many problems with data
redundancy is the likely occurrence of data inconsistencies—two different initials have been entered for the
teacher named Maria Cordoza.)
10. GiventhefilestructureshowninFigureP1.9,whatproblem(s)mightyouencounterifbuildingKOMweredeleted?

## Page 59

2
Data Models
In this chapter, you will learn:
(cid:1) About data modeling and why data models are important
(cid:1) About the basic data-modeling building blocks
(cid:1) What business rules are and how they influence database design
(cid:1) How the major data models evolved
(cid:1) How data models can be classified by level of abstraction
Thischapterexaminesdatamodeling.Datamodelingisthefirststepinthedatabasedesign
journey,servingasabridgebetweenreal-worldobjectsandthedatabasethatresidesinthe
computer.
P
One of the most vexing problems of database design is that designers,programmers,and
review
endusersseedataindifferentways.Consequently,differentviewsofthesamedatacanlead
to database designs that do not reflect an organization’s actual operation,thus failing to
meet end-user needs and data efficiency requirements.To avoid such failures, database
designersmustobtainaprecisedescriptionofthenatureofthedataandofthemanyuses
of that data within the organization.Communication among database designers,program-
mers,and end users should be frequent and clear.Data modeling clarifies such communi-
cation by reducing the complexities of database design to more easily understood
abstractions that define entities and the relations among them.
First,you will learn what some of the basic data-modeling concepts are and how current
data models developed from earlier models.Tracing the development of those database
models will help you understand the database design and implementation issues that are
addressed in the rest of this book. Second, you will be introduced to the entity
relationship diagram (ERD) as a data-modeling tool.ER diagrams can be drawn using a
variety of notations.Within this chapter,you will be introduced to the traditional Chen
notation,the more current Crow’s Foot notation,and the newer class diagram notation,
which is part of the Unified Modeling Language (UML).Finally,you will learn how various
degrees of data abstraction help reconcile varying views of the same data.
O
W
T

## Page 60

30 CHAPTER 2
2.1 DATA MODELING AND DATA MODELS
Databasedesignfocusesonhowthedatabasestructurewillbeusedtostoreandmanageend-userdata.Datamodeling,
thefirststepindesigningadatabase,referstotheprocessofcreatingaspecificdatamodelforadeterminedproblem
domain.(Aproblemdomainisaclearlydefinedareawithinthereal-worldenvironment,withwell-definedscopeand
boundaries, that is to be systematically addressed.) A data model is a relatively simple representation, usually
graphical,ofmorecomplexreal-worlddatastructures.Ingeneralterms,amodelisanabstractionofamorecomplex
real-world object or event. A model’s main function is to help you understand the complexities of the real-world
environment. Within the database environment, a data model represents data structures and their characteristics,
relations,constraints,transformations,andotherconstructswiththepurposeofsupportingaspecificproblemdomain.
Note
The terms data model and database model are often used interchangeably. In this book, the term database
modelisusedtorefertotheimplementationofadatamodelinaspecificdatabasesystem.
Datamodelingisaniterative,progressiveprocess.Youstartwithasimpleunderstandingoftheproblemdomain,and
asyourunderstandingoftheproblemdomainincreases,sodoesthelevelofdetailofthedatamodel.Doneproperly,
thefinaldatamodelisineffecta“blueprint”containingalltheinstructionstobuildadatabasethatwillmeetallend-user
requirements. This blueprint is narrative and graphical in nature, meaning that it contains both text descriptions in
plain, unambiguous language and clear, useful diagrams depicting the main data elements.
Note
Animplementation-readydatamodelshouldcontainatleastthefollowingcomponents:
• Adescriptionofthedatastructurethatwillstoretheend-userdata.
• Asetofenforceablerulestoguaranteetheintegrityofthedata.
• Adatamanipulationmethodologytosupportthereal-worlddatatransformations.
Traditionally, database designers relied on good judgment to help them develop a good data model. Unfortunately,
goodjudgmentisoftenintheeyeofthebeholder,anditoftendevelopsaftermuchtrialanderror.Forexample,ifeach
of the students in this class has to create a data model for a video store, it’s very likely that each of them will come
up with a different model. Which one would be the correct one? The simple answer is “the one that meets all the
end-userrequirements,”andtheremaybemorethanonecorrectsolution!Fortunately,databasedesignersmakeuse
of existing data-modeling constructs and powerful database design tools that substantially diminish the potential for
errors in database modeling. In the following sections, you will learn how existing data models are used to represent
real-worlddataandhowthedifferentdegreesofdataabstractionfacilitatedatamodeling.Forexample,ifeachstudent
in a class has to create a data model for a video store, it’s very likely that each will come up with a different model.
2.2 THE IMPORTANCE OF DATA MODELS
Data models can facilitate interaction among the designer, the applications programmer, and the end user. A
well-developeddatamodelcanevenfosterimprovedunderstandingoftheorganizationforwhichthedatabasedesign
is developed. In short, data models are a communication tool. This important aspect of data modeling was summed
upneatlybyaclientwhosereactionwasasfollows:“Icreatedthisbusiness,Iworkedwiththisbusinessforyears,and
this is the first time I’ve really understood how all the pieces really fit together.”

## Page 61

DATA MODELS 31
Theimportanceofdatamodelingcannotbeoverstated.Dataconstitutethemostbasicinformationunitsemployedby
a system. Applications are created to manage data and to help transform data into information.But data are viewed
in different ways by different people. For example, contrast the (data) view of a company manager with that of a
companyclerk.Althoughthemanagerandtheclerkbothworkforthesamecompany,themanagerismorelikelyto
have an enterprise-wide view of company data than the clerk.
Even different managers view data differently. For example, a company president is likely to take a universal view of
the data because he or she must be able to tie the company’s divisions to a common (database) vision. A purchasing
manager in the same company is likely to have a more restricted view of the data, as is the company’s inventory
manager. In effect, each department manager works with a subset of the company’s data. The inventory manager is
moreconcernedaboutinventorylevels,whilethepurchasingmanagerismoreconcernedaboutthecostofitemsand
about personal/business relationships with the suppliers of those items.
Applications programmers have yet another view of data, being more concerned with data location, formatting, and
specificreportingrequirements.Basically,applicationsprogrammerstranslatecompanypoliciesandproceduresfrom
a variety of sources into appropriate interfaces, reports, and query screens.
Thedifferentusersandproducersofdataandinformationoftenreflectthe“blindpeopleandtheelephant”analogy:the
blindpersonwhofelttheelephant’strunkhadquiteadifferentviewoftheelephantfromtheonewhofelttheelephant’s
leg or tail. What is needed is a view of the whole elephant. Similarly, a house is not a random collection of rooms; if
someoneisgoingtobuildahouse,heorsheshouldfirsthavetheoverallviewthatisprovidedbyblueprints.Likewise,a
sound data environment requires an overall database blueprint based on an appropriate data model.
Whenagooddatabaseblueprintisavailable,itdoesnotmatterthatanapplicationsprogrammer’sviewofthedatais
differentfromthatofthemanagerand/ortheenduser.Conversely,whenagooddatabaseblueprintisnotavailable,
problems are likely to ensue. For instance, an inventory management program and an order entry system may use
conflicting product-numbering schemes, thereby costing the company thousands (or even millions) of dollars.
Keepinmindthatahouseblueprintisanabstraction;youcannotliveintheblueprint.Similarly,thedatamodelisan
abstraction;youcannotdrawtherequireddataoutofthedatamodel.Justasyouarenotlikelytobuildagoodhouse
withoutablueprint,youareequallyunlikelytocreateagooddatabasewithoutfirstcreatinganappropriatedatamodel.
2.3 DATA MODEL BASIC BUILDING BLOCKS
Thebasicbuildingblocksofalldatamodelsareentities,attributes,relationships,andconstraints.Anentityisanything
(a person, a place, a thing, or an event) about which data are to be collected and stored. An entity represents a
particular type of object in the real world. Because an entity represents a particular type of object, entities are
“distinguishable”—thatis,eachentityoccurrenceisuniqueanddistinct.Forexample,aCUSTOMERentitywouldhave
many distinguishable customer occurrences, such as John Smith, Pedro Dinamita, Tom Strickland, etc. Entities may
bephysicalobjects,suchascustomersorproducts,butentitiesmayalsobeabstractions,suchasflightroutesormusical
concerts.
Anattributeisacharacteristicofanentity.Forexample,aCUSTOMERentitywouldbedescribedbyattributessuch
ascustomerlastname,customerfirstname,customerphone,customeraddress,andcustomercreditlimit.Attributes
are the equivalent of fields in file systems.
A relationship describes an association among entities. For example, a relationship exists between customers and
agentsthatcanbedescribedasfollows:anagentcanservemanycustomers,andeachcustomermaybeservedbyone
agent.Datamodelsusethreetypesofrelationships:one-to-many,many-to-many,andone-to-one.Databasedesigners
usuallyusetheshorthandnotations1:Mor1..*,M:Nor*..*,and1:1or1..1,respectively.(AlthoughtheM:Nnotation
is a standard label for the many-to-many relationship, the label M:M may also be used.) The following examples
illustrate the distinctions among the three.

## Page 62

32 CHAPTER 2
(cid:2) One-to-many(1:Mor1..*)relationship.Apainterpaintsmanydifferentpaintings,buteachoneofthem
ispaintedbyonlyonepainter.Thus,thepainter(the“one”)isrelatedtothepaintings(the“many”).Therefore,
database designers label the relationship “PAINTER paints PAINTING” as 1:M. (Note that entity names are
oftencapitalizedasaconvention,sotheyareeasilyidentified.)Similarly,acustomer(the“one”)maygenerate
many invoices, but each invoice (the “many”) is generated by only a single customer. The “CUSTOMER
generates INVOICE” relationship would also be labeled 1:M.
(cid:2) Many-to-many(M:Nor*..*)relationship.Anemployeemaylearnmanyjobskills,andeachjobskillmay
belearnedbymanyemployees.Databasedesignerslabeltherelationship“EMPLOYEElearnsSKILL”asM:N.
Similarly,astudentcantakemanyclassesandeachclasscanbetakenbymanystudents,thusyieldingtheM:N
relationship label for the relationship expressed by “STUDENT takes CLASS.”
(cid:2) One-to-one(1:1or1..1)relationship.Aretailcompany’smanagementstructuremayrequirethateachof
itsstoresbemanagedbyasingleemployee.Inturn,eachstoremanager,whoisanemployee,managesonly
a single store. Therefore, the relationship “EMPLOYEE manages STORE” is labeled 1:1.
The preceding discussion identified each relationship in both directions; that is, relationships are bidirectional:
(cid:2) One CUSTOMER can generate many INVOICEs.
(cid:2) Each of the many INVOICEs is generated by only one CUSTOMER.
Aconstraintisarestrictionplacedonthedata.Constraintsareimportantbecausetheyhelptoensuredataintegrity.
Constraints are normally expressed in the form of rules. For example:
(cid:2) An employee’s salary must have values that are between 6,000 and 350,000.
(cid:2) A student’s GPA must be between 0.00 and 4.00.
(cid:2) Each class must have one and only one teacher.
Howdoyouproperlyidentifyentities,attributes,relationships,andconstraints?Thefirststepistoclearlyidentifythe
business rules for the problem domain you are modeling.
2.4 BUSINESS RULES
Whendatabasedesignersgoaboutselectingordeterminingtheentities,attributes,andrelationshipsthatwillbeused
to build a data model, they might start by gaining a thorough understanding of what types of data are in an
organization, how the data are used, and in what time frames they are used. But such data and information do not,
bythemselves,yieldtherequiredunderstandingofthetotalbusiness.Fromadatabasepointofview,thecollectionof
data becomes meaningful only when it reflects properly defined business rules. A business rule is a brief, precise,
and unambiguous description of a policy, procedure, or principle within a specific organization. In a sense, business
rulesaremisnamed:theyapplytoanyorganization,largeorsmall—abusiness,agovernmentunit,areligiousgroup,
or a research laboratory—that stores and uses data to generate information.
Businessrules,derivedfromadetaileddescriptionofanorganization’soperations,helptocreateandenforceactions
withinthatorganization’senvironment.Businessrulesmustberenderedinwritingandupdatedtoreflectanychange
in the organization’s operational environment.
Properlywrittenbusinessrulesareusedtodefineentities,attributes,relationships,andconstraints.Anytimeyousee
relationship statements such as “an agent can serve many customers, and each customer can be served by only one
agent,” you are seeing business rules at work. You will see the application of business rules throughout this book,
especially in the chapters devoted to data modeling and database design.

## Page 63

DATA MODELS 33
Tobeeffective,businessrulesmustbeeasytounderstandandwidelydisseminated,toensurethateverypersoninthe
organization shares a common interpretation of the rules. Business rules describe, in simple language, the main and
distinguishing characteristics of the data as viewed by the company. Examples of business rules are as follows:
(cid:2) A customer may generate many invoices.
(cid:2) An invoice is generated by only one customer.
(cid:2) A training session cannot be scheduled for fewer than 10 employees or for more than 30 employees.
Notethatthosebusinessrulesestablishentities,relationships,andconstraints.Forexample,thefirsttwobusinessrules
establish two entities (CUSTOMER and INVOICE) and a 1:M relationship between those two entities. The third
businessruleestablishesaconstraint(nofewerthan10peopleandnomorethan30people),twoentities(EMPLOYEE
and TRAINING), and a relationship between EMPLOYEE and TRAINING.
2.4.1 Discovering Business Rules
The main sources of business rules are company managers, policy makers, department managers, and written
documentationsuchasacompany’sprocedures,standards,andoperationsmanuals.Afasterandmoredirectsource
ofbusinessrulesisdirectinterviewswithendusers.Unfortunately,becauseperceptionsdiffer,endusersaresometimes
a less reliable source when it comes to specifying business rules. For example, a maintenance department mechanic
mightbelievethatanymechaniccaninitiateamaintenanceprocedure,whenactuallyonlymechanicswithinspection
authorizationcanperformsuchatask.Suchadistinctionmightseemtrivial,butitcanhavemajorlegalconsequences.
Although end users are crucial contributors to the development of business rules, it pays to verify end-user
perceptions. Too often, interviews with several people who perform the same job yield very different perceptions of
what the job components are. While such a discovery may point to “management problems,” that general diagnosis
doesnothelpthedatabasedesigner.Thedatabasedesigner’sjobistoreconcilesuchdifferencesandverifytheresults
of the reconciliation to ensure that the business rules are appropriate and accurate.
The process of identifying and documenting business rules is essential to database design for several reasons:
(cid:2) They help to standardize the company’s view of data.
(cid:2) They can be a communications tool between users and designers.
(cid:2) They allow the designer to understand the nature, role, and scope of the data.
(cid:2) They allow the designer to understand business processes.
(cid:2) They allow the designer to develop appropriate relationship participation rules and constraints and to create
an accurate data model.
Ofcourse,notallbusinessrulescanbemodeled.Forexample,abusinessrulethatspecifiesthat“nopilotcanflymore
than 10 hours within any 24-hour period” cannot be modeled. However, such a business rule can be enforced by
application software.
2.4.2 Translating Business Rules into Data Model Components
Businessrulessetthestagefortheproperidentificationofentities,attributes,relationships,andconstraints.Inthereal
world,namesareusedtoidentifyobjects.Ifthebusinessenvironmentwantstokeeptrackoftheobjects,therewillbe
specificbusinessrulesforthem.Asageneralrule,anouninabusinessrulewilltranslateintoanentityinthemodel,
andaverb(activeorpassive)associatingnounswilltranslateintoarelationshipamongtheentities.Forexample,the
business rule “a customer may generate many invoices” contains two nouns (customer and invoices) and a verb
(generate) that associates the nouns. From this business rule, you could deduce that:
(cid:2) Customerandinvoiceareobjectsofinterestfortheenvironmentandshouldberepresentedbytheirrespective
entities.
(cid:2) There is a “generate” relationship between customer and invoice.

## Page 64

34 CHAPTER 2
To properly identify the type of relationship, you should consider that relationships are bidirectional; that is, they go
bothways.Forexample,thebusinessrule“acustomermaygeneratemanyinvoices”iscomplementedbythebusiness
rule “an invoice is generated by only one customer.” In that case, the relationship is one-to-many (1:M). Customer is
the “1” side, and invoice is the “many” side.
As a general rule, to properly identify the relationship type, you should ask two questions:
(cid:2) How many instances of B are related to one instance of A?
(cid:2) How many instances of A are related to one instance of B?
For example, you can assess the relationship between student and class by asking two questions:
(cid:2) In how many classes can one student enroll? Answer: many classes.
(cid:2) How many students can enroll in one class? Answer: many students.
Therefore, the relationship between student and class is many-to-many (M:N). You will have many opportunities to
determine the relationships between entities as you proceed through this book, and soon the process will become
second nature.
2.4.3 Naming Conventions
Duringthetranslationofbusinessrulestodatamodelcomponents,youidentifyentities,attributes,relationships,and
constraints. This identification process includes naming the object in a way that makes the object unique and
distinguishablefromotherobjectsintheproblemdomain.Therefore,itisimportantthatyoupayspecialattentionto
how you name the objects you are discovering.
Entitynamesshouldbedescriptiveoftheobjectsinthebusinessenvironment,anduseterminologythatisfamiliarto
the users. An attribute name should also be descriptive of the data represented by that attribute. It is also a good
practicetoprefixthenameofanattributewiththenameoftheentity(oranabbreviationoftheentityname)inwhich
itoccurs.Forexample,intheCUSTOMERentity,thecustomer’screditlimitmaybecalledCUS_CREDIT_LIMIT.The
CUS indicates that the attribute is descriptive of the CUSTOMER entity, while CREDIT_LIMIT makes it easy to
recognizethedatathatwillbecontainedintheattribute.Thiswillbecomeincreasinglyimportantinlaterchapterswhen
we discuss the need to use common attributes to specify relationships between entities. The use of a proper naming
convention will improve the data model’s ability to facilitate communication among the designer, application
programmer, and the end user. In fact, a proper naming convention can go a long way toward making your model
self-documenting.
2.5 THE EVOLUTION OF DATA MODELS
The quest for better data management has led to several models that attempt to resolve the file system’s critical
shortcomings. These models represent schools of thought as to what a database is, what it should do, the types of
structures that it should employ, and the technology that would be used to implement these structures. Perhaps
confusingly, these models are called data models just as are the graphical data models that we have been discussing.
This section gives an overview of the major data models in roughly chronological order. You will discover that many
of the “new” database concepts and structures bear a remarkable resemblance to some of the “old” data model
concepts and structures. Table 2.1 traces the evolution of the major data models.

## Page 65

DATA MODELS 35
TABLE Evolution of Major Data Models
2.1
GENERATION TIME DATAMODEL EXAMPLES COMMENTS
First 1960s−1970s Filesystem VMS/VSAM UsedmainlyonIBMmainframe
systems
Managedrecords,notrelationships
Second 1970s Hierarchicaland IMS Earlydatabasesystems
network ADABAS Navigationalaccess
IDS-II
Third Mid-1970sto Relational DB2 Conceptualsimplicity
present Oracle Entityrelationship(ER)modelingand
MSSQL-Server supportforrelationaldatamodeling
MySQL
Fourth Mid-1980sto Object-oriented Versant Object/relationalsupportsobject
present Object/relational Objectivity/DB datatypes
(O/R) DB/2UDB StarSchemasupportfordata
Oracle11g warehousing
Webdatabasesbecomecommon
Next Presentto XML dbXML Unstructureddatasupport
generation future HybridDBMS Tamino O/RmodelsupportsXMLdocuments
DB2UDB HybridDBMSaddsanobjectfront
Oracle11g endtorelationaldatabases
MSSQLServer
O n l i n e C o n t e n t
Thehierarchicalandnetworkmodelsarelargelyofhistoricalinterest,yettheydocontainsomeelementsand
featuresthatinterestcurrentdatabaseprofessionals.Thetechnicaldetailsofthosetwomodelsarediscussedin
detailinAppendixesKandL,respectively,inthePremiumWebsiteforthisbook.AppendixGisdevotedtothe
object-oriented(OO)model.However,giventhedominantmarketpresenceoftherelationalmodel,mostof
thebookfocusesonthatmodel.
2.5.1 Hierarchical and Network Models
The hierarchical model was developed in the 1960s to manage large amounts of data for complex manufacturing
projects such as the Apollo rocket that landed on the moon in 1969. Its basic logical structure is represented by an
upside-down tree. The hierarchical structure contains levels, or segments. A segment is the equivalent of a file
system’s record type. Within the hierarchy, a higher layer is perceived as the parent of the segment directly beneath
it,whichiscalledthechild.Thehierarchicalmodeldepictsasetofone-to-many(1:M)relationshipsbetweenaparent
and its children segments. (Each parent can have many children, but each child has only one parent.)
The network model was created to represent complex data relationships more effectively than the hierarchical
model, to improve database performance, and to impose a database standard. In the network model, the user
perceivesthenetworkdatabaseasacollectionofrecordsin1:Mrelationships.However,unlikethehierarchicalmodel,
thenetworkmodelallowsarecordtohavemorethanoneparent.Whilethenetworkdatabasemodelisgenerallynot
used today, the definitions of standard database concepts that emerged with the network model are still used by
modern data models. Some important concepts that were defined at this time are:
(cid:2) The schema, which is the conceptual organization of the entire database as viewed by the database
administrator.

## Page 66

36 CHAPTER 2
(cid:2) Thesubschema,whichdefinestheportionofthedatabase“seen”bytheapplicationprogramsthatactually
produce the desired information from the data contained within the database.
(cid:2) Adatamanagementlanguage(DML),whichdefinestheenvironmentinwhichdatacanbemanagedand
to work with the data in the database.
(cid:2) Aschemadatadefinitionlanguage(DDL),whichenablesthedatabaseadministratortodefinetheschema
components.
As information needs grew and as more sophisticated databases and applications were required, the network model
became too cumbersome. The lack of ad hoc query capability put heavy pressure on programmers to generate the
code required to produce even the simplest reports. And although the existing databases provided limited data
independence, any structural change in the database could still produce havoc in all application programs that drew
data from the database. Because of the disadvantages of the hierarchical and network models, they were largely
replaced by the relational data model in the 1980s.
2.5.2 The Relational Model
Therelationalmodelwasintroducedin1970byE.F.Codd(ofIBM)inhislandmarkpaper“ARelationalModelof
DataforLargeSharedDatabanks”(CommunicationsoftheACM,June1970,pp.377−387).Therelationalmodel
representedamajorbreakthroughforbothusersanddesigners.Touseananalogy,therelationalmodelproducedan
“automatic transmission” database to replace the “standard transmission” databases that preceded it. Its conceptual
simplicity set the stage for a genuine database revolution.
Note
Therelationaldatabasemodelpresentedinthischapterisanintroductionandanoverview.Amoredetailed
discussionisinChapter3,TheRelationalDatabaseModel.Infact,therelationalmodelissoimportantthat
itwillserveasthebasisfordiscussionsinmostoftheremainingchapters.
The relational model foundation is a mathematical concept known as a relation. To avoid the complexity of abstract
mathematicaltheory,youcanthinkofarelation(sometimescalledatable)asamatrixcomposedofintersectingrows
andcolumns.Eachrowinarelationiscalledatuple.Eachcolumnrepresentsanattribute.Therelationalmodelalso
describes a precise set of data manipulation constructs based on advanced mathematical concepts.
In 1970, Codd’s work was considered ingenious but impractical. The relational model’s conceptual simplicity was
bought at the expense of computer overhead; computers at that time lacked the power to implement the relational
model. Fortunately, computer power grew exponentially, as did operating system efficiency. Better yet, the cost of
computers diminished rapidly as their power grew. Today even PCs, costing a fraction of what their mainframe
ancestorsdid,canrunsophisticatedrelationaldatabasesoftwaresuchasOracle,DB2,MicrosoftSQLServer,MySQL,
and other mainframe relational software.
Therelationaldatamodelisimplementedthroughaverysophisticatedrelationaldatabasemanagementsystem
(RDBMS).TheRDBMSperformsthesamebasicfunctionsprovidedbythehierarchicalandnetworkDBMSsystems,
in addition to a host of other functions that make the relational data model easier to understand and implement.
Arguably the most important advantage of the RDBMS is its ability to hide the complexities of the relational model
from the user. The RDBMS manages all of the physical details, while the user sees the relational database as a
collectionoftablesinwhichdataarestored.Theusercanmanipulateandquerythedatainawaythatseemsintuitive
and logical.
Tables are related to each other through the sharing of a common attribute (value in a column). For example, the
CUSTOMER table in Figure 2.1 might contain a sales agent’s number that is also contained in the AGENT table.

## Page 67

DATA MODELS 37
FIGURE Linking relational tables
2.1
Table name: AGENT (first six attributes) Database name: Ch02_InsureCo
Link through AGENT_CODE
Table name: CUSTOMER
O n l i n e C o n t e n t
Thischapter’sdatabasescanbefoundinthePremiumWebsite.Forexample,thecontentsoftheAGENTand
CUSTOMERtablesshowninFigure2.1arefoundinthedatabasenamedCh02_InsureCo.
ThecommonlinkbetweentheCUSTOMERandAGENTtablesenablesyoutomatchthecustomertohisorhersales
agent, even though the customer data are stored in one table and the sales representative data are stored in another
table.Forexample,youcaneasilydeterminethatcustomerDunne’sagentisAlexAlbybecauseforcustomerDunne,
the CUSTOMER table’s AGENT_CODE is 501, which matches the AGENT table’s AGENT_CODE for Alex Alby.
Although the tables are independent of one another, you can easily associate the data between tables. The relational
modelprovidesaminimumlevelofcontrolledredundancytoeliminatemostoftheredundanciescommonlyfoundin
file systems.
The relationship type (1:1, 1:M, or M:N) is often shown
FIGURE A relational diagram
in a relational schema, an example of which is shown in
2.2
Figure2.2.Arelationaldiagramisarepresentationof
the relational database’s entities, the attributes within
those entities, and the relationships between those
entities.
InFigure2.2,therelationaldiagramshowstheconnecting
fields (in this case, AGENT_CODE) and the relationship
type,1:M.MicrosoftAccess,thedatabasesoftwareappli-
cationusedtogenerateFigure2.2,employsthe(cid:1)(infinity)
symbol to indicate the “many” side. In this example, the
CUSTOMER represents the “many” side because an
AGENTcanhavemanyCUSTOMERs.TheAGENTrep-
resents the “1” side because each CUSTOMER has only
one AGENT.

## Page 68

38 CHAPTER 2
Arelationaltablestoresacollectionofrelatedentities.Inthisrespect,therelationaldatabasetableresemblesafile.But
there is one crucial difference between a table and a file: A table yields complete data and structural independence
becauseitisapurelylogicalstructure.Howthedataarephysicallystoredinthedatabaseisofnoconcerntotheuser
or the designer; the perception is what counts. And this property of the relational data model, explored in depth in
the next chapter, became the source of a real database revolution.
Anotherreasonfortherelationaldatamodel’srisetodominanceisitspowerfulandflexiblequerylanguage.Formost
relationaldatabasesoftware,thequerylanguageisStructuredQueryLanguage(SQL),whichallowstheusertospecify
what must be done without specifying how it must be done. The RDBMS uses SQL to translate user queries into
instructionsforretrievingtherequesteddata.SQLmakesitpossibletoretrievedatawithfarlesseffortthananyother
database or file environment.
Fromanend-userperspective,anySQL-basedrelationaldatabaseapplicationinvolvesthreeparts:auserinterface,a
set of tables stored in the database, and the SQL “engine.” Each of these parts is explained below.
(cid:2) Theend-userinterface.Basically,theinterfaceallowstheendusertointeractwiththedata(byauto-generating
SQL code). Each interface is a product of the software vendor’s idea of meaningful interaction with the data.
You can also design your own customized interface with the help of application generators that are now
standard fare in the database software arena.
(cid:2) A collection of tables stored in the database. In a relational database, all data are perceived to be stored in
tables.Thetablessimply“present”thedatatotheenduserinawaythatiseasytounderstand.Eachtableis
independent. Rows in different tables are related by common values in common attributes.
(cid:2) SQL engine. Largely hidden from the end user, the SQL engine executes all queries, or data requests. Keep
inmindthattheSQLengineispartoftheDBMSsoftware.TheenduserusesSQLtocreatetablestructures
and to perform data access and table maintenance. The SQL engine processes all user requests—largely
behind the scenes and without the end user’s knowledge. Hence, it’s said that SQL is a declarative language
that tells what must be done but not how it must be done. (You will learn more about the SQL engine in
Chapter 11, Database Performance Tuning and Query Optimization.)
Because the RDBMS performs the behind-the-scenes tasks, it is not necessary to focus on the physical aspects of the
database. Instead, the chapters that follow concentrate on the logical portion of the relational database and its design.
Furthermore,SQLiscoveredindetailinChapter7,IntroductiontoStructuredQueryLanguage(SQL),andinChapter8,
Advanced SQL.
2.5.3 The Entity Relationship Model
The conceptual simplicity of relational database technology triggered the demand for RDBMSs. In turn, the rapidly
increasingrequirementsfortransactionandinformationcreatedtheneedformorecomplexdatabaseimplementation
structures,thuscreatingtheneedformoreeffectivedatabasedesigntools.(Buildingaskyscraperrequiresmoredetailed
design activities than building a doghouse, for example.)
Complexdesignactivitiesrequireconceptualsimplicitytoyieldsuccessfulresults.Althoughtherelationalmodelwasa
vastimprovementoverthehierarchicalandnetworkmodels,itstilllackedthefeaturesthatwouldmakeitaneffective
database design tool. Because it is easier to examine structures graphically than to describe them in text, database
designers prefer to use a graphical tool in which entities and their relationships are pictured. Thus, the entity
relationship (ER) model, orERM, has become a widely accepted standard for data modeling.
Peter Chen first introduced the ER data model in 1976; it was the graphical representation of entities and their
relationshipsinadatabasestructurethatquicklybecamepopularbecauseitcomplementedtherelationaldatamodel
concepts. The relational data model and ERM combined to provide the foundation for tightly structured database
design. ER models are normally represented in an entity relationship diagram (ERD), which uses graphical
representations to model database components.

## Page 69

DATA MODELS 39
Note
Becausethischapter’sobjectiveistointroducedata-modelingconcepts,asimplifiedERDisdiscussedinthis
section.YouwilllearnhowtouseERDstodesigndatabasesinChapter4,EntityRelationship(ER)Modeling.
The ER model is based on the following components:
(cid:2) Entity. Earlier in this chapter, an entity was defined as anything about which data are to be collected and
stored.AnentityisrepresentedintheERDbyarectangle,alsoknownasanentitybox.Thenameoftheentity,
a noun, is written in the center of the rectangle. The entity name is generally written in capital letters and is
written in the singular form: PAINTER rather than PAINTERS, and EMPLOYEE rather than EMPLOYEES.
Usually, when applying the ERD to the relational model, an entity is mapped to a relational table. Each row
in the relational table is known as an entity instance or entity occurrence in the ER model.
Note
Acollectionoflikeentitiesisknownasanentityset.Forexample,youcanthinkoftheAGENTfileinFigure2.1
asacollectionofthreeagents(entities)intheAGENTentityset.Technicallyspeaking,theERDdepictsentity
sets.Unfortunately,ERDdesignersusethewordentityasasubstituteforentityset,andthisbookwillconform
tothatestablishedpracticewhendiscussinganyERDanditscomponents.
Eachentityisdescribedbyasetofattributesthatdescribesparticularcharacteristicsoftheentity.Forexample,
the entity EMPLOYEE will have attributes such as a Social Security number, a last name, and a first name.
(Chapter 4 explains how attributes are included in the ERD.)
(cid:2) Relationships. Relationships describe associations among data. Most relationships describe associations
between two entities. When the basic data model components were introduced, three types of relationships
among data were illustrated: one-to-many (1:M), many-to-many (M:N), and one-to-one (1:1). The ER model
uses the term connectivity to label the relationship types. The name of the relationship is usually an active
orpassiveverb.Forexample,aPAINTERpaintsmanyPAINTINGs;anEMPLOYEElearnsmanySKILLs;an
EMPLOYEE manages a STORE.
Figure2.3showsthedifferenttypesofrelationshipsusingtwoERnotations:theoriginalChennotationandthemore
current Crow’s Foot notation.
TheleftsideoftheERdiagramshowstheChennotation,basedonPeterChen’slandmarkpaper.Inthisnotation,the
connectivitiesarewrittennexttoeachentitybox.Relationshipsarerepresentedbyadiamondconnectedtotherelated
entities through a relationship line. The relationship name is written inside the diamond.
The right side of Figure 2.3 illustrates the Crow’s Foot notation. The name “Crow’s Foot” is derived from the
three-pronged symbol used to represent the “many” side of the relationship. As you examine the basic Crow’s Foot
ERD in Figure 2.3, note that the connectivities are represented by symbols. For example, the “1” is represented by
ashortlinesegment,andthe“M”isrepresentedbythethree-pronged“crow’sfoot.”Inthisexample,therelationship
name is written above the relationship line.
InFigure2.3,entitiesandrelationshipsareshowninahorizontalformat,buttheymayalsobeorientedvertically.The
entity location and the order in which the entities are presented are immaterial; just remember to read a 1:M
relationship from the “1” side to the “M” side.
TheCrow’sFootnotationisusedasthedesignstandardinthisbook.However,theChennotationisusedtoillustrate
some of the ER modeling concepts whenever necessary. Most data modeling tools let you select the Crow’s Foot
notation. Microsoft Visio Professional software was used to generate the Crow’s Foot designs you will see in
subsequent chapters.

## Page 70

40 CHAPTER 2
FIGURE The Chen and Crow’s Foot notations
2.3
Note
Many-to-many(M:N)relationshipsexistataconceptuallevel,andyoushouldknowhowtorecognizethem.
However,youwilllearninChapter3thatM:Nrelationshipsarenotappropriateinarelationalmodel.Forthat
reason,MicrosoftVisiodoesnotsupporttheM:Nrelationshipdirectly.Therefore,toillustratetheexistenceof
aM:NrelationshipusingVisio,youhavetochangethelinestyleoftheconnector(seeAppendixA,Designing
DatabaseswithVisioProfessional:ATutorial,inthePremiumWebsite).
O n l i n e C o n t e n t
Aside from the Chen and Crow’s Foot notations, there are other ER model notations. For a summary of the
symbolsusedbyseveraladditionalERmodelnotations,seeAppendixD,ComparisonofERModelNotations,
inthePremiumWebsite.
Its exceptional visual simplicity makes the ER model the dominant database modeling and design tool. Nevertheless,
the search for better data-modeling tools continues as the data environment continues to evolve.
2.5.4 The Object-Oriented (OO) Model
Increasinglycomplexreal-worldproblemsdemonstratedaneedforadatamodelthatmorecloselyrepresentedthereal
world. In the object-oriented data model (OODM), both data and their relationships are contained in a single
structure known as an object. In turn, the OODM is the basis for the object-oriented database management
system (OODBMS).

## Page 71

DATA MODELS 41
O n l i n e C o n t e n t
ThischapterintroducesonlybasicOOconcepts.You’llhaveachancetoexamineobject-orientationconcepts
andprinciplesindetailinAppendixG,Object-OrientedDatabases,inthePremiumWebsite.
An OODM reflects a very different way to define and use entities. Like the relational model’s entity, an object is
describedbyitsfactualcontent.Butquiteunlikeanentity,anobjectincludesinformationaboutrelationshipsbetween
thefactswithintheobject,aswellasinformationaboutitsrelationshipswithotherobjects.Therefore,thefactswithin
theobjectaregivengreatermeaning.TheOODMissaidtobeasemanticdatamodelbecausesemanticindicates
meaning.
SubsequentOODMdevelopmenthasallowedanobjecttoalsocontainalloperationsthatcanbeperformedonit,such
aschangingitsdatavalues,findingaspecificdatavalue,andprintingdatavalues.Becauseobjectsincludedata,various
typesofrelationships,andoperationalprocedures,theobjectbecomesself-contained,thusmakingtheobject—atleast
potentially—a basic building block for autonomous structures.
The OO data model is based on the following components:
(cid:2) Anobjectisanabstractionofareal-worldentity.Ingeneralterms,anobjectmaybeconsideredequivalentto
an ER model’s entity. More precisely, an object represents only one occurrence of an entity. (The object’s
semantic content is defined through several of the items in this list.)
(cid:2) Attributes describe the properties of an object. For example, a PERSON object includes the attributes Name,
Social Security Number, and Date of Birth.
(cid:2) Objectsthatsharesimilarcharacteristicsaregroupedinclasses.Aclassisacollectionofsimilarobjectswith
sharedstructure(attributes)andbehavior(methods).Inageneralsense,aclassresemblestheERmodel’sentity
set.However,aclassisdifferentfromanentitysetinthatitcontainsasetofproceduresknownasmethods.
A class’s method represents a real-world action such as finding a selected PERSON’s name, changing a
PERSON’sname,orprintingaPERSON’saddress.Inotherwords,methodsaretheequivalentofprocedures
in traditional programming languages. In OO terms, methods define an object’s behavior.
(cid:2) Classesareorganizedinaclasshierarchy.Theclasshierarchyresemblesanupside-downtreeinwhicheach
class has only one parent. For example, the CUSTOMER class and the EMPLOYEE class share a parent
PERSON class. (Note the similarity to the hierarchical data model in this respect.)
(cid:2) Inheritance is the ability of an object within the class hierarchy to inherit the attributes and methods of the
classes above it. For example, two classes, CUSTOMER and EMPLOYEE, can be created as subclasses from
the class PERSON. In this case, CUSTOMER and EMPLOYEE will inherit all attributes and methods from
PERSON.
Object-oriented data models are typically depicted using Unified Modeling Language (UML) class diagrams. Unified
ModelingLanguage(UML)isalanguagebasedonOOconceptsthatdescribesasetofdiagramsandsymbolsthat
can be used to graphically model a system. UML class diagrams are used to represent data and their relationships
within the larger UML object-oriented system’s modeling language. For a more complete description of UML see
Appendix H, Unified Modeling Language (UML).
To illustrate the main concepts of the object-oriented data model, let’s use a simple invoicing problem. In this case,
invoices are generated by customers, each invoice references one or more lines, and each line represents an item
purchasedbyacustomer.Figure2.4illustratestheobjectrepresentationforthissimpleinvoicingproblem,aswellas
theequivalentUMLclassdiagramandERmodel.Theobjectrepresentationisasimplewaytovisualizeasingleobject
occurrence.

## Page 72

42 CHAPTER 2
FIGURE A comparison of OO, UML, and ER models
2.4
Object Representation UML Class Diagram ER Model
CUSTOMER +generates +belongs to INVOICE
INVOICE
+INV_NUMBER : Integer
1..1 0..* +INV_DATE : Date
+INV_SHIP_DATE : Date
INV_DATE +INV_TOTAL : Double
INV_NUMBER
INV_SHIP_DATE 1..1 +generates
INV_TOTAL
1
CUSTOMER
1..* +belongs to
M
LINE
LINE
As you examine Figure 2.4, note that:
(cid:2) The object representation of the INVOICE includes all related objects within the same object box. Note that
theconnectivities(1andM)indicatetherelationshipoftherelatedobjectstotheINVOICE.Forexample,the
1nexttotheCUSTOMERobjectindicatesthateachINVOICEisrelatedtoonlyoneCUSTOMER.TheMnext
to the LINE object indicates that each INVOICE contains many LINEs.
(cid:2) The UML class diagram uses three separate object classes (CUSTOMER, INVOICE, and LINE) and two
relationships to represent this simple invoicing problem. Note that the relationship connectivities are
representedbythe1..1,0..*,and1..*symbolsandthattherelationshipsarenamedinbothendstorepresent
the different “roles” that the objects play in the relationship.
(cid:2) TheERmodelalsousesthreeseparateentitiesandtworelationshipstorepresentthissimpleinvoiceproblem.
The OODM advances were felt in many areas, from system modeling to programming. The added semantics of the
OODM allowed for a richer representation of complex objects. This in turn enabled applications to support
increasingly complex objects in innovative ways. As you will see in the next section, such evolutionary advances also
affected the relational model.
2.5.5 Newer Data Models: Object/Relational and XML
Facing the demand to support more complex data representations, the relational model’s main vendors evolved the
modelfurtherandcreatedtheextendedrelationaldatamodel(ERDM).TheERDMaddsmanyoftheOOmodel’s
features within the inherently simpler relational database structure. The ERDM gave birth to a new generation of
relational databases supporting OO features such as objects (encapsulated data and methods), extensible data types
basedonclasses,andinheritance.That’swhyaDBMSbasedontheERDMisoftendescribedasanobject/relational
database management system (O/R DBMS).
The use of complex objects received a boost with the Internet revolution. When organizations integrated their business
models with the Internet, they realized the potential of the Internet to access, distribute, and exchange critical business
information. This resulted in the widespread adoption of the Internet as a business communication tool. It is in this
environment that Extensible Markup Language (XML) emerged as the de facto standard for the efficient and effective
exchange of structured, semistructured, and unstructured data.Organizations using XML data soon realized there was a
need to manage the large amounts of unstructured data such as word-processing documents, Web pages, e-mails,
diagrams, etc., found in most of today’s organizations. To address this need, XML databases emerged to manage
unstructureddatawithinanativeXMLformat(seeChapter14,DatabaseConnectivityandWebTechnologies,formore

## Page 73

DATA MODELS 43
informationaboutXML).Atthesametime,O/RDBMSsaddedsupportforXML-baseddocumentswithintheirrelational
data structure.
2.5.6 The Future of Data Models
TodaytheO/RDBMSisthedominantdatabaseforbusinessapplications.Itssuccesscouldbeattributedtothemodel’s
conceptualsimplicity,easy-to-usequerylanguage,hightransactionperformance,highavailability,security,scalability,
andexpandability.Incontrast,theOODBMSispopularinnichemarketssuchascomputer-aideddrawing/computer-
aidedmanufacturing(CAD/CAM),geographicinformationsystems(GIS),telecommunications,andmultimedia,which
require support for complex objects.
The OO and the relational data models have two totally different approaches. The OO data model was created to
addressveryspecificengineeringneeds,notthewide-rangingneedsofgeneraldatamanagementtasks.Therelational
modelwascreatedwithafocusonbetterdatamanagementbasedonasoundmathematicalfoundation.Giventhese
differences,itisnotsurprisingthatthegrowthoftheOOmarkethasbeenslowcomparedtotherapidgrowthofthe
relational data model.
OneareainwhichOOconceptshavebeenveryinfluentialissystemsdevelopmentandprogramminglanguages.Most
contemporary programming languages are object-oriented (Java, Ruby, Perl, C#, .NET, to name a few). Also, there
is an increasing need to manage an organization’s unstructured data.
It is difficult to speculate on the future development of database models. Will unstructured data management overcome
structureddatamanagement?Wethinkthateachapproachcomplementsandaugmentstheother.O/Rdatabaseshave
proven to efficiently support structured and unstructured data management. Furthermore, history has shown that O/R
DBMSareremarkablyadaptableinsupportingever-evolvingdatamanagementneeds.Twoexamplesofthisevolutionare:
(cid:2) HybridDBMSsareemergingthatretaintheadvantagesoftherelationalmodelandatthesametimeprovide
programmers with an object-oriented view of the underlying data. These types of databases preserve the
performance characteristics of the relational model and the semantically rich programmatic support of the
object-oriented model.
(cid:2) SQLdataservices,suchasMicrosoftSQLDataServices(SDS)onitsAzureServicesPlatform,arebecoming
a critical component of relational database vendors’ Internet service strategies. These “cloud-based” (that is,
remotelyprocessedandInternet-based)dataservicesmakeitpossibleforcompaniesofanysizetostoretheir
datainrelationaldatabaseswithoutincurringexpensivehardware,software,andpersonnelcosts,whilehaving
access to high-end database features such as failover, backup, high transaction rates, and global data
distribution. Companies can use a “pay as you go” system based primarily on their storage and bandwidth
utilization and the features used.
2.5.7 Data Models: A Summary
The evolution of DBMSs has always been driven by the search for new ways of modeling increasingly complex
real-world data. A summary of the most commonly recognized data models is shown in Figure 2.5.
In the evolution of data models, there are some common characteristics that data models must have in order to be
widely accepted:
(cid:2) A data model must show some degree of conceptual simplicity without compromising the semantic
completeness of the database. It does not make sense to have a data model that is more difficult to
conceptualize than the real world.
(cid:2) A data model must represent the real world as closely as possible.This goal is more easily realized by adding
moresemanticstothemodel’sdatarepresentation.(Semanticsconcernthedynamicdatabehavior,whiledata
representation constitutes the static aspect of the real-world scenario.)
(cid:2) Representation of the real-world transformations (behavior) must be in compliance with the consistency and
integrity characteristics of any data model.

## Page 74

44 CHAPTER 2
FIGURE The evolution of data models
2.5
Semantics in
Comments
Data Model
least
Hierarchical • Difficult to represent M:N relationships
(hierarchical only)
• Structural level dependence
• No ad hoc queries (record-at-a-time access)
Network • Access path predefined (navigational access)
• Conceptual simplicity (structual independence)
Relational • Provides ad hoc queries (SQL)
• Set-oriented access
• Easy to understand (more semantics)
Entity Relationship • Limited to conceptual modeling
(no implementation component)
Semantic
• More semantics in data model
• Support for complex objects
• Inheritance (class hierarchy)
• Behavior
Extended Relational • Unstructured data (XML)
Object-Oriented
most (O/R DBMS) • XML data exchanges
Each new data model addresses the shortcomings of previous models. The network model replaced the hierarchical
modelbecausetheformermadeitmucheasiertorepresentcomplex(many-to-many)relationships.Inturn,therelational
model offers several advantages over the hierarchical and network models through its simpler data representation,
superiordataindependence,andeasy-to-usequerylanguage;thesefeaturesmadeitthepreferreddatamodelforbusiness
applications. The OO data model introduced support for complex data within a rich semantic framework. The ERDM
added many of the OO features to the relational model and allowed it to maintain its strong market share within the
businessenvironment.Andinrecentyears,successfuldatamodelshavefacilitatedthedevelopmentofdatabaseproducts
that incorporate unstructured data as well as provide support for easy data exchanges via XML.
It is important to note that not all data models are created equal; some data models are better suited than others for
some tasks. For example, conceptual models are better suited for high-level data modeling, while implementation
modelsarebetterformanagingstoreddataforimplementationpurposes.Theentityrelationshipmodelisanexample
of a conceptual model, while the hierarchical and network models are examples of implementation models. At the
same time, some models, such as the relational model and the OODM, could be used as both conceptual and
implementation models. Table 2.2 summarizes the advantages and disadvantages of the various database models.

## Page 75

sledoM
esabataD
suoiraV
fo
segatnavdasiD
dna
segatnavdA
ELBAT
2.2
LARUTCURTS
ATAD
ATAD
SEGATNAVDASID
SEGATNAVDA
ECNEDNEPEDNI
ECNEDNEPEDNI
LEDOM
atadlacisyhpfoegdelwonkseriuqernoitatnemelpmixelpmoC
.1
.gnirahsatadsetomorptI
.1
.scitsiretcarahcegarots
.yticilpmislautpecnocsetomorppihsnoitalerdlihC/tneraP
.2
oN
seY
lacihcrareiH
,tnempolevednoitacilppaxelpmocsdleiymetsyslanoitagivaN
.2
.SMBDybdecrofnednadedivorpsiytirucesesabataD
.3
.htaplacihcrareihfoegdelwonkseriuqer;esudna,tnemeganam
.ytirgetniatadsetomorppihsnoitalerdlihC/tneraP
.4
.smargorpnoitacilppallanisegnahceriuqererutcurtsnisegnahC
.3
.spihsnoitalerM:1htiwtneiciffesitI
.5
N:Mrotnerapitlumon(snoitatimilnoitatnemelpmieraerehT
.4
.)spihsnoitaler
niegaugnalnoitalupinamatadronoitinifedatadonsierehT
.5
.SMBDeht
.sdradnatsfokcalasierehT
.6
.metsyslanoitagivanallits—ycneiciffestimilytixelpmocmetsyS
.1
ehtfotahtotlauqetsaeltasiyticilpmislautpecnoC
.1
noitacilppa,noitatnemelpmixelpmocsdleiymetsyslanoitagivaN
.2
.ledomlacihcrareih
oN
seY
krowteN
.tnemeganamdna,tnempoleved
.tnerapitlumdnaN:Msahcus,sepytpihsnoitalereromseldnahtI
.2
.smargorpnoitacilppallanisegnahceriuqersegnahclarutcurtS
.3
metsyselifdnalacihcrareihninahtelbixelferomsisseccaataD
.3
.sledom
.ytirgetniatadsetomorppihsnoitalerrebmeM/renwOataD
.4
.sdradnatsotecnamrofnocsierehT
.5
noitalupinamataddna)LDD(egaugnalnoitinifedatadsedulcnitI
.6
.SMBDni)LMD(egaugnal
erawtfosmetsysdnaerawdrahlaitnatsbusseriuqerSMBDRehT
.1
tnednepednifoesuehtybdetomorpsiecnednepednilarutcurtS
.1
.daehrevo
rosseccaatadtceffatonoderutcurtss’elbatanisegnahC.selbat
seY
seY
lanoitaleR
otslootehtelpoepdeniartnuylevitalersevigyticilpmislautpecnoC
.2
.smargorpnoitacilppa
ehtecudorpyamti,dekcehcnufidna,ylroopmetsysdoogaesu
ybereht,yticilpmislautpecnocsevorpmiyllaitnatsbusweivralubaT
.2
.smetsyselifnidnuofseilamonaatademas
,tnemeganam,noitatnemelpmi,ngisedesabatadreisaegnitomorp
slaudividnisasmelborp”noitamrofnifosdnalsi“etomorpyamtI
.3
.esudna
.snoitacilppanworiehtpolevedylisaenacstnemtrapeddna
.LQSnodesabsiytilibapacyreuqcohdA
.3
sliatedlevel-lacisyhpmorfresudneehtsetalosiSMBDRlufrewoP
.4
.yticilpmistnemeganamdnanoitatnemelpmisevorpmidna
.noitatneserpertniartsnocdetimilsierehT
.1
.yticilpmislautpecnoclanoitpecxesdleiygniledomlausiV
.1
.noitatneserperpihsnoitalerdetimilsierehT
.2
.lootnoitacinummocevitceffenatisekamnoitatneserperlausiV
.2
seY
seY
ytitnE
.egaugnalnoitalupinamatadonsierehT
.3
.ledomlanoitalertnanimodhtiwdetargetnisitI
.3
pihsnoitaler
devomererasetubirttanehwsruccotnetnocnoitamrofnifossoL
.4
neebsahnoitatimilsihT(.syalpsiddedworcdiovaotseititnemorf
).snoisrevlacihpargtneuqesbusnidesserdda
riehtylppusotsrodnevdesuacsdradnatsfotnempolevedwolS
.1
.deddasitnetnoccitnameS
.1
.dradnatsdetpeccaylediwagnitanimilesuht,stnemecnahnenwo
.tnetnoccitnamessedulcninoitatneserperlausiV
.2
seY
seY
-tcejbO
.metsyslanoitagivanxelpmocasitI
.2
.ytirgetniatadsetomorpecnatirehnI
.3
detneiro
.evrucgninraelpeetsasierehT
.3
.snoitcasnartswolsdaehrevometsyshgiH
.4
laitnetop
eht
gnitanimile
suht
,gnirahs
atad
etomorp
sledom
esabatad
lla
,eroferehT
.esabatad
eht
nihtiw
loop
atad
nommoc
a
fo
esu
eht
emussa
sesabatad
llA
:etoN
.noitamrofnifosdnalsifomelborp
DATA MODELS 45

## Page 76

46 CHAPTER 2
Thusfar,youhavebeenintroducedtothebasicconstructsofthemoreprominentdatamodels.Eachmodelusessuch
constructstocapturethemeaningofthereal-worlddataenvironment.Table2.3showsthebasicterminologyusedby
the various data models.
TABLE Data Model Basic Terminology Comparison
2.3
REAL EXAMPLE FILE HIERARCHICAL NETWORK RELATIONAL ERMODEL OO
WORLD PROCESSING MODEL MODEL MODEL MODEL
Agroupof Vendor File Segment Record Table Entity Class
vendors filecabinet type type Set
Asingle Global Record Segment Current Row Entity Object
vendor supplies occurrence record (tuple) occurrence instance
Thecontact Johnny Field Segment Record Table Entity Object
name Ventura field field attribute Attribute attribute
Thevendor G12987 Index Sequence Record Key Entity Object
identifier field key Identifier identifier
Note:Foradditionalinformationaboutthetermsusedinthistable,pleaseconsultthecorrespondingchaptersandonlineappen-
dixesaccompanyingthisbook.Forexample,ifyouwanttoknowmoreabouttheOOmodel,refertoAppendixG,Object-Oriented
Databases.
2.6 DEGREES OF DATA ABSTRACTION
Ifyouask10databasedesignerswhatadatamodelis,youwillendupwith10differentanswers—dependingonthe
degree of data abstraction. To illustrate the meaning of data abstraction, consider the example of automotive design.
Acardesignerbeginsbydrawingtheconceptofthecarthatistobeproduced.Next,engineersdesignthedetailsthat
helptransferthebasicconceptintoastructurethatcanbeproduced.Finally,theengineeringdrawingsaretranslated
intoproductionspecificationstobeusedonthefactoryfloor.Asyoucansee,theprocessofproducingthecarbegins
at a high level of abstraction and proceeds to an ever-increasing level of detail. The factory floor process cannot
proceedunlesstheengineeringdetailsareproperlyspecified,andtheengineeringdetailscannotexistwithoutthebasic
conceptual framework created by the designer. Designing a usable database follows the same basic process. That is,
adatabasedesignerstartswithanabstractviewoftheoveralldataenvironmentandaddsdetailsasthedesigncomes
closer to implementation. Using levels of abstraction can also be very helpful in integrating multiple (and sometimes
conflicting) views of data as seen at different levels of an organization.
In the early 1970s, the American National Standards Institute (ANSI) Standards Planning and Requirements
Committee(SPARC)definedaframeworkfordatamodelingbasedondegreesofdataabstraction.TheANSI/SPARC
architecture (as it is often referred to) defines three levels of data abstraction: external, conceptual, and internal. You
canusethisframeworktobetterunderstanddatabasemodels,asshowninFigure2.6.Inthefigure,theANSI/SPARC
frameworkhasbeenexpandedwiththeadditionofaphysicalmodeltoexplicitlyaddressphysical-levelimplementation
details of the internal model.
2.6.1 The External Model
The external model is the end users’ view of the data environment. The term end users refers to people who use
the application programs to manipulate the data and generate information. End users usually operate in an
environment in which an application has a specific business unit focus. Companies are generally divided into several
business units, such as sales, finance, and marketing. Each business unit is subject to specific constraints and
requirements, and each one uses a data subset of the overall data in the organization. Therefore, end users working
withinthosebusinessunitsviewtheirdatasubsetsasseparatefromorexternaltootherunitswithintheorganization.

## Page 77

DATA MODELS 47
FIGURE Data abstraction levels
2.6
End-User View End-User View
External External
Model Model
Degree of
Abstraction Characteristics
Conceptual Designer’s
Model View High ER Hardware-independent
Software-independent
Object-Oriented
Logical independence
Medium Relational Hardware-independent
Software-dependent
Internal DBMS
Model View
Network Hardware-dependent
Low Hierarchical Software-dependent
Physical independence
Physical
Model
Becausedataarebeingmodeled,ERdiagramswillbeusedtorepresenttheexternalviews.Aspecificrepresentation
of an external view is known as an external schema. To illustrate the external model’s view, examine the data
environment of Tiny College. Figure 2.7 presents the external schemas for two Tiny College business units: student
registrationandclassscheduling.Eachexternalschemaincludestheappropriateentities,relationships,processes,and
constraintsimposedbythebusinessunit.Alsonotethatalthoughtheapplicationviewsareisolatedfromeachother,
each view shares a common entity with the other view. For example, the registration and scheduling external
schemas share the entities CLASS and COURSE.
Note the entity relationships represented in Figure 2.7. For example:
(cid:2) A PROFESSOR may teach many CLASSes, and each CLASS is taught by only one PROFESSOR; that is,
there is a 1:M relationship between PROFESSOR and CLASS.
(cid:2) ACLASSmayENROLLmanystudents,andeachstudentmayENROLLinmanyCLASSes,thuscreatingan
M:N relationship between STUDENT and CLASS. (You will learn about the precise nature of the ENROLL
entity in Chapter 4.)
(cid:2) Each COURSE may generate many CLASSes, but each CLASS references a single COURSE. For example,
theremaybeseveralclasses(sections)ofadatabasecoursehavingacoursecodeofCIS-420.Oneofthoseclasses
mightbeofferedonMWFfrom8:00a.m.to8:50a.m.,anothermightbeofferedonMWFfrom1:00p.m.to
1:50p.m.,whileathirdmightbeofferedonThursdaysfrom6:00p.m.to8:40p.m.Yetallthreeclasseshave
the course code CIS-420.
(cid:2) Finally, a CLASS requires one ROOM, but a ROOM may be scheduled for many CLASSes. That is, each
classroom may be used for several classes: one at 9:00 a.m., one at 11:00 a.m., and one at 1 p.m., for
example. In other words, there is a 1:M relationship between ROOM and CLASS.

## Page 78

48 CHAPTER 2
FIGURE External models for Tiny College
2.7
The use of external views representing subsets of the database has some important advantages:
(cid:2) It makes it easy to identify specific data required to support each business unit’s operations.
(cid:2) Itmakesthedesigner’sjobeasybyprovidingfeedbackaboutthemodel’sadequacy.Specifically,themodelcan
becheckedtoensurethatitsupportsallprocessesasdefinedbytheirexternalmodels,aswellasalloperational
requirements and constraints.
(cid:2) It helps to ensure security constraints in the database design. Damaging an entire database is more difficult
when each business unit works with only a subset of data.
(cid:2) It makes application program development much simpler.
2.6.2 The Conceptual Model
Havingidentifiedtheexternalviews,aconceptualmodelisused,graphicallyrepresentedbyanERD(asinFigure2.8),
to integrate all external views into a single view. The conceptual model represents a global view of the entire
database as viewed by the entire organization. That is, the conceptual model integrates all external views (entities,
relationships, constraints, and processes) into a single global view of the data in the enterprise. Also known as a
conceptualschema,itisthebasisfortheidentificationandhigh-leveldescriptionofthemaindataobjects(avoiding
any database model–specific details).
ThemostwidelyusedconceptualmodelistheERmodel.RememberthattheERmodelisillustratedwiththehelpofthe
ERD,whichis,ineffect,thebasicdatabaseblueprint.TheERDisusedtographicallyrepresenttheconceptualschema.
Theconceptualmodelyieldssomeveryimportantadvantages.First,itprovidesarelativelyeasilyunderstoodbird’s-eye
(macrolevel)viewofthedataenvironment.Forexample,youcangetasummaryofTinyCollege’sdataenvironment
by examining the conceptual model presented in Figure 2.8.
Second,theconceptualmodelisindependentofbothsoftwareandhardware.Softwareindependencemeansthat
themodeldoesnotdependontheDBMSsoftwareusedtoimplementthemodel.Hardwareindependencemeans
that the model does not depend on the hardware used in the implementation of the model. Therefore, changes in

## Page 79

DATA MODELS 49
either the hardware or the DBMS software will
FIGURE Conceptual model for Tiny College
2.8 have no effect on the database design at the
conceptual level. Generally, the term logical
designisusedtorefertothetaskofcreatinga
conceptual data model that could be imple-
mented in any DBMS.
2.6.3 The Internal Model
Once a specific DBMS has been selected, the
internal model maps the conceptual model to
the DBMS. The internal model is the repre-
sentation of the database as “seen” by the
DBMS. In other words, the internal model
requires the designer to match the conceptual
model’s characteristics and constraints to those
of the selected implementation model. An
internalschemadepictsaspecificrepresenta-
tion of an internal model, using the database
constructs supported by the chosen database.
Becausethisbookfocusesontherelationalmodel,arelationaldatabasewaschosentoimplementtheinternalmodel.
Therefore,theinternalschemashouldmaptheconceptualmodeltotherelationalmodelconstructs.Inparticular,the
entitiesintheconceptualmodelaremappedtotablesintherelationalmodel.Likewise,becausearelationaldatabase
hasbeenselected,theinternalschemaisexpressedusingSQL,thestandardlanguageforrelationaldatabases.Inthe
caseoftheconceptualmodelforTinyCollegedepictedinFigure2.8,theinternalmodelwasimplementedbycreating
the tables PROFESSOR, COURSE, CLASS, STUDENT, ENROLL, and ROOM. A simplified version of the internal
model for Tiny College is shown in Figure 2.9.
Thedevelopmentofadetailedinternalmodelisespeciallyimportanttodatabasedesignerswhoworkwithhierarchical
or network models because those models require very precise specification of data storage location and data access
paths. In contrast, the relational model requires less detail in its internal model because most RDBMSs handle data
access path definition transparently; that is, the designer need not be aware of the data access path details.
Nevertheless, even relational database software usually requires data storage location specification, especially in a
mainframe environment. For example, DB2 requires that you specify the data storage group, the location of the
database within the storage group, and the location of the tables within the database.
Because the internal model depends on specific database software, it is said to be software-dependent. Therefore, a
changeintheDBMSsoftwarerequiresthattheinternalmodelbechangedtofitthecharacteristicsandrequirements
of the implementation database model. When you can change the internal model without affecting the conceptual
model, you have logical independence. However, the internal model is still hardware-independent because it is
unaffected by the choice of the computer on which the software is installed. Therefore, a change in storage devices
or even a change in operating systems will not affect the internal model.
2.6.4 The Physical Model
Thephysicalmodeloperatesatthelowestlevelofabstraction,describingthewaydataaresavedonstoragemedia
suchasdisksortapes.Thephysicalmodelrequiresthedefinitionofboththephysicalstoragedevicesandthe(physical)
access methods required to reach the data within those storage devices, making it both software- and hardware-
dependent.Thestoragestructuresusedaredependentonthesoftware(theDBMSandtheoperatingsystem)andon
the type of storage devices that the computer can handle. The precision required in the physical model’s definition
demandsthatdatabasedesignerswhoworkatthislevelhaveadetailedknowledgeofthehardwareandsoftwareused
to implement the database design.

## Page 80

50 CHAPTER 2
FIGURE Internal model for Tiny College
2.9
Early data models forced the database designer to take the details of the physical model’s data storage requirements
intoaccount.However,thenowdominantrelationalmodelisaimedlargelyatthelogicalratherthanthephysicallevel;
therefore, it does not require the physical-level details common to its predecessors.
Although the relational model does not require the designer to be concerned about the data’s physical storage
characteristics, the implementation of a relational model may require physical-level fine-tuning for increased
performance.Fine-tuningisespeciallyimportantwhenverylargedatabasesareinstalledinamainframeenvironment.
Yet even such performance fine-tuning at the physical level does not require knowledge of physical data storage
characteristics.
As noted earlier, the physical model is dependent on the DBMS, methods of accessing files, and types of hardware
storage devices supported by the operating system. When you can change the physical model without affecting the
internal model, you have physical independence. Therefore, a change in storage devices or methods and even a
change in operating system will not affect the internal model.
A summary of the levels of data abstraction is given in Table 2.4.
TABLE Levels of Data Abstraction
2.4
DEGREEOF
MODEL ABSTRACTION FOCUS INDEPENDENTOF
External High End-userviews Hardwareandsoftware
Conceptual Globalviewofdata Hardwareandsoftware
(databasemodel−independent)
Internal Specificdatabasemodel Hardware
Physical Low Storageandaccessmethods Neitherhardwarenorsoftware

## Page 81

DATA MODELS 51
S u m m a r y
◗
Adatamodelisanabstractionofacomplexreal-worlddataenvironment.Databasedesignersusedatamodelsto
communicate with applications programmers and end users. The basic data-modeling components are entities,
attributes, relationships, and constraints. Business rules are used to identify and define the basic modeling
components within a specific real-world environment.
◗
Thehierarchicalandnetworkdatamodelswereearlydatamodelsthatarenolongerused,butsomeoftheconcepts
arefoundincurrentdatamodels.Thehierarchicalmodeldepictsasetofone-to-many(1:M)relationshipsbetweena
parentanditschildrensegments.Thenetworkmodelusessetstorepresent1:Mrelationshipsbetweenrecordtypes.
◗
The relational model is the current database implementation standard. In the relational model, the end user
perceives the data as being stored in tables. Tables are related to each other by means of common values in
common attributes. The entity relationship (ER) model is a popular graphical tool for data modeling that
complements the relational model. The ER model allows database designers to visually present different views of
thedata—asseenbydatabasedesigners,programmers,andendusers—andtointegratethedataintoacommon
framework.
◗
Theobject-orienteddatamodel(OODM)usesobjectsasthebasicmodelingstructure.Anobjectresemblesanentity
in that it includes the facts that define it. But unlike an entity, the object also includes information about
relationships between the facts, as well as relationships with other objects, thus giving its data more meaning.
◗
The relational model has adopted many object-oriented (OO) extensions to become the extended relational data
model (ERDM). Object/relational database management systems (O/R DBMS) were developed to implement the
ERDM. At this point, the OODM is largely used in specialized engineering and scientific applications, while the
ERDMisprimarilygearedtobusinessapplications.Althoughthemostlikelyfuturescenarioisanincreasingmerger
of OODM and ERDM technologies, both are overshadowed by the need to develop Internet access strategies for
databases. Usually OO data models are depicted using Unified Modeling Language (UML) class diagrams.
◗
Data-modelingrequirementsareafunctionofdifferentdataviews(globalvs.local)andthelevelofdataabstraction.
The American National Standards Institute Standards Planning and Requirements Committee (ANSI/SPARC)
describes three levels of data abstraction: external, conceptual, and internal. There is also a fourth level of data
abstraction, the physical level. This lowest level of data abstraction is concerned exclusively with physical storage
methods.
K e y T e r ms
American National Standards Crow’s Foot notation, 39 entity set, 39
Institute (ANSI), 46 data definition language (DDL), 36 extended relational data model
attribute, 31 data management language (ERDM), 42
business rule, 32 (DML), 36 external model, 46
Chen notation, 39 data model, 30 external schema, 47
class, 41 entity, 31 hardware independence, 48
class diagram, 41 entity instance, 39 hierarchical model, 35
class hierarchy, 41 entity occurrence, 39 hybrid DBMS , 43
conceptual model, 48 entity relationship diagram inheritance, 41
conceptual schema, 48 (ERD), 38 internal model, 49
connectivity, 39 entity relationship (ER) model internal schema, 49
(ERM), 38
constraint, 32 logical design, 49
logical independence, 49

## Page 82

52 CHAPTER 2
many-to-many (M:N or*..*) one-to-many (1:M or 1..*) relationship, 31
relationship, 32 relationship, 32 schema, 35
method, 41 one-to-one (1:1 or 1..1) segment, 35
network model, 35 relationship, 32 semantic data model, 41
object, 40 physical independence, 50 software independence, 48
object-oriented data model physical model, 49 subschema, 36
(OODM), 40 relation, 36
SQL data services, 43
object-oriented database relational database management
table, 36
management system system (RDBMS), 36
tuple, 36
(OODBMS), 40 relational diagram, 37
Unified Modeling Language
object/relational database relational model, 36
(UML), 41
management system
(O/R DBMS), 42
O n l i n e C o n t e n t
AnswerstoselectedReviewQuestionsandProblemsforthischapterarecontainedinthePremiumWebsitefor
thisbook.
R e v ie w Q u e st i o ns
1. Discuss the importance of data modeling.
2. What is a business rule, and what is its purpose in data modeling?
3. How do you translate business rules into data model components?
4. What languages emerged to standardize the basic network data model, and why was such standardization
important to users and designers?
5. Describethebasicfeaturesoftherelationaldatamodelanddiscusstheirimportancetotheenduserandthedesigner.
6. Explain how the entity relationship (ER) model helped produce a more structured relational database design
environment.
7. Use the scenario described by “A customer can make many payments, but each payment is made by only one
customer” as the basis for an entity relationship diagram (ERD) representation.
8. Why is an object said to have greater semantic content than an entity?
9. What is the difference between an object and a class in the object-oriented data model (OODM)?
10. How would you model Question 7 with an OODM? (Use Figure 2.4 as your guide.)
11. What is an ERDM, and what role does it play in the modern (production) database environment?
12. In terms of data and structural independence, compare file system data management with the five data models
discussed in this chapter.
13. What is a relationship, and what three types of relationships exist?
14. Give an example of each of the three types of relationships.
15. What is a table, and what role does it play in the relational model?
16. What is a relational diagram? Give an example.
17. What is logical independence?
18. What is physical independence?
19. What is connectivity? (Use a Crow’s Foot ERD to illustrate connectivity.)

## Page 83

DATA MODELS 53
P r o b le m s
Use the contents of Figure 2.1 to work Problems 1−3.
1. Write the business rule(s) that govern the relationship between AGENT and CUSTOMER.
2. Given the business rule(s) you wrote in Problem 1, create the basic Crow’s Foot ERD.
3. UsingtheERDyoudrewinProblem2,createtheequivalentobjectrepresentationandUMLclassdiagram.(Use
Figure 2.4 as your guide.)
Using Figure P2.4 as your guide, work Problems 4–5. The DealCo relational diagram shows the initial entities and
attributes for the DealCo stores, located in two regions of the country.
FIGURE The DealCo relational diagram
P2.4
4. Identify each relationship type and write all of the business rules.
5. Create the basic Crow’s Foot ERD for DealCo.
Using Figure P2.6 as your guide, work Problems 6−8. The Tiny College relational diagram shows the initial entities
and attributes for Tiny College.
FIGURE The Tiny College relational diagram
P2.6
6. Identify each relationship type and write all of the business rules.

## Page 84

54 CHAPTER 2
7. Create the basic Crow’s Foot ERD for Tiny College.
8. CreatetheUMLclassdiagramthatreflectstheentitiesandrelationshipsyouidentifiedintherelationaldiagram.
9. Typically, a patient staying in a hospital receives medications that have been ordered by a particular doctor.
Becausethepatientoftenreceivesseveralmedicationsperday,thereisa1:MrelationshipbetweenPATIENTand
ORDER.Similarly,eachordercanincludeseveralmedications,creatinga1:MrelationshipbetweenORDERand
MEDICATION.
a. Identify the business rules for PATIENT, ORDER, and MEDICATION.
b. Create a Crow’s Foot ERD that depicts a relational database model to capture these business rules.
10. United Broke Artists (UBA) is a broker for not-so-famous artists. UBA maintains a small database to track
painters, paintings, and galleries. A painting is painted by a particular artist, and that painting is exhibited in a
particular gallery. A gallery can exhibit many paintings, but each painting can be exhibited in only one gallery.
Similarly,apaintingispaintedbyasinglepainter,buteachpaintercanpaintmanypaintings.UsingPAINTER,
PAINTING, and GALLERY, in terms of a relational database:
a. What tables would you create, and what would the table components be?
b. How might the (independent) tables be related to one another?
11. UsingtheERDfromProblem10,createtherelationalschema.(Createanappropriatecollectionofattributesfor
each of the entities. Make sure you use the appropriate naming conventions to name the attributes.)
12. Convert the ERD from Problem 10 into the corresponding UML class diagram.
13. Describetherelationships(identifythebusinessrules)depictedintheCrow’sFootERDshowninFigureP2.13.
FIGURE The Crow’s Foot ERD
P2.13 for Problem 13
14. Create a Crow’s Foot ERD to include the following business rules for the ProdCo company:
a. Each sales representative writes many invoices.
b. Each invoice is written by one sales representative.
c. Each sales representative is assigned to one department.
d. Each department has many sales representatives.
e. Each customer can generate many invoices.
f. Each invoice is generated by one customer.

## Page 85

DATA MODELS 55
15. WritethebusinessrulesthatarereflectedintheERDshowninFigureP2.15.(NotethattheERDreflectssome
simplifying assumptions. For example, each book is written by only one author. Also, remember that the ERD
is always read from the “1” to the “M” side, regardless of the orientation of the ERD components.)
FIGURE The Crow’s Foot ERD
P2.15 for Problem 15
16. Create a Crow’s Foot ERD for each of the following descriptions.(Note: The word many merely means “more
than one” in the database modeling environment.)
a. EachoftheMegaCoCorporation’sdivisionsiscomposedofmanydepartments.Eachdepartmenthasmany
employees assigned to it, but each employee works for only one department. Each department is managed
by one employee, and each of those managers can manage only one department at a time.
b. During some period of time, a customer can rent many videotapes from the BigVid store. Each of BigVid’s
videotapes can be rented to many customers during that period of time.
c. An airliner can be assigned to fly many flights, but each flight is flown by only one airliner.
d. TheKwikTiteCorporationoperatesmanyfactories.Eachfactoryislocatedinaregion.Eachregioncanbe
“home” to many of KwikTite’s factories. Each factory employs many employees, but each of those
employees is employed by only one factory.
e. Anemployeemayhaveearnedmanydegrees,andeachdegreemayhavebeenearnedbymanyemployees.

## Page 86

PART
II
Design Concepts
3
The Relational Database Model
4
Entity Relationship (ER) Modeling
5
Advanced Data Modeling
6
Normalization of Database Tables

## Page 87

BP’s Data Modeling Initiative
B
British Petroleum is one of the largest energy companies in the world,engaged in fuel
exploration and production in 29 countries and actively developing alternative energy usiness
sources such as solar and wind energy and biofuels.In this large,diverse corporation, V
ignette
management is decentralized and IT expenditure and infrastructure development has
historically been project-driven.As a result, BP’s InformationTechnology and Services
(IT&S)divisionwasunabletoimplementuniformITstandardsandplatformsthroughout
the company.The company had adopted well over 5,000 software applications.
The decentralized company structure strongly impacted database development. Each
projectcreateditsowndatamodels.Theextentandapproachtodatamodelingdiffered
witheachproject.Projectmanagersusedalargevarietyofdatamodelingtools,including
SystemArchitecture,ERWin,ARIS,EnterpriseArchitecture,Visio,and even PowerPoint.
Moreover,there was no central repository where models and data definitions could be
stored.Once a project was finished,these models were frequently lost.So,BP suffered
from inconsistent data definitions,data duplication,and quality problems.
In 2003, BP decided to change all that.The company set a goal to manage data and
information“asasharedcorporateassetthatiseasilyaccessible.”ItcreatedanEnterprise
Architecture team to identify common IT standards.By the end of 2005,the team had
conducted a cross-company data modeling study and created a list of agreed upon
requirements.Theideawastoestablish“datamodelingasaservice”toallbusinessunits.
ThefunctionoftheEnterpriseArchitectureteamwouldnotbetoenforcestandardsand
procedures,but to train,support,and provide resources.
Since potential users were located all over the globe,the team decided to build a data
modeling portal that would house all data modeling related resources: standards and
guidelines,discussionboards,registrationfortrainings,andalargedatamodelrepository
where data models are automatically uploaded and shared.To support this effort, BP
adopted a single data modeling tool,ER/Studio.Users could work in ER/Studio and the
data models would automatically be published to Microsoft SharePoint. By 2009, the
repository contained 235 models for over 50,000 entities.
The response from users has been very positive.A recent survey found that nearly all
usersagreethattheyarebenefitingfromtheuseofacommonmodelingtool,acommon
repository,and common standards and guidelines.In addition,the number of employees
using the portal has increased.These two indicators strongly suggest that BP’s “data
modelingasaservice”strategyisovercomingthedisadvantagescreatedbyitspoliciesof
decentralized management and voluntary adoption.

## Page 88

3
The Relational Database Model
In this chapter, you will learn:
(cid:1) That the relational database model offers a logical view of data
(cid:1) About the relational model’s basic component: relations
(cid:1) That relations are logical constructs composed of rows (tuples) and columns (attributes)
(cid:1) That relations are implemented as tables in a relational DBMS
(cid:1) About relational database operators, the data dictionary, and the system catalog
(cid:1) How data redundancy is handled in the relational database model
(cid:1) Why indexing is important
InChapter2,DataModels,youlearnedthattherelationaldatamodel’sstructuralanddata
independence allow you to examine the model’s logical structure without considering the
physical aspects of data storage and retrieval.You also learned that entity relationship
P
diagrams (ERDs) may be used to depict entities and their relationships graphically.In this
chapter,youwilllearnsomeimportantdetailsabouttherelationalmodel’slogicalstructure review
and more about how the ERD can be used to design a relational database.
You will also learn how the relational database’s basic data components fit into a logical
construct known as a table.You will discover that one important reason for the relational
database model’s simplicity is that its tables can be treated as logical rather than physical
units.Youwillalsolearnhowtheindependenttableswithinthedatabasecanberelatedto
one another.
Afterlearningabouttables,theircomponents,andtheirrelationships,youwillbeintroduced
to the basic concepts that shape the design of tables.Because the table is such an integral
partofrelationaldatabasedesign,youwillalsolearnthecharacteristicsofwell-designedand
poorly designed tables.
Finally,youwillbeintroducedtosomebasicconceptsthatwillbecomeyourgatewaytothe
next few chapters.For example,you will examine different kinds of relationships and the
way those relationships might be handled in the relational database environment.
E
E
R
H
T

## Page 89

THE RELATIONAL DATABASE MODEL 59
Note
Therelationalmodel,introducedbyE.F.Coddin1970,isbasedonpredicatelogicandsettheory.Predicatelogic,
usedextensivelyinmathematics,providesaframeworkinwhichanassertion(statementoffact)canbeverifiedas
eithertrueorfalse.Forexample,supposethatastudentwithastudentIDof12345678isnamedMelissaSanduski.
Thisassertioncaneasilybedemonstratedtobetrueorfalse.Settheoryisamathematicalsciencethatdealswith
sets, or groups of things, and is used as the basis for data manipulation in the relational model. For example,
assumethatsetAcontainsthreenumbers:16,24,and77.ThissetisrepresentedasA(16,24,77).Furthermore,
setBcontainsfournumbers:44,77,90,and11,andsoisrepresentedasB(44,77,90,11).Giventhisinformation,
youcanconcludethattheintersectionofAandByieldsaresultsetwithasinglenumber,77.Thisresultcanbe
expressedasA(cid:1)B=77.Inotherwords,AandBshareacommonvalue,77.
Basedontheseconcepts,therelationalmodelhasthreewell-definedcomponents:
1. Alogicaldatastructurerepresentedbyrelations(Sections3.1,3.2,and3.5).
2. Asetofintegrityrulestoenforcethatthedataareandremainconsistentovertime(Sections3.3,3.6,3.7,
and3.8).
3. Asetofoperationsthatdefineshowdataaremanipulated(Section3.4).
3.1 A LOGICAL VIEW OF DATA
In Chapter 1, Database Systems, you learned that a database stores and manages both data and metadata. You also
learnedthattheDBMSmanagesandcontrolsaccesstothedataandthedatabasestructure.Suchanarrangement—
placingtheDBMSbetweentheapplicationandthedatabase—eliminatesmostofthefilesystem’sinherentlimitations.
Theresultofsuchflexibility,however,isafarmorecomplexphysicalstructure.Infact,thedatabasestructuresrequired
byboththehierarchicalandnetworkdatabasemodelsoftenbecomecomplicatedenoughtodiminishefficientdatabase
design. The relational data model changed all of that by allowing the designer to focus on the logical representation
of the data and its relationships, rather than on the physical storage details. To use an automotive analogy, the
relational database uses an automatic transmission to relieve you of the need to manipulate clutch pedals and
gearshifts. In short, the relational model enables you to view data logically rather than physically.
The practical significance of taking the logical view is that it serves as a reminder of the simple file concept of data
storage.Althoughtheuseofatable,quiteunlikethatofafile,hastheadvantagesofstructuralanddataindependence,
atabledoesresembleafilefromaconceptualpointofview.Becauseyoucanthinkofrelatedrecordsasbeingstored
in independent tables, the relational database model is much easier to understand than the hierarchical and network
models. Logical simplicity tends to yield simple and effective database design methodologies.
Because the table plays such a prominent role in the relational model, it deserves a closer look. Therefore, our
discussion begins with an exploration of the details of table structure and contents.
3.1.1 Tables and Their Characteristics
Thelogicalviewoftherelationaldatabaseisfacilitatedbythecreationofdatarelationshipsbasedonalogicalconstruct
knownasarelation.Becausearelationisamathematicalconstruct,endusersfinditmucheasiertothinkofarelation
as a table. A table is perceived as a two-dimensional structure composed of rows and columns. A table is also called
arelationbecausetherelationalmodel’screator,E.F.Codd,usedthetermrelationasasynonymfortable.Youcan
think of a table as a persistent representation of a logical relation, that is, a relation whose contents can be
permanentlysavedforfutureuse.Asfarasthetable’suserisconcerned,atablecontainsagroupofrelatedentity
occurrences, that is, an entity set. For example, a STUDENT table contains a collection of entity occurrences, each
representing a student. For that reason, the terms entity set and table are often used interchangeably.

## Page 90

60 CHAPTER 3
Note
Thewordrelation,alsoknownasadatasetinMicrosoftAccess,isbasedonthemathematicalsettheoryfrom
which Codd derived his model. Because the relational model uses attribute values to establish relationships
amongtables,manydatabaseusersincorrectlyassumethatthetermrelationreferstosuchrelationships.Many
thenincorrectlyconcludethatonlytherelationalmodelpermitstheuseofrelationships.
You will discover that the table view of data makes it easy to spot and define entity relationships, thereby greatly
simplifying the task of database design. The characteristics of a relational table are summarized in Table 3.1.
TABLE Characteristics of a Relational Table
3.1
1 Atableisperceivedasatwo-dimensionalstructurecomposedofrowsandcolumns.
2 Eachtablerow(tuple)representsasingleentityoccurrencewithintheentityset.
3 Eachtablecolumnrepresentsanattribute,andeachcolumnhasadistinctname.
4 Eachrow/columnintersectionrepresentsasingledatavalue.
5 Allvaluesinacolumnmustconformtothesamedataformat.
6 Eachcolumnhasaspecificrangeofvaluesknownastheattributedomain.
7 TheorderoftherowsandcolumnsisimmaterialtotheDBMS.
8 Eachtablemusthaveanattributeoracombinationofattributesthatuniquelyidentifieseachrow.
The table shown in Figure 3.1 illustrates the characteristics listed in Table 3.1.
FIGURE STUDENT table attribute values
3.1
Table name: STUDENT Database name: Ch03_TinyCollege
STU_NUM = Student number
STU_LNAME = Student last name
STU_FNAME = Student first name
STU_INIT = Student middle initial
STU_DOB = Student date of birth
STU_HRS = Credit hours earned
STU_CLASS = Student classification
STU_GPA = Grade point average
STU_TRANSFER = Student transferred from another institution
DEPT_CODE = Department code
STU_PHONE = 4-digit campus phone extension
PROF_NUM = Number of the professor who is the student’s advisor

## Page 91

THE RELATIONAL DATABASE MODEL 61
Note
Relationaldatabaseterminologyisveryprecise.Unfortunately,filesystemterminologysometimescreepsinto
thedatabaseenvironment.Thus,rowsaresometimesreferredtoasrecordsandcolumnsaresometimeslabeled
as fields. Occasionally, tables are labeled files. Technically speaking, this substitution of terms is not always
appropriate;thedatabasetableisalogicalratherthanaphysicalconcept,andthetermsfile,record,andfield
describephysicalconcepts.Nevertheless,aslongasyourecognizethatthetableisactuallyalogicalratherthan
aphysicalconstruct,youmay(attheconceptuallevel)thinkoftablerowsasrecordsandoftablecolumnsas
fields.Infact,manydatabasesoftwarevendorsstillusethisfamiliarfilesystemterminology.
O n l i n e C o n t e n t
AllofthedatabasesusedtoillustratethematerialinthischapterarefoundinthePremiumWebsiteforthisbook.
Thedatabasenamesusedinthefoldermatchthedatabasenamesusedinthefigures.Forexample,thesource
ofthetablesshowninFigure3.1istheCh03_TinyCollegedatabase.
UsingtheSTUDENTtableshowninFigure3.1,youcandrawthefollowingconclusionscorrespondingtothepoints
in Table 3.1:
1. TheSTUDENTtableisperceivedtobeatwo-dimensionalstructurecomposedofeightrows(tuples)andtwelve
columns (attributes).
2. Each row in the STUDENT table describes a single entity occurrence within the entity set. (The entity set is
representedbytheSTUDENTtable.)Forexample,row4inFigure3.1describesastudentnamedWalterH.
Oblonski.Giventhetablecontents,theSTUDENTentitysetincludeseightdistinctentities(rows),orstudents.
3. Each column represents an attribute, and each column has a distinct name.
4. All of the values in a column match the attribute’s characteristics. For example, the grade point average
(STU_GPA) column contains only STU_GPA entries for each of the table rows. Data must be classified
according to their format and function. Although various DBMSs can support different data types, most
support at least the following:
a. Numeric. Numeric data are data on which you can perform meaningful arithmetic procedures. For
example, in Figure 3.1, STU_HRS and STU_GPA are numeric attributes.
b. Character.Characterdata,alsoknownastextdataorstringdata,cancontainanycharacterorsymbolnot
intended for mathematical manipulation. In Figure 3.1, STU_CLASS and STU_PHONE are examples of
character attributes.
c. Date. Date attributes contain calendar dates stored in a special format known as the Julian date format.
For example, STU_DOB in Figure 3.1 is a date attribute.
d. Logical. Logical data can only have true or false (yes or no) values. In Figure 3.1, the STU_TRANSFER
attribute uses a logical data format.
5. The column’s range of permissible values is known as its domain. Because the STU_GPA values are limited
to the range 0–4, inclusive, the domain is [0,4].
6. The order of rows and columns is immaterial to the user.
7. Eachtablemusthaveaprimarykey.Ingeneralterms,theprimarykey(PK)isanattribute(oracombination
ofattributes)thatuniquelyidentifiesanygivenrow.Inthiscase,STU_NUM(thestudentnumber)istheprimary
key. Using the data presented in Figure 3.1, observe that a student’s last name (STU_LNAME) would not be

## Page 92

62 CHAPTER 3
a good primary key because it is possible to find several students whose last name is Smith. Even the
combinationofthelastnameandfirstname(STU_FNAME)wouldnotbeanappropriateprimarykeybecause,
as Figure 3.1 shows, it is quite possible to find more than one student named John Smith.
3.2 KEYS
In the relational model, keys are important because they are used to ensure that each row in a table is uniquely
identifiable. They are also used to establish relationships among tables and to ensure the integrity of the data.
Therefore, a proper understanding of the concept and use of keys in the relational model is very important. A key
consistsofoneormoreattributesthatdetermineotherattributes.Forexample,aninvoicenumberidentifiesallofthe
invoice attributes, such as the invoice date and the customer name.
Onetypeofkey,theprimarykey,hasalreadybeenintroduced.GiventhestructureoftheSTUDENTtableshownin
Figure3.1,defininganddescribingtheprimarykeyseemsimpleenough.However,becausetheprimarykeyplayssuch
animportantroleintherelationalenvironment,youwillexaminetheprimarykey’spropertiesmorecarefully.Inthis
section, you also will become acquainted with superkeys, candidate keys, and secondary keys.
Thekey’sroleisbasedonaconceptknownasdetermination.Inthecontextofadatabasetable,thestatement“A
determines B” indicates that if you know the value of attribute A, you can look up (determine) the value of attribute
B.Forexample,knowingtheSTU_NUMintheSTUDENTtable(seeFigure3.1)meansthatyouareabletolookup
(determine) that student’s last name, grade point average, phone number, and so on. The shorthand notation for “A
determinesB”isA→B.IfAdeterminesB,C,andD,youwriteA→B,C,D.Therefore,usingtheattributesofthe
STUDENT table in Figure 3.1, you can represent the statement “STU_NUM determines STU_LNAME” by writing:
STU_NUM → STU_LNAME
Infact,theSTU_NUMvalueintheSTUDENTtabledeterminesallofthestudent’sattributevalues.Forexample,you
can write:
STU_NUM → STU_LNAME, STU_FNAME, STU_INIT
and
STU_NUM → STU_LNAME, STU_FNAME, STU_INIT, STU_DOB, STU_TRANSFER
Incontrast,STU_NUMisnotdeterminedbySTU_LNAMEbecauseitisquitepossibleforseveralstudentstohavethe
last name Smith.
The principle of determination is very important because it is used in the definition of a central relational database
conceptknownasfunctionaldependence.Thetermfunctionaldependencecanbedefinedmosteasilythisway:the
attribute B is functionally dependent on A if A determines B. More precisely:
The attribute B is functionally dependent on the attribute A if each value in column A determines
one and only one value in column B.
Using the contents of the STUDENT table in Figure 3.1, it is appropriate to say that STU_PHONE is functionally
dependentonSTU_NUM.Forexample,theSTU_NUMvalue321452determinestheSTU_PHONEvalue2134.On
theotherhand,STU_NUMisnotfunctionallydependentonSTU_PHONEbecausetheSTU_PHONEvalue2267is
associatedwithtwoSTU_NUMvalues:324274and324291.(Thiscouldhappenwhenroommatesshareasingleland
line phone number.) Similarly, the STU_NUM value 324273 determines the STU_LNAME value Smith. But the
STU_NUM value is not functionally dependent on STU_LNAME because more than one student may have the last
name Smith.

## Page 93

THE RELATIONAL DATABASE MODEL 63
The functional dependence definition can be generalized to cover the case in which the determining attribute values
occur more than once in a table. Functional dependence can then be defined this way:1
Attribute A determines attribute B (that is, B is functionally dependent on A) if all of the rows in the
table that agree in value for attribute A also agree in value for attribute B.
Be careful when defining the dependency’s direction. For example, Gigantic State University determines its student
classification based on hours completed; these are shown in Table 3.2.
Therefore, you can write:
TABLE Student Classification
3.2 STU_HRS → STU_CLASS
HOURSCOMPLETED CLASSIFICATION But the specific number of hours is not dependent on the
Lessthan30 Fr classification. It is quite possible to find a junior with 62
30−59 So completed hours or one with 84 completed hours. In other
60−89 Jr words, the classification (STU_CLASS) does not determine
90ormore Sr one and only one value for completed hours (STU_HRS).
Keepinmindthatitmighttakemorethanasingleattribute
todefinefunctionaldependence;thatis,akeymaybecomposedofmorethanoneattribute.Suchamultiattributekey
is known as a composite key.
Any attribute that is part of a key is known as a key attribute. For instance, in the STUDENT table, the student’s
lastnamewouldnotbesufficienttoserveasakey.Ontheotherhand,thecombinationoflastname,firstname,initial,
and phone is very likely to produce unique matches for the remaining attributes. For example, you can write:
STU_LNAME, STU_FNAME, STU_INIT, STU_PHONE → STU_HRS, STU_CLASS
or
STU_LNAME, STU_FNAME, STU_INIT, STU_PHONE → STU_HRS, STU_CLASS, STU_GPA
or
STU_LNAME, STU_FNAME, STU_INIT, STU_PHONE → STU_HRS, STU_CLASS, STU_GPA, STU_DOB
Given the possible existence of a composite key, the notion of functional dependence can be further refined by
specifying full functional dependence:
If the attribute (B) is functionally dependent on a composite key (A) but not on any subset of that
composite key, the attribute (B) is fully functionally dependent on (A).
Withinthebroadkeyclassification,severalspecializedkeyscanbedefined.Forexample,asuperkeyisanykeythat
uniquelyidentifieseachrow.Inshort,thesuperkeyfunctionallydeterminesallofarow’sattributes.IntheSTUDENT
table, the superkey could be any of the following:
STU_NUM
STU_NUM, STU_LNAME
STU_NUM, STU_LNAME, STU_INIT
In fact, STU_NUM, with or without additional attributes, can be a superkey even when the additional attributes are
redundant.
1SQL:2003ANSIstandardspecification.ISO/IEC9075-2:2003–SQL/Foundation.

## Page 94

64 CHAPTER 3
A candidate key can be described as a superkey without unnecessary attributes, that is, a minimal superkey. Using
this distinction, note that the composite key
STU_NUM, STU_LNAME
is a superkey, but it is not a candidate key because STU_NUM by itself is a candidate key! The combination
STU_LNAME, STU_FNAME, STU_INIT, STU_PHONE
mightalsobeacandidatekey,aslongasyoudiscountthepossibilitythattwostudentssharethesamelastname,first
name, initial, and phone number.
If the student’s Social Security number had been included as one of the attributes in the STUDENT table in
Figure3.1—perhapsnamedSTU_SSN—bothitandSTU_NUMwouldhavebeencandidatekeysbecauseeitherone
woulduniquelyidentifyeachstudent.Inthatcase,theselectionofSTU_NUMastheprimarykeywouldbedrivenby
the designer’s choice or by end-user requirements. In short, the primary key is the candidate key chosen to be the
unique row identifier. Note, incidentally, that a primary key is a superkey as well as a candidate key.
Within a table, each primary key value must be unique to ensure that each row is uniquely identified by the primary
key.Inthatcase,thetableissaidtoexhibitentityintegrity.Tomaintainentityintegrity,anull(thatis,nodataentry
at all) is not permitted in the primary key.
Note
Anullisnovalueatall.Itdoesnotmeanazerooraspace.AnulliscreatedwhenyoupresstheEnterkeyor
theTabkeytomovetothenextentrywithoutmakingapriorentryofanykind.PressingtheSpacebarcreates
ablank(oraspace).
Nulls can never be part of a primary key, and they should be avoided—to the greatest extent possible—in other
attributes,too.Therearerarecasesinwhichnullscannotbereasonablyavoidedwhenyouareworkingwithnonkey
attributes. For example, one of an EMPLOYEE table’s attributes is likely to be the EMP_INITIAL. However, some
employeesdonothaveamiddleinitial.Therefore,someoftheEMP_INITIALvaluesmaybenull.Youwillalsodiscover
laterinthissectionthattheremaybesituationsinwhichanullexistsbecauseofthenatureoftherelationshipbetween
twoentities.Inanycase,evenifnullscannotalwaysbeavoided,theymustbeusedsparingly.Infact,theexistenceof
nulls in a table is often an indication of poor database design.
Nulls, if used improperly, can create problems because they have many different meanings. For example, a null can
represent:
(cid:2) An unknown attribute value.
(cid:2) A known, but missing, attribute value.
(cid:2) A “not applicable” condition.
Depending on the sophistication of the application development software, nulls can create problems when functions
suchasCOUNT,AVERAGE,andSUMareused.Inaddition,nullscancreatelogicalproblemswhenrelationaltables
are linked.
Controlledredundancymakestherelationaldatabasework.Tableswithinthedatabasesharecommonattributesthat
enablethetablestobelinkedtogether.Forexample,notethatthePRODUCTandVENDORtablesinFigure3.2share
acommonattributenamedVEND_CODE.AndnotethatthePRODUCTtable’sVEND_CODEvalue232occursmore
than once, as does the VEND_CODE value 235. Because the PRODUCT table is related to the VENDOR table
through these VEND_CODE values, the multiple occurrence of the values is required to make the 1:M relationship
between VENDOR and PRODUCT work. Each VEND_CODE value in the VENDOR table is unique—the VENDOR
isthe“1”sideintheVENDOR-PRODUCTrelationship.ButanygivenVEND_CODEvaluefromtheVENDORtable

## Page 95

THE RELATIONAL DATABASE MODEL 65
may occur more than once in the PRODUCT table, thus providing evidence that PRODUCT is the “M” side of the
VENDOR-PRODUCT relationship. In database terms, the multiple occurrences of the VEND_CODE values in the
PRODUCTtablearenotredundantbecausetheyarerequiredtomaketherelationshipwork.Youshouldrecallfrom
Chapter 2 that data redundancy exists only when there is unnecessary duplication of attribute values.
FIGURE An example of a simple relational database
3.2
Table name: PRODUCT Database name: Ch03_SaleCo
Primary key: PROD_CODE
Foreign key: VEND_CODE
link
Table name: VENDOR
Primary key: VEND_CODE
Foreign key: none
AsyouexamineFigure3.2,notethattheVEND_CODEvalueinonetablecanbeusedtopointtothecorresponding
value in the other table. For example, the VEND_CODE value 235 in the PRODUCT table points to vendor Henry
Ortozo in the VENDOR table. Consequently, you discover that the product “Houselite chain saw, 16-in. bar” is
deliveredbyHenryOrtozoandthathecanbecontactedbycalling615-899-3425.Thesameconnectioncanbemade
for the product “Steel tape, 12-ft. length” in the PRODUCT table.
Remember the naming convention—the prefix PROD was used in Figure 3.2 to indicate that the attributes “belong”
to the PRODUCT table. Therefore, the prefix VEND in the PRODUCT table’s VEND_CODE indicates that
VEND_CODE points to some other table in the database. In this case, the VEND prefix is used to point to the
VENDOR table in the database.
Arelationaldatabasecanalsoberepresentedbyarelationalschema.Arelationalschemaisatextualrepresentation
of the database tables where each table is listed by its name followed by the list of its attributes in parentheses. The
primarykeyattribute(s)is(are)underlined.YouwillseesuchschemasinChapter6,NormalizationofDatabaseTables.
For example, the relational schema for Figure 3.2 would be shown as:
VENDOR (VEND_CODE, VEND_CONTACT, VEND_AREACODE, VEND_PHONE)
PRODUCT (PROD_CODE, PROD_DESCRIPT, PROD_PRICE, PROD_ON_HAND, VEND_CODE)
ThelinkbetweenthePRODUCTandVENDORtablesinFigure3.2canalsoberepresentedbytherelationaldiagram
showninFigure3.3.Inthiscase,thelinkisindicatedbythelinethatconnectstheVENDORandPRODUCTtables.
NotethatthelinkinFigure3.3istheequivalentoftherelationshiplineinanERD.Thislinkiscreatedwhentwotables
share an attribute with common values. More specifically, the primary key of one table (VENDOR) appears as the
foreign key in a related table (PRODUCT). A foreign key (FK) is an attribute whose values match the primary key
values in the related table. For example, in Figure 3.2, the VEND_CODE is the primary key in the VENDOR table,

## Page 96

66 CHAPTER 3
and it occurs as a foreign key in the PRODUCT table.
FIGURE The relational diagram for
3.3 the Ch03_SaleCo database BecausetheVENDORtableisnotlinkedtoathirdtable,the
VENDOR table shown in Figure 3.2 does not contain a
foreign key.
If the foreign key contains either matching values or nulls,
thetablethatmakesuseofthatforeignkeyissaidtoexhibit
referentialintegrity.Inotherwords,referentialintegrity
means that if the foreign key contains a value, that value
refers to an existing valid tuple (row) in another relation.
Note that referential integrity is maintained between the
PRODUCT and VENDOR tables shown in Figure 3.2.
Finally, a secondary key is defined as a key that is used strictly for data retrieval purposes. Suppose customer data
are stored in a CUSTOMER table in which the customer number is the primary key. Do you suppose that most
customerswillremembertheirnumbers?Dataretrievalforacustomercanbefacilitatedwhenthecustomer’slastname
and phone number are used. In that case, the primary key is the customer number; the secondary key is the
combinationofthecustomer’slastnameandphonenumber.Keepinmindthatasecondarykeydoesnotnecessarily
yield a unique outcome. For example, a customer’s last name and home telephone number could easily yield several
matches where one family lives together and shares a phone line. A less efficient secondary key would be the
combination of the last name and zip code; this could yield dozens of matches, which could then be combed for a
specific match.
A secondary key’s effectiveness in narrowing down a search depends on how restrictive that secondary key is. For
instance,althoughthesecondarykeyCUS_CITYislegitimatefromadatabasepointofview,theattributevalues“New
York”or“Sydney”arenotlikelytoproduceausablereturnunlessyouwanttoexaminemillionsofpossiblematches.
(Of course, CUS_CITY is a better secondary key than CUS_COUNTRY.)
Table 3.3 summarizes the various relational database table keys.
TABLE Relational Database Keys
3.3
KEYTYPE DEFINITION
Superkey Anattribute(orcombinationofattributes)thatuniquelyidentifieseachrowinatable.
Candidatekey Aminimal(irreducible)superkey.Asuperkeythatdoesnotcontainasubsetofattributes
thatisitselfasuperkey.
Primarykey Acandidatekeyselectedtouniquelyidentifyallotherattributevaluesinanygivenrow.
Cannotcontainnullentries.
Secondarykey Anattribute(orcombinationofattributes)usedstrictlyfordataretrievalpurposes.
Foreignkey Anattribute(orcombinationofattributes)inonetablewhosevaluesmusteithermatchthe
primarykeyinanothertableorbenull.
3.3 INTEGRITY RULES
Relational database integrity rules are very important to good database design. Many (but by no means all) RDBMSs
enforceintegrityrulesautomatically.However,itismuchsafertomakesurethatyourapplicationdesignconformsto
the entity and referential integrity rules mentioned in this chapter. Those rules are summarized in Table 3.4.

## Page 97

THE RELATIONAL DATABASE MODEL 67
TABLE Integrity Rules
3.4
ENTITYINTEGRITY DESCRIPTION
Requirement Allprimarykeyentriesareunique,andnopartofaprimarykeymay
benull.
Purpose Eachrowwillhaveauniqueidentity,andforeignkeyvaluescanproperly
referenceprimarykeyvalues.
Example Noinvoicecanhaveaduplicatenumber,norcanitbenull.Inshort,all
invoicesareuniquelyidentifiedbytheirinvoicenumber.
REFERENCEINTEGRITY DESCRIPTION
Requirement Aforeignkeymayhaveeitheranullentry,aslongasitisnotapartofits
table’sprimarykey,oranentrythatmatchestheprimarykeyvalueina
tabletowhichitisrelated.(Everynon-nullforeignkeyvaluemustrefer-
enceanexistingprimarykeyvalue.)
Purpose ItispossibleforanattributeNOTtohaveacorrespondingvalue,butitwill
beimpossibletohaveaninvalidentry.Theenforcementofthereferential
integrityrulemakesitimpossibletodeletearowinonetablewhosepri-
marykeyhasmandatorymatchingforeignkeyvaluesinanothertable.
Example Acustomermightnotyethaveanassignedsalesrepresentative(number),
butitwillbeimpossibletohaveaninvalidsalesrepresentative(number).
The integrity rules summarized in Table 3.4 are illustrated in Figure 3.4.
FIGURE An illustration of integrity rules
3.4
Table name: CUSTOMER Database name: Ch03_InsureCo
Primary key: CUS_CODE
Foreign key: AGENT_CODE
Table name: AGENT
Primary key: AGENT_CODE
Foreign key: none
Note the following features of Figure 3.4.
1. Entityintegrity.TheCUSTOMERtable’sprimarykeyisCUS_CODE.TheCUSTOMERprimarykeycolumn
hasnonullentries,andallentriesareunique.Similarly,theAGENTtable’sprimarykeyisAGENT_CODE,and
this primary key column is also free of null entries.
2. Referential integrity. The CUSTOMER table contains a foreign key, AGENT_CODE, which links entries in
theCUSTOMERtabletotheAGENTtable.TheCUS_CODErowthatisidentifiedbythe(primarykey)number

## Page 98

68 CHAPTER 3
10013containsanullentryinitsAGENT_CODEforeignkeybecauseMr.PaulF.Olowskidoesnotyethave
a sales representative assigned to him. The remaining AGENT_CODE entries in the CUSTOMER table all
match the AGENT_CODE entries in the AGENT table.
To avoid nulls, some designers use special codes, known as flags, to indicate the absence of some value. Using
Figure 3.4 as an example, the code -99 could be used as the AGENT_CODE entry of the fourth row of the
CUSTOMER table to indicate that customer Paul Olowski does not yet have an agent assigned to him. If such a flag
isused,theAGENTtablemustcontainadummyrowwithanAGENT_CODEvalueof-99.Thus,theAGENTtable’s
first record might contain the values shown in Table 3.5.
TABLE A Dummy Variable Value Used as a Flag
3.5
AGENT_CODE AGENT_AREACODE AGENT_PHONE AGENT_LNAME AGENT_YTD_SALES
-99 000 000-0000 None $0.00
Chapter 4, Entity Relationship (ER) Modeling, discusses several ways in which nulls may be handled.
OtherintegrityrulesthatcanbeenforcedintherelationalmodelaretheNOTNULLandUNIQUEconstraints.The
NOT NULL constraint can be placed on a column to ensure that every row in the table has a value for that column.
The UNIQUE constraint is a restriction placed on a column to ensure that no duplicate values exist for that column.
3.4 RELATIONAL SET OPERATORS
Thedatainrelationaltablesareoflimitedvalueunlessthedatacanbemanipulatedtogenerateusefulinformation.This
section describes the basic data manipulation capabilities of the relational model. Relational algebra defines the
theoretical way of manipulating table contents using the eight relational operators: SELECT, PROJECT, JOIN,
INTERSECT, UNION, DIFFERENCE, PRODUCT, and DIVIDE. In Chapter 7, Introduction to Structured Query
Language (SQL), and Chapter 8, Advanced SQL, you will learn how SQL commands can be used to accomplish
relational algebra operations.
Note
Thedegreeofrelationalcompletenesscanbedefinedbytheextenttowhichrelationalalgebraissupported.To
beconsideredminimallyrelational,theDBMSmustsupportthekeyrelationaloperatorsSELECT,PROJECT,and
JOIN.VeryfewDBMSsarecapableofsupportingalleightrelationaloperators.
The relational operators have the property of closure; that is, the use of relational algebra operators on existing
relations (tables) produces new relations. There is no need to examine the mathematical definitions, properties, and
characteristics of those relational algebra operators. However, their use can easily be illustrated as follows:
1. SELECT, also known as RESTRICT, yields values for all rows found in a table that satisfy a given condition.
SELECT can be used to list all of the row values, or it can yield only those row values that match a specified
criterion. In other words, SELECT yields a horizontal subset of a table. The effect of a SELECT is shown in
Figure 3.5.
2. PROJECTyieldsallvaluesforselectedattributes.Inotherwords,PROJECTyieldsaverticalsubsetofatable.
The effect of a PROJECT is shown in Figure 3.6.

## Page 99

THE RELATIONAL DATABASE MODEL 69
FIGURE SELECT
3.5
Original table New table
SELECT ALL yields
SELECT only PRICE less than $2.00 yields
SELECT only P_CODE = 311452 yields
FIGURE PROJECT
3.6
Original table New table
PROJECT PRICE yields
PROJECT P_DESCRIPT and PRICE yields
PROJECT P_CODE and PRICE yields
3. UNIONcombinesallrowsfromtwotables,excludingduplicaterows.Thetablesmusthavethesameattribute
characteristics (the columns and domains must be compatible) to be used in the UNION. When two or more
tables share the same number of columns, and when their corresponding columns share the same (or
compatible)domains,theyaresaidtobeunion-compatible.TheeffectofaUNIONisshowninFigure3.7.
4. INTERSECTyieldsonlytherowsthatappearinbothtables.AswastrueinthecaseofUNION,thetablesmust
beunion-compatibletoyieldvalidresults.Forexample,youcannotuseINTERSECTifoneoftheattributesis
numeric and one is character-based. The effect of an INTERSECT is shown in Figure 3.8.

## Page 100

70 CHAPTER 3
FIGURE UNION
3.7
UNION yields
FIGURE INTERSECT
3.8
INTERSECT yields
5. DIFFERENCE yields all rows in one table that are not found in the other table; that is, it subtracts one table
from the other. As was true in the case of UNION, the tables must be union-compatible to yield valid results.
The effect of a DIFFERENCE is shown in Figure 3.9. However, note that subtracting the first table from the
second table is not the same as subtracting the second table from the first table.
FIGURE DIFFERENCE
3.9
DIFFERENCE yields
6. PRODUCTyieldsallpossiblepairsofrowsfromtwotables—alsoknownastheCartesianproduct.Therefore,
if one table has six rows and the other table has three rows, the PRODUCT yields a list composed of 6 × 3
= 18 rows. The effect of a PRODUCT is shown in Figure 3.10.
7. JOINallowsinformationtobecombinedfromtwoormoretables.JOINistherealpowerbehindtherelational
database,allowingtheuseofindependenttableslinkedbycommonattributes.TheCUSTOMERandAGENT
tables shown in Figure 3.11 will be used to illustrate several types of joins.

## Page 101

THE RELATIONAL DATABASE MODEL 71
FIGURE PRODUCT
3.10
PRODUCT yields
FIGURE Two tables that will be used in join illustrations
3.11
Table name: CUSTOMER Table name: AGENT
A natural join links tables by selecting only the rows with common values in their common attribute(s). A
natural join is the result of a three-stage process:
a. First, a PRODUCT of the tables is created, yielding the results shown in Figure 3.12.
b. Second, a SELECT is performed on the output of Step a to yield only the rows for which the
AGENT_CODEvaluesareequal.Thecommoncolumnsarereferredtoasthejoincolumns.Stepbyields
the results shown in Figure 3.13.
c. A PROJECT is performed on the results of Step b to yield a single copy of each attribute, thereby
eliminating duplicate columns. Step c yields the output shown in Figure 3.14.
Thefinaloutcomeofanaturaljoinyieldsatablethatdoesnotincludeunmatchedpairsandprovidesonlythecopies
of the matches.
Note a few crucial features of the natural join operation:
(cid:2) Ifnomatchismadebetweenthetablerows,thenewtabledoesnotincludetheunmatchedrow.Inthatcase,
neither AGENT_CODE 421 nor the customer whose last name is Smithson is included. Smithson’s
AGENT_CODE 421 does not match any entry in the AGENT table.
(cid:2) The column on which the join was made—that is, AGENT_CODE—occurs only once in the new table.
(cid:2) If the same AGENT_CODE were to occur several times in the AGENT table, a customer would be listed for
each match. For example, if the AGENT_CODE 167 were to occur three times in the AGENT table, the
customer named Rakowski, who is associated with AGENT_CODE 167, would occur three times in the

## Page 102

72 CHAPTER 3
FIGURE Natural join, Step 1: PRODUCT
3.12
FIGURE Natural join, Step 2: SELECT
3.13
FIGURE Natural join, Step 3: PROJECT resulting table. (A good AGENT table
3.14 cannot, of course, yield such a result
because it would contain unique pri-
mary key values.)
Anotherformofjoin,knownasequijoin,links
tablesonthebasisofanequalityconditionthat
comparesspecifiedcolumnsofeachtable.The
outcome of the equijoin does not eliminate
duplicate columns, and the condition or crite-
rion used to join the tables must be explicitly
defined. The equijoin takes its name from the equality comparison operator (=) used in the condition. If any other
comparison operator is used, the join is called a theta join.
Eachoftheprecedingjoinsisoftenclassifiedasaninnerjoin.Aninnerjoinisajointhatonlyreturnsmatchedrecords
from the tables that are being joined. In an outer join, the matched pairs would be retained, and any unmatched
values in the other table would be left null. It is an easy mistake to think that an outer join is the opposite of an

## Page 103

THE RELATIONAL DATABASE MODEL 73
inner join. However, it is more accurate to think of an outer join as an “inner join plus.” The outer join still returns
all of the matched records that the inner join returns, plus it returns the unmatched records from one of the tables.
More specifically, if an outer join is produced for tables CUSTOMER and AGENT, two scenarios are possible:
A left outer join yields all of the rows in the CUSTOMER table, including those that do not have a matching value
in the AGENT table. An example of such a join is shown in Figure 3.15.
Arightouterjoinyieldsalloftherows
FIGURE Left outer join in the AGENT table, including those
3.15 thatdonothavematchingvaluesinthe
CUSTOMERtable.Anexampleofsuch
a join is shown in Figure 3.16.
Generally speaking, outer joins operate
like equijoins. The outer join does not
droponecopyofthecommonattribute,
and it requires the specification of the
join condition. Figures 3.15 and 3.16
illustrate the result of outer joins after a
relationalPROJECToperationisapplied
FIGURE Right outer join
3.16 to them to manually remove the dupli-
cate column.
Outer joins are especially useful when
you are trying to determine what val-
ue(s)inrelatedtablescause(s)referential
integrity problems. Such problems are
created when foreign key values do not
match the primary key values in the
related table(s). In fact, if you are asked
to convert large spreadsheets or other
nondatabase data into relational database tables, you will discover that the outer joins save you vast amounts
of time and uncounted headaches when you encounter referential integrity errors after the conversions.
Youmaywonderwhytheouterjoinsarelabeledleftandright.Thelabelsrefertotheorderinwhichthetables
are listed in the SQL command. Chapter 8 explores such joins in more detail.
8. The DIVIDE operation uses one single-column table (e.g., column “a”) as the divisor and one 2-column table
(i.e., columns “a” and “b”) as the dividend. The tables must have a common column (e.g., column “a”). The
outputoftheDIVIDEoperationisasinglecolumnwiththevaluesofcolumn“a”fromthedividendtablerows
wherethevalueofthecommoncolumn(i.e.,column“a”)inbothtablesmatches.Figure3.17showsaDIVIDE.
FIGURE DIVIDE
3.17
DIVIDE yields

## Page 104

74 CHAPTER 3
Using the example shown in Figure 3.17, note that:
a. Table1is“divided”byTable2toproduceTable3.Tables1and2bothcontainthecolumnCODEbutdo
not share LOC.
b. To be included in the resulting Table 3, a value in the unshared column (LOC) must be associated (in the
dividing Table 2) with every value in Table 1.
c. The only value associated with both A and B is 5.
3.5 THE DATA DICTIONARY AND THE SYSTEM CATALOG
The data dictionary provides a detailed description of all tables found within the user/designer-created database.
Thus, the data dictionary contains at least all of the attribute names and characteristics for each table in the system.
In short, the data dictionary contains metadata—data about data. Using the small database presented in Figure 3.4,
you might picture its data dictionary as shown in Table 3.6.
Note
ThedatadictionaryinTable3.6isanexampleofthehumanviewoftheentities,attributes,andrelationships.
Thepurposeofthisdatadictionaryistoensurethatallmembersofdatabasedesignandimplementationteams
use the same table and attribute names and characteristics. The DBMS’s internally stored data dictionary
contains additional information about relationship types, entity and referential integrity checks and enforce-
ment,andindextypesandcomponents.Thisadditionalinformationisgeneratedduringthedatabaseimple-
mentationstage.
The data dictionary is sometimes described as “the database designer’s database” because it records the design
decisions about tables and their structures.
Like the data dictionary, the system catalog contains metadata. The system catalog can be described as a detailed
system data dictionary that describes all objects within the database, including data about table names, the table’s
creator and creation date, the number of columns in each table, the data type corresponding to each column, index
filenames,indexcreators,authorizedusers,andaccessprivileges.Becausethesystemcatalogcontainsallrequireddata
dictionaryinformation,thetermssystemcataloganddatadictionaryareoftenusedinterchangeably.Infact,current
relational database software generally provides only a system catalog, from which the designer’s data dictionary
information may be derived. The system catalog is actually a system-created database whose tables store the
user/designer-created database characteristics and contents. Therefore, the system catalog tables can be queried just
like any user/designer-created table.
Ineffect,thesystemcatalogautomaticallyproducesdatabasedocumentation.Asnewtablesareaddedtothedatabase,
that documentation also allows the RDBMS to check for and eliminate homonyms and synonyms. In general terms,
homonyms are similar-sounding words with different meanings, such as boar and bore, or identically spelled words
with different meanings, such as fair (meaning “just”) and fair (meaning “festival”). In a database context, the word
homonym indicates the use of the same attribute name to label different attributes. For example, you might use
C_NAMEtolabelacustomernameattributeinaCUSTOMERtableandalsouseC_NAMEtolabelaconsultantname
attributeinaCONSULTANTtable.Tolessenconfusion,youshouldavoiddatabasehomonyms;thedatadictionaryis
very useful in this regard.
Inadatabasecontext,asynonymistheoppositeofahomonymandindicatestheuseofdifferentnamestodescribe
thesameattribute.Forexample,carandautorefertothesameobject.Synonymsmustbeavoided.Youwilldiscover
why using synonyms is a bad idea when you work through Problem 27 at the end of this chapter.

## Page 105

yranoitciD
ataD
elpmaS
A
ELBAT
6.3
KF
KP
DECNEREFER
RO
DERIUQER
EGNAR
TAMROF
EPYT
STNETNOC
EMANETUBIRTTA
EMANELBAT
ELBAT
KF KP
Y
99999−00001
99999
)5(RAHC
edoctnuoccaremotsuC
EDOC_SUC
REMOTSUC
Y
xxxxxxxX
)02(RAHCRAV
emantsalremotsuC
EMANL_SUC
Y
xxxxxxxX
)02(RAHCRAV
emantsrifremotsuC
EMANF_SUC
X
)1(RAHC
laitiniremotsuC
LAITINI_SUC
yyyy-mmm-dd
ETAD
ecnarusniremotsuC
ETAD_WENER_SUC
etadlawener
EDOC_TNEGA
KF
999
)3(RAHC
edoctnegA
EDOC_TNEGA
KP
Y
999
)3(RAHC
edoctnegA
EDOC_TNEGA
TNEGA
Y
999
)3(RAHC
edocaeratnegA
EDOCAERA_TNEGA
Y
9999-999
)8(RAHC
rebmunenohpelettnegA
ENOHP_TNEGA
Y
xxxxxxxX
)02(RAHCRAV
emantsaltnegA
EMANL_TNEGA
Y
99.999,999,9
)2,9(REBMUN
selasetad-ot-raeytnegA
SLS_DTY_TNEGA
yekngieroF
=
KF
yekyramirP
=
KP
)sretcarahc552−1(atadhtgnelretcarahcdexiF
=
RAHC
)sretcarahc000,2−1(atadhtgnelretcarahcelbairaV
=
RAHCRAV
.secalplamicedehtgnidulcni,stigideninotpudnasecalplamicedowthtiwsrebmunyficepsotdesuera))2,9(REBMUN(atadciremuN
=
REBMUN
.epytatadYCNERRUCroYENOMafoesuehttimrepsSMBDRemoS
,oslA.atadretcarahcsaderotsyltneiciffetsomerayeht,yllacitemhtiradesutonerasedocaeraesuaceB.9−0stigidfodesopmocsyawlaerasedocaeraenohpeleT:etoN dradnatsemosotmrofnoctonodseman,dnahrehtoehtnO.)3(RAHCsadenifedsiepytatadedocaeraeht,eroferehT.stigideerhtfodesopmocsyawlaerasedocaeraeht eraatadretcarahC.semanehterotsotdesuebyamsretcarahc02otputahtgnitacidnisuht,)02(RAHCRAVsadenifederasemantsrifremotsuceht,eroferehT.htgnel
.deifitsuj-tfelsanwohs
THE RELATIONAL DATABASE MODEL 75

## Page 106

76 CHAPTER 3
3.6 RELATIONSHIPS WITHIN THE RELATIONAL DATABASE
Youalreadyknowthatrelationshipsareclassifiedasone-to-one(1:1),one-to-many(1:M),andmany-to-many(M:Nor
M:M). This section explores those relationships further to help you apply them properly when you start developing
database designs, focusing on the following points:
(cid:2) The 1:M relationship is the relational modeling ideal. Therefore, this relationship type should be the norm in
any relational database design.
(cid:2) The 1:1 relationship should be rare in any relational database design.
(cid:2) M:N relationships cannot be implemented as such in the relational model. Later in this section, you will see
how any M:N relationship can be changed into two 1:M relationships.
3.6.1 The 1:M Relationship
The 1:M relationship is the relational database norm. To see how such a relationship is modeled and implemented,
consider the PAINTER paints PAINTING example shown in Figure 3.18.
Compare the data model in Figure 3.18 with its implemen-
FIGURE The 1:M relationship between
tation in Figure 3.19.
3.18 PAINTER and PAINTING
AsyouexaminethePAINTERandPAINTINGtablecontents
in Figure 3.19, note the following features:
(cid:2) Each painting is painted by one and only one
painter, but each painter could have painted many
paintings.Notethatpainter123(GeorgetteP.Ross)
has three paintings stored in the PAINTING table.
FIGURE The implemented 1:M relationship between PAINTER and PAINTING
3.19
Table name: PAINTER
Primary key: PAINTER_NUM Database name: Ch03_Museum
Foreign key: none
Table name: PAINTING
Primary key: PAINTING_NUM
Foreign key: PAINTER_NUM
(cid:2) ThereisonlyonerowinthePAINTERtableforanygivenrowinthePAINTINGtable,buttheremaybemany
rows in the PAINTING table for any given row in the PAINTER table.
The1:Mrelationshipisfoundinanydatabaseenvironment.Studentsinatypicalcollegeoruniversitywilldiscoverthat
each COURSE can generate many CLASSes but that each CLASS refers to only one COURSE. For example, an

## Page 107

THE RELATIONAL DATABASE MODEL 77
Note
Theone-to-many(1:M)relationshipiseasilyimplementedintherelationalmodelbyputtingtheprimarykeyof
the1sideinthetableofthemanysideasaforeignkey.
AccountingIIcoursemightyieldtwoclasses:oneofferedonMonday,Wednesday,andFriday(MWF)from10:00a.m.
to 10:50 a.m. and one offered on Thursday (Th) from 6:00 p.m. to 8:40 p.m. Therefore, the 1:M relationship
between COURSE and CLASS might be described this way:
(cid:2) Each COURSE can have many CLASSes, but each CLASS references only one COURSE.
(cid:2) TherewillbeonlyonerowintheCOURSEtableforanygivenrowintheCLASStable,buttherecanbemany
rows in the CLASS table for any given row in the COURSE table.
Figure 3.20 maps the ERM (entity relationship model) for the 1:M relationship between COURSE and CLASS.
The 1:M relationship between COURSE and CLASS is
FIGURE The 1:M relationship between
further illustrated in Figure 3.21.
3.20 COURSE and CLASS
FIGURE The implemented 1:M relationship between COURSE and CLASS
3.21
Table name: COURSE
Primary key: CRS_CODE Database name: Ch03_TinyCollege
Foreign key: none
Table name: CLASS
Primary key: CLASS_CODE
Foreign key: CRS_CODE

## Page 108

78 CHAPTER 3
UsingFigure3.21,takeaminutetoreviewsomeimportantterminology.NotethatCLASS_CODEintheCLASStable
uniquely identifies each row. Therefore, CLASS_CODE has been chosen to be the primary key. However, the
combinationCRS_CODEandCLASS_SECTIONwillalsouniquelyidentifyeachrowintheclasstable.Inotherwords,
thecompositekeycomposedofCRS_CODEandCLASS_SECTIONisacandidatekey.Anycandidatekeymusthave
the not null and unique constraints enforced. (You will see how this is done when you learn SQL in Chapter 7.)
Forexample,noteinFigure3.19thatthePAINTERtable’sprimarykey,PAINTER_NUM,isincludedinthePAINTING
table as a foreign key. Similarly, in Figure 3.21, the COURSE table’s primary key, CRS_CODE, is included in the
CLASS table as a foreign key.
3.6.2 The 1:1 Relationship
As the 1:1 label implies, in this relationship, one entity can be related to only one other entity, and vice versa. For
example,onedepartmentchair—aprofessor—canchaironlyonedepartment,andonedepartmentcanhaveonlyone
departmentchair.TheentitiesPROFESSORandDEPARTMENTthusexhibita1:1relationship.(Youmightarguethat
notallprofessorschairadepartmentandprofessorscannotberequiredtochairadepartment.Thatis,therelationship
between the two entities is optional. However, at this stage of the discussion, you should focus your attention on the
basic 1:1 relationship. Optional relationships will be addressed in Chapter 4.) The basic 1:1 relationship is modeled
in Figure 3.22, and its implementation is shown in Figure 3.23.
As you examine the tables in Figure 3.23, note that there
FIGURE The 1:1 relationship between
are several important features:
3.22 PROFESSOR and DEPARTMENT
(cid:2) EachprofessorisaTinyCollegeemployee.Therefore,
theprofessoridentificationisthroughtheEMP_NUM.
(However, note that not all employees are
professors—there’sanotheroptionalrelationship.)
(cid:2) The 1:1 PROFESSOR chairs DEPARTMENT rela-
tionship is implemented by having the EMP_NUM
foreign key in the DEPARTMENT table. Note that
the1:1relationshipistreatedasaspecialcaseofthe
1:M relationship in which the “many” side is restricted to a single occurrence. In this case, DEPARTMENT
contains the EMP_NUM as a foreign key to indicate that it is the department that has a chair.
(cid:2) Also note that the PROFESSOR table contains the DEPT_CODE foreign key to implement the 1:M
DEPARTMENTemploysPROFESSORrelationship.Thisisagoodexampleofhowtwoentitiescanparticipate
in two (or even more) relationships simultaneously.
The preceding “PROFESSOR chairs DEPARTMENT” example illustrates a proper 1:1 relationship. In fact, the use
of a 1:1 relationship ensures that two entity sets are not placed in the same table when they should not be.
However,theexistenceofa1:1relationshipsometimesmeansthattheentitycomponentswerenotdefinedproperly.
It could indicate that the two entities actually belong in the same table!
As rare as 1:1 relationships should be, certain conditions absolutely require their use. In Chapter 5, Advanced Data
Modeling, we will explore a concept called a generalization hierarchy, which is a powerful tool for improving our
databasedesignsunderspecificconditionstoavoidaproliferationofnulls.Oneofthecharacteristicsofgeneralization
hierarchies is that they are implemented as 1:1 relationships.
3.6.3 The M:N Relationship
Amany-to-many(M:N)relationshipisnotsupporteddirectlyintherelationalenvironment.However,M:Nrelationships
can be implemented by creating a new entity in 1:M relationships with the original entities.

## Page 109

THE RELATIONAL DATABASE MODEL 79
FIGURE The implemented 1:1 relationship between PROFESSOR and DEPARTMENT
3.23
Table name: PROFESSOR Database name: Ch03_TinyCollege
Primary key: EMP_NUM
Foreign key: DEPT_CODE
The 1:M DEPARTMENT employs PROFESSOR relationship is implemented through
the placement of the DEPT_CODE foreign key in the PROFESSOR table.
The 1:1 PROFESSOR chairs DEPARTMENT relationship
Table name: DEPARTMENT is implemented through the placement of the
Primary key: DEPT_CODE EMP_NUM foreign key in the DEPARTMENT table.
Foreign key: EMP_NUM
O n l i n e C o n t e n t
IfyouopentheCh03_TinyCollegedatabaseinthePremiumWebsite,you’llseethattheSTUDENTandCLASS
entitiesstillusePROF_NUMastheirforeignkey.PROF_NUMandEMP_NUMarelabelsforthesameattribute,
whichisanexampleoftheuseofsynonyms;thatis,differentnamesforthesameattribute.Thesesynonymswill
beeliminatedinfuturechaptersastheTinyCollegedatabasecontinuestobeimproved.

## Page 110

80 CHAPTER 3
O n l i n e C o n t e n t
IfyoulookattheCh03_AviaCodatabaseinthePremiumWebsite,youwillseetheimplementationofthe1:1
PILOTtoEMPLOYEErelationship.Thisrelationshipisbasedonaconceptknownas“generalizationhierarchy,”
whichyouwilllearnaboutinChapter5.
To explore the many-to-many (M:N) relationship, consider a rather typical college environment in which each
STUDENTcantakemanyCLASSes,andeachCLASScancontainmanySTUDENTs.TheERmodelinFigure3.24
shows this M:N relationship.
Note the features of the ERM in Figure 3.24.
FIGURE The ERM’s M:N relationship
(cid:2) EachCLASScanhavemanySTUDENTs,andeach
3.24 between STUDENT and CLASS
STUDENT can take many CLASSes.
(cid:2) TherecanbemanyrowsintheCLASStableforany
given row in the STUDENT table, and there can be
manyrowsintheSTUDENTtableforanygivenrow
in the CLASS table.
To examine the M:N relationship more closely, imagine a
small college with two students, each of whom takes three
classes. Table 3.7 shows the enrollment data for the two
students.
TABLE Sample Student Enrollment Data
3.7
STUDENT'SLASTNAME SELECTEDCLASSES
Bowser Accounting1,ACCT-211,code10014
IntrotoMicrocomputing,CIS-220,code10018
IntrotoStatistics,QM-261,code10021
Smithson Accounting1,ACCT-211,code10014
IntrotoMicrocomputing,CIS-220,code10018
IntrotoStatistics,QM-261,code10021
GivensuchadatarelationshipandthesampledatainTable3.7,youcouldwronglyassumethatyoucouldimplement
this M:N relationship by simply adding a foreign key in the many side of the relationship that points to the primary
key of the related table, as shown in Figure 3.25.
However, the M:N relationship should not be implemented as shown in Figure 3.25 for two good reasons:
(cid:2) Thetablescreatemanyredundancies.Forexample,notethattheSTU_NUMvaluesoccurmanytimesinthe
STUDENT table. In a real-world situation, additional student attributes such as address, classification, major,
andhomephonewouldalsobecontainedintheSTUDENTtable,andeachofthoseattributevalueswouldbe
repeated in each of the records shown here. Similarly, the CLASS table contains many duplications: each
student taking the class generates a CLASS record. The problem would be even worse if the CLASS table
included such attributes as credit hours and course description. Those redundancies lead to the anomalies
discussed in Chapter 1.
(cid:2) Given the structure and contents of the two tables, the relational operations become very complex and are
likely to lead to system efficiency errors and output errors.

## Page 111

THE RELATIONAL DATABASE MODEL 81
FIGURE The wrong implementation of the M:N relationship between STUDENT and CLASS
3.25
Table name: STUDENT
Primary key: STU_NUM Database name: Ch03_CollegeTry
Foreign key: none
Table name: CLASS
Primary key: CLASS_CODE
Foreign key: STU_NUM
Fortunately, the problems inherent in the many-to-many (M:N) relationship can easily be avoided by creating a
compositeentity(alsoreferredtoasabridgeentityoranassociativeentity).Becausesuchatableisusedtolink
the tables that were originally related in an M:N relationship, the composite entity structure includes—as foreign
keys—atleasttheprimarykeysofthetablesthataretobelinked.Thedatabasedesignerhastwomainoptionswhen
defining a composite table’s primary key: use the combination of those foreign keys or create a new primary key.
RememberthateachentityintheERMisrepresentedbyatable.Therefore,youcancreatethecompositeENROLL
tableshowninFigure3.26tolinkthetablesCLASSandSTUDENT.Inthisexample,theENROLLtable’sprimarykey
is the combination of its foreign keys CLASS_CODE and STU_NUM. But the designer could have decided to create
asingle-attributenewprimarykeysuchasENROLL_LINE,usingadifferentlinevaluetoidentifyeachENROLLtable
rowuniquely.(MicrosoftAccessusersmightusetheAutonumberdatatypetogeneratesuchlinevaluesautomatically.)

## Page 112

82 CHAPTER 3
FIGURE Converting the M:N relationship into two 1:M relationships
3.26
Table name: STUDENT
Primary key: STU_NUM Database name: Ch03_CollegeTry2
Foreign key: none
Table name: ENROLL
Primary key: CLASS_CODE + STU_NUM
Foreign key: CLASS_CODE, STU_NUM
Table name: CLASS
Primary key: CLASS_CODE
Foreign key: CRS_CODE
BecausetheENROLLtableinFigure3.26linkstwotables,STUDENTandCLASS,itisalsocalledalinkingtable.
In other words, a linking table is the implementation of a composite entity.
Note
Inadditiontothelinkingattributes,thecompositeENROLLtablecanalsocontainsuchrelevantattributesasthe
gradeearnedinthecourse.Infact,acompositetablecancontainanynumberofattributesthatthedesigner
wants to track. Keep in mind that the composite entity, although it is implemented as an actual table, is
conceptually a logical entity that was created as a means to an end: to eliminate the potential for multiple
redundanciesintheoriginalM:Nrelationship.
The ENROLL table shown in Figure 3.26 yields the required M:N to 1:M conversion. Observe that the composite
entity represented by the ENROLL table must contain at least the primary keys of the CLASS and STUDENT tables
(CLASS_CODE and STU_NUM, respectively) for which it serves as a connector. Also note that the STUDENT and
CLASStablesnowcontainonlyonerowperentity.TheENROLLtablecontainsmultipleoccurrencesoftheforeign
key values, but those controlled redundancies are incapable of producing anomalies as long as referential integrity is
enforced. Additional attributes may be assigned as needed. In this case, ENROLL_GRADE is selected to satisfy a
reporting requirement. Also note that the ENROLL table’s primary key consists of the two attributes CLASS_CODE
andSTU_NUMbecauseboththeclasscodeandthestudentnumberareneededtodefineaparticularstudent’sgrade.
Naturally, the conversion is reflected in the ERM, too. The revised relationship is shown in Figure 3.27.
As you examine Figure 3.27, note that the composite entity named ENROLL represents the linking table between
STUDENT and CLASS.
The 1:M relationship between COURSE and CLASS was first illustrated in Figure 3.20 and Figure 3.21. You can
increase the amount of available information even as you control the database’s redundancies. Thus, Figure 3.28

## Page 113

THE RELATIONAL DATABASE MODEL 83
shows the expanded ERM, including the 1:M relationship
FIGURE Changing the M:N relationship
3.27 to two 1:M relationships betweenCOURSEandCLASSshowninFigure3.20.Note
that the model is able to handle multiple sections of a
CLASS while controlling redundancies by making sure that
all of the COURSE data common to each CLASS are kept
in the COURSE table.
The relational diagram that corresponds to the ERM in
Figure 3.28 is shown in Figure 3.29.
TheERMwillbeexaminedingreaterdetailinChapter4to
showyouhowitisusedtodesignmorecomplexdatabases.
TheERMwillalsobeusedasthebasisforthedevelopment
FIGURE The expanded entity
andimplementationofarealisticdatabasedesigninAppen-
3.28 relationship model
dixes B and C (see the Premium Website) for a university
computer lab.
FIGURE The relational diagram for the Ch03_TinyCollege database
3.29

## Page 114

84 CHAPTER 3
3.7 DATA REDUNDANCY REVISITED
InChapter1youlearnedthatdataredundancyleadstodataanomalies.Thoseanomaliescandestroytheeffectiveness
ofthedatabase.Youalsolearnedthattherelationaldatabasemakesitpossibletocontroldataredundanciesbyusing
common attributes that are shared by tables, called foreign keys.
The proper use of foreign keys is crucial to controlling data redundancy. Although the use of foreign keys does not
totally eliminate data redundancies, because the foreign key values can be repeated many times, the proper use of
foreign keys minimizes data redundancies, thus minimizing the chance that destructive data anomalies will develop.
Note
Therealtestofredundancyisnothowmanycopiesofagivenattributearestored,butwhethertheelimination
ofanattributewilleliminateinformation.Therefore,ifyoudeleteanattributeandtheoriginalinformationcan
stillbegeneratedthroughrelationalalgebra,theinclusionofthatattributewouldberedundant.Giventhatview
ofredundancy,properforeignkeysareclearlynotredundantinspiteoftheirmultipleoccurrencesinatable.
However,evenwhenyouusethislessrestrictiveviewofredundancy,keepinmindthatcontrolledredundancies
areoftendesignedaspartofthesystemtoensuretransactionspeedand/orinformationrequirements.Exclusive
relianceonrelationalalgebratoproducerequiredinformationmayleadtoelegantdesignsthatfailthetestof
practicality.
You will learn in Chapter 4 that database designers must reconcile three often contradictory requirements: design
elegance,processingspeed,andinformationrequirements.AndyouwilllearninChapter13,BusinessIntelligenceand
DataWarehouses,thatproperdatawarehousingdesignrequirescarefullydefinedandcontrolleddataredundanciesto
function properly. Regardless of how you describe data redundancies, the potential for damage is limited by proper
implementation and careful control.
As important as data redundancy control is, there are times when the level of data redundancy must actually be
increasedtomakethedatabaseservecrucialinformationpurposes.YouwilllearnaboutsuchredundanciesinChapter
13. There are also times when data redundancies seem to exist to preserve the historical accuracy of the data. For
example, consider a small invoicing system. The system includes the CUSTOMER, who may buy one or more
PRODUCTs,thusgeneratinganINVOICE.Becauseacustomermaybuymorethanoneproductatatime,aninvoice

## Page 115

THE RELATIONAL DATABASE MODEL 85
maycontainseveralinvoiceLINEs,eachprovidingdetailsaboutthepurchasedproduct.ThePRODUCTtableshould
containtheproductpricetoprovideaconsistentpricinginputforeachproductthatappearsontheinvoice.Thetables
that are part of such a system are shown in Figure 3.30. The system’s relational diagram is shown in Figure 3.31.
FIGURE A small invoicing system
3.30
Table name: CUSTOMER Database name: Ch03_SaleCo
Primary key: CUS_CODE
Foreign key: none
Table name: INVOICE Table name: LINE
Primary key: INV_NUMBER Primary key: INV_NUMBER + LINE_NUMBER
Foreign key: CUS_CODE Foreign keys: INV_NUMBER, PROD_CODE
Table name: PRODUCT
Primary key: PROD_CODE
Foreign key: none
FIGURE The relational diagram for the invoicing system
3.31

## Page 116

86 CHAPTER 3
AsyouexaminethetablesintheinvoicingsysteminFigure3.30andtherelationshipsdepictedinFigure3.31,note
thatyoucankeeptrackoftypicalsalesinformation.Forexample,bytracingtherelationshipsamongthefourtables,
youdiscoverthatcustomer10014(MyronOrlando)boughttwoitemsonMarch8,2010,thatwerewrittentoinvoice
number 1001: one Houselite chain saw with a 16-inch bar and three rat-tail files. (Note: Trace the CUS_CODE
number 10014 in the CUSTOMER table to the matching CUS_CODE value in the INVOICE table. Next, take the
INV_NUMBER1001andtraceittothefirsttworowsintheLINEtable.Finally,matchthetwoPROD_CODEvalues
in LINE with the PROD_CODE values in PRODUCT.) Application software will be used to write the correct bill by
multiplying each invoice line item’s LINE_UNITS by its LINE_PRICE, adding the results, applying appropriate taxes,
etc.Later,otherapplicationsoftwaremightusethesametechniquetowritesalesreportsthattrackandcomparesales
by week, month, or year.
As you examine the sales transactions in Figure 3.30, you might reasonably suppose that the product price billed to
thecustomerisderivedfromthePRODUCTtablebecausethat’swheretheproductdataarestored.Butwhydoesthat
sameproductpriceoccuragainintheLINEtable?Isn’tthatadataredundancy?Itcertainlyappearstobe.Butthis
time,theapparentredundancyiscrucialtothesystem’ssuccess.CopyingtheproductpricefromthePRODUCTtable
totheLINEtablemaintainsthehistoricalaccuracyofthetransactions.Suppose,forinstance,thatyoufailtowrite
theLINE_PRICEintheLINEtableandthatyouusethePROD_PRICEfromthePRODUCTtabletocalculatethesales
revenue.NowsupposethatthePRODUCTtable’sPROD_PRICEchanges,aspricesfrequentlydo.Thispricechange
willbeproperlyreflectedinallsubsequentsalesrevenuecalculations.However,thecalculationsofpastsalesrevenues
willalsoreflectthenewproductprice,whichwasnotineffectwhenthetransactiontookplace!Asaresult,therevenue
calculations for all past transactions will be incorrect, thus eliminating the possibility of making proper sales
comparisonsovertime.Ontheotherhand,ifthepricedataarecopiedfromthePRODUCTtableandstoredwiththe
transactionintheLINEtable,thatpricewillalwaysaccuratelyreflectthetransactionthattookplaceatthattime.You
will discover that such planned “redundancies” are common in good database design.
Finally,youmightwonderwhytheLINE_NUMBERattributewasusedintheLINEtableinFigure3.30.Wouldn’tthe
combination of INV_NUMBER and PROD_CODE be a sufficient composite primary key—and, therefore, isn’t the
LINE_NUMBERredundant?Yes,theLINE_NUMBERisredundant,butthisredundancyisquitecommonpracticeon
invoicing software that typically generates such line numbers automatically. In this case, the redundancy is not
necessary. But given its automatic generation, the redundancy is not a source of anomalies. The inclusion of
LINE_NUMBER also adds another benefit: the order of the retrieved invoicing data will always match the order in
whichthedatawereentered.Ifproductcodesareusedaspartoftheprimarykey,indexingwillarrangethoseproduct
codes as soon as the invoice is completed and the data are stored. You can imagine the potential confusion when a
customer calls and says, “The second item on my invoice has an incorrect price” and you are looking at an invoice
whose lines show a different order from those on the customer’s copy!
3.8 INDEXES
Supposeyouwanttolocateaparticularbookinalibrary.Doesitmakesensetolookthrougheverybookinthelibrary
until you find the one you want? Of course not; you use the library’s catalog, which is indexed by title, topic, and
author.Theindex(ineitheramanualoracomputersystem)pointsyoutothebook’slocation,therebymakingretrieval
of the book a quick and simple matter. An index is an orderly arrangement used to logically access rows in a table.
Orsupposeyouwanttofindatopic,suchas“ERmodel,”inthisbook.Doesitmakesensetoreadthrougheverypage
untilyoustumbleacrossthetopic?Ofcoursenot;itismuchsimplertogotothebook’sindex,lookupthephraseER
model,andreadthepagereferencesthatpointyoutotheappropriatepage(s).Ineachcase,anindexisusedtolocate
a needed item quickly.
Indexes in the relational database environment work like the indexes described in the preceding paragraphs. From a
conceptualpointofview,anindexiscomposedofanindexkeyandasetofpointers.Theindexkeyis,ineffect,the

## Page 117

THE RELATIONAL DATABASE MODEL 87
index’sreferencepoint.Moreformally,anindexisanorderedarrangementofkeysandpointers.Eachkeypointsto
the location of the data identified by the key.
For example, suppose you want to look up all of the paintings created by a given painter in the Ch03_Museum
database in Figure 3.19. Without an index, you must read each row in the PAINTING table and see if the
PAINTER_NUM matches the requested painter. However, if you index the PAINTER table and use the index key
PAINTER_NUM, you merely need to look up the appropriate PAINTER_NUM in the index and find the matching
pointers. Conceptually speaking, the index would resemble the presentation depicted in Figure 3.32.
FIGURE Components of an index
3.32
Painting Table Index
Painting Table
123 1, 2, 4
126 3, 5
PAINTER_NUM
(index key)
Pointers to the
PAINTING
table rows
As you examine Figure 3.32, note that the first PAINTER_NUM index key value (123) is found in records 1, 2,
and 4 of the PAINTING table. The second PAINTER_NUM index key value (126) is found in records 3 and 5 of the
PAINTING table.
DBMSs use indexes for many different purposes. You just learned that an index can be used to retrieve data more
efficiently. But indexes can also be used by a DBMS to retrieve data ordered by a specific attribute or attributes. For
example,creatinganindexonacustomer’slastnamewillallowyoutoretrievethecustomerdataalphabeticallybythe
customer’s last name. Also, an index key can be composed of one or more attributes. For example, in Figure 3.30,
you can create an index on VEND_CODE and PROD_CODE to retrieve all rows in the PRODUCT table ordered by
vendor, and within vendor, ordered by product.
IndexesplayanimportantroleinDBMSsfortheimplementationofprimarykeys.Whenyoudefineatable’sprimary
key,theDBMSautomaticallycreatesauniqueindexontheprimarykeycolumn(s)youdeclared.Forexample,inFigure
3.30,whenyoudeclareCUS_CODEtobetheprimarykeyoftheCUSTOMERtable,theDBMSautomaticallycreates
a unique index on that attribute. A unique index, as its name implies, is an index in which the index key can have
only one pointer value (row) associated with it. (The index in Figure 3.32 is not a unique index because the
PAINTER_NUM has multiple pointer values associated with it. For example, painter number 123 points to three
rows—1, 2, and 4—in the PAINTING table.)
A table can have many indexes, but each index is associated with only one table. The index key can have multiple
attributes (composite index). Creating an index is easy. You will learn in Chapter 7 that a simple SQL command
produces any required index.

## Page 118

88 CHAPTER 3
3.9 CODD’S RELATIONAL DATABASE RULES
In 1985, Dr. E. F. Codd published a list of 12 rules to define a relational database system.2 The reason Dr. Codd
published the list was his concern that many vendors were marketing products as “relational” even though those
productsdidnotmeetminimumrelationalstandards.Dr.Codd’slist,showninTable3.8,servesasaframeofreference
for what a truly relational database should be. Bear in mind that even the dominant database vendors do not fully
support all 12 rules.
TABLE Dr. Codd’s 12 Relational Database Rules
3.8
RULE RULENAME DESCRIPTION
1 Information Allinformationinarelationaldatabasemustbelogicallyrep-
resentedascolumnvaluesinrowswithintables.
2 GuaranteedAccess Everyvalueinatableisguaranteedtobeaccessiblethrougha
combinationoftablename,primarykeyvalue,andcolumn
name.
3 SystematicTreatmentofNulls Nullsmustberepresentedandtreatedinasystematicway,
independentofdatatype.
4 DynamicOnlineCatalogBasedon Themetadatamustbestoredandmanagedasordinarydata,
theRelationalModel thatis,intableswithinthedatabase.Suchdatamustbeavail-
abletoauthorizedusersusingthestandarddatabaserela-
tionallanguage.
5 ComprehensiveDataSublanguage Therelationaldatabasemaysupportmanylanguages.How-
ever,itmustsupportonewell-defined,declarativelanguage
withsupportfordatadefinition,viewdefinition,datamanipu-
lation(interactiveandbyprogram),integrityconstraints,
authorization,andtransactionmanagement(begin,commit,
androllback).
6 ViewUpdating Anyviewthatistheoreticallyupdatablemustbeupdatable
throughthesystem.
7 High-LevelInsert,Update,andDelete Thedatabasemustsupportset-levelinserts,updates,and
deletes.
8 PhysicalDataIndependence Applicationprogramsandadhocfacilitiesarelogicallyunaf-
fectedwhenphysicalaccessmethodsorstoragestructuresare
changed.
9 LogicalDataIndependence Applicationprogramsandadhocfacilitiesarelogicallyunaf-
fectedwhenchangesaremadetothetablestructuresthat
preservetheoriginaltablevalues(changingorderofcolumns
orinsertingcolumns).
10 IntegrityIndependence Allrelationalintegrityconstraintsmustbedefinableinthe
relationallanguageandstoredinthesystemcatalog,notat
theapplicationlevel.
11 DistributionIndependence Theendusersandapplicationprogramsareunawareand
unaffectedbythedatalocation(distributedvs.local
databases).
12 Nonsubversion Ifthesystemsupportslow-levelaccesstothedata,theremust
notbeawaytobypasstheintegrityrulesofthedatabase.
RuleZero Allprecedingrulesarebasedonthenotionthatinorderfora
databasetobeconsideredrelational,itmustuseitsrelational
facilitiesexclusivelytomanagethedatabase.
2Codd,E.,“IsYourDBMSReallyRelational?”and“DoesYourDBMSRunbytheRules?”Computerworld,October14andOctober21,1985.

## Page 119

THE RELATIONAL DATABASE MODEL 89
S u m m a r y
◗
Tablesarethebasicbuildingblocksofarelationaldatabase.Agroupingofrelatedentities,knownasanentityset,
is stored in a table. Conceptually speaking, the relational table is composed of intersecting rows (tuples) and
columns. Each row represents a single entity, and each column represents the characteristics (attributes) of the
entities.
◗
Keys are central to the use of relational tables. Keys define functional dependencies; that is, other attributes are
dependentonthekeyandcan,therefore,befoundifthekeyvalueisknown.Akeycanbeclassifiedasasuperkey,
a candidate key, a primary key, a secondary key, or a foreign key.
◗
Eachtablerowmusthaveaprimarykey.Theprimarykeyisanattributeoracombinationofattributesthatuniquely
identifiesallremainingattributesfoundinanygivenrow.Becauseaprimarykeymustbeunique,nonullvaluesare
allowed if entity integrity is to be maintained.
◗
Althoughthetablesareindependent,theycanbelinkedbycommonattributes.Thus,theprimarykeyofonetable
can appear as the foreign key in another table to which it is linked. Referential integrity dictates that the foreign
key must contain values that match the primary key in the related table or must contain nulls.
◗
The relational model supports relational algebra functions: SELECT, PROJECT, JOIN, INTERSECT, UNION,
DIFFERENCE, PRODUCT, and DIVIDE. A relational database performs much of the data manipulation work
behind the scenes. For example, when you create a database, the RDBMS automatically produces a structure to
house a data dictionary for your database. Each time you create a new table within the database, the RDBMS
updates the data dictionary, thereby providing the database documentation.
◗
Once you know the relational database basics, you can concentrate on design. Good design begins by identifying
appropriate entities and their attributes and then the relationships among the entities. Those relationships (1:1,
1:M,andM:N)canberepresentedusingERDs.TheuseofERDsallowsyoutocreateandevaluatesimplelogical
design. The 1:M relationship is most easily incorporated in a good design; you just have to make sure that the
primary key of the “1” is included in the table of the “many.”
K e y T e r ms
associative entity, 81 functional dependence, 62 referential integrity, 66
attribute domain, 60 homonym, 74 relational algebra, 68
bridge entity, 81 index, 86 relational schema, 65
candidate key, 64 index key, 86 right outer join, 73
closure, 68 inner join, 72 secondary key, 66
composite entity, 81 join column(s), 71 set theory, 59
composite key, 63 key, 62 superkey, 63
data dictionary, 74 key attribute, 63 synonym, 74
determination, 62 left outer join, 73 system catalog, 74
domain, 61 linking table, 82 theta join, 72
entity integrity, 64 natural join, 71 tuple, 60
equijoin, 72 null, 64 union-compatible, 69
flags, 68 outer join, 72 unique index, 87
foreign key (FK), 65 predicate logic, 59
full functional dependence, 63 primary key (PK), 61

## Page 120

90 CHAPTER 3
O n l i n e C o n t e n t
AnswerstoselectedReviewQuestionsandProblemsforthischapterarecontainedinthePremiumWebsitefor
thisbook.
R e v ie w Q u e st i o ns
1. What is the difference between a database and a table?
2. What does it mean to say that a database displays both entity integrity and referential integrity?
3. Why are entity integrity and referential integrity important in a database?
4. What are the requirements that two relations must satisfy in order to be considered union-compatible?
5. Which relational algebra operators can be applied to a pair of tables that are not union-compatible?
6. Explain why the data dictionary is sometimes called “the database designer’s database.”
7. Adatabaseusermanuallynotesthat“Thefilecontainstwohundredrecords,eachrecordcontainingninefields.”
Use appropriate relational database terminology to “translate” that statement.
O n l i n e C o n t e n t
AllofthedatabasesusedinthequestionsandproblemsarefoundinthePremiumWebsiteforthisbook.The
databasenamesusedinthefoldermatchthedatabasenamesusedinthefigures.Forexample,thesourceofthe
tablesshowninFigureQ3.5istheCh03_CollegeQuedatabase.
Use Figure Q3.8 to answer Questions 8–10.
8. Using the STUDENT and PROFESSOR tables, illus-
FIGURE The Ch03_CollegeQue tratethedifferencebetweenanaturaljoin,anequijoin,
Q3.8 database tables and an outer join.
9. Create the basic ERD for the database shown in
Figure Q3.8.
Database name: Ch03_CollegeQue
Table name: STUDENT 10. Create the relational diagram for the database shown
in Figure Q3.8.
Use Figure Q3.11 to answer Questions 11–13.
11. Create the table that results from applying a
UNION relational operator to the tables shown in
Figure Q3.11.
Table name: PROFESSOR 12. Create the table that results from applying an
INTERSECTrelationaloperatortothetablesshownin
Figure Q3.11.
13. UsingthetablesinFigureQ3.11,createthetablethat
results from MACHINE DIFFERENCE BOOTH.
14. Suppose you have the ERM shown in Figure Q3.14.
How would you convert this model into an ERM that
displaysonly1:Mrelationships?(Makesureyoucreate
the revised ERM.)

## Page 121

THE RELATIONAL DATABASE MODEL 91
FIGURE The Ch03_VendingCo database tables
Q3.11
Database name: Ch03_VendingCo
Table name: BOOTH Table name: MACHINE
FIGURE The Crow’s Foot ERM for Question 14
Q3.14
15. What are homonyms and synonyms, and why should they be avoided in database design?
16. How would you implement a l:M relationship in a database composed of two tables? Give an example.
17. Identify and describe the components of the table shown in Figure Q3.17, using correct terminology. Use your
knowledge of naming conventions to identify the table’s probable foreign key(s).
FIGURE The Ch03_NoComp database EMPLOYEE table
Q3.17
Table name: EMPLOYEE Database name: Ch03_NoComp
Use the database shown in Figure Q3.18 to answer Questions 18–23.
18. Identify the primary keys.
19. Identify the foreign keys.
20. Create the ERM.

## Page 122

92 CHAPTER 3
21. Create the relational diagram to show the relationship
FIGURE The Ch03_Theater database
Q3.18 tables between DIRECTOR and PLAY.
22. Suppose you wanted quick lookup capability to get a
listing of all plays directed by a given director. Which
Database name: Ch03_Theater
tablewouldbethebasisfortheINDEXtable,andwhat
Table name: DIRECTOR
would be the index key?
23. WhatwouldbetheconceptualviewoftheINDEXtable
that is described in Question 22? Depict the contents
of the conceptual INDEX table.
Table name: PLAY
P r o b le m s
Use the database shown in Figure P3.1 to answer Problems 1−9.
1. Foreachtable,identifytheprimarykeyandtheforeignkey(s).Ifatabledoesnothaveaforeignkey,writeNone
in the space provided.
TABLE PRIMARYKEY FOREIGNKEY(S)
EMPLOYEE
STORE
REGION
2. Do the tables exhibit entity integrity? Answer yes or no, and then explain your answer.
TABLE ENTITYINTEGRITY EXPLANATION
EMPLOYEE
STORE
REGION
3. Do the tables exhibit referential integrity? Answer yes or no, and then explain your answer. Write NA (Not
Applicable) if the table does not have a foreign key.
TABLE REFERENTIALINTEGRITY FOREIGNKEY(S)
EMPLOYEE
STORE
REGION
4. Describe the type(s) of relationship(s) between STORE and REGION.
5. Create the ERD to show the relationship between STORE and REGION.
6. Create the relational diagram to show the relationship between STORE and REGION.

## Page 123

THE RELATIONAL DATABASE MODEL 93
FIGURE The Ch03_StoreCo database tables
P3.1
Table name: EMPLOYEE Database name: Ch03_StoreCo
Table name: STORE
Table name: REGION
7. Describe the type(s) of relationship(s) between EMPLOYEE and STORE. (Hint: Each store employs many
employees, one of whom manages the store.)
8. Create the ERD to show the relationships among EMPLOYEE, STORE, and REGION.
9. Create the relational diagram to show the relationships among EMPLOYEE, STORE, and REGION.
UsethedatabaseshowninFigureP3.10toworkProblems10−16.Notethatthedatabaseiscomposedoffourtables
that reflect these relationships:
(cid:2) An EMPLOYEE has only one JOB_CODE, but a JOB_CODE can be held by many EMPLOYEEs.
(cid:2) An EMPLOYEE can participate in many PLANs, and any PLAN can be assigned to many EMPLOYEEs.
Note also that the M:N relationship has been broken down into two 1:M relationships for which the BENEFIT table
serves as the composite or bridge entity.

## Page 124

94 CHAPTER 3
FIGURE The Ch03_BeneCo database tables
P3.10
Database name: Ch03_BeneCo
Table name: EMPLOYEE Table name: BENEFIT
Table name: JOB Table name: PLAN
10. Foreachtableinthedatabase,identifytheprimarykeyandtheforeignkey(s).Ifatabledoesnothaveaforeign
key, write None in the space provided.
TABLE PRIMARYKEY FOREIGNKEY(S)
EMPLOYEE
BENEFIT
JOB
PLAN
11. Create the ERD to show the relationship between EMPLOYEE and JOB.
12. Create the relational diagram to show the relationship between EMPLOYEE and JOB.
13. Do the tables exhibit entity integrity? Answer yes or no, and then explain your answer.
TABLE ENTITYINTEGRITY EXPLANATION
EMPLOYEE
BENEFIT
JOB
PLAN
14. Do the tables exhibit referential integrity? Answer yes or no, and then explain your answer. Write NA (Not
Applicable) if the table does not have a foreign key.
TABLE REFERENTIALINTEGRITY EXPLANATION
EMPLOYEE
BENEFIT
JOB
PLAN
15. Create the ERD to show the relationships among EMPLOYEE, BENEFIT, JOB, and PLAN.

## Page 125

THE RELATIONAL DATABASE MODEL 95
16. Create the relational diagram to show the relationships among EMPLOYEE, BENEFIT, JOB, and PLAN.
Use the database shown in Figure P3.17 to answer Problems 17−23.
FIGURE The Ch03_TransCo database tables
P3.17
Table name: TRUCK Database name: Ch03_TransCo
Primary key: TRUCK_NUM
Foreign key: BASE_CODE, TYPE_CODE
Table name: BASE
Primary key: BASE_CODE
Foreign key: none
Table name: TYPE
Primary key: TYPE_CODE
Foreign key: none
17. Foreachtable,identifytheprimarykeyandtheforeignkey(s).Ifatabledoesnothaveaforeignkey,writeNone
in the space provided.
TABLE PRIMARYKEY FOREIGNKEY(S)
TRUCK
BASE
TYPE
18. Do the tables exhibit entity integrity? Answer yes or no, and then explain your answer.
TABLE ENTITYINTEGRITY EXPLANATION
TRUCK
BASE
TYPE
19. Do the tables exhibit referential integrity? Answer yes or no, and then explain your answer. Write NA (Not
Applicable) if the table does not have a foreign key.

## Page 126

96 CHAPTER 3
TABLE REFERENTIALINTEGRITY EXPLANATION
TRUCK
BASE
TYPE
20. Identify the TRUCK table’s candidate key(s).
21. For each table, identify a superkey and a secondary key.
TABLE SUPERKEY SECONDARYKEY
TRUCK
BASE
TYPE
22. Create the ERD for this database.
23. Create the relational diagram for this database.
Use the database shown in Figure P3.24 to answer Problems 24−31. ROBCOR is an aircraft charter company that
supplieson-demandcharterflightservicesusingafleetoffouraircraft.Aircraftareidentifiedbyauniqueregistration
number. Therefore, the aircraft registration number is an appropriate primary key for the AIRCRAFT table.
FIGURE The Ch03_AviaCo database tables
P3.24
Table name: CHARTER Database name: Ch03_AviaCo
The destinations are indicated by standard three-letter airport codes. For example,
STL = St. Louis, MO ATL = Atlanta, GA BNA = Nashville, TN
Table name: AIRCRAFT AC-TTAF = Aircraft total time, airframe (hours)
AC-TTEL = Total time, left engine (hours)
AC_TTER = Total time, right engine (hours)
In a fully developed system, such attribute values
would be updated by application software when the
CHARTER table entries were posted.
Table name: MODEL
Customers are charged per round-trip mile, using the MOD_CHG_MILE rate. The MOD_SEATS gives the total number of
seats in the airplane, including the pilot and copilot seats. Therefore, a PA31-350 trip that is flown by a pilot and a copilot
has six passenger seats available.

## Page 127

THE RELATIONAL DATABASE MODEL 97
FIGURE The Ch03_AviaCo database tables (continued)
P3.24
Table name: PILOT Database name: Ch03_AviaCo
The pilot licenses shown in the PILOT table include the ATP = Airline Transport Pilot and COMM = Commercial Pilot.
Businesses that operate on-demand air services are governed by Part 135 of the Federal Air Regulations (FARs) that are
enforced by the Federal Aviation Administration (FAA). Such businesses are known as “Part 135 operators.” Part 125
operations require that pilots successfully complete flight proficiency checks every six months. The “Part 135” flight
proficiency check data are recorded in PIL_PT135_DATE. To fly commercially, pilots must have at least a commercial
license and a second-class medical certificate (PIL_MED_TYPE = 2).
The PIL_RATINGS include
SEL = Single Engine, Land MEL = Multiengine, Land
SES = Single Engine, Sea Instr. = Instrument
CFI = Certified Flight Instructor CFII = Certified Flight Instructor, Instrument
Table name: EMPLOYEE
Table name: CUSTOMER
The nulls in the CHARTER table’s CHAR_COPILOT column indicate that a copilot is not required for some charter
trips or for some aircraft. Federal Aviation Administration (FAA) rules require a copilot on jet aircraft and on aircraft
having a gross take-off weight over 12,500 pounds. None of the aircraft in the AIRCRAFT table is governed by this
requirement; however, some customers may require the presence of a copilot for insurance reasons. All charter trips
are recorded in the CHARTER table.

## Page 128

98 CHAPTER 3
Note
Earlierinthechapter,itwasstatedthatitisbesttoavoidhomonymsandsynonyms.Inthisproblem,boththe
pilotandthecopilotarepilotsinthePILOTtable,butEMP_NUMcannotbeusedforbothintheCHARTER
table.Therefore,thesynonymsCHAR_PILOTandCHAR_COPILOTwereusedintheCHARTERtable.
Although the solution works in this case, it is very restrictive and it generates nulls when a copilot is not
required. Worse, such nulls proliferate as crew requirements change. For example, if the AviaCo charter
companygrowsandstartsusinglargeraircraft,crewrequirementsmayincreasetoincludeflightengineersand
loadmasters.TheCHARTERtablewouldthenhavetobemodifiedtoincludetheadditionalcrewassignments;
suchattributesasCHAR_FLT_ENGINEERandCHAR_LOADMASTERwouldhavetobeaddedtotheCHARTER
table.Giventhischange,eachtimeasmalleraircraftflewachartertripwithoutthenumberofcrewmembers
requiredinlargeraircraft,themissingcrewmemberswouldyieldadditionalnullsintheCHARTERtable.
You will have a chance to correct those design shortcomings in Problem 27. The problem illustrates two
importantpoints:
1. Don’tusesynonyms.Ifyourdesignrequirestheuseofsynonyms,revisethedesign!
2. Tothegreatestpossibleextent,designthedatabasetoaccommodategrowthwithoutrequiringstructural
changesinthedatabasetables.Planaheadandtrytoanticipatetheeffectsofchangeonthedatabase.
24. For each table, where possible, identify:
a. The primary key.
b. A superkey.
c. A candidate key.
d. The foreign key(s).
e. A secondary key.
25. CreatetheERD.(Hint:Lookatthetablecontents.YouwilldiscoverthatanAIRCRAFTcanflymanyCHARTER
tripsbutthateachCHARTERtripisflownbyoneAIRCRAFT,thataMODELreferencesmanyAIRCRAFTbut
that each AIRCRAFT references a single MODEL, etc.)
26. Create the relational diagram.
27. Modify the ERD you created in Problem 25 to eliminate the problems created by the use of synonyms. (Hint:
Modify the CHARTER table structure by eliminating the CHAR_PILOT and CHAR_COPILOT attributes; then
create a composite table named CREW to link the CHARTER and EMPLOYEE tables. Some crew members,
such as flight attendants, may not be pilots. That’s why the EMPLOYEE table enters into this relationship.)
28. Create the relational diagram for the design you revised in Problem 27. (After you have had a chance to revise
the design, your instructor will show you the results of the design change, using a copy of the revised database
named Ch03_AviaCo_2.)
YouareinterestedinseeingdataonchartersflownbyeitherMr.RobertWilliams(employeenumber105)orMs.Elizabeth
Travis(employeenumber109)aspilotorcopilot,butnotchartersflownbybothofthem.Completeproblems29−31to
find these data.
29. Create the table that would result from applying the SELECT and PROJECT relational operators to the
CHARTER table to return only the CHAR_TRIP, CHAR_PILOT, and CHAR_COPILOT attributes for charters
flown by either employee 104 or employee 109.
30. Create the table that would result from applying the SELECT and PROJECT relational operators to the
CHARTER table to return only the CHAR_TRIP, CHAR_PILOT, and CHAR_COPILOT attributes for charters
flown by both employee 104 and employee 109.
31. CreatethetablethatwouldresultfromapplyingaDIFFERENCErelationaloperatorofyourresultfromproblem
29 to your result from problem 30.

## Page 129

4
Entity Relationship (ER) Modeling
In this chapter, you will learn:
(cid:1) The main characteristics of entity relationship components
(cid:1) How relationships between entities are defined, refined, and incorporated into the database
design process
(cid:1) How ERD components affect database design and implementation
(cid:1) That real-world database design often requires the reconciliation of conflicting goals
This chapter expands coverage of the data-modeling aspect of database design. Data
modeling is the first step in the database design journey, serving as a bridge between
real-worldobjectsandthedatabasemodelthatisimplementedinthecomputer.Therefore,
P
the importance of data-modeling details,expressed graphically through entity relationship
review diagrams (ERDs),cannot be overstated.
Mostofthebasicconceptsanddefinitionsusedintheentityrelationshipmodel(ERM)were
introduced in Chapter 2,Data Models.For example,the basic components of entities and
relationships and their representation should now be familiar to you.This chapter goes
muchdeeperandfurther,analyzingthegraphicdepictionofrelationshipsamongtheentities
and showing how those depictions help you summarize the wealth of data required to
implement a successful design.
Finally,the chapter illustrates how conflicting goals can be a challenge in database design,
possibly requiring you to make design compromises.
R
U
O
F

## Page 130

100 CHAPTER 4
Note
Becausethisbookgenerallyfocusesontherelationalmodel,youmightbetemptedtoconcludethattheERM
is exclusively a relational tool. Actually, conceptual models such as the ERM can be used to understand and
design the data requirements of an organization. Therefore, the ERM is independent of the database type.
Conceptual models are used in the conceptual design of databases, while relational models are used in the
logicaldesignofdatabases.However,becauseyouarenowfamiliarwiththerelationalmodelfromtheprevious
chapter,therelationalmodelisusedextensivelyinthischaptertoexplainERconstructsandthewaytheyare
usedtodevelopdatabasedesigns.
4.1 THE ENTITY RELATIONSHIP MODEL (ERM)
You should remember from Chapter 2, Data Models, and Chapter 3, The Relational Database Model, that the ERM
formsthebasisofanERD.TheERDrepresentstheconceptualdatabaseasviewedbytheenduser.ERDsdepictthe
database’s main components: entities, attributes, and relationships. Because an entity represents a real-world object,
the words entity and object are often used interchangeably. Thus, the entities (objects) of the Tiny College database
design developed in this chapter include students, classes, teachers, and classrooms. The order in which the ERD
components are covered in the chapter is dictated by the way the modeling tools are used to develop ERDs that can
form the basis for successful database design and implementation.
InChapter2,youalsolearnedaboutthevariousnotationsusedwithERDs—theoriginalChennotationandthenewer
Crow’sFootandUMLnotations.Thefirsttwonotationsareusedatthebeginningofthischaptertointroducesome
basic ER modeling concepts. Some conceptual database modeling concepts can be expressed only using the Chen
notation.However,becausetheemphasisisondesignandimplementationofdatabases,theCrow’sFootandUML
class diagram notations are used for the final Tiny College ER diagram example. Because of its implementation
emphasis, the Crow’s Foot notation can represent only what could be implemented. In other words:
(cid:2) The Chen notation favors conceptual modeling.
(cid:2) The Crow’s Foot notation favors a more implementation-oriented approach.
(cid:2) The UML notation can be used for both conceptual and implementation modeling.
O n l i n e C o n t e n t
TolearnhowtocreateERdiagramswiththehelpofMicrosoftVisio,seethePremiumWebsiteforthisbook:
• AppendixA,DesigningDatabaseswithVisioProfessional:ATutorialshowsyouhowtocreateCrow’s
FootERDs.
• AppendixH,UnifiedModelingLanguage(UML),showsyouhowtocreateUMLclassdiagrams.
4.1.1 Entities
Recallthatanentityisanobjectofinteresttotheenduser.InChapter2,youlearnedthatattheERmodelinglevel,
anentityactuallyreferstotheentitysetandnottoasingleentityoccurrence.Inotherwords,thewordentityinthe
ERMcorrespondstoatable—nottoarow—intherelationalenvironment.TheERMreferstoatablerowasanentity
instance or entity occurrence. In both the Chen and Crow’s Foot notations, an entity is represented by a rectangle
containing the entity’s name. The entity name, a noun, is usually written in all capital letters.

## Page 131

ENTITY RELATIONSHIP (ER) MODELING 101
4.1.2 Attributes
Attributes are characteristics of entities. For example, the STUDENT entity includes, among many others, the
attributes STU_LNAME, STU_FNAME, and STU_INITIAL. In the original Chen notation, attributes are represented
byovalsandareconnectedtotheentityrectanglewithaline.Eachovalcontainsthenameoftheattributeitrepresents.
IntheCrow’sFootnotation,theattributesarewrittenintheattributeboxbelowtheentityrectangle.(SeeFigure4.1.)
BecausetheChenrepresentationisratherspace-consuming,softwarevendorshaveadoptedtheCrow’sFootattribute
display.
FIGURE The attributes of the STUDENT entity: Chen and Crow’s Foot
4.1
Chen Model Crow’s Foot Model
STU_INITIAL
STU_FNAME STU_EMAIL
STU_LNAME STUDENT STU_PHONE
Required and Optional Attributes
A required attribute is an attribute that must have a value; in other words, it cannot be left empty. As shown in
Figure 4.1, there are two boldfaced attributes in the Crow’s Foot notation. This indicates that a data entry will be
required. In this example, STU_LNAME and STU_FNAME require data entries because of the assumption that all
studentshavealastnameandafirstname.Butstudentsmightnothaveamiddlename,andperhapstheydonot(yet)
have a phone number and an e-mail address. Therefore, those attributes are not presented in boldface in the entity
box. An optional attribute is an attribute that does not require a value; therefore, it can be left empty.
Domains
Attributes have a domain. As you learned in Chapter 3, a domain is the set of possible values for a given attribute.
Forexample,thedomainforthegradepointaverage(GPA)attributeiswritten(0,4)becausethelowestpossibleGPA
valueis0andthehighestpossiblevalueis4.Thedomainforthegenderattributeconsistsofonlytwopossibilities:M
or F (or some other equivalent code). The domain for a company’s date of hire attribute consists of all dates that fit
in a range (for example, company startup date to current date).
Attributesmayshareadomain.Forinstance,astudentaddressandaprofessoraddresssharethesamedomainofall
possibleaddresses.Infact,thedatadictionarymayletanewlydeclaredattributeinheritthecharacteristicsofanexisting
attributeifthesameattributenameisused.Forexample,thePROFESSORandSTUDENTentitiesmayeachhavean
attribute named ADDRESS and could therefore share a domain.
Identifiers (Primary Keys)
TheERMusesidentifiers,thatis,oneormoreattributesthatuniquelyidentifyeachentityinstance.Intherelational
model,suchidentifiersaremappedtoprimarykeys(PKs)intables.IdentifiersareunderlinedintheERD.Keyattributes
are also underlined in a frequently used table structure shorthand notation using the format:
TABLE NAME (KEY_ATTRIBUTE 1, ATTRIBUTE 2, ATTRIBUTE 3, . . .ATTRIBUTE K)

## Page 132

102 CHAPTER 4
For example, a CAR entity may be represented by:
CAR (CAR_VIN, MOD_CODE, CAR_YEAR, CAR_COLOR)
(Each car is identified by a unique vehicle identification number, or CAR_VIN.)
Composite Identifiers
Ideally, an entity identifier is composed of only a single attribute. For example, the table in Figure 4.2 uses a
single-attributeprimarykeynamedCLASS_CODE.However,itispossibletouseacompositeidentifier,thatis,a
primarykeycomposedofmorethanoneattribute.Forinstance,theTinyCollegedatabaseadministratormaydecide
toidentifyeachCLASSentityinstance(occurrence)byusingacompositeprimarykeycomposedofthecombination
ofCRS_CODEandCLASS_SECTIONinsteadofusingCLASS_CODE.Eitherapproachuniquelyidentifieseachentity
instance.GiventhecurrentstructureoftheCLASStableshowninFigure4.2,CLASS_CODEistheprimarykey,and
the combination of CRS_CODE and CLASS_SECTION is a proper candidate key. If the CLASS_CODE attribute is
deleted from the CLASS entity, the candidate key (CRS_CODE and CLASS_SECTION) becomes an acceptable
composite primary key.
FIGURE The CLASS table (entity) components and contents
4.2
Note
Remember that Chapter 3 made a commonly accepted distinction between COURSE and CLASS. A CLASS
constitutesaspecifictimeandplaceofaCOURSEoffering.Aclassisdefinedbythecoursedescriptionandits
time and place, or section. Consider a professor who teaches Database I, Section 2; Database I, Section 5;
Database I, Section 8; and Spreadsheet II, Section 6. That instructor teaches two courses (Database I and
Spreadsheet II), but four classes. Typically, the COURSE offerings are printed in a course catalog, while the
CLASSofferingsareprintedinaclassscheduleforeachsemester,trimester,orquarter.
If the CLASS_CODE in Figure 4.2 is used as the primary key, the CLASS entity may be represented in shorthand
form by:
CLASS (CLASS_CODE, CRS_CODE, CLASS_SECTION, CLASS_TIME, ROOM_CODE, PROF_NUM)

## Page 133

ENTITY RELATIONSHIP (ER) MODELING 103
Ontheotherhand,ifCLASS_CODEisdeleted,andthecompositeprimarykeyisthecombinationofCRS_CODEand
CLASS_SECTION, the CLASS entity may be represented by:
CLASS (CRS_CODE, CLASS_SECTION, CLASS_TIME, ROOM_CODE, PROF_NUM)
Note that both key attributes are underlined in the entity notation.
Composite and Simple Attributes
Attributes are classified as simple or composite. A composite attribute, not to be confused with a composite key,
is an attribute that can be further subdivided to yield additional attributes. For example, the attribute ADDRESS can
be subdivided into street, city, state, and zip code. Similarly, the attribute PHONE_NUMBER can be subdivided into
areacodeandexchangenumber.Asimpleattributeisanattributethatcannotbesubdivided.Forexample,age,sex,
andmaritalstatuswouldbeclassifiedassimpleattributes.Tofacilitatedetailedqueries,itiswisetochangecomposite
attributes into a series of simple attributes.
Single-Valued Attributes
Asingle-valuedattributeisanattributethatcanhaveonlyasinglevalue.Forexample,apersoncanhaveonlyone
SocialSecuritynumber,andamanufacturedpartcanhaveonlyoneserialnumber.Keepinmindthatasingle-valued
attribute is not necessarily a simple attribute. For instance, a part’s serial number, such as SE-08-02-189935, is
single-valued,butitisacompositeattributebecauseitcanbesubdividedintotheregioninwhichthepartwasproduced
(SE), the plant within that region (08), the shift within the plant (02), and the part number (189935).
Multivalued Attributes
Multivalued attributes are attributes that can have many values. For instance, a person may have several college
degrees, and a household may have several different phones, each with its own number. Similarly, a car’s color may
besubdividedintomanycolors(thatis,colorsfortheroof,body,andtrim).IntheChenERM,themultivaluedattributes
are shown by a double line connecting the attribute to the entity. The Crow’s Foot notation does not identify
multivaluedattributes.TheERDinFigure4.3containsallofthecomponentsintroducedthusfar.InFigure4.3,note
that CAR_VIN is the primary key, and CAR_COLOR is a multivalued attribute of the CAR entity.
FIGURE A multivalued attribute in an entity
4.3
Chen Model Crow’s Foot Model
MOD_CODE CAR_YEAR
CAR_VIN CAR CAR_COLOR

## Page 134

104 CHAPTER 4
Note
IntheERDmodelsinFigure4.3,theCARentity’sforeignkey(FK)hasbeentypedasMOD_CODE.Thisattribute
was manually added to the entity. Actually, proper use of database modeling software will automatically
producetheFKwhentherelationshipisdefined.Inaddition,thesoftwarewilllabeltheFKappropriatelyand
writetheFK’simplementationdetailsinadatadictionary.Therefore,whenyouusedatabasemodelingsoftware
like Visio Professional, never type the FK attribute yourself; let the software handle that task when the
relationshipbetweentheentitiesisdefined.(Youcanseehowthat'sdoneinAppendixA,DesigningDatabases
withVisioProfessional:ATutorial,inthePremiumWebsite.)
Implementing Multivalued Attributes
AlthoughtheconceptualmodelcanhandleM:Nrelationshipsandmultivaluedattributes,youshouldnotimplement
themintheRDBMS.RememberfromChapter3thatintherelationaltable,eachcolumn/rowintersectionrepresents
asingledatavalue.Soifmultivaluedattributesexist,thedesignermustdecideononeoftwopossiblecoursesofaction:
1. Within the original entity, create several new attributes, one for each of the original multivalued attribute’s
components. For example, the CAR entity’s attribute CAR_COLOR can be split to create the new attributes
CAR_TOPCOLOR, CAR_BODYCOLOR, and CAR_TRIMCOLOR, which are then assigned to the CAR
entity. (See Figure 4.4.)
FIGURE Splitting the multivalued attribute into new attributes
4.4
Chen Model Crow’s Foot Model
CAR_YEAR
MOD_CODE CAR_TOPCOLOR
CAR_VIN CAR CAR_TRIMCOLOR
CAR_BODYCOLOR
Although this solution seems to work, its adoption can lead to major structural problems in the table. For
example, if additional color components—such as a logo color—are added for some cars, the table structure
mustbemodifiedtoaccommodatethenewcolorsection.Inthatcase,carsthatdonothavesuchcolorsections
generatenullsforthenonexistingcomponents,ortheircolorentriesforthosesectionsareenteredasN/Ato
indicate “not applicable.” (Imagine how the solution in Figure 4.4—splitting a multivalued attribute into new
attributes—would cause problems if it were applied to an employee entity containing employee degrees and
certifications. If some employees have 10 degrees and certifications while most have fewer or none, the
number of degree/certification attributes would number 10, and most of those attribute values would be null
formostoftheemployees.)Inshort,althoughyouhaveseensolution1applied,itisnotanacceptablesolution.
2. Create a new entity composed of the original multivalued attribute’s components. This new entity allows the
designertodefinecolorfordifferentsectionsofthecar.(SeeTable4.1.)Then,thisnewCAR_COLORentity
is related to the original CAR entity in a 1:M relationship.

## Page 135

ENTITY RELATIONSHIP (ER) MODELING 105
Using the approach illustrated in Table 4.1, you even get a
TABLE Components of the
4.1 Multivalued Attribute fringebenefit:youarenowabletoassignasmanycolorsas
necessarywithouthavingtochangethetablestructure.Note
SECTION COLOR that the ERM shown in Figure 4.5 reflects the components
Top White listed in Table 4.1. This is the preferred way to deal with
Body Blue multivalued attributes. Creating a new entity in a 1:M rela-
Trim Gold tionship with the original entity yields several benefits: it’s a
Interior Blue moreflexible,expandablesolution,anditiscompatiblewith
the relational model!
FIGURE A new entity set composed of a multivalued attribute’s components
4.5
Derived Attributes
Finally, an attribute may be classified as a derived attribute. A derived attribute is an attribute whose value is
calculated (derived) from other attributes. The derived attribute need not be physically stored within the database;
instead, it can be derived by using an algorithm. For example, an employee’s age, EMP_AGE, may be found by
computing the integer value of the difference between the current date and the EMP_DOB. If you use Microsoft
Access,youwouldusetheformulaINT((DATE()–EMP_DOB)/365).InMicrosoftSQLServer,youwoulduseSELECT
DATEDIFF(“YEAR”, EMP_DOB, GETDATE()), where DATEDIFF is a function that computes the difference between
dates. The first parameter indicates the measurement, in this case, years.
IfyouuseOracle,youwoulduseSYSDATEinsteadofDATE().(Youareassuming,ofcourse,thattheEMP_DOBwas
storedintheJuliandateformat.)Similarly,thetotalcostofanordercanbederivedbymultiplyingthequantityordered
bytheunitprice.Ortheestimatedaveragespeedcanbederivedbydividingtripdistancebythetimespentenroute.
A derived attribute is indicated in the Chen notation by a dashed line connecting the attribute and the entity. (See
Figure 4.6.) The Crow’s Foot notation does not have a method for distinguishing the derived attribute from other
attributes.
Derivedattributesaresometimesreferredtoascomputedattributes.Aderivedattributecomputationcanbeassimple
asaddingtwoattributevalueslocatedonthesamerow,oritcanbetheresultofaggregatingthesumofvalueslocated
onmanytablerows(fromthesametableorfromadifferenttable).Thedecisiontostorederivedattributesindatabase
tables depends on the processing requirements and the constraints placed on a particular application. The designer
should be able to balance the design in accordance with such constraints. Table 4.2 shows the advantages and
disadvantages of storing (or not storing) derived attributes in the database.
4.1.3 Relationships
Recall from Chapter 2 that a relationship is an association between entities. The entities that participate in a
relationship are also known as participants, and each relationship is identified by a name that describes the
relationship. The relationship name is an active or passive verb; for example, a STUDENT takes a CLASS, a
PROFESSOR teaches a CLASS, a DEPARTMENT employs a PROFESSOR, a DIVISION is managed by an
EMPLOYEE, and an AIRCRAFT is flown by a CREW.

## Page 136

106 CHAPTER 4
FIGURE Depiction of a derived attribute
4.6
Chen Model Crow’s Foot Model
EMP_FNAME EMP_INITIAL
EMP_LNAME EMP_DOB
EMP_NUM EMPLOYEE EMP_AGE
TABLE Advantages and Disadvantages of Storing Derived Attributes
4.2
DERIVEDATTRIBUTE
STORED NOTSTORED
Advantage SavesCPUprocessingcycles Savesstoragespace
Savesdataaccesstime Computationalwaysyieldscurrentvalue
Datavalueisreadilyavailable
Canbeusedtokeeptrackofhistoricaldata
Disadvantage Requiresconstantmaintenancetoensure UsesCPUprocessingcycles
derived value is current, especially if any values Increasesdataaccesstime
usedinthecalculationchange Addscodingcomplexitytoqueries
Relationshipsbetweenentitiesalwaysoperateinbothdirections.Thatis,todefinetherelationshipbetweentheentities
named CUSTOMER and INVOICE, you would specify that:
(cid:2) A CUSTOMER may generate many INVOICEs.
(cid:2) Each INVOICE is generated by one CUSTOMER.
Because you know both directions of the relationship between CUSTOMER and INVOICE, it is easy to see that this
relationship can be classified as 1:M.
Therelationshipclassificationisdifficulttoestablishifyouknowonlyonesideoftherelationship.Forexample,ifyou
specify that:
A DIVISION is managed by one EMPLOYEE.
Youdon’tknowiftherelationshipis1:1or1:M.Therefore,youshouldaskthequestion“Cananemployeemanage
morethanonedivision?”Iftheanswerisyes,therelationshipis1:M,andthesecondpartoftherelationshipisthen
written as:
An EMPLOYEE may manage many DIVISIONs.
Ifanemployeecannotmanagemorethanonedivision,therelationshipis1:1,andthesecondpartoftherelationship
is then written as:
An EMPLOYEE may manage only one DIVISION.

## Page 137

ENTITY RELATIONSHIP (ER) MODELING 107
4.1.4 Connectivity and Cardinality
YoulearnedinChapter2thatentityrelationshipsmaybeclassifiedasone-to-one,one-to-many,ormany-to-many.You
alsolearnedhowsuchrelationshipsweredepictedintheChenandCrow’sFootnotations.Thetermconnectivityis
used to describe the relationship classification.
Cardinality expresses the minimum and maximum number of entity occurrences associated with one occurrence of
therelatedentity.IntheERD,cardinalityisindicatedbyplacingtheappropriatenumbersbesidetheentities,usingthe
format(x,y).Thefirstvaluerepresentstheminimumnumberofassociatedentities,whilethesecondvaluerepresents
themaximumnumberofassociatedentities.ManydatabasedesignerswhouseCrow’sFootmodelingnotationdonot
depictthespecificcardinalitiesontheERdiagramitselfbecausethespecificlimitsdescribedbythecardinalitiescannot
beimplementeddirectlythroughthedatabasedesign.Correspondingly,someCrow’sFootERmodelingtoolsdonot
printthenumericcardinalityrangeinthediagram;instead,youcanadditastextifyouwanttohaveitshown.When
thespecificcardinalitiesarenotincludedonthediagraminCrow’sFootnotation,cardinalityisimpliedbytheuseof
the symbols shown in Figure 4.7, which describe the connectivity and participation (discussed below). The numeric
cardinality range has been added using the Visio text drawing tool.
Knowing the minimum and maximum number of entity
FIGURE Connectivity and cardinality in
occurrences is very useful at the application software level.
4.7 an ERD
Forexample,TinyCollegemightwanttoensurethataclass
is not taught unless it has at least 10 students enrolled.
Similarly, if the classroom can hold only 30 students, the
application software should use that cardinality to limit
enrollment in the class. However, keep in mind that the
DBMScannothandletheimplementationofthecardinalities
atthetablelevel—thatcapabilityisprovidedbytheapplica-
tionsoftwareorbytriggers.Youwilllearnhowtocreateand
execute triggers in Chapter 8, Advanced SQL.
As you examine the Crow’s Foot diagram in Figure 4.7,
keep in mind that the cardinalities represent the number of occurrences in the related entity. For example, the
cardinality (1,4) written next to the CLASS entity in the “PROFESSOR teaches CLASS” relationship indicates that
eachprofessorteachesuptofourclasses,whichmeansthatthePROFESSORtable’sprimarykeyvalueoccursatleast
onceandnomorethanfourtimesasforeignkeyvaluesintheCLASStable.Ifthecardinalityhadbeenwrittenas(1,N),
therewouldbenoupperlimittothenumberofclassesaprofessormightteach.Similarly,thecardinality(1,1)written
nexttothePROFESSORentityindicatesthateachclassistaughtbyoneandonlyoneprofessor.Thatis,eachCLASS
entity occurrence is associated with one and only one entity occurrence in PROFESSOR.
Connectivities and cardinalities are established by very concise statements known as business rules, which were
introduced in Chapter 2. Such rules, derived from a precise and detailed description of an organization’s data
environment, also establish the ERM’s entities, attributes, relationships, connectivities, cardinalities, and constraints.
BecausebusinessrulesdefinetheERM’scomponents,makingsurethatallappropriatebusinessrulesareidentifiedis
a very important part of a database designer’s job.
Note
TheplacementofthecardinalitiesintheERdiagramisamatterofconvention.TheChennotationplacesthe
cardinalitiesonthesideoftherelatedentity.TheCrow’sFootandUMLdiagramsplacethecardinalitiesnextto
theentitytowhichthecardinalitiesapply.

## Page 138

108 CHAPTER 4
O n l i n e C o n t e n t
Becausethecarefuldefinitionofcompleteandaccuratebusinessrulesiscrucialtogooddatabasedesign,their
derivationisexaminedindetailinAppendixB,TheUniversityLab:ConceptualDesign. Themodelingskills
youarelearninginthischapterareappliedinthedevelopmentofarealdatabasedesigninAppendixB.The
initialdesignshowninAppendixBisthenmodifiedinAppendixC,TheUniversityLab:ConceptualDesign
Verification,LogicalDesign,andImplementation.(BothappendixesarefoundinthePremiumWebsite.)
4.1.5 Existence Dependence
An entity is said to be existence-dependent if it can exist in the database only when it is associated with another
related entity occurrence. In implementation terms, an entity is existence-dependent if it has a mandatory foreign
key—that is, a foreign key attribute that cannot be null. For example, if an employee wants to claim one or more
dependentsfortax-withholdingpurposes,therelationship“EMPLOYEEclaimsDEPENDENT”wouldbeappropriate.
Inthatcase,theDEPENDENTentityisclearlyexistence-dependentontheEMPLOYEEentitybecauseitisimpossible
for the dependent to exist apart from the EMPLOYEE in the database.
Ifanentitycanexistapartfromallofitsrelatedentities(itisexistence-independent),thenthatentityisreferredto
as a strong entity or regular entity. For example, suppose that the XYZ Corporation uses parts to produce its
products. Furthermore, suppose that some of those parts are produced in-house and other parts are bought from
vendors. In that scenario, it is quite possible for a PART to exist independently from a VENDOR in the relationship
“PART is supplied by VENDOR,” because at least some of the parts are not supplied by a vendor. Therefore, PART
is existence-independent from VENDOR.
Note
TherelationshipstrengthconceptisnotpartoftheoriginalERM.Instead,thisconceptappliesdirectlytoCrow’s
Footdiagrams.BecauseCrow’sFootdiagramsareusedextensivelytodesignrelationaldatabases,itisimportant
tounderstandrelationshipstrengthasitaffectsdatabaseimplementation.TheChenERDnotationisoriented
towardconceptualmodelingandthereforedoesnotdistinguishbetweenweakandstrongrelationships.
4.1.6 Relationship Strength
The concept of relationship strength is based on how the primary key of a related entity is defined. To implement a
relationship, the primary key of one entity appears as a foreign key in the related entity. For example, the 1:M
relationshipbetweenVENDORandPRODUCTinChapter3,Figure3.3,isimplementedbyusingtheVEND_CODE
primarykeyinVENDORasaforeignkeyinPRODUCT.Therearetimeswhentheforeignkeyalsoisaprimarykey
componentintherelatedentity.Forexample,inFigure4.5,theCARentityprimarykey(CAR_VIN)appearsasboth
a primary key component and a foreign key in the CAR_COLOR entity. In this section, you will learn how various
relationship strength decisions affect primary key arrangement in database design.

## Page 139

ENTITY RELATIONSHIP (ER) MODELING 109
Weak (Non-identifying) Relationships
Aweakrelationship,alsoknownasanon-identifyingrelationship,existsifthePKoftherelatedentitydoesnot
containaPKcomponentoftheparententity.Bydefault,relationshipsareestablishedbyhavingthePKoftheparent
entity appear as an FK on the related entity. For example, suppose that the COURSE and CLASS entities are
defined as:
COURSE(CRS_CODE, DEPT_CODE, CRS_DESCRIPTION, CRS_CREDIT)
CLASS(CLASS_CODE, CRS_CODE, CLASS_SECTION, CLASS_TIME, ROOM_CODE, PROF_NUM)
In this case, a weak relationship exists between COURSE and CLASS because the CLASS_CODE is the CLASS
entity’s PK, while the CRS_CODE in CLASS is only an FK. In this example, the CLASS PK did not inherit the PK
component from the COURSE entity.
Figure 4.8 shows how the Crow’s Foot notation depicts a weak relationship by placing a dashed relationship line
between the entities. The tables shown below the ERD illustrate how such a relationship is implemented.
FIGURE A weak (non-identifying) relationship between COURSE and CLASS
4.8
Table name: COURSE Database name: Ch04_TinyCollege
Table name: CLASS

## Page 140

110 CHAPTER 4
O n l i n e C o n t e n t
AllofthedatabasesusedtoillustratethematerialinthischapterarefoundinthePremiumWebsite.
Note
IfyouareusedtolookingatrelationaldiagramssuchastheonesproducedbyMicrosoftAccess,youexpectto
seetherelationshiplineintherelationaldiagramdrawnfromthePKtotheFK.However,therelationaldiagram
conventionisnotnecessarilyreflectedintheERD.InanERD,thefocusisontheentitiesandtherelationships
betweenthem,ratherthanonthewaythoserelationshipsareanchoredgraphically.Youwilldiscoverthatthe
placement of the relationship lines in a complex ERD that includes both horizontally and vertically placed
entitiesislargelydictatedbythedesigner’sdecisiontoimprovethereadabilityofthedesign.(Rememberthat
theERDisusedforcommunicationbetweenthedesigner(s)andendusers.)
Strong (Identifying) Relationships
Astrongrelationship,alsoknownasanidentifyingrelationship,existswhenthePKoftherelatedentitycontains
a PK component of the parent entity. For example, the definitions of the COURSE and CLASS entities
COURSE(CRS_CODE, DEPT_CODE, CRS_DESCRIPTION, CRS_CREDIT)
CLASS(CRS_CODE, CLASS_SECTION , CLASS_TIME, ROOM_CODE, PROF_NUM)
indicate that a strong relationship exists between COURSE and CLASS, because the CLASS entity’s composite PK
is composed of CRS_CODE + CLASS_SECTION. (Note that the CRS_CODE in CLASS is also the FK to the
COURSE entity.)
TheCrow’sFootnotationdepictsthestrong(identifying)relationshipwithasolidlinebetweentheentities,shownin
Figure 4.9. Whether the relationship between COURSE and CLASS is strong or weak depends on how the CLASS
entity’s primary key is defined.
Keep in mind that the order in which the tables are created and loaded is very important. For example, in the
“COURSE generates CLASS” relationship, the COURSE table must be created before the CLASS table. After all, it
would not be acceptable to have the CLASS table’s foreign key reference a COURSE table that did not yet exist. In
fact, you must load the data of the “1” side first in a 1:M relationship to avoid the possibility of referential
integrity errors, regardless of whether the relationships are weak or strong.
AsyouexamineFigure4.9youmightwonderwhattheOsymbolnexttotheCLASSentitysignifies.Youwilldiscover
the meaning of this cardinality in Section 4.1.8, Relationship Participation.
Rememberthatthenatureoftherelationshipisoftendeterminedbythedatabasedesigner,whomustuseprofessional
judgment to determine which relationship type and strength best suit the database transaction, efficiency, and
information requirements. That point will often be emphasized in detail!
4.1.7 Weak Entities
IncontrasttothestrongorregularentitymentionedinSection4.1.5,aweakentityisonethatmeetstwoconditions:
1. The entity is existence-dependent; that is, it cannot exist without the entity with which it has a relationship.
2. The entity has a primary key that is partially or totally derived from the parent entity in the relationship.

## Page 141

ENTITY RELATIONSHIP (ER) MODELING 111
FIGURE A strong (identifying) relationship between COURSE and CLASS
4.9
Table name: COURSE Database name: Ch04_TinyCollege_Alt
Table name: CLASS
Forexample,acompanyinsurancepolicyinsuresanemployeeandhis/herdependents.Forthepurposeofdescribing
an insurance policy, an EMPLOYEE might or might not have a DEPENDENT, but the DEPENDENT must be
associatedwithanEMPLOYEE.Moreover,theDEPENDENTcannotexistwithouttheEMPLOYEE;thatis,aperson
cannotgetinsurancecoverageasadependentunlesss(he)happenstobeadependentofanemployee.DEPENDENT
is the weak entity in the relationship “EMPLOYEE has DEPENDENT.” This relationship is shown in Figure 4.10.
NotethattheChennotationinFigure4.10identifiestheweakentitybyusingadouble-walledentityrectangle.TheCrow’s
FootnotationgeneratedbyVisioProfessionalusestherelationshiplineandthePK/FKdesignationtoindicatewhetherthe
relatedentityisweak.Astrong(identifying)relationshipindicatesthattherelatedentityisweak.Sucharelationshipmeans
thatbothconditionsfortheweakentitydefinitionhavebeenmet—therelatedentityisexistence-dependent,andthePK
of the related entity contains a PK component of the parent entity.(Some versions of the Crow’s Foot ERD depict the
weak entity by drawing a short line segment in each of the four corners of the weak entity box.)
Rememberthattheweakentityinheritspartofitsprimarykeyfromitsstrongcounterpart.Forexample,atleastpart
of the DEPENDENT entity’s key shown in Figure 4.10 was inherited from the EMPLOYEE entity:
EMPLOYEE (EMP_NUM, EMP_LNAME, EMP_FNAME, EMP_INITIAL, EMP_DOB, EMP_HIREDATE)
DEPENDENT (EMP_NUM, DEP_NUM, DEP_FNAME, DEP_DOB)

## Page 142

112 CHAPTER 4
FIGURE A weak entity in an ERD
4.10
Chen Model
1 M
EMPLOYEE has DEPENDENT
(0,N) (1,1)
EMP_NUM EMP_NUM
EMP_LNAME DEP_NUM
EMP_FNAME DEP_FNAME
EMP_INITIAL DEP_DOB
EMP_DOB
EMP_HIREDATE
Crow’s Foot Model
Figure 4.11 illustrates the implementation of the relationship between the weak entity (DEPENDENT) and its parent
orstrongcounterpart(EMPLOYEE).NotethatDEPENDENT’sprimarykeyiscomposedoftwoattributes,EMP_NUM
and DEP_NUM, and that EMP_NUM was inherited from EMPLOYEE.
FIGURE A weak entity in a strong relationship
4.11
Table name: EMPLOYEE Database name: Ch04_ShortCo
Table name: DEPENDENT

## Page 143

ENTITY RELATIONSHIP (ER) MODELING 113
Given this scenario, and with the help of this relationship, you can determine that:
Jeanine J. Callifante claims two dependents, Annelise and Jorge.
Keepinmindthatthedatabasedesignerusuallydetermineswhetheranentitycanbedescribedasweakbasedonthe
business rules. An examination of the relationship between COURSE and CLASS in Figure 4.8 might cause you to
concludethatCLASSisaweakentitytoCOURSE.Afterall,inFigure4.8,itseemsclearthataCLASScannotexist
withoutaCOURSE;sothereisexistencedependence.Forexample,astudentcannotenrollintheAccountingIclass
ACCT-211,Section3(CLASS_CODE10014)unlessthereisanACCT-211course.However,notethattheCLASS
table’sprimarykeyisCLASS_CODE,whichisnotderivedfromtheCOURSEparententity.Thatis,CLASSmaybe
represented by:
CLASS (CLASS_CODE, CRS_CODE, CLASS_SECTION, CLASS_TIME, ROOM_CODE, PROF_NUM)
Thesecondweakentityrequirementhasnotbeenmet;therefore,bydefinition,theCLASSentityinFigure4.8may
notbeclassifiedasweak.Ontheotherhand,iftheCLASSentity’sprimarykeyhadbeendefinedasacompositekey,
composed of the combination CRS_CODE and CLASS_SECTION, CLASS could be represented by:
CLASS (CRS_CODE, CLASS_SECTION, CLASS_TIME, ROOM_CODE, PROF_NUM)
Inthatcase,illustratedinFigure4.9,theCLASSprimarykeyispartiallyderivedfromCOURSEbecauseCRS_CODE
is the COURSE table’s primary key. Given this decision, CLASS is a weak entity by definition. (In Visio Professional
Crow’sFootterms,therelationshipbetweenCOURSEandCLASSisclassifiedasstrong,oridentifying.)Inanycase,
CLASS is always existence-dependent on COURSE, whether or not it is defined as weak.
4.1.8 Relationship Participation
Participation in an entity relationship is either optional or mandatory. Recall that relationships are bidirectional; that
is,theyoperateinbothdirections.IfCOURSEisrelatedtoCLASS,thenbydefinition,CLASSisrelatedtoCOURSE.
Because of the bidirectional nature of relationships, it is necessary to determine the connectivity of the relationship
from COURSE to CLASS and the connectivity of the relationship from CLASS to COURSE. Similarly, the specific
maximumandminimumcardinalitiesmustbedeterminedineachdirectionfortherelationship.Onceagain,youmust
consider the bidirectional nature of the relationship when determining participation.
Optional participation means that one entity occurrence does not require a corresponding entity occurrence in a
particular relationship. For example, in the “COURSE generates CLASS” relationship, you noted that at least some
coursesdonotgenerateaclass.Inotherwords,anentityoccurrence(row)intheCOURSEtabledoesnotnecessarily
require the existence of a corresponding entity occurrence in the CLASS table. (Remember that each entity is
implementedasatable.)Therefore,theCLASSentityisconsideredtobeoptionaltotheCOURSEentity.InCrow’s
Foot notation, an optional relationship between entities is shown by drawing a small circle (O) on the side of the
optionalentity,asillustratedinFigure4.9.Theexistenceofanoptionalentityindicatesthattheminimumcardinality
is 0 for the optional entity. (The term optionality is used to label any condition in which one or more optional
relationships exist.)
Note
Remember that the burden of establishing the relationship is always placed on the entity that contains the
foreignkey.Inmostcases,thatwillbetheentityonthe“many”sideoftherelationship.
Mandatory participation means that one entity occurrence requires a corresponding entity occurrence in a
particularrelationship.Ifnooptionalitysymbolisdepictedwiththeentity,theentityisassumedtoexistinamandatory
relationshipwiththerelatedentity.Ifthemandatoryparticipationisdepictedgraphically,itistypicallyshownasasmall

## Page 144

114 CHAPTER 4
hash mark across the relationship line, similar to the Crow’s Foot depiction of a connectivity of 1. The existence of
a mandatory relationship indicates that the minimum cardinality is at least 1 for the mandatory entity.
Note
Youmightbetemptedtoconcludethatrelationshipsareweakwhentheyoccurbetweenentitiesinanoptional
relationship and that relationships are strong when they occur between entities in a mandatory relationship.
However, this conclusion is not warranted. Keep in mind that relationship participation and relationship
strengthdonotdescribethesamething.Youarelikelytoencounterastrongrelationshipwhenoneentityis
optionaltoanother.Forexample,therelationshipbetweenEMPLOYEEandDEPENDENTisclearlyastrongone,
butDEPENDENTisclearlyoptionaltoEMPLOYEE.Afterall,youcannotrequireemployeestohavedependents.
Anditisjustaspossibleforaweakrelationshiptobeestablishedwhenoneentityismandatorytoanother.The
relationship strength depends on how the PK of the related entity is formulated, while the relationship
participationdependsonhowthebusinessruleiswritten.Forexample,thebusinessrules“Eachpartmustbe
suppliedbyavendor”and“Apartmayormaynotbesuppliedbyavendor”createdifferentoptionalitiesfor
the same entities! Failure to understand this distinction may lead to poor design decisions that cause major
problemswhentablerowsareinsertedordeleted.
When you create a relationship in MS Visio, the default relationship will be mandatory on the “1” side and optional
onthe“many”side.Table4.3showsthevariousconnectivityandparticipationcombinationsthataresupportedbythe
Crow’sFootnotation.RecallthatthesecombinationsareoftenreferredtoascardinalityinCrow’sFootnotationwhen
specific cardinalities are not used.
TABLE Crow’s Foot Symbols
4.3
CROW’SFOOTSYMBOL CARDINALITY COMMENT
(0,N) Zeroormany.Manysideisoptional.
(1,N) Oneormany.Manysideismandatory.
(1,1) Oneandonlyone.1sideismandatory.
(0,1) Zeroorone.1sideisoptional.
Because relationship participation turns out to be a very important component of the database design process, let’s
examine a few more scenarios. Suppose that Tiny College employs some professors who conduct research without
teaching classes. If you examine the “PROFESSOR teaches CLASS” relationship, it is quite possible for a
PROFESSORnottoteachaCLASS.Therefore,CLASSisoptionaltoPROFESSOR.Ontheotherhand,aCLASS
must be taught by a PROFESSOR. Therefore, PROFESSOR is mandatory to CLASS. Note that the ERD model in
Figure4.12showsthecardinalitynexttoCLASStobe(0,3),thusindicatingthataprofessormayteachnoclassesat
all or as many as three classes. And each CLASS table row will reference one and only one PROFESSOR
row—assuming each class is taught by one and only one professor—represented by the (1,1) cardinality next to the
PROFESSOR table.
Failure to understand the distinction between mandatory and optional participation in relationships might yield
designs in which awkward (and unnecessary) temporary rows (entity instances) must be created just to accommodate
thecreationofrequiredentities.Therefore,itisimportantthatyouclearlyunderstandtheconceptsofmandatoryand
optional participation.
It is also important to understand that the semantics of a problem might determine the type of participation in a
relationship. For example, suppose that Tiny College offers several courses; each course has several classes. Note

## Page 145

ENTITY RELATIONSHIP (ER) MODELING 115
FIGURE An optional CLASS entity in the relationship “PROFESSOR teaches CLASS”
4.12
again the distinction between class and course in this discussion: a CLASS constitutes a specific offering (or section)
of a COURSE. (Typically, courses are listed in the university’s course catalog, while classes are listed in the class
schedules that students use to register for their classes.)
Analyzing the CLASS entity’s contribution to the “COURSE generates CLASS” relationship, it is easy to see that a
CLASScannotexistwithoutaCOURSE.Therefore,youcanconcludethattheCOURSEentityismandatoryinthe
relationship. But two scenarios for the CLASS entity may be written, shown in Figures 4.13 and 4.14.
FIGURE CLASS is optional to COURSE
4.13
FIGURE COURSE and CLASS in a mandatory relationship
4.14
The different scenarios are a function of the semantics of the problem; that is, they depend on how the relationship
is defined.
1. CLASS is optional. It is possible for the department to create the entity COURSE first and then create the
CLASSentityaftermakingtheteachingassignments.Intherealworld,suchascenarioisverylikely;theremay
be courses for which sections (classes) have not yet been defined. In fact, some courses are taught only once
a year and do not generate classes each semester.
2. CLASS is mandatory. This condition is created by the constraint that is imposed by the semantics of the
statement“EachCOURSEgeneratesoneormoreCLASSes.”InERterms,eachCOURSEinthe“generates”
relationshipmusthaveatleastoneCLASS.Therefore,aCLASSmustbecreatedastheCOURSEiscreated,
in order to comply with the semantics of the problem.
KeepinmindthepracticalaspectsofthescenariopresentedinFigure4.14.Giventhesemanticsofthisrelationship,
thesystemshouldnotacceptacoursethatisnotassociatedwithatleastoneclasssection.Issucharigidenvironment

## Page 146

116 CHAPTER 4
desirablefromanoperationalpointofview?Forexample,whenanewCOURSEiscreated,thedatabasefirstupdates
theCOURSEtable,therebyinsertingaCOURSEentitythatdoesnotyethaveaCLASSassociatedwithit.Naturally,
the apparent problem seems to be solved when CLASS entities are inserted into the corresponding CLASS table.
However, because of the mandatory relationship, the system will be in temporary violation of the business rule
constraint.Forpracticalpurposes,itwouldbedesirabletoclassifytheCLASSasoptionalinordertoproduceamore
flexible design.
Finally, as you examine the scenarios presented in Figures 4.13 and 4.14, keep in mind the role of the DBMS. To
maintaindataintegrity,theDBMSmustensurethatthe“many”side(CLASS)isassociatedwithaCOURSEthrough
the foreign key rules.
4.1.9 Relationship Degree
A relationship degree indicates the number of entities or participants associated with a relationship. A unary
relationshipexistswhenanassociationismaintainedwithinasingleentity.Abinaryrelationshipexistswhentwo
entities are associated. A ternary relationship exists when three entities are associated. Although higher degrees
exist,theyarerareandarenotspecificallynamed.(Forexample,anassociationoffourentitiesisdescribedsimplyas
a four-degree relationship.) Figure 4.15 shows these types of relationship degrees.
Unary Relationships
InthecaseoftheunaryrelationshipshowninFigure4.15,anemployeewithintheEMPLOYEEentityisthemanager
for one or more employees within that entity. In this case, the existence of the “manages” relationship means that
EMPLOYEErequiresanotherEMPLOYEEtobethemanager—thatis,EMPLOYEEhasarelationshipwithitself.Such
arelationshipisknownasarecursiverelationship.Thevariouscasesofrecursiverelationshipswillbeexploredin
Section 4.1.10.
Binary Relationships
Abinaryrelationshipexistswhentwoentitiesareassociatedinarelationship.Binaryrelationshipsaremostcommon.
Infact,tosimplifytheconceptualdesign,wheneverpossible,mosthigher-order(ternaryandhigher)relationshipsare
decomposedintoappropriateequivalentbinaryrelationships.InFigure4.15,therelationship“aPROFESSORteaches
one or more CLASSes” represents a binary relationship.
Ternary and Higher-Degree Relationships
Althoughmostrelationshipsarebinary,theuseofternaryandhigher-orderrelationshipsdoesallowthedesignersome
latitude regarding the semantics of a problem. A ternary relationship implies an association among three different
entities. For example, note the relationships (and their consequences) in Figure 4.16, which are represented by the
following business rules:
(cid:2) A DOCTOR writes one or more PRESCRIPTIONs.
(cid:2) A PATIENT may receive one or more PRESCRIPTIONs.
(cid:2) A DRUG may appear in one or more PRESCRIPTIONs. (To simplify this example, assume that the business
rulestatesthateachprescriptioncontainsonlyonedrug.Inshort,ifadoctorprescribesmorethanonedrug,
a separate prescription must be written for each drug.)
As you examine the table contents in Figure 4.16, note that it is possible to track all transactions. For instance, you
can tell that the first prescription was written by doctor 32445 for patient 102, using the drug DRZ.

## Page 147

ENTITY RELATIONSHIP (ER) MODELING 117
FIGURE Three types of relationship degree
4.15
4.1.10 Recursive Relationships
As was previously mentioned, a recursive relationship is one in which a relationship can exist between occurrences
of the same entity set. (Naturally, such a condition is found within a unary relationship.) For example, a 1:M unary
relationship can be expressed by “an EMPLOYEE may manage many EMPLOYEEs, and each EMPLOYEE is
managed by one EMPLOYEE.” And as long as polygamy is not legal, a 1:1 unary relationship may be expressed by
“an EMPLOYEE may be married to one and only one other EMPLOYEE.” Finally, the M:N unary relationship may
be expressed by “a COURSE may be a prerequisite to many other COURSEs, and each COURSE may have many
other COURSEs as prerequisites.” Those relationships are shown in Figure 4.17.
The 1:1 relationship shown in Figure 4.17 can be implemented in the single table shown in Figure 4.18. Note that
you can determine that James Ramirez is married to Louise Ramirez, who is married to James Ramirez. And Anne
Jones is married to Anton Shapiro, who is married to Anne Jones.

## Page 148

118 CHAPTER 4
FIGURE The implementation of a ternary relationship
4.16
Database name: Ch04_Clinic
Table name: DRUG Table name: PATIENT
Table name: DOCTOR Table name: PRESCRIPTION
FIGURE An ER representation of recursive relationships
4.17
FIGURE The 1:1 recursive relationship Unary relationships are common in manufacturing
4.18 “EMPLOYEE is married to
industries. For example, Figure 4.19 illustrates that a rotor
EMPLOYEE”
assembly(C-130)iscomposedofmanyparts,buteachpart
is used to create only one rotor assembly. Figure 4.19
Database name: CH04_PartCo
Table name: EMPLOYEE_V1 indicates that a rotor assembly is composed of four 2.5-cm
washers, two cotter pins, one 2.5-cm steel shank, four
10.25-cm rotor blades, and two 2.5-cm hex nuts. The
relationshipimplementedinFigure4.19thusenablesyouto
track each part within each rotor assembly.
If a part can be used to assemble several different kinds of
otherpartsandisitselfcomposedofmanyparts,twotables

## Page 149

ENTITY RELATIONSHIP (ER) MODELING 119
FIGURE Another unary relationship: “PART contains PART”
4.19
Table name: PART_V1 Database name; CH04_PartCo
arerequiredtoimplementthe“PARTcontainsPART”relationship.Figure4.20illustratessuchanenvironment.Parts
tracking is increasingly important as managers become more aware of the legal ramifications of producing more
complex output. In fact, in many industries, especially those involving aviation, full parts tracking is required by law.
FIGURE Implementation of the M:N recursive relationship “PART contains PART”
4.20
Table name: COMPONENT Database name: Ch04_PartCo
Table name: PART
The M:N recursive relationship might be more familiar in a school environment. For instance, note how the M:N
“COURSErequiresCOURSE”relationshipillustratedinFigure4.17isimplementedinFigure4.21.Inthisexample,
MATH-243 is a prerequisite to QM-261 and QM-362, while both MATH-243 and QM-261 are prerequisites to
QM-362.
Finally,the1:Mrecursiverelationship“EMPLOYEEmanagesEMPLOYEE,”showninFigure4.17,isimplementedin
Figure 4.22.
One common pitfall when working with unary relationships is to confuse participation with referential integrity. In
theory,participationandreferentialintegrityareverydifferentconceptsandarenormallyeasytodistinguishinbinary
relationships. In practical terms, conversely, participation and referential integrity are very similar because they are
bothimplementedthroughconstraintsonthesamesetofattributes.Thissimilarityoftenleadstoconfusionwhenthe
conceptsareappliedwithinthelimitedstructureofaunaryrelationship.Considertheunary1:1relationshipdescribed
in Figure 4.18 of a spousal relationship between employees. Participation, as described above, is bidirectional,

## Page 150

120 CHAPTER 4
FIGURE Implementation of the M:N recursive relationship “COURSE requires COURSE”
4.21
Table name: COURSE Database name: Ch04_TinyCollege
Table name: PREREQ
FIGURE Implementation of the 1:M recursive relationship “EMPLOYEE manages EMPLOYEE”
4.22
Database name: Ch04_PartCo
Table name: EMPLOYEE_V2
meaningthatitmustbeaddressedinbothdirectionsalongtherelationship.ParticipationinFigure4.18addressesthe
questions:
(cid:2) Must every employee have a spouse who is an employee?
(cid:2) Must every employee be a spouse to another employee?
For the data shown in Figure 4.18, the correct answer to both of those questions is “No.” It is possible to be an
employee and not have another employee as a spouse. Also, it is possible to be an employee and not be the spouse
of another employee.
Referentialintegritydealswiththecorrespondenceofvaluesintheforeignkeywithvaluesintherelatedprimarykey.
Referential integrity is not bidirectional, and therefore has only one question that it answers.
(cid:2) Must every employee spouse be a valid employee?
For the data shown in Figure 4.18, the correct answer is “Yes.” Another way to frame this question is to consider
whether or not every value provided for the EMP_SPOUSE attribute must match some value in the EMP_NUM
attribute.
In practical terms, both participation and referential integrity involve the values used as primary key/foreign key to
implementtherelationship.Referentialintegrityrequiresthatthevaluesintheforeignkeycorrespondtovaluesinthe
primarykey.Inonedirection,participationconsiderswhetherornottheforeignkeycancontainanull.InFigure4.18,

## Page 151

ENTITY RELATIONSHIP (ER) MODELING 121
for example, employee Robert Delaney is not required to have a value in EMP_SPOUSE. In the other direction,
participation considers whether or not every value in the primary key must appear as a value in the foreign key. In
Figure4.18,forexample,employeeRobertDelaney’svalueforEMP_NUM(348)isnotrequiredtoappearasavalue
in EMP_SPOUSE for any other employee.
4.1.11 Associative (Composite) Entities
IntheoriginalERMdescribedbyChen,relationshipsdonotcontainattributes.YoushouldrecallfromChapter3that
therelationalmodelgenerallyrequirestheuseof1:Mrelationships.(Also,recallthatthe1:1relationshiphasitsplace,
but it should be used with caution and proper justification.) If M:N relationships are encountered, you must create a
bridge between the entities that display such relationships. The associative entity is used to implement a M:N
relationship between two or more entities. This associative entity (also known as a composite or bridge entity) is
composedoftheprimarykeysofeachoftheentitiestobeconnected.AnexampleofsuchabridgeisshowninFigure
4.23. The Crow’s Foot notation does not identify the composite entity as such. Instead, the composite entity is
identifiedbythesolidrelationshiplinebetweentheparentandchildentities,therebyindicatingthepresenceofastrong
(identifying) relationship.
FIGURE Converting the M:N relationship into two 1:M relationships
4.23
Table name: STUDENT Database name: Ch04_CollegeTry
Table name: ENROLL
Table name: CLASS
Note that the composite ENROLL entity in Figure 4.23 is existence-dependent on the other two entities; the
composition of the ENROLL entity is based on the primary keys of the entities that are connected by the composite
entity. The composite entity may also contain additional attributes that play no role in the connective process. For
example, although the entity must be composed of at least the STUDENT and CLASS primary keys, it may also
includesuchadditionalattributesasgrades,absences,andotherdatauniquelyidentifiedbythestudent’sperformance
in a specific class.
Finally, keep in mind that the ENROLL table’s key (CLASS_CODE and STU_NUM) is composed entirely of the
primarykeysoftheCLASSandSTUDENTtables.Therefore,nonullentriesarepossibleintheENROLLtable’skey
attributes.
ImplementingthesmalldatabaseshowninFigure4.23requiresthatyoudefinetherelationshipsclearly.Specifically,
you must know the “1” and the “M” sides of each relationship, and you must know whether the relationships are
mandatory or optional. For example, note the following points:

## Page 152

122 CHAPTER 4
(cid:2) A class may exist (at least at the start of registration) even though it contains no students. Therefore, if you
examine Figure 4.24, an optional symbol should appear on the STUDENT side of the M:N relationship
between STUDENT and CLASS.
You might argue that to be classified as a STUDENT, a person must be enrolled in at least one CLASS.
Therefore, CLASS is mandatory to STUDENT from a purely conceptual point of view. However, when a
studentisadmittedtocollege,thatstudenthasnot(yet)signedupforanyclasses.Therefore,atleastinitially,
CLASS is optional to STUDENT. Note that the practical considerations in the data environment help dictate
the use of optionalities. If CLASS is not optional to STUDENT—from a database point of view—a class
assignment must be made when the student is admitted. But that’s not how the process actually works, and
the database design must reflect this. In short, the optionality reflects practice.
FIGURE The M:N relationship between STUDENT and CLASS
4.24
Because the M:N relationship between STUDENT and CLASS is decomposed into two 1:M relationships
throughENROLL,theoptionalitiesmustbetransferredtoENROLL.(SeeFigure4.25.)Inotherwords,itnow
becomespossibleforaclassnottooccurinENROLLifnostudenthassignedupforthatclass.Becauseaclass
need not occur in ENROLL, the ENROLL entity becomes optional to CLASS. And because the ENROLL
entity is created before any students have signed up for a class, the ENROLL entity is also optional to
STUDENT, at least initially.
FIGURE A composite entity in an ERD
4.25
(cid:2) As students begin to sign up for their classes, they will be entered into the ENROLL entity. Naturally, if a
studenttakesmorethanoneclass,thatstudentwilloccurmorethanonceinENROLL.Forexample,notethat
in the ENROLL table in Figure 4.23, STU_NUM = 321452 occurs three times. On the other hand, each
studentoccursonlyonceintheSTUDENTentity.(NotethattheSTUDENTtableinFigure4.23hasonlyone
STU_NUM = 321452 entry.) Therefore, in Figure 4.25, the relationship between STUDENT and ENROLL
is shown to be 1:M, with the M on the ENROLL side.

## Page 153

ENTITY RELATIONSHIP (ER) MODELING 123
(cid:2) As you can see in Figure 4.23, a class can occur more than once in the ENROLL table. For example,
CLASS_CODE = 10014 occurs twice. However, CLASS_CODE = 10014 occurs only once in the CLASS
tabletoreflectthattherelationshipbetweenCLASSandENROLLis1:M.NotethatinFigure4.25,theMis
located on the ENROLL side, while the 1 is located on the CLASS side.
4.2 DEVELOPING AN ER DIAGRAM
The process of database design is an iterative rather than a linear or sequential process. The verb iterate means “to
doagainorrepeatedly.”Aniterativeprocess is,thus,onebasedonrepetitionofprocessesandprocedures.Building
an ERD usually involves the following activities:
(cid:2) Create a detailed narrative of the organization’s description of operations.
(cid:2) Identify the business rules based on the description of operations.
(cid:2) Identify the main entities and relationships from the business rules.
(cid:2) Develop the initial ERD.
(cid:2) Identify the attributes and primary keys that adequately describe the entities.
(cid:2) Revise and review the ERD.
Duringthereviewprocess,itislikelythatadditionalobjects,attributes,andrelationshipswillbeuncovered.Therefore,
thebasicERMwillbemodifiedtoincorporatethenewlydiscoveredERcomponents.Subsequently,anotherroundof
reviewsmightyieldadditionalcomponentsorclarificationoftheexistingdiagram.Theprocessisrepeateduntiltheend
users and designers agree that the ERD is a fair representation of the organization’s activities and functions.
During the design process, the database designer does not depend simply on interviews to help define entities,
attributes,andrelationships.Asurprisingamountofinformationcanbegatheredbyexaminingthebusinessformsand
reports that an organization uses in its daily operations.
To illustrate the use of the iterative process that ultimately yields a workable ERD, let’s start with an initial interview
with the Tiny College administrators. The interview process yields the following business rules:
1. TinyCollege(TC)isdividedintoseveralschools:aschoolofbusiness,aschoolofartsandsciences,aschool
ofeducation,andaschoolofappliedsciences.Eachschoolisadministeredbyadeanwhoisaprofessor.Each
professor can be the dean of only one school, and a professor is not required to be the dean of any school.
Therefore, a 1:1 relationship exists between PROFESSOR and SCHOOL. Note that the cardinality can be
expressed by writing (1,1) next to the entity PROFESSOR and (0,1) next to the entity SCHOOL.
2. Each school comprises several departments. For example, the school of business has an accounting
department, a management/marketing department, an economics/finance department, and a computer
information systems department. Note again the cardinality rules: The smallest number of departments
operatedbyaschoolisone,andthelargestnumberofdepartmentsisindeterminate(N).Ontheotherhand,
each department belongs to only a single school; thus, the cardinality is expressed by (1,1). That is, the
minimum number of schools that a department belongs to is one, as is the maximum number. Figure 4.26
illustrates these first two business rules.

## Page 154

124 CHAPTER 4
FIGURE The first Tiny College ERD segment
4.26
Note
Itisagainappropriatetoevaluatethereasonformaintainingthe1:1relationshipbetween PROFESSORand
SCHOOLinthePROFESSOR isdeanofSCHOOLrelationship.Itisworthrepeatingthattheexistenceof1:1
relationshipsoftenindicatesamisidentificationofattributesasentities.Inthiscase,the1:1relationshipcould
easily be eliminated by storing the dean’s attributes in the SCHOOL entity. This solution would also make it
easiertoanswerthequeries,“Whoisthedean?”and“Whatarethatdean’scredentials?”Thedownsideofthis
solutionisthatitrequirestheduplicationofdatathatarealreadystoredinthePROFESSORtable,thussetting
thestageforanomalies.However,becauseeachschoolisrunbyasingledean,theproblemofdataduplication
is rather minor. The selection of one approach over another often depends on information requirements,
transaction speed, and the database designer’s professional judgment. In short, do not use 1:1 relationships
lightly,andmakesurethateach1:1relationshipwithinthedatabasedesignisdefensible.
3. Eachdepartmentmayoffercourses.Forexample,themanagement/marketingdepartmentofferscoursessuch
asIntroductiontoManagement,PrinciplesofMarketing,andProductionManagement.TheERDsegmentfor
thisconditionisshowninFigure4.27.NotethatthisrelationshipisbasedonthewayTinyCollegeoperates.
If,forexample,TinyCollegehadsomedepartmentsthatwereclassifiedas“researchonly,”thosedepartments
would not offer courses; therefore, the COURSE entity would be optional to the DEPARTMENT entity.
4. The relationship between COURSE and CLASS was illustrated in Figure 4.9. Nevertheless, it is worth
repeatingthataCLASSisasectionofaCOURSE.Thatis,adepartmentmayofferseveralsections(classes)
of the same database course. Each of those classes is taught by a professor at a given time in a given place.
In short, a 1:M relationship exists between COURSE and CLASS. However, because a course may exist in
Tiny College’s course catalog even when it is not offered as a class in a current class schedule, CLASS is
optional to COURSE. Therefore, the relationship between COURSE and CLASS looks like Figure 4.28.

## Page 155

ENTITY RELATIONSHIP (ER) MODELING 125
FIGURE The second Tiny College ERD segment
4.27
FIGURE The third Tiny College ERD segment
4.28
5. Each department should have one or more professors assigned to it. One and only one of those professors
chairs the department, and no professor is required to accept the chair position. Therefore, DEPARTMENT
isoptionaltoPROFESSORinthe“chairs”relationship.ThoserelationshipsaresummarizedintheERsegment
shown in Figure 4.29.
FIGURE The fourth Tiny College ERD segment
4.29
6. Each professor may teach up to four classes; each class is a section of a course. A professor may also be on
a research contract and teach no classes at all. The ERD segment in Figure 4.30 depicts those conditions.
7. Astudentmayenrollinseveralclassesbuttakeseachclassonlyonceduringanygivenenrollmentperiod.For
example, during the current enrollment period, a student may decide to take five classes—Statistics,
Accounting,English,Database,andHistory—butthatstudentwouldnotbeenrolledinthesameStatisticsclass
fivetimesduringtheenrollmentperiod!Eachstudentmayenrollinuptosixclasses,andeachclassmayhave
upto35students,thuscreatinganM:NrelationshipbetweenSTUDENTandCLASS.BecauseaCLASScan

## Page 156

126 CHAPTER 4
FIGURE The fifth Tiny College ERD segment
4.30
initially exist (at the start of the enrollment period) even though no students have enrolled in it, STUDENT is
optionaltoCLASSintheM:Nrelationship.ThisM:Nrelationshipmustbedividedintotwo1:Mrelationships
throughtheuseoftheENROLLentity,shownintheERDsegmentinFigure4.31.Butnotethattheoptional
symbol is shown next to ENROLL. If a class exists but has no students enrolled in it, that class doesn’t occur
intheENROLLtable.NotealsothattheENROLLentityisweak:itisexistence-dependent,andits(composite)
PK is composed of the PKs of the STUDENT and CLASS entities. You can add the cardinalities (0,6) and
(0,35) next to the ENROLL entity to reflect the business rule constraints, as shown in Figure 4.31. (Visio
Professional does not automatically generate such cardinalities, but you can use a text box to accomplish
that task.)
FIGURE The sixth Tiny College ERD segment
4.31
8. Each department has several (or many) students whose major is offered by that department. However, each
student has only a single major and is, therefore, associated with a single department. (See Figure 4.32.)
However, in the Tiny College environment, it is possible—at least for a while—for a student not to declare a
major field of study. Such a student would not be associated with a department; therefore, DEPARTMENT is
optionaltoSTUDENT.Itisworthrepeatingthattherelationshipsbetweenentitiesandtheentitiesthemselves
reflect the organization’s operating environment. That is, the business rules define the ERD components.
9. Eachstudenthasanadvisorinhisorherdepartment;eachadvisorcounselsseveralstudents.Anadvisorisalso
a professor, but not all professors advise students. Therefore, STUDENT is optional to PROFESSOR in the
“PROFESSOR advises STUDENT” relationship. (See Figure 4.33.)
10. As you can see in Figure 4.34, the CLASS entity contains a ROOM_CODE attribute. Given the naming
conventions, it is clear that ROOM_CODE is an FK to another entity. Clearly, because a class is taught in a
room, it is reasonable to assume that the ROOM_CODE in CLASS is the FK to an entity named ROOM. In
turn,eachroomislocatedinabuilding.SothelastTinyCollegeERDiscreatedbyobservingthataBUILDING

## Page 157

ENTITY RELATIONSHIP (ER) MODELING 127
FIGURE The seventh Tiny College ERD segment
4.32
FIGURE The eighth Tiny College ERD segment
4.33
can contain many ROOMs, but each ROOM is found in a single BUILDING. In this ERD segment, it is clear
thatsomebuildingsdonotcontain(class)rooms.Forexample,astoragebuildingmightnotcontainanynamed
rooms at all.
FIGURE The ninth Tiny College ERD segment
4.34
Using the preceding summary, you can identify the following entities:
SCHOOL COURSE
DEPARTMENT CLASS
PROFESSOR STUDENT
BUILDING ROOM
ENROLL (the associative entity between STUDENT and CLASS)

## Page 158

128 CHAPTER 4
Onceyouhavediscoveredtherelevantentities,youcandefinetheinitialsetofrelationshipsamongthem.Next,you
describe the entity attributes. Identifying the attributes of the entities helps you to better understand the relationships
among entities. Table 4.4 summarizes the ERM’s components, and names the entities and their relations.
TABLE Components of the ERM
4.4
ENTITY RELATIONSHIP CONNECTIVITY ENTITY
SCHOOL operates 1:M DEPARTMENT
DEPARTMENT has 1:M STUDENT
DEPARTMENT employs 1:M PROFESSOR
DEPARTMENT offers 1:M COURSE
COURSE generates 1:M CLASS
PROFESSOR isdeanof 1:1 SCHOOL
PROFESSOR chairs 1:1 DEPARTMENT
PROFESSOR teaches 1:M CLASS
PROFESSOR advises 1:M STUDENT
STUDENT enrollsin M:N CLASS
BUILDING contains 1:M ROOM
ROOM isusedfor 1:M CLASS
Note:ENROLListhecompositeentitythatimplementstheM:Nrelationship“STUDENTenrollsinCLASS.”
You must also define the connectivity and cardinality for the just-discovered relations based on the business rules.
However,toavoidcrowdingthediagram,thecardinalitiesarenotshown.Figure4.35showstheCrow’sFootERDfor
Tiny College. Note that this is an implementation-ready model. Therefore it shows the ENROLL composite entity.
Figure4.36showstheconceptualUMLclassdiagramforTinyCollege.NotethatthisclassdiagramdepictstheM:N
relationship between STUDENT and CLASS. Figure 4.37 shows the implementation-ready UML class diagram for
Tiny College (note that the ENROLL composite entity is shown in this class diagram.
4.3 DATABASE DESIGN CHALLENGES: CONFLICTING GOALS
Databasedesignersoftenmustmakedesigncompromisesthataretriggeredbyconflictinggoals,suchasadherenceto
design standards (design elegance), processing speed, and information requirements.
(cid:2) Design standards. The database design must conform to design standards. Such standards have guided you
in developing logical structures that minimize data redundancies, thereby minimizing the likelihood that
destructive data anomalies will occur. You have also learned how standards prescribe avoiding nulls to the
greatest extent possible. In fact, you have learned that design standards govern the presentation of all
components within the database design. In short, design standards allow you to work with well-defined
components and to evaluate the interaction of those components with some precision. Without design
standards, it is nearly impossible to formulate a proper design process, to evaluate an existing design, or to
trace the likely logical impact of changes in design.
(cid:2) Processing speed. In many organizations, particularly those generating large numbers of transactions, high
processing speeds are often a top priority in database design. High processing speed means minimal access
time,whichmaybeachievedbyminimizingthenumberandcomplexityoflogicallydesirablerelationships.For
example,a“perfect”designmightusea1:1relationshiptoavoidnulls,whileahighertransaction-speeddesign
mightcombinethetwotablestoavoidtheuseofanadditionalrelationship,usingdummyentriestoavoidthe
nulls.Ifthefocusisondata-retrievalspeed,youmightalsobeforcedtoincludederivedattributesinthedesign.
(cid:2) Informationrequirements.Thequestfortimelyinformationmightbethefocusofdatabasedesign.Complex
informationrequirementsmaydictatedatatransformations,andtheymayexpandthenumberofentitiesand

## Page 159

ENTITY RELATIONSHIP (ER) MODELING 129
FIGURE The completed Tiny College ERD
4.35
attributeswithinthedesign.Therefore,thedatabasemayhavetosacrificesomeofits“clean”designstructures
and/orsomeofitshightransactionspeedtoensuremaximuminformationgeneration.Forexample,suppose

## Page 160

130 CHAPTER 4
FIGURE The conceptual UML class diagram for Tiny College
4.36
thatadetailedsalesreportmustbegeneratedperiodically.Thesalesreportincludesallinvoicesubtotals,taxes,
andtotals;eventheinvoicelinesincludesubtotals.Ifthesalesreportincludeshundredsofthousands(oreven
millions)ofinvoices,computingthetotals,taxes,andsubtotalsislikelytotakesometime.Ifthosecomputations
had been made and the results had been stored as derived attributes in the INVOICE and LINE tables at the
timeofthetransaction,thereal-timetransactionspeedmighthavedeclined.Butthatlossofspeedwouldonly
benoticeableifthereweremanysimultaneoustransactions.Thecostofaslightlossoftransactionspeedatthe
frontendandtheadditionofmultiplederivedattributesislikelytopayoffwhenthesalesreportsaregenerated
(not to mention the fact that it will be simpler to generate the queries).
A design that meets all logical requirements and design conventions is an important goal. However, if this perfect
designfailstomeetthecustomer’stransactionspeedand/orinformationrequirements,thedesignerwillnothavedone
a proper job from the end user’s point of view. Compromises are a fact of life in the real world of database design.
Evenwhilefocusingontheentities,attributes,relationships,andconstraints,thedesignershouldbeginthinkingabout
end-user requirements such as performance, security, shared access, and data integrity. The designer must consider
processing requirements and verify that all update, retrieval, and deletion options are available. Finally, a design is of
little value unless the end product is capable of delivering all specified query and reporting requirements.

## Page 161

ENTITY RELATIONSHIP (ER) MODELING 131
FIGURE The implementation-ready UML class diagram for Tiny College
4.37
You are quite likely to discover that even the best design process produces an ERD that requires further changes
mandatedbyoperationalrequirements.Suchchangesshouldnotdiscourageyoufromusingtheprocess.ERmodeling
is essential in the development of a sound design that is capable of meeting the demands of adjustment and growth.
UsingERDsyieldsperhapstherichestbonusofall:athoroughunderstandingofhowanorganizationreallyfunctions.
Thereareoccasionaldesignandimplementationproblemsthatdonotyield“clean”implementationsolutions.Toget
asenseofthedesignandimplementationchoicesadatabasedesignerfaces,let’srevisitthe1:1recursiverelationship
“EMPLOYEE is married to EMPLOYEE” first examined in Figure 4.18. Figure 4.38 shows three different ways of
implementing such a relationship.
Note that the EMPLOYEE_V1 table in Figure 4.38 is likely to yield data anomalies. For example, if Anne Jones
divorces Anton Shapiro, two records must be updated—by setting the respective EMP_SPOUSE values to null—to
properlyreflectthatchange.Ifonlyonerecordisupdated,inconsistentdataoccur.Theproblembecomesevenworse
ifseveralofthedivorcedemployeesthenmarryeachother.Inaddition,thatimplementationalsoproducesundesirable
nulls for employees who are not married to other employees in the company.
Another approach would be to create a new entity shown as MARRIED_V1 in a 1:M relationship with EMPLOYEE.
(See Figure 4.38.) This second implementation does eliminate the nulls for employees who are not married to
somebody working for the same company. (Such employees would not be entered in the MARRIED_V1 table.)
However,thisapproachstillyieldspossibleduplicatevalues.Forexample,themarriagebetweenemployees345and

## Page 162

132 CHAPTER 4
FIGURE Various implementations of the 1:1 recursive relationship
4.38
Table name: EMPLOYEE_V1 Database name: Ch04_PartCo
First implementation
Table name: EMPLOYEE Table name: MARRIED_V1
Second implementation
Table name: MARRIAGE Table name: MARPART Table name: EMPLOYEE
The relational diagram for the third implementation
Third implementation
347maystillappeartwice,onceas345,347andonceas347,345.(Sinceeachofthosepermutationsisuniquethe
first time it appears, the creation of a unique index will not solve the problem.)
As you can see, the first two implementations yield several problems:
(cid:2) Both solutions use synonyms. The EMPLOYEE_V1 table uses EMP_NUM and EMP_SPOUSE to refer to an
employee. The MARRIED_V1 table uses the same synonyms.
(cid:2) Both solutions are likely to produce inconsistent data. For example, it is possible to enter employee 345 as
married to employee 347 and to enter employee 348 as married to employee 345.
(cid:2) Both solutions allow data entries to show one employee married to several other employees. For example, it
is possible to have data pairs such as 345,347 and 348,347 and 349,347, none of which will violate entity
integrity requirements, because they are all unique.
Athirdapproachwouldbetohavetwonewentities,MARRIAGEandMARPART,ina1:Mrelationship.MARPART
contains the EMP_NUM foreign key to EMPLOYEE. (See the relational diagram in Figure 4.38.) But even this
approach has issues. It requires the collection of additional data regarding the employees’ marriage—the marriage

## Page 163

ENTITY RELATIONSHIP (ER) MODELING 133
date. If the business users do not need this data, then requiring them to collect it would be inappropriate. To ensure
thatanemployeeoccursonlyonceinanygivenmarriage,youwouldhavetocreateauniqueindexontheEMP_NUM
attributeintheMARPARTtable.Anotherpotentialproblemwiththissolutionisthatthedatabaseimplementationwill
allow more than two employees to “participate” in the same marriage.
As you can see, a recursive 1:1 relationship yields many different solutions with varying degrees of effectiveness and
adherencetobasicdesignprinciples.Anyoftheabovesolutionswouldlikelyinvolvethecreationofprogramcodeto
help ensure the integrity and consistency of the data. In a later chapter, we will examine the creation of database
triggersthatcandoexactlythat.Yourjobasadatabasedesigneristouseyourprofessionaljudgmenttoyieldasolution
that meets the requirements imposed by business rules, processing requirements, and basic design principles.
Finally, document, document, and document! Put all design activities in writing. Then review what you’ve written.
Documentation not only helps you stay on track during the design process, but also enables you (or those following
you) to pick up the design thread when the time comes to modify the design. Although the need for documentation
shouldbeobvious,oneofthemostvexingproblemsindatabaseandsystemsanalysisworkisthatthe“putitinwriting”
rule is often not observed in all of the design and implementation stages. The development of organizational
documentation standards is a very important aspect of ensuring data compatibility and coherence.

## Page 164

134 CHAPTER 4
S u m m a r y
◗
TheERMusesERDstorepresenttheconceptualdatabaseasviewedbytheenduser.TheERM’smaincomponents
areentities,relationships,andattributes.TheERDalsoincludesconnectivityandcardinalitynotations.AnERDcan
also show relationship strength, relationship participation (optional or mandatory), and degree of relationship
(unary, binary, ternary, etc.).
◗
Connectivitydescribestherelationshipclassification(1:1,1:M,orM:N).Cardinalityexpressesthespecificnumber
ofentityoccurrencesassociatedwithanoccurrenceofarelatedentity.Connectivitiesandcardinalitiesareusually
based on business rules.
◗
In the ERM, an M:N relationship is valid at the conceptual level. However, when implementing the ERM in a
relationaldatabase,theM:Nrelationshipmustbemappedtoasetof1:Mrelationshipsthroughacompositeentity.
◗
ERDsmaybebasedonmanydifferentERMs.However,regardlessofwhichmodelisselected,themodelinglogic
remains the same. Because no ERM can accurately portray all real-world data and action constraints, application
software must be used to augment the implementation of at least some of the business rules.
◗
UnifiedModelingLanguage(UML)classdiagramsareusedtorepresentthestaticdatastructuresinadatamodel.
The symbols used in the UML class and ER diagrams are very similar. The UML class diagrams can be used to
depict data models at the conceptual or implementation abstraction levels.
◗
Databasedesigners,nomatterhowwelltheyareabletoproducedesignsthatconformtoallapplicablemodeling
conventions,areoftenforcedtomakedesigncompromises.Thosecompromisesarerequiredwhenendusershave
vital transaction-speed and/or information requirements that prevent the use of “perfect” modeling logic and
adherence to all modeling conventions. Therefore, database designers must use their professional judgment to
determine how and to what extent the modeling conventions are subject to modification. To ensure that their
professionaljudgmentsaresound,databasedesignersmusthavedetailedandin-depthknowledgeofdata-modeling
conventions. It is also important to document the design process from beginning to end, which helps keep the
design process on track and allows for easy modifications down the road.
K e y T e r ms
binary relationship, 116 mandatory participation, 113 required attribute, 101
cardinality, 107 multivalued attributes, 103 simple attribute, 103
composite attribute, 103 non-identifying relationship, 109 single-valued attribute, 103
composite identifier, 102 optional attribute, 101 strong entity, 108
connectivity, 107 optional participation, 113 strong relationship, 110
derived attribute, 105 participants, 105 ternary relationship, 116
existence-dependent, 108 recursive relationship, 116 unary relationship, 116
existence-independent, 108 regular entity, 108 weak entity, 110
identifiers, 101 relationship degree, 116 weak relationship, 109
identifying relationship, 110
iterative process, 123

## Page 165

ENTITY RELATIONSHIP (ER) MODELING 135
O n l i n e C o n t e n t
AnswerstoselectedReviewQuestionsandProblemsforthischapterarecontainedinthePremiumWebsitefor
thisbook.
R e v ie w Q u e st i o ns
1. Whattwoconditionsmustbemetbeforeanentitycanbeclassifiedasaweakentity?Giveanexampleofaweak
entity.
2. What is a strong (or identifying) relationship, and how is it depicted in a Crow’s Foot ERD?
3. Given the business rule “an employee may have many degrees,” discuss its effect on attributes, entities, and
relationships. (Hint: Remember what a multivalued attribute is and how it might be implemented.)
4. What is a composite entity, and when is it used?
5. Suppose you are working within the framework of the conceptual model in Figure Q4.5.
FIGURE The conceptual model for Question 5
Q4.5
Given the conceptual model in Figure Q4.5:
a. Write the business rules that are reflected in it.
b. Identify all of the cardinalities.
6. What is a recursive relationship? Give an example.
7. How would you (graphically) identify each of the following ERM components in a Crow’s Foot notation?
a. an entity
b. the cardinality (0,N)
c. a weak relationship
d. a strong relationship
8. Discuss the difference between a composite key and a composite attribute. How would each be indicated in
an ERD?
9. What two courses of action are available to a designer encountering a multivalued attribute?

## Page 166

136 CHAPTER 4
10. What is a derived attribute? Give an example.
11. How is a relationship between entities indicated in an ERD? Give an example, using the Crow’s Foot notation.
12. Discuss two ways in which the 1:M relationship between COURSE and CLASS can be implemented. (Hint:
Think about relationship strength.)
13. HowisacompositeentityrepresentedinanERD,andwhatisitsfunction?IllustratetheCrow’sFootnotation.
14. What three (often conflicting) database requirements must be addressed in database design?
15. Briefly, but precisely, explain the difference between single-valued attributes and simple attributes. Give an
example of each.
16. What are multivalued attributes, and how can they be handled within the database design?
The next four questions are based on the ERD in Figure Q4.17.
FIGURE The ERD for Questions 17–20
Q4.17
17. Write the 10 cardinalities that are appropriate for this ERD.
18. Write the business rules reflected in this ERD.
19. What two attributes must be contained in the composite entity between STORE and PRODUCT? Use proper
terminology in your answer.
20. Describe precisely the composition of the DEPENDENT weak entity’s primary key. Use proper terminology in
your answer.
21. Thelocalcityyouthleagueneedsadatabasesystemtohelptrackchildrenwhosignuptoplaysoccer.Dataneed
to be kept on each team and the children who will be playing on each team and their parents. Also, data need
to be kept on the coaches for each team.
Draw the data model described below.
Entities required: Team, Player, Coach, and Parent.
Attributes required:
Team: Team ID number, Team name, and Team colors.
Player: Player ID number, Player first name, Player last name, and Player age.
Coach: Coach ID number, Coach first name, Coach last name, and Coach home phone number.
Parent: Parent ID number, Parent last name, Parent first name, Home phone number, and Home Address
(Street, City, State, and Zip Code).

## Page 167

ENTITY RELATIONSHIP (ER) MODELING 137
The following relationships must be defined:
(cid:2) Team is related to Player.
(cid:2) Team is related to Coach.
(cid:2) Player is related to Parent.
Connectivities and participations are defined as follows:
(cid:2) A Team may or may not have a Player.
(cid:2) A Player must have a Team.
(cid:2) A Team may have many Players.
(cid:2) A Player has only one Team.
(cid:2) A Team may or may not have a Coach.
(cid:2) A Coach must have a Team.
(cid:2) A Team may have many Coaches.
(cid:2) A Coach has only one Team.
(cid:2) A Player must have a Parent.
(cid:2) A Parent must have a Player.
(cid:2) A Player may have many Parents.
(cid:2) A Parent may have many Players.
P r o b le m s
1. Use the following business rules to create a Crow’s Foot ERD. Write all appropriate connectivities and
cardinalities in the ERD.
a. A department employs many employees, but each employee is employed by only one department.
b. Some employees, known as “rovers,” are not assigned to any department.
c. A division operates many departments, but each department is operated by only one division.
d. An employee may be assigned many projects, and a project may have many employees assigned to it.
e. A project must have at least one employee assigned to it.
f. Oneoftheemployeesmanageseachdepartment,andeachdepartmentismanagedbyonlyoneemployee.
g. One of the employees runs each division, and each division is run by only one employee.
2. The Jonesburgh County Basketball Conference (JCBC) is an amateur basketball association. Each city in the
countyhasoneteamasitsrepresentative.Eachteamhasamaximumof12playersandaminimumof9players.
Eachteamalsohasuptothreecoaches(offensive,defensive,andphysicaltrainingcoaches).Duringtheseason,
each team plays two games (home and visitor) against each of the other teams. Given those conditions, do the
following:
a. Identify the connectivity of each relationship.
b. Identify the type of dependency that exists between CITY and TEAM.
c. Identify the cardinality between teams and players and between teams and city.
d. Identify the dependency between coach and team and between team and player.
e. Draw the Chen and Crow’s Foot ERDs to represent the JCBC database.
f. Draw the UML class diagram to depict the JCBC database.
3. Create an ERD based on the Crow’s Foot notation, using the following requirements:
a. AnINVOICEiswrittenbyaSALESREP.Eachsalesrepresentativecanwritemanyinvoices,buteachinvoice
is written by a single sales representative.
b. The INVOICE is written for a single CUSTOMER. However, each customer can have many invoices.

## Page 168

138 CHAPTER 4
c. An INVOICE can include many detail lines (LINE), each of which describes one product bought by the
customer.
d. The product information is stored in a PRODUCT entity.
e. The product’s vendor information is found in a VENDOR entity.
4. The Hudson Engineering Group (HEG) has contacted you to create a conceptual model whose application will
meettheexpecteddatabaserequirementsforthecompany’strainingprogram.TheHEGadministratorgivesyou
thedescription(seebelow)ofthetraininggroup’soperatingenvironment.(Hint:Someofthefollowingsentences
identify the volume of data rather than cardinalities. Can you tell which ones?)
TheHEGhas12instructorsandcanhandleupto30traineesperclass.HEGoffersfiveAdvancedTechnology
courses, each of which may generate several classes. If a class has fewer than 10 trainees, it will be canceled.
Therefore, it is possible for a course not to generate any classes. Each class is taught by one instructor. Each
instructormayteachuptotwoclassesormaybeassignedtodoresearchonly.Eachtraineemaytakeuptotwo
classes per year.
Given that information, do the following:
a. Define all of the entities and relationships. (Use Table 4.4 as your guide.)
b. Describe the relationship between instructor and class in terms of connectivity, cardinality, and existence
dependence.
5. Automata, Inc. produces specialty vehicles by contract. The company operates several departments, each of
which builds a particular vehicle, such as a limousine, a truck, a van, or an RV.
(cid:2) Before a new vehicle is built, the department places an order with the purchasing department to request
specific components. Automata’s purchasing department is interested in creating a database to keep track
of orders and to accelerate the process of delivering materials.
(cid:2) The order received by the purchasing department may contain several different items. An inventory is
maintained so that the most frequently requested items are delivered almost immediately. When an order
comesin,itischeckedtodeterminewhethertherequesteditemisininventory.Ifanitemisnotininventory,
it must be ordered from a supplier. Each item may have several suppliers.
Given that functional description of the processes encountered at Automata’s purchasing department, do the
following:
a. Identify all of the main entities.
b. Identify all of the relations and connectivities among entities.
c. Identify the type of existence dependence in all the relationships.
d. Give at least two examples of the types of reports that can be obtained from the database.
6. United Helpers is a nonprofit organization that provides aid to people after natural disasters. Based on the
following brief description of operations, create the appropriate fully labeled Crow’s Foot ERD.
(cid:2) Individualsvolunteertheirtimetocarryoutthetasksoftheorganization.Thename,address,andtelephone
numberforeachvoluteeraretracked.Eachvolunteermaybeassignedtoseveraltasksduringthetimethat
heorsheisdoingvolunteerwork,andsometasksrequiremanyvolunteers.Itispossibleforavolunteerto
be in the system without having been assigned a task yet. It is possible to have tasks that no one has been
assigned.Whenavolunteerisassignedtoatask,thesystemshouldtrackthestarttimeandendtimeofthat
assignment.
(cid:2) For each task, there is a task code, task description, task type, and task status. For example, there may be
ataskwithtaskcode“101,”adescriptionof“answerthetelephone,”atypeof“recurring,”andastatusof
“ongoing.”Therecouldbeanothertaskwithacodeof“102,”adescriptionof“prepare5000packagesof
basic medical supplies,” a type of “packing,” and a status of “open.”

## Page 169

ENTITY RELATIONSHIP (ER) MODELING 139
(cid:2) Foralltasksoftype“packing,”thereisapackinglistthatspecifiesthecontentsofthepackages.Thereare
many different packing lists to produce different packages, such as basic medical packages, child-care
packages, food packages, etc. Each packing list has a packing list ID number, a packing list name, and a
packing list description, which describes the items that ideally go into making that type of package. Every
packing task is associated with only one packing list. A packing list may not be associated with any tasks,
or may be associated with many tasks. Tasks that are not packing tasks are not associated with any
packing list.
(cid:2) Packingtasksresultinthecreationofpackages.Eachindividualpackageofsuppliesthatisproducedbythe
organizationistracked.EachpackageisassignedanIDnumber.Thedatethepackagewascreatedandthe
totalweightofthepackagearerecorded.Agivenpackageisassociatedwithonlyonetask.Sometasks(e.g.,
“answerthephones”)willnothaveproducedanypackages,whileothertasks(e.g.,“prepare5000packages
of basic medical supplies”) will be associated with many packages.
(cid:2) Thepackinglistdescribestheidealcontentsofeachpackage,butitisnotalwayspossibletoincludetheideal
number of each item. Therefore, the actual items included in each package should be tracked. A package
can contain many different items, and a given item can be used in many different packages.
(cid:2) Foreachitemthattheorganizationprovides,thereisanitemIDnumber,itemdescription,itemvalue,and
item quantity on hand stored in the system. Along with tracking the actual items that are placed in each
package, the quantity of each item placed in the package must be tracked too. For example, a packing list
may state that basic medical packages should include 100 bandages, 4 bottles of iodine, and 4 bottles of
hydrogenperoxide.However,becauseofthelimitedsupplyofitems,agivenpackagemayincludeonly10
bandages, 1 bottle of iodine, and no hydrogen peroxide. The fact that this package includes bandages and
iodineneedstoberecordedalongwiththequantityofeachthatisincluded.Itispossiblefortheorganization
tohaveitemsdonatedthathavenotbeenincludedinanypackageyet,buteverypackagewillcontainatleast
one item.
7. UsingtheCrow’sFootnotation,createanERDthatcanbeimplementedforamedicalclinic,usingthefollowing
business rules:
(cid:2) A patient can make many appointments with one or more doctors in the clinic, and a doctor can accept
appointments with many patients. However, each appointment is made with only one doctor and one
patient.
(cid:2) Emergency cases do not require an appointment. However, for appointment management purposes, an
emergency is entered in the appointment book as “unscheduled.”
(cid:2) Ifkept,anappointmentyieldsavisitwiththedoctorspecifiedintheappointment.Thevisityieldsadiagnosis
and, when appropriate, treatment.
(cid:2) With each visit, the patient’s records are updated to provide a medical history.
(cid:2) Each patient visit creates a bill. Each patient visit is billed by one doctor, and each doctor can bill many
patients.
(cid:2) Each bill must be paid. However, a bill may be paid in many installments, and a payment may cover more
than one bill.
(cid:2) A patient may pay the bill directly, or the bill may be the basis for a claim submitted to an insurance
company.
(cid:2) If the bill is paid by an insurance company, the deductible is submitted to the patient for payment.

## Page 170

140 CHAPTER 4
Note
ThefollowingcasesandadditionalproblemsfromtheInstructorOnlineCompanionmaybeusedasthebasis
forclassprojects.Theseproblemsillustratethechallengeoftranslatingadescriptionofoperationsintoasetof
business rules that will define the components for an ERD that can be successfully implemented. These
problems can also be used as the basis for discussions about the components and contents of a proper
description of operations. One of the things you must learn if you want to create databases that can be
successfully implemented is to separate the generic background material from the details that directly affect
databasedesign.Youmustalsokeepinmindthatmanyconstraintscannotbeincorporatedintothedatabase
design;instead,suchconstraintsarehandledbytheapplicationssoftware.
C as e s
8. The administrators of Tiny College are so pleased with your design and implementation of their student
registration/tracking system that they want you to expand the design to include the database for their motor
vehicle pool. A brief description of operations follows:
(cid:2) FacultymembersmayusethevehiclesownedbyTinyCollegeforofficiallysanctionedtravel.Forexample,
thevehiclesmaybeusedbyfacultymemberstotraveltooff-campuslearningcenters,totraveltolocations
atwhichresearchpapersarepresented,totransportstudentstoofficiallysanctionedlocations,andtotravel
forpublicservicepurposes.ThevehiclesusedforsuchpurposesaremanagedbyTinyCollege’sTravelFar
But Slowly (TFBS) Center.
(cid:2) Usingreservationforms,eachdepartmentcanreservevehiclesforitsfaculty,whoareresponsibleforfilling
out the appropriate trip completion form at the end of a trip. The reservation form includes the expected
departure date, vehicle type required, destination, and name of the authorized faculty member. The faculty
member arriving to pick up a vehicle must sign a checkout form to log out the vehicle and pick up a trip
completionform.(TheTFBSemployeewhoreleasesthevehicleforusealsosignsthecheckoutform.)The
faculty member’s trip completion form includes the faculty member’s identification code, the vehicle’s
identification,theodometerreadingsatthestartandendofthetrip,maintenancecomplaints(ifany),gallons
of fuel purchased (if any), and the Tiny College credit card number used to pay for the fuel. If fuel is
purchased, the credit card receipt must be stapled to the trip completion form. Upon receipt of the faculty
tripcompletionform,thefacultymember’sdepartmentisbilledatamileageratebasedonthevehicletype
(sedan, station wagon, panel truck, minivan, or minibus) used. (Hint: Do not use more entities than are
necessary. Remember the difference between attributes and entities!)
(cid:2) AllvehiclemaintenanceisperformedbyTFBS.Eachtimeavehiclerequiresmaintenance,amaintenancelog
entryiscompletedonaprenumberedmaintenancelogform.Themaintenancelogformincludesthevehicle
identification, a brief description of the type of maintenance required, the initial log entry date, the date on
whichthemaintenancewascompleted,andtheidentificationofthemechanicwhoreleasedthevehicleback
intoservice.(Onlymechanicswhohaveaninspectionauthorizationmayreleasethevehiclebackintoservice.)
(cid:2) As soon as the log form has been initiated, the log form’s number is transferred to a maintenance detail
form;thelogform’snumberisalsoforwardedtothepartsdepartmentmanager,whofillsoutapartsusage
form on which the maintenance log number is recorded. The maintenance detail form contains separate
lines for each maintenance item performed, for the parts used, and for identification of the mechanic who
performedthemaintenanceitem.Whenallmaintenanceitemshavebeencompleted,themaintenancedetail
formisstapledtothemaintenancelogform,themaintenancelogform’scompletiondateisfilledout,and
themechanicwhoreleasesthevehiclebackintoservicesignstheform.Thestapledformsarethenfiled,to
be used later as the source for various maintenance reports.

## Page 171

ENTITY RELATIONSHIP (ER) MODELING 141
(cid:2) TFBS maintains a parts inventory, including oil, oil filters, air filters, and belts of various types. The parts
inventoryischeckeddailytomonitorpartsusageandtoreorderpartsthatreachthe“minimumquantityon
hand” level. To track parts usage, the parts manager requires each mechanic to sign out the parts that are
usedtoperformeachvehicle’smaintenance;thepartsmanagerrecordsthemaintenancelognumberunder
which the part is used.
(cid:2) EachmonthTFBSissuesasetofreports.Thereportsincludethemileagedrivenbyvehicle,bydepartment,
and by faculty members within a department. In addition, various revenue reports are generated by vehicle
and department. A detailed parts usage report is also filed each month. Finally, a vehicle maintenance
summary is created each month.
Given that brief summary of operations, draw the appropriate (and fully labeled) ERD. Use the Chen
methodology to indicate entities, relationships, connectivities, and cardinalities.
9. During peak periods, Temporary Employment Corporation (TEC) places temporary workers in companies.
TEC’s manager gives you the following description of the business:
(cid:2) TEC has a file of candidates who are willing to work.
(cid:2) Ifthecandidatehasworkedbefore,thatcandidatehasaspecificjobhistory.(Naturally,nojobhistoryexists
if the candidate has never worked.) Each time the candidate works, one additional job history record is
created.
(cid:2) Each candidate has earned several qualifications. Each qualification may be earned by more than one
candidate. (For example, it is possible for more than one candidate to have earned a Bachelor of Business
AdministrationdegreeoraMicrosoftNetworkCertification.Andclearly,acandidatemayhaveearnedboth
a BBA and a Microsoft Network Certification.)
(cid:2) TEC offers courses to help candidates improve their qualifications.
(cid:2) Every course develops one specific qualification; however, TEC does not offer a course for every
qualification. Some qualifications have multiple courses that develop that qualification.
(cid:2) Somecoursescoveradvancedtopicsthatrequirespecificqualificationsasprerequisites.Somecoursescover
basic topics that do not require any prerequisite qualifications. A course can have several prerequisites. A
qualification can be a prerequisite for more than one course.
(cid:2) Courses are taught during training sessions. A training session is the presentation of a single course. Over
time,TECwilloffermanytrainingsessionsforeachcourse;however,newcoursesmaynothaveanytraining
sessions scheduled right away.
(cid:2) Candidates can pay a fee to attend a training session. A training session can accommodate several
candidates, although new training sessions will not have any candidates registered at first.
(cid:2) TEC also has a list of companies that request temporaries.
(cid:2) Each time a company requests a temporary employee, TEC makes an entry in the Openings folder. That
foldercontainsanopeningnumber,acompanyname,requiredqualifications,astartingdate,ananticipated
ending date, and hourly pay.
(cid:2) Each opening requires only one specific or main qualification.
(cid:2) When a candidate matches the qualification, the job is assigned, and an entry is made in the Placement
Recordfolder.Thatfoldercontainsanopeningnumber,acandidatenumber,thetotalhoursworked,etc.In
addition, an entry is made in the job history for the candidate.
(cid:2) An opening can be filled by many candidates, and a candidate can fill many openings.
(cid:2) TECusesspecialcodestodescribeacandidate’squalificationsforanopening.Thelistofcodesisshownin
Table P4.9.

## Page 172

142 CHAPTER 4
TABLE
P4.9
CODE DESCRIPTION
SEC-45 Secretarialwork,atleast45wordsperminute
SEC-60 Secretarialwork,atleast60wordsperminute
CLERK Generalclerkingwork
PRG-VB Programmer,VisualBasic
PRG-C++ Programmer,C++
DBA-ORA DatabaseAdministrator,Oracle
DBA-DB2 DatabaseAdministrator,IBMDB2
DBA-SQLSERV DatabaseAdministrator,MSSQLServer
SYS-1 SystemsAnalyst,level1
SYS-2 SystemsAnalyst,level2
NW-NOV NetworkAdministrator,Novellexperience
WD-CF WebDeveloper,ColdFusion
TEC’s management wants to keep track of the following entities:
COMPANY, OPENING, QUALIFICATION, CANDIDATE, JOB_HISTORY, PLACEMENT, COURSE, and
SESSION. Given that information, do the following:
a. Draw the Crow’s Foot ERDs for this enterprise.
b. Identify all necessary relationships.
c. Identify the connectivity for each relationship.
d. Identify the mandatory/optional dependencies for the relationships.
e. Resolve all M:N relationships.
10. Use the following description of the operations of the RC_Charter2 Company to complete this exercise.
(cid:2) The RC_Charter2 Company operates a fleet of aircraft under the Federal Air Regulations (FAR) Part 135
(airtaxiorcharter)certificate,enforcedbytheFAA.Theaircraftareavailableforairtaxi(charter)operations
within the United States and Canada.
(cid:2) Chartercompaniesprovideso-called“unscheduled”operations—thatis,charterflightstakeplaceonlyafter
a customer reserves the use of an aircraft to fly at a customer-designated date and time to one or more
customer-designated destinations, transporting passengers, cargo, or some combination of passengers and
cargo. A customer can, of course, reserve many different charter flights (trips) during any time frame.
However, for billing purposes, each charter trip is reserved by one and only one customer. Some of
RC_Charter2’s customers do not use the company’s charter operations; instead, they purchase fuel, use
maintenance services, or use other RC_Charter2 services. However, this database design will focus on the
charter operations only.
(cid:2) Each charter trip yields revenue for the RC_Charter2 Company. This revenue is generated by the charges
acustomerpaysuponthecompletionofaflight.Thecharterflightchargesareafunctionofaircraftmodel
used, distance flown, waiting time, special customer requirements, and crew expenses. The distance flown
chargesarecomputedbymultiplyingtheround-tripmilesbythemodel’schargepermile.Round-tripmiles
are based on the actual navigational path flown. The sample route traced in Figure P4.10 illustrates the
procedure. Note that the number of round-trip miles is calculated to be 130 + 200 + 180 + 390 = 900.
Depending on whether a customer has RC_Charter2 credit authorization, the customer may:
(cid:2) Pay the entire charter bill upon the completion of the charter flight.
(cid:2) Payapartofthecharterbillandchargetheremaindertotheaccount.Thechargeamountmaynotexceed
the available credit.
(cid:2) Charge the entire charter bill to the account. The charge amount may not exceed the available credit.
(cid:2) Customers may pay all or part of the existing balance for previous charter trips. Such payments may be

## Page 173

ENTITY RELATIONSHIP (ER) MODELING 143
FIGURE Round-trip mile determination
P4.10
Destination
180 miles
Intermediate Stop
200 miles
390 miles
Pax Pickup
130 miles
Home Base
madeatanytimeandarenotnecessarilytiedtoaspecificchartertrip.Thechartermileagechargeincludes
theexpenseofthepilot(s)andothercrewrequiredbyFAR135.However,ifcustomersrequestadditional
crewnotrequiredbyFAR135,thosecustomersarechargedforthecrewmembersonanhourlybasis.The
hourly crew-member charge is based on each crew member’s qualifications.
(cid:2) Thedatabasemustbeabletohandlecrewassignments.Eachchartertriprequirestheuseofanaircraft,and
a crew flies each aircraft. The smaller piston-engine-powered charter aircraft require a crew consisting of
onlyasinglepilot.Largeraircraft(i.e.,aircrafthavingagrosstakeoffweightof12,500poundsormore)and
jet-powered aircraft require a pilot and a copilot, while some of the larger aircraft used to transport
passengers may require flight attendants as part of the crew. Some of the older aircraft require the
assignmentofaflightengineer,andlargercargo-carryingaircraftrequiretheassignmentofaloadmaster.In
short, a crew can consist of more than one person, and not all crew members are pilots.
(cid:2) The charter flight’s aircraft waiting charges are computed by multiplying the hours waited by the model’s
hourly waiting charge. Crew expenses are limited to meals, lodging, and ground transportation.
TheRC_Charter2databasemustbedesignedtogenerateamonthlysummaryofallchartertrips,expenses,and
revenues derived from the charter records. Such records are based on the data that each pilot in command is
required to record for each charter trip: trip date(s) and time(s), destination(s), aircraft number, pilot (and other
crew)data,distanceflown,fuelusage,andotherdatapertinenttothecharterflight.Suchcharterdataarethen
usedtogeneratemonthlyreportsthatdetailrevenueandoperatingcostinformationforcustomers,aircraft,and
pilots.AllpilotsandothercrewmembersareRC_Charter2Companyemployees;thatis,thecompanydoesnot
use contract pilots and crew.
FARPart135operationsareconductedunderastrictsetofrequirementsthatgovernthelicensingandtraining
ofcrewmembers.Forexample,pilotsmusthaveearnedeitheracommerciallicenseoranAirlineTransportPilot
(ATP) license. Both licenses require appropriate ratings. Ratings are specific competency requirements. For
example:
(cid:2) To operate a multiengine aircraft designed for takeoffs and landings on land only, the appropriate rating is
MEL,orMultiengineLandplane.Whenamultiengineaircraftcantakeoffandlandonwater,theappropriate
rating is MES, or Multiengine Seaplane.

## Page 174

144 CHAPTER 4
(cid:2) Theinstrumentratingisbasedonademonstratedabilitytoconductallflightoperationswithsolereference
to cockpit instrumentation. The instrument rating is required to operate an aircraft under Instrument
Meteorological Conditions (IMC), and all such operations are governed under FAR-specified Instrument
Flight Rules (IFR). In contrast, operations conducted under “good weather” or visual flight conditions are
based on the FAR Visual Flight Rules (VFR).
(cid:2) Thetyperatingisrequiredforallaircraftwithatakeoffweightofmorethan12,500poundsorforaircraft
that are purely jet-powered. If an aircraft uses jet engines to drive propellers, that aircraft is said to be
turboprop-powered.Aturboprop—thatis,aturbo-propeller-poweredaircraft—doesnotrequireatyperating
unless it meets the 12,500-pound weight limitation.
(cid:2) Although pilot licenses and ratings are not time-limited, exercising the privilege of the license and ratings
under Part 135 requires both a current medical certificate and a current Part 135 checkride. The
following distinctions are important:
(cid:2) ThemedicalcertificatemaybeClassIorClassII.TheClassImedicalismorestringentthantheClassII,and
itmustberenewedeverysixmonths.TheClassIImedicalmustberenewedyearly.IftheClassImedicalis
not renewed during the six-month period, it automatically reverts to a Class II certificate. If the Class II
medicalisnotrenewedwithinthespecifiedperiod,itautomaticallyrevertstoaClassIIImedical,whichisnot
valid for commercial flight operations.
(cid:2) APart135checkrideisapracticalflightexaminationthatmustbesuccessfullycompletedeverysixmonths.
The checkride includes all flight maneuvers and procedures specified in Part 135.
Nonpilot crew members must also have the proper certificates in order to meet specific job requirements. For
example,loadmastersneedanappropriatecertificate,asdoflightattendants.Inaddition,crewmemberssuchas
loadmasters and flight attendants, who may be required in operations that involve large aircraft (more than a
12,500-pound takeoff weight and passenger configurations over 19) are also required periodically to pass a
writtenandpracticalexam.TheRC_Charter2Companyisrequiredtokeepacompleterecordofalltesttypes,
dates, and results for each crew member, as well as pilot medical certificate examination dates.
In addition, all flight crew members are required to submit to periodic drug testing; the results must be tracked,
too.(Notethatnonpilotcrewmembersarenotrequiredtotakepilot-specifictestssuchasPart135checkrides.
Nor are pilots required to take crew tests such as loadmaster and flight attendant practical exams.) However,
manycrewmembershavelicensesand/orcertificationsinseveralareas.Forexample,apilotmayhaveanATP
andaloadmastercertificate.Ifthatpilotisassignedtobealoadmasteronagivencharterflight,theloadmaster
certificate is required. Similarly, a flight attendant may have earned a commercial pilot’s license. Sample data
formats are shown in Table P4.10.
Pilots and other crew members must receive recurrency training appropriate to their work assignments.
Recurrency training is based on an FAA-approved curriculum that is job-specific. For example, pilot recurrency
training includes a review of all applicable Part 135 flight rules and regulations, weather data interpretation,
companyflightoperationsrequirements,andspecifiedflightprocedures.TheRC_Charter2Companyisrequired
to keep a complete record of all recurrency training for each crew member subject to the training.
TheRC_Charter2Companyisrequiredtomaintainadetailedrecordofallcrewcredentialsandalltrainingmandated
by Part 135.The company must keep a complete record of each requirement and of all compliance data.
Toconductacharterflight,thecompanymusthaveaproperlymaintainedaircraftavailable.Apilotwhomeets
all of the FAA’s licensing and currency requirements must fly the aircraft as Pilot in Command (PIC). For those
aircraftthatarepoweredbypistonenginesorturbopropsandhaveagrosstakeoffweightunder12,500pounds,
single-pilot operations are permitted under Part 135 as long as a properly maintained autopilot is available.
However,evenifFARPart135permitssingle-pilotoperations,manycustomersrequirethepresenceofacopilot
who is capable of conducting the flight operations under Part 135.
The RC_Charter2 operations manager anticipates the lease of turbojet-powered aircraft, and those aircraft are
required to have a crew consisting of a pilot and copilot. Both pilot and copilot must meet the same Part 135
licensing, ratings, and training requirements.

## Page 175

ENTITY RELATIONSHIP (ER) MODELING 145
TABLE
P4.10
PARTATESTS
TESTCODE TESTDESCRIPTION TESTFREQUENCY
1 Part135FlightCheck 6months
2 Medical,Class1 6months
3 Medical,Class2 12months
4 LoadmasterPractical 12months
5 FlightAttendantPractical 12months
6 Drugtest Random
7 Operations,writtenexam 6months
PARTBRESULTS
EMPLOYEE TESTCODE TESTDATE TESTRESULT
101 1 12-Nov-09 Pass-1
103 6 23-Dec-09 Pass-1
112 4 23-Dec-09 Pass-2
103 7 11-Jan-10 Pass-1
112 7 16-Jan-10 Pass-1
101 7 16-Jan-10 Pass-1
101 6 11-Feb-10 Pass-2
125 2 15-Feb-10 Pass-1
PARTCLICENSESANDCERTIFICATIONS
LICENSEORCERTIFICATE LICENSEORCERTIFICATEDESCRIPTION
ATP AirlineTransportPilot
Comm Commerciallicense
Med-1 Medicalcertificate,ClassI
Med-2 Medicalcertificate,ClassII
Instr Instrumentrating
MEL MultiengineLandaircraftrating
LM Loadmaster
FA FlightAttendant
EMPLOYEE LICENSEORCERTIFICATE DATEEARNED
101 Comm 12-Nov-93
101 Instr 28-Jun-94
101 MEL 9-Aug-94
103 Comm 21-Dec-95
112 FA 23-Jun-02
103 Instr 18-Jan-96
112 LM 27-Nov-05
The company also leases larger aircraft that exceed the 12,500-pound gross takeoff weight. Those aircraft can
carrythenumberofpassengersthatrequiresthepresenceofoneormoreflightattendants.Ifthoseaircraftcarry
cargoweighingover12,500pounds,aloadmastermustbeassignedasacrewmembertosupervisetheloading
and securing of the cargo. The database must be designed to meet the anticipated additional charter crew
assignment capability.
a. Given this incomplete description of operations, write all applicable business rules to establish entities,
relationships, optionalities, connectivities, and cardinalities. (Hint: Use the following five business rules as
examples, writing the remaining business rules in the same format.)
(cid:2) A customer may request many charter trips.
(cid:2) Each charter trip is requested by only one customer.

## Page 176

146 CHAPTER 4
(cid:2) Some customers have not (yet) requested a charter trip.
(cid:2) An employee may be assigned to serve as a crew member on many charter trips.
(cid:2) Each charter trip may have many employees assigned to it to serve as crew members.
b. DrawthefullylabeledandimplementableCrow’sFootERDbasedonthebusinessrulesyouwroteinPart(a)
of this problem. Include all entities, relationships, optionalities, connectivities, and cardinalities.

## Page 177

5
Advanced Data Modeling
In this chapter, you will learn:
(cid:1) About the extended entity relationship (EER) model
(cid:1) How entity clusters are used to represent multiple entities and relationships
(cid:1) The characteristics of good primary keys and how to select them
(cid:1) How to use flexible solutions for special data-modeling cases
In the previous two chapters,you learned how to use entity relationship diagrams (ERDs)
to properly create a data model.In this chapter,you will learn about the extended entity
relationship(EER)model.TheEERmodelbuildsonERconceptsandaddssupportforentity
P
supertypes,subtypes,and entity clustering.
review
Most current database implementations are based on relational databases. Because the
relational model uses keys to create associations among tables, it is essential to learn
thecharacteristicsofgoodprimarykeysandhowtoselectthem.Selectingagoodprimary
key is too important to be left to chance,so in this chapter we cover the critical aspects
of primary key identification and placement.
Focusingonpracticaldatabasedesign,thischapteralsoillustratessomespecialdesigncasesthat
highlight the importance of flexible designs,which can be adapted to meet the demands of
changingdataandinformationrequirements.Datamodelingisavitalstepinthedevelopment
of databases that in turn provide a good foundation for successful application development.
Rememberthatgooddatabaseapplicationscannotbebasedonbaddatabasedesigns,andno
amount of outstanding coding can overcome the limitations of poor database design.
E
V
I
F

## Page 178

148 CHAPTER 5
5.1 THE EXTENDED ENTITY RELATIONSHIP MODEL
As the complexity of the data structures being modeled has increased and as application software requirements have
becomemorestringent,therehasbeenanincreasingneedtocapturemoreinformationinthedatamodel.Theextended
entityrelationshipmodel(EERM),sometimesreferredtoastheenhancedentityrelationshipmodel,istheresultof
addingmoresemanticconstructstotheoriginalentityrelationship(ER)model.Asyoumightexpect,adiagramusing
this model is called an EER diagram (EERD). In the following sections, you will learn about the main EER model
constructs—entity supertypes, entity subtypes, and entity clustering—and see how they are represented in ERDs.
5.1.1 Entity Supertypes and Subtypes
Becausemostemployeespossessawiderangeofskillsandspecialqualifications,datamodelersmustfindavarietyof
ways to group employees based on employee characteristics. For instance, a retail company could group employees
as salaried and hourly employees, while a university could group employees as faculty, staff, and administrators.
The grouping of employees to create various types of employees provides two important benefits:
(cid:2) Itavoidsunnecessarynullsintheemployeeattributeswhensomeemployeeshavecharacteristicsthatarenot
shared by other employees.
(cid:2) It enables a particular employee type to participate in relationships that are unique to that employee type.
To illustrate those benefits, let’s explore the case of an aviation business. The aviation business employs pilots,
mechanics, secretaries, accountants, database managers, and many other types of employees. Figure 5.1 illustrates
how pilots share certain characteristics with other employees, such as a last name (EMP_LNAME) and hire date
(EMP_HIRE_DATE).Ontheotherhand,manypilotcharacteristicsarenotsharedbyotheremployees.Forexample,
unlike other employees, pilots must meet special requirements such as flight hour restrictions, flight checks, and
periodic training. Therefore, if all employee characteristics and special qualifications were stored in a single
EMPLOYEEentity,youwouldhavealotofnullsoryouwouldhavetomakealotofneedlessdummyentries.Inthis
case, special pilot characteristics such as EMP_LICENSE, EMP_RATINGS, and EMP_MED_TYPE will generate nulls
for employees who are not pilots. In addition, pilots participate in some relationships that are unique to their
qualifications.Forexample,notallemployeescanflyairplanes;onlyemployeeswhoarepilotscanparticipateinthe
“employee flies airplane” relationship.
FIGURE Nulls created by unique attributes
5.1
Basedontheprecedingdiscussion,youwouldcorrectlydeducethatthePILOTentitystoresonlythoseattributesthat
areuniquetopilots,andthattheEMPLOYEEentitystoresattributesthatarecommontoallemployees.Basedonthat
hierarchy,youcanconcludethatPILOTisasubtypeofEMPLOYEE,andthatEMPLOYEEisthesupertypeofPILOT.
Inmodelingterms,anentitysupertypeisagenericentitytypethatisrelatedtooneormoreentitysubtypes,where

## Page 179

ADVANCED DATA MODELING 149
theentitysupertypecontainsthecommoncharacteristics,andtheentitysubtypescontaintheuniquecharacteristicsof
each entity subtype.
There are two criteria that help the designer determine when to use subtypes and supertypes:
(cid:2) There must be different, identifiable kinds or types of the entity in the user’s environment.
(cid:2) Thedifferentkindsortypesofinstancesshouldhaveoneormoreattributesthatareuniquetothatkindortype
of instance.
Intheprecedingexample,becausepilotsmeetbothcriteriaofbeinganidentifiablekindofemployeeandhavingunique
attributesthatotheremployeesdonotpossess,itisappropriatetocreatePILOTasasubtypeofEMPLOYEE.Letus
assume that mechanics and accountants also have attributes that are unique to them, respectively, and that clerks do
not.Inthatcase,MECHANICandACCOUNTANTwouldalsobelegitimatesubtypesofEMPLOYEEbecausetheyare
identifiable kinds of employees and they have unique attributes. CLERK would not be an acceptable subtype of
EMPLOYEEbecauseitonlysatisfiesoneofthecriteria—itisanidentifiablekindofemployee—buttherearenotany
attributes that are unique to just clerks. In the next section, you will learn how entity supertypes and subtypes are
related in a specialization hierarchy.
5.1.2 Specialization Hierarchy
Entity supertypes and subtypes are organized in a specialization hierarchy, which depicts the arrangement of
higher-level entity supertypes (parent entities) and lower-level entity subtypes (child entities). Figure 5.2 shows the
specialization hierarchy formed by an EMPLOYEE supertype and three entity subtypes—PILOT, MECHANIC, and
ACCOUNTANT.Thespecializationhierarchyreflectsthe1:1relationshipbetweenEMPLOYEEanditssubtypes.For
example, a PILOT subtype occurrence is related to one instance of the EMPLOYEE supertype, and a MECHANIC
subtype occurrence is related to one instance of the EMPLOYEE supertype. The terminology and symbols in
Figure 5.2 are explained throughout this chapter.
Therelationshipsdepictedwithinthespecializationhierarchyaresometimesdescribedintermsof“is-a”relationships.
Forexample,apilotisanemployee,amechanicisanemployee,andanaccountantisanemployee.Itisimportant
to understand that within a specialization hierarchy, a subtype can exist only within the context of a supertype, and
everysubtypecanhaveonlyonesupertypetowhichitisdirectlyrelated.However,aspecializationhierarchycanhave
manylevelsofsupertype/subtyperelationships—thatis,youcanhaveaspecializationhierarchyinwhichasupertype
has many subtypes; in turn, one of the subtypes is the supertype to other lower-level subtypes.
O n l i n e C o n t e n t
Thischaptercoversonlyspecializationhierarchies.TheEERmodelalsosupportsspecializationlattices,where
a subtype can have multiple parents (supertypes). However, those concepts are better covered under the
object-orientedmodelinAppendixG,Object-OrientedDatabases.TheappendixisavailableinthePremium
Websiteforthisbook.
AsyoucanseeinFigure5.2,thearrangementofentitysupertypesandsubtypesinaspecializationhierarchyismore
thanacosmeticconvenience.Specializationhierarchiesenablethedatamodeltocaptureadditionalsemanticcontent
(meaning) into the ERD. A specialization hierarchy provides the means to:
(cid:2) Support attribute inheritance.
(cid:2) Define a special supertype attribute known as the subtype discriminator.
(cid:2) Define disjoint/overlapping constraints and complete/partial constraints.
The following sections cover such characteristics and constraints in more detail.

## Page 180

150 CHAPTER 5
FIGURE A specialization hierarchy
5.2
5.1.3 Inheritance
Thepropertyofinheritanceenablesanentitysubtypetoinherittheattributesandrelationshipsofthesupertype.As
discussed earlier, a supertype contains those attributes that are common to all of its subtypes. In contrast, subtypes
contain only the attributes that are unique to the subtype. For example, Figure 5.2 illustrates that pilots, mechanics,
and accountants all inherit the employee number, last name, first name, middle initial, hire date, and so on from the
EMPLOYEEentity.However,Figure5.2alsoillustratesthatpilotshaveattributesthatareunique;thesameistruefor
mechanics and accountants. One important inheritance characteristic is that all entity subtypes inherit their
primarykeyattributefromtheirsupertype.NoteinFigure5.2thattheEMP_NUMattributeistheprimarykeyfor
each of the subtypes.
At the implementation level, the supertype and its subtype(s) depicted in the specialization hierarchy maintain a
1:1relationship.Forexample,thespecializationhierarchyletsyoureplacetheundesirableEMPLOYEEtablestructure
in Figure 5.1 with two tables—one representing the supertype EMPLOYEE and the other representing the subtype
PILOT. (See Figure 5.3.)
Entitysubtypesinheritallrelationshipsinwhichthesupertypeentityparticipates.Forexample,Figure5.2showsthe
EMPLOYEEentitysupertypeparticipatingina1:MrelationshipwithaDEPENDENTentity.Throughinheritance,all
subtypes also participate in that relationship. In specialization hierarchies with multiple levels of supertype/subtypes,
a lower-level subtype inherits all of the attributes and relationships from all of its upper-level supertypes.

## Page 181

ADVANCED DATA MODELING 151
FIGURE The EMPLOYEE-PILOT supertype-subtype relationship
5.3
Table Name: EMPLOYEE Table Name: PILOT
5.1.4 Subtype Discriminator
A subtype discriminator is the attribute in the supertype entity that determines to which subtype the supertype
occurrence is related. As seen in Figure 5.2, the subtype discriminator is the employee type (EMP_TYPE).
ItiscommonpracticetoshowthesubtypediscriminatoranditsvalueforeachsubtypeintheERdiagram,asseenin
Figure 5.2. However, not all ER modeling tools follow that practice. For example, MS Visio shows the subtype
discriminator,butnotitsvalue.InFigure5.2,theVisiotexttoolwasusedtomanuallyaddthediscriminatorvalueabove
the entity subtype, close to the connector line. Using Figure 5.2 as your guide, note that the supertype is related to
a PILOT subtype if the EMP_TYPE has a value of “P.” If the EMP_TYPE value is “M,” the supertype is related to a
MECHANIC subtype. And if the EMP_TYPE value is “A,” the supertype is related to the ACCOUNTANT subtype.
Notethatthedefaultcomparisonconditionforthesubtypediscriminatorattributeistheequalitycomparison.However,
there may be situations in which the subtype discriminator is not necessarily based on an equality comparison. For
example,basedonbusinessrequirements,youmightcreatetwonewpilotsubtypes,pilot-in-command(PIC)-qualified
andcopilot-qualifiedonly.APIC-qualifiedpilotwillbeanyonewithmorethan1,500PICflighthours.Inthiscase,the
subtype discriminator would be “Flight_Hours,” and the criteria would be > 1,500 or <= 1,500, respectively.
Note
In Visio, you select the subtype discriminator when creating a category using the Category shape from the
availableshapes.TheCategoryshapeisasmallcirclewithahorizontallineunderitthatconnectsthesupertype
toitssubtypes.
O n l i n e C o n t e n t
ForatutorialonusingMSVisiotocreateaspecializationhierarchy,seeAppendixA,DesigningDatabaseswith
VisioProfessional:ATutorial,inthePremiumWebsiteforthisbook.
5.1.5 Disjoint and Overlapping Constraints
Anentitysupertypecanhavedisjointoroverlappingentitysubtypes.Forexample,intheaviationexample,anemployee
canbeapilotoramechanicoranaccountant.Assumethatoneofthebusinessrulesdictatesthatanemployeecannot
belong to more than one subtype at a time; that is, an employee cannot be a pilot and a mechanic at the same time.
Disjoint subtypes, also known as nonoverlapping subtypes, are subtypes that contain a unique subset of the
supertypeentityset;inotherwords,eachentityinstanceofthesupertypecanappearinonlyoneofthesubtypes.For

## Page 182

152 CHAPTER 5
example, in Figure 5.2, an employee (supertype) who is a pilot (subtype) can appear only in the PILOT subtype, not
in any of the other subtypes. In Visio, such disjoint subtypes are indicated by the letter d inside the category shape.
On the other hand, if the business rule specifies that employees can have multiple classifications, the EMPLOYEE
supertype may contain overlapping job classification subtypes. Overlapping subtypes are subtypes that contain
nonuniquesubsetsofthesupertypeentityset;thatis,eachentityinstanceofthesupertypemayappearinmorethan
one subtype. For example, in a university environment, a person may be an employee or a student or both. In turn,
anemployeemaybeaprofessoraswellasanadministrator.Becauseanemployeemayalsobeastudent,STUDENT
and EMPLOYEE are overlapping subtypes of the supertype PERSON, just as PROFESSOR and ADMINISTRATOR
areoverlappingsubtypesofthesupertypeEMPLOYEE.Figure5.4illustratesoverlappingsubtypeswiththeuseofthe
letter o inside the category shape.
FIGURE Specialization hierarchy with overlapping subtypes
5.4
Itiscommonpracticetoshowthedisjoint/overlappingsymbolsintheERD.(SeeFigure5.2andFigure5.4.)However,
not all ER modeling tools follow that practice. For example, by default, Visio shows only the subtype discriminator
(usingtheCategoryshape)butnotthedisjoint/overlappingsymbol.Therefore,theVisiotexttoolwasusedtomanually
add the d and o symbols in Figures 5.2 and 5.4.
Note
Alternativenotationsexistforrepresentingdisjoint/overlappingsubtypes.Forexample,TobyJ.Teoreypopular-
izedtheuseofGandGstoindicatedisjointandoverlappingsubtypes.

## Page 183

ADVANCED DATA MODELING 153
As you learned earlier in this section, the implementation of disjoint subtypes is based on the value of the subtype
discriminator attribute in the supertype. However, implementing overlapping subtypes requires the use of one
discriminator attribute for each subtype. For example, in the case of the Tiny College database design you saw in
Chapter 4, Entity Relationship (ER) Modeling, a professor can also be an administrator. Therefore, the EMPLOYEE
supertype would have the subtype discriminator attributes and values shown in Table 5.1.
TABLE Discriminator Attributes with Overlapping Subtypes
5.1
DISCRIMINATORATTRIBUTES
COMMENT
Professor Administrator
“Y” “N” TheEmployeeisamemberoftheProfessorsubtype.
“N” “Y” TheEmployeeisamemberoftheAdministratorsubtype.
“Y” “Y” TheEmployeeisbothaProfessorandanAdministrator.
5.1.6 Completeness Constraint
Thecompletenessconstraintspecifieswhethereachentitysupertypeoccurrencemustalsobeamemberofatleast
onesubtype.Thecompletenessconstraintcanbepartialortotal.Partialcompleteness(symbolizedbyacircleover
a single line) means that not every supertype occurrence is a member of a subtype; that is, there may be some
supertype occurrences that are not members of any subtype. Total completeness (symbolized by a circle over a
double line) means that every supertype occurrence must be a member of at least one subtype.
TheERDsinFigures5.2and5.4representthecompletenessconstraintbasedontheVisioCategoryshape.Asingle
horizontal line under the circle represents a partial completeness constraint; a double horizontal line under the circle
represents a total completeness constraint.
Note
Alternativenotationsexisttorepresentthecompletenessconstraint.Forexample,somenotationsuseasingle
line(partial)ordoubleline(total)toconnectthesupertypetotheCategoryshape.
Giventhedisjoint/overlappingsubtypesandcompletenessconstraints,it’spossibletohavethespecializationhierarchy
constraint scenarios shown in Table 5.2.
TABLE Specialization Hierarchy Constraint Scenarios
5.2
TYPE DISJOINTCONSTRAINT OVERLAPPINGCONSTRAINT
Partial Supertypehasoptionalsubtypes. Supertypehasoptionalsubtypes.
Subtypediscriminatorcanbenull. Subtypediscriminatorscanbenull.
Subtypesetsareunique. Subtypesetsarenotunique.
Total Everysupertypeoccurrenceisamemberofa Everysupertypeoccurrenceisamemberofa
(atleastone)subtype. (atleastone)subtype.
Subtypediscriminatorcannotbenull. Subtypediscriminatorscannotbenull.
Subtypesetsareunique. Subtypesetsarenotunique.

## Page 184

154 CHAPTER 5
5.1.7 Specialization and Generalization
Youcanusevariousapproachestodevelopentitysupertypesandsubtypes.Forexample,youcanfirstidentifyaregular
entity,andthenidentifyallentitysubtypesbasedontheirdistinguishingcharacteristics.Youcanalsostartbyidentifying
multiple entity types and then later extract the common characteristics of those entities to create a higher-level
supertype entity.
Specialization is the top-down process of identifying lower-level, more specific entity subtypes from a higher-level
entity supertype. Specialization is based on grouping unique characteristics and relationships of the subtypes. In the
aviation example, you used specialization to identify multiple entity subtypes from the original employee supertype.
Generalizationisthebottom-upprocessofidentifyingahigher-level,moregenericentitysupertypefromlower-level
entity subtypes. Generalization is based on grouping common characteristics and relationships of the subtypes. For
example, you might identify multiple types of musical instruments: piano, violin, and guitar. Using the generalization
approach,youcouldidentifya“stringinstrument”entitysupertypetoholdthecommoncharacteristicsofthemultiple
subtypes.
5.2 ENTITY CLUSTERING
DevelopinganERdiagramentailsthediscoveryofpossiblyhundredsofentitytypesandtheirrespectiverelationships.
Generally,thedatamodelerwilldevelopaninitialERDcontainingafewentities.Asthedesignapproachescompletion,
theERDwillcontainhundredsofentitiesandrelationshipsthatcrowdthediagramtothepointofmakingitunreadable
andinefficientasacommunicationtool.Inthosecases,youcanuseentityclusterstominimizethenumberofentities
shown in the ERD.
Anentityclusterisa“virtual”entitytypeusedtorepresentmultipleentitiesandrelationshipsintheERD.Anentity
cluster is formed by combining multiple interrelated entities into a single abstract entity object. An entity cluster is
considered“virtual”or“abstract”inthesensethatitisnotactuallyanentityinthefinalERD.Instead,itisatemporary
entityusedtorepresentmultipleentitiesandrelationships,withthepurposeofsimplifyingtheERDandthusenhancing
its readability.
Figure 5.5 illustrates the use of entity clusters based on the Tiny College example in Chapter 4. Note that the ERD
contains two entity clusters:
(cid:2) OFFERING, which groups the COURSE and CLASS entities and relationships.
(cid:2) LOCATION, which groups the ROOM and BUILDING entities and relationships.
NotealsothattheERDinFigure5.5doesnotshowattributesfortheentities.Whenusingentityclusters,thekeyattributes
ofthecombinedentitiesarenolongeravailable.Withoutthekeyattributes,primarykeyinheritanceruleschange.Inturn,
thechangeintheinheritancerulescanhaveundesirableconsequences,suchaschangesinrelationships—fromidentifying
tononidentifyingorviceversa—andthelossofforeignkeyattributesfromsomeentities.Toeliminatethoseproblems,the
general rule is to avoid the displayofattributes when entity clusters are used.

## Page 185

ADVANCED DATA MODELING 155
FIGURE Tiny College ERD using entity clusters
5.5
5.3 ENTITY INTEGRITY: SELECTING PRIMARY KEYS
Arguably, the most important characteristic of an entity is its primary key (a single attribute or some combination of
attributes), which uniquely identifies each entity instance. The primary key’s function is to guarantee entity integrity.
Furthermore, primary keys and foreign keys work together to implement relationships in the relational model.
Therefore,theimportanceofproperlyselectingtheprimarykeyhasadirectbearingontheefficiencyandeffectiveness
of database implementation.

## Page 186

156 CHAPTER 5
5.3.1 Natural Keys and Primary Keys
Theconceptofauniqueidentifieriscommonlyencounteredintherealworld.Forexample,youuseclass(orsection)
numberstoregisterforclasses,invoicenumberstoidentifyspecificinvoices,accountnumberstoidentifycreditcards,
andsoon.Thoseexamplesillustratenaturalidentifiersorkeys.Anaturalkeyornaturalidentifierisareal-world,
generally accepted identifier used to distinguish—that is, uniquely identify—real-world objects. As its name implies, a
natural key is familiar to end users and forms part of their day-to-day business vocabulary.
Usually, if an entity has a natural identifier, a data modeler uses that as the primary key of the entity being modeled.
Generally,mostnaturalkeysmakeacceptableprimarykeyidentifiers.Thenextsectionpresentssomebasicguidelines
for selecting primary keys.
5.3.2 Primary Key Guidelines
A primary key is the attribute or combination of attributes that uniquely identifies entity instances in an entity set.
However,cantheprimarykeybebasedon,say,12attributes?Andjusthowlongcanaprimarykeybe?Inprevious
examples, why was EMP_NUM selected as a primary key of EMPLOYEE and not a combination of EMP_LNAME,
EMP_FNAME,EMP_INITIAL,andEMP_DOB?Canasingle256-bytetextattributebeagoodprimarykey?Thereis
nosingleanswertothosequestions,butthereisabodyofpracticethatdatabaseexpertshavebuiltovertheyears.This
section examines that body of documented practices.
First,youshouldunderstandthefunctionofaprimarykey.Theprimarykey’smainfunctionistouniquelyidentifyan
entityinstanceorrowwithinatable.Inparticular,givenaprimarykeyvalue—thatis,thedeterminant—therelational
model can determine the value of all dependent attributes that “describe” the entity. Note that identification and
description are separate semantic constructs in the model. The function of the primary key is to guarantee entity
integrity, not to “describe” the entity.
Second,primarykeysandforeignkeysareusedtoimplementrelationshipsamongentities.However,theimplemen-
tation of such relationships is done mostly behind the scenes, hidden from end users. In the real world, end users
identify objects based on the characteristics they know about the objects. For example, when shopping at a grocery
store,youselectproductsbytakingthemfromastoredisplayshelfandreadingthelabels,notbylookingatthestock
number. It’s wise for database applications to mimic the human selection process as much as possible. Therefore,
database applications should let the end user choose among multiple descriptive narratives of different objects, while
using primary key values behind the scenes. Keeping those concepts in mind, look at Table 5.3, which summarizes
desirable primary key characteristics.
TABLE Desirable Primary Key Characteristics
5.3
PKCHARACTERISTIC RATIONALE
Uniquevalues ThePKmustuniquelyidentifyeachentityinstance.Aprimarykeymustbeable
toguaranteeuniquevalues.Itcannotcontainnulls.
Nonintelligent ThePKshouldnothaveembeddedsemanticmeaningotherthantouniquely
identifyeachentityinstance.Anattributewithembeddedsemanticmeaningis
probablybetterusedasadescriptivecharacteristicoftheentitythanasan
identifier.Forexample,astudentIDof650973wouldbepreferredoverSmith,
MarthaL.asaprimarykeyidentifier.
Nochangeovertime Ifanattributehassemanticmeaning,itmightbesubjecttoupdates.Thisiswhy
namesdonotmakegoodprimarykeys.IfyouhaveVickieSmithastheprimary
key,whathappensifshechangeshernamewhenshegetsmarried?Ifaprimary
keyissubjecttochange,theforeignkeyvaluesmustbeupdated,thusaddingto
thedatabaseworkload.Furthermore,changingaprimarykeyvaluemeansthat
youarebasicallychangingtheidentityofanentity.Inshort,thePKshouldbe
permanentandunchangeable.

## Page 187

ADVANCED DATA MODELING 157
TABLE Desirable Primary Key Characteristics (continued)
5.3
PKCHARACTERISTIC RATIONALE
Preferablysingle-attribute Aprimarykeyshouldhavetheminimumnumberofattributespossible
(irreducible).Single-attributeprimarykeysaredesirablebutnotrequired.Single-
attributeprimarykeyssimplifytheimplementationofforeignkeys.Having
multiple-attributeprimarykeyscancauseprimarykeysofrelatedentitiestogrow
throughthepossibleadditionofmanyattributes,thusaddingtothedatabase
workloadandmaking(application)codingmorecumbersome.
Preferablynumeric Uniquevaluescanbebettermanagedwhentheyarenumeric,becausethe
databasecanuseinternalroutinestoimplementacounter-styleattributethat
automaticallyincrementsvalueswiththeadditionofeachnewrow.Infact,most
databasesystemsincludetheabilitytousespecialconstructs,suchasAutonum-
berinMicrosoftAccess,tosupportself-incrementingprimarykeyattributes.
Security-compliant Theselectedprimarykeymustnotbecomposedofanyattribute(s)thatmightbe
consideredasecurityriskorviolation.Forexample,usingaSocialSecuritynum-
berasaPKinanEMPLOYEEtableisnotagoodidea.
5.3.3 When to Use Composite Primary Keys
Intheprevioussection,youlearnedaboutthedesirablecharacteristicsofprimarykeys.Forexample,youlearnedthat
theprimarykeyshouldusetheminimumnumberofattributespossible.However,thatdoesnotmeanthatcomposite
primary keys are not permitted in a model. In fact, composite primary keys are particularly useful in two cases:
(cid:2) As identifiers of composite entities, where each primary key combination is allowed only once in the
M:N relationship.
(cid:2) Asidentifiersofweakentities,wheretheweakentityhasastrongidentifyingrelationshipwiththeparententity.
Toillustratethefirstcase,assumethatyouhaveaSTUDENTentitysetandaCLASSentityset.Inaddition,assumethat
thosetwosetsarerelatedinanM:NrelationshipviaanENROLLentitysetinwhicheachstudent/classcombinationmay
appear only once in the composite entity.Figure 5.6 shows the ERD to represent such a relationship.
As shown in Figure 5.6, the composite primary key automatically provides the benefit of ensuring that there cannot
be duplicate values—that is, it ensures that the same student cannot enroll more than once in the same class.
Inthesecondcase,aweakentityinastrongidentifyingrelationshipwithaparententityisnormallyusedtorepresent
one of two situations:
1. A real-world object that is existence-dependent on another real-world object. Those types of objects are
distinguishable in the real world. A dependent and an employee are two separate people who exist
independentlyofeachother.However,suchobjectscanexistinthemodelonlywhentheyrelatetoeachother
in a strong identifying relationship. For example, the relationship between EMPLOYEE and DEPENDENT is
oneofexistencedependencyinwhichtheprimarykeyofthedependententityisacompositekeythatcontains
the key of the parent entity.
2. A real-world object that is represented in the data model as two separate entities in a strong identifying
relationship. For example, the real-world invoice object is represented by two entities in a data model:
INVOICE and LINE. Clearly, the LINE entity does not exist in the real world as an independent object, but
rather as part of an INVOICE.
In both situations, having a strong identifying relationship ensures that the dependent entity can exist only when it is
relatedtotheparententity.Insummary,theselectionofacompositeprimarykeyforcompositeandweakentitytypes
provides benefits that enhance the integrity and consistency of the model.

## Page 188

158 CHAPTER 5
FIGURE The M:N relationship between STUDENT and CLASS
5.6
Database name: Ch06_Tinycollege
Table name: STUDENT Table name: CLASS
(first four fields) Table name: ENROLL (first three fields)
5.3.4 When to Use Surrogate Primary Keys
There are some instances when a primary key doesn’t exist in the real world or when the existing natural key might
not be a suitable primary key. In these cases, it is standard practice to create a surrogate key. A surrogate key is a
primary key created by the database designer to simplify the identification of entity instances. The surrogate key has
no meaning in the user’s environment—it exists only to distinguish one entity instance from another. One practical
advantageofasurrogatekeyisthatsinceithasnointrinsicmeaning,valuesforitcanbegeneratedbytheDBMSto
ensure that unique values are always provided.
For example, consider the case of a park recreation facility that rents rooms for small parties. The manager of the
facility keeps track of all events, using a folder with the format shown in Table 5.4.
TABLE Data Used to Keep Track of Events
5.4
DATE TIME_START TIME_END ROOM EVENT_NAME PARTY_OF
6/17/2010 11:00AM 2:00PM Allure BurtonWedding 60
6/17/2010 11:00AM 2:00PM Bonanza AdamsOffice 12
6/17/2010 3:00PM 5:30PM Allure SmithFamily 15
6/17/2010 3:30PM 5:30PM Bonanza AdamsOffice 12
6/18/2010 1:00PM 3:00PM Bonanza BoyScouts 33
6/18/2010 11:00AM 2:00PM Allure MarchofDimes 25
6/18/2010 11:00AM 12:30PM Bonanza SmithFamily 12
Given the data shown in Table 5.4, you would model the EVENT entity as:
EVENT (DATE, TIME_START, TIME_END, ROOM, EVENT_NAME, PARTY_OF)

## Page 189

ADVANCED DATA MODELING 159
Whatprimarykeywouldyousuggest?Inthiscase,thereisnosimplenaturalkeythatcouldbeusedasaprimarykey
in the model. Based on the primary key concepts you learned about in previous chapters, you might suggest one of
these options:
(DATE, TIME_START, ROOM) or (DATE, TIME_END, ROOM)
Assume you select the composite primary key (DATE, TIME_START, ROOM) for the EVENT entity. Next, you
determine that one EVENT may use many RESOURCEs (such as tables, projectors, PCs, and stands), and that the
same RESOURCE may be used for many EVENTs. The RESOURCE entity would be represented by the following
attributes:
RESOURCE (RSC_ID, RSC_DESCRIPTION, RSC_TYPE, RSC_QTY, RSC_PRICE)
Given the business rules, the M:N relationship between RESOURCE and EVENT would be represented via the
EVNTRSC composite entity with a composite primary key as follows:
EVNTRSC (DATE, TIME_START, ROOM, RSC_ID, QTY_USED)
Younowhavealengthyfour-attributecompositeprimarykey.WhatwouldhappeniftheEVNTRSCentity’sprimary
keywereinheritedbyanotherexistence-dependententity?Atthispoint,youcanseethatthecompositeprimarykey
could make the implementation of the database and program coding unnecessarily complex.
Asadatamodeler,youprobablynoticedthattheEVENTentity’sselectedprimarykeymightnotfarewell,giventhe
primarykeyguidelinesinTable5.3.Inthiscase,theEVENTentity’sselectedprimarykeycontainsembeddedsemantic
informationandisformedbyacombinationofdate,time,andtextdatacolumns.Inaddition,theselectedprimarykey
would cause lengthy primary keys for existence-dependent entities. The preferred alternative is to use a numeric
single-attribute surrogate primary key.
Surrogate primary keys are accepted practice in today’s complex data environments.They are especially helpful when
thereisnonaturalkey,whentheselectedcandidatekeyhasembeddedsemanticcontents,orwhentheselectedcandidate
key is too long or cumbersome. However, there is a trade-off: if you use a surrogate key, you must ensure that the
candidatekeyoftheentityinquestionperformsproperlythroughtheuseof“uniqueindex”and“notnull”constraints.
5.4 DESIGN CASES: LEARNING FLEXIBLE DATABASE DESIGN
Datamodelinganddatabasedesignrequireskillsthatareacquiredthroughexperience.Inturn,experienceisacquired
through practice—regular and frequent repetition, applying the concepts learned to specific and different design
problems. This section presents four special design cases that highlight the importance of flexible designs, proper
identification of primary keys, and placement of foreign keys.
Note
Indescribingthevariousmodelingconceptsthroughoutthisbook,thefocusisonrelationalmodels.Also,given
thefocusonthepracticalnatureofdatabasedesign,alldesignissuesareaddressedwiththeimplementation
goalinmind.Therefore,thereisnosharplineofdemarcationbetweendesignandimplementation.
Atthepureconceptualstageofthedesign,foreignkeysarenotpartofanERdiagram.TheERDdisplaysonly
entitiesandrelationships.Entitiesareidentifiedbyidentifiersthatmaybecomeprimarykeys.Duringdesign,the
modelerattemptstounderstandanddefinetheentitiesandrelationships.Foreignkeysarethemechanismthrough
whichtherelationshipdesignedinanERDisimplementedinarelationalmodel.IfyouuseVisioProfessionalasyour
modelingtool,youwilldiscoverthatthisbook’smethodologyisreflectedintheVisiomodelingpractice.

## Page 190

160 CHAPTER 5
5.4.1 Design Case #1: Implementing 1:1 Relationships
Foreignkeysworkwithprimarykeystoproperlyimplementrelationshipsintherelationalmodel.Thebasicruleisvery
simple:puttheprimarykeyofthe“one”side(theparententity)onthe“many”side(thedependententity)asaforeign
key.However,wheredoyouplacetheforeignkeywhenyouareworkingwitha1:1relationship?Forexample,take
thecaseofa1:1relationshipbetweenEMPLOYEEandDEPARTMENTbasedonthebusinessrule“oneEMPLOYEE
isthemanagerofoneDEPARTMENT,andoneDEPARTMENTismanagedbyoneEMPLOYEE.”Inthatcase,there
are two options for selecting and placing the foreign key:
1. Placeaforeignkeyinbothentities.ThisoptionisderivedfromthebasicruleyoulearnedinChapter4.Place
EMP_NUMasaforeignkeyinDEPARTMENT,andplaceDEPT_IDasaforeignkeyinEMPLOYEE.However,
this solution is not recommended, as it would create duplicated work, and it could conflict with other existing
relationships. (Remember that DEPARTMENT and EMPLOYEE also participate in a 1:M relationship—one
department employs many employees.)
2. Place a foreign key in one of the entities. In that case, the primary key of one of the two entities appears
as a foreign key in the other entity. That is the preferred solution, but there is a remaining question: which
primary key should be used as a foreign key? The answer to that question is found in Table 5.5. Table 5.5
shows the rationale for selecting the foreign key in a 1:1 relationship based on the relationship properties in
the ERD.
TABLE Selection of Foreign Key in a 1:1 Relationship
5.5
CASE ERRELATIONSHIPCONSTRAINTS ACTION
I Onesideismandatoryandtheother PlacethePKoftheentityonthemandatorysideintheentity
sideisoptional. ontheoptionalsideasaFK,andmaketheFKmandatory.
II Bothsidesareoptional. SelecttheFKthatcausesthefewestnulls,orplacetheFKin
theentityinwhichthe(relationship)roleisplayed.
III Bothsidesaremandatory. SeeCaseII,orconsiderrevisingyourmodeltoensurethat
thetwoentitiesdonotbelongtogetherinasingleentity.
Figure 5.7 illustrates the “EMPLOYEE manages DEPARTMENT” relationship. Note that in this case, EMPLOYEE is
mandatorytoDEPARTMENT.Therefore,EMP_NUMisplacedastheforeignkeyinDEPARTMENT.Alternatively,you
might also argue that the “manager” role is played by the EMPLOYEE in the DEPARTMENT.
FIGURE The 1:1 relationship between DEPARTMENT and EMPLOYEE
5.7
Asadesigner,youmustrecognizethat1:1relationshipsexistintherealworld,andtherefore,theyshouldbesupported
in the data model. In fact, a 1:1 relationship is used to ensure that two entity sets are not placed in the same table.

## Page 191

ADVANCED DATA MODELING 161
In other words, EMPLOYEE and DEPARTMENT are clearly separate and unique entity types that do not belong
together in a single entity. If you grouped them together in one entity, what would be the name of that entity?
5.4.2 Design Case #2: Maintaining History of Time-Variant Data
Companymanagersgenerallyrealizethatgooddecisionmakingisbasedontheinformationthatisgeneratedthrough
thedatastoredindatabases.Suchdatareflectcurrentaswellaspastevents.Companymanagersusethedatastored
indatabasestoanswerquestionssuchas:“Howdothecurrentcompanyprofitscomparetothoseofpreviousyears?”
and“WhatareXYZproduct’ssalestrends?”Inotherwords,thedatastoredondatabasesreflectnotonlycurrentdata,
but also historic data.
Normally,datachangesaremanagedbyreplacingtheexistingattributevaluewiththenewvalue,withoutregardtothe
previous value. However, there are situations in which the history of values for a given attribute must be preserved.
From a data-modeling point of view, time-variant data refer to data whose values change over time and for which
you must keep a history of the data changes. You could argue that all data in a database are subject to change over
timeandare,therefore,timevariant.However,someattributevalues,suchasyourdateofbirthoryourSocialSecurity
number, are not time variant. On the other hand, attributes such as your student GPA or your bank account balance
are subject to change over time. Sometimes the data changes are externally originated and event driven, such as a
productpricechange.Onotheroccasions,changesarebasedonwell-definedschedules,suchasthedailystockquote
“open” and “close” values.
In any case, keeping the history of time-variant data is equivalent to having a multivalued attribute in your entity. To
model time-variant data, you must create a new entity in a 1:M relationship with the original entity. This new entity
will contain the new value, the date of the change, and whatever other attribute is pertinent to the event being
modeled. For example, if you want to keep track of the current manager as well as the history of all department
managers, you can create the model shown in Figure 5.8.
FIGURE Maintaining manager history
5.8

## Page 192

162 CHAPTER 5
Note that in Figure 5.8, the MGR_HIST entity has a 1:M relationship with EMPLOYEE and a 1:M relationship with
DEPARTMENTtoreflectthefactthat,overtime,anemployeecouldbethemanagerofmanydifferentdepartments,
and a department could have many different employee managers. Because you are recording time-variant data, you
must store the DATE_ASSIGN attribute in the MGR_HIST entity to provide the date on which the employee
(EMP_NUM)becamethemanagerofthedepartment.TheprimarykeyofMGR_HISTpermitsthesameemployeeto
bethemanagerofthesamedepartment,butondifferentdates.Ifthatscenarioisnotthecaseinyourenvironment—if,
for example, an employee is the manager of a department only once—you could make DATE_ASSIGN a nonprime
attribute in the MGR_HIST entity.
Note in Figure 5.8 that the “manages” relationship is optional in theory and redundant in practice.At any time, you
couldfindoutwhothemanagerofadepartmentisbyretrievingthemostrecentDATE_ASSIGNdatefromMGR_HIST
foragivendepartment.Ontheotherhand,theERDinFigure5.8differentiatesbetweencurrentdataandhistoricdata.
The current manager relationship is implemented by the “manages” relationship between EMPLOYEE and
DEPARTMENT. Additionally, the historic data are managed through EMP_MGR_HIST and DEPT_MGR_HIST. The
trade-off with that model is that each time a new manager is assigned to a department, there will be two data
modifications: one update in the DEPARTMENT entity and one insert in the MGR_HIST entity.
TheflexibilityofthemodelproposedinFigure5.8becomesmoreapparentwhenyouaddthe1:M“onedepartment
employs many employees” relationship. In that case, the PK of the “1” side (DEPT_ID) appears in the “many” side
(EMPLOYEE)asaforeignkey.Nowsupposeyouwouldliketokeeptrackofthejobhistoryforeachofthecompany’s
employees—you’d probably want to store the department, the job code, the date assigned, and the salary. To
accomplishthattask,youwouldmodifythemodelinFigure5.8byaddingaJOB_HISTentity.Figure5.9showsthe
use of the new JOB_HIST entity to maintain the employee’s history.
Again,it’sworthemphasizingthatthe“manages”and“employs”relationshipsaretheoreticallyoptionalandredundant
in practice. You can always find out where each employee works by looking at the job history and selecting only the
mostcurrentdatarowforeachemployee.However,asyouwilldiscoverinChapter7,IntroductiontoStructuredQuery
Language(SQL),andinChapter8,AdvancedSQL,findingwhereeachemployeeworksisnotatrivialtask.Therefore,
the model represented in Figure 5.9 includes the admittedly redundant but unquestionably useful “manages” and
“employs” relationships to separate current data from historic data.
5.4.3 Design Case #3: Fan Traps
Creating a data model requires proper identification of the data relationships among entities. However, due to
miscommunicationorincompleteunderstandingofthebusinessrulesorprocesses,itisnotuncommontomisidentify
relationshipsamongentities.Underthosecircumstances,theERDmaycontainadesigntrap.Adesigntrapoccurs
whenarelationshipisimproperlyorincompletelyidentifiedandisthereforerepresentedinawaythatisnotconsistent
with the real world. The most common design trap is known as a fan trap.
Afantrapoccurswhenyouhaveoneentityintwo1:Mrelationshipstootherentities,thusproducinganassociation
amongtheotherentitiesthatisnotexpressedinthemodel.Forexample,assumetheJCBbasketballleaguehasmany
divisions.Eachdivisionhasmanyplayers,andeachdivisionhasmanyteams.Giventhose“incomplete”businessrules,
you might create an ERD that looks like the one in Figure 5.10.
AsyoucanseeinFigure5.10,DIVISIONisina1:MrelationshipwithTEAMandina1:MrelationshipwithPLAYER.
Althoughthatrepresentationissemanticallycorrect,therelationshipsarenotproperlyidentified.Forexample,there
is no way to identify which players belong to which team. Figure 5.10 also shows a sample instance relationship
representation for the ERD. Note that the relationship lines for the DIVISION instances fan out to the TEAM and
PLAYER entity instances—thus the “fan trap” label.
Figure 5.11 shows the correct ERD after the fan trap has been eliminated. Note that, in this case, DIVISION is in a
1:M relationship with TEAM. In turn, TEAM is in a 1:M relationship with PLAYER. Figure 5.11 also shows the
instance relationship representation after eliminating the fan trap.

## Page 193

ADVANCED DATA MODELING 163
FIGURE Maintaining job history
5.9
FIGURE Incorrect ERD with fan trap problem
5.10
Given the design in Figure 5.11, note how easy it is to see which players play for which team. However, to find out
whichplayersplayinwhichdivision,youfirstneedtoseewhatteamsbelongtoeachdivision;thenyouneedtofind
outwhichplayersplayoneachteam.Inotherwords,thereisatransitiverelationshipbetweenDIVISIONandPLAYER
via the TEAM entity.

## Page 194

164 CHAPTER 5
FIGURE Corrected ERD after removal of the fan trap
5.11
5.4.4 Design Case #4: Redundant Relationships
Althoughredundancyisoftenagoodthingtohaveincomputerenvironments(multiplebackupsinmultipleplaces,for
example), redundancy is seldom a good thing in the database environment. (As you learned in Chapter 3, The
Relational Database Model, redundancies can cause data anomalies in a database.) Redundant relationships occur
whentherearemultiplerelationshippathsbetweenrelatedentities.Themainconcernwithredundantrelationshipsis
that they remain consistent across the model. However, it’s important to note that some designs use redundant
relationships as a way to simplify the design.
AnexampleofredundantrelationshipswasfirstintroducedinFigure5.8duringthediscussiononmaintainingahistory
of time-variant data. However, the use of the redundant “manages” and “employs” relationships was justified by the
factthatsuchrelationshipsweredealingwithcurrentdataratherthanhistoricdata.Anothermorespecificexampleof
a redundant relationship is represented in Figure 5.12.
FIGURE A redundant relationship
5.12
In Figure 5.12, note the transitive 1:M relationship between DIVISION and PLAYER through the TEAM entity set.
Therefore,therelationshipthatconnectsDIVISIONandPLAYERis,forallpracticalpurposes,redundant.Inthatcase,
the relationship could be safely deleted without losing any information-generation capabilities in the model.

## Page 195

ADVANCED DATA MODELING 165
S u m m a r y
◗
Theextendedentityrelationship(EER)modeladdssemanticstotheERmodelviaentitysupertypes,subtypes,and
clusters. An entity supertype is a generic entity type that is related to one or more entity subtypes.
◗
Aspecializationhierarchydepictsthearrangementandrelationshipsbetweenentitysupertypesandentitysubtypes.
Inheritancemeansthatanentitysubtypeinheritstheattributesandrelationshipsofthesupertype.Subtypescanbe
disjoint or overlapping. A subtype discriminator is used to determine to which entity subtype the supertype
occurrence is related. The subtypes can exhibit partial or total completeness. There are basically two approaches
to developing a specialization hierarchy of entity supertypes and subtypes: specialization and generalization.
◗
Anentityclusterisa“virtual”entitytypeusedtorepresentmultipleentitiesandrelationshipsintheERD.Anentity
cluster is formed by combining multiple interrelated entities and relationships into a single, abstract entity object.
◗
Naturalkeysareidentifiersthatexistintherealworld.Naturalkeyssometimesmakegoodprimarykeys,butthisisnot
necessarily true. Primary keys should have these characteristics: they must have unique values, they should be
nonintelligent,theymustnotchangeovertime,andtheyarepreferablynumericandcomposedofasingleattribute.
◗
Composite keys are useful to represent M:N relationships and weak (strong identifying) entities.
◗
Surrogateprimarykeysareusefulwhenthereisnonaturalkeythatmakesasuitableprimarykey,whentheprimary
keyisacompositeprimarykeywithmultipledifferentdatatypes,orwhentheprimarykeyistoolongtobeusable.
◗
Ina1:1relationship,placethePKofthemandatoryentityasaforeignkeyintheoptionalentity,asanFKinthe
entity that causes the least number of nulls, or as an FK where the role is played.
◗
Time-variant data refers to data whose values change over time and whose requirements mandate that you keep
a history of data changes. To maintain the history of time-variant data, you must create an entity containing the
newvalue,thedateofchange,andanyothertime-relevantdata.Thisentitymaintainsa1:Mrelationshipwiththe
entity for which the history is to be maintained.
◗
A fan trap occurs when you have one entity in two 1:M relationships to other entities and there is an association
amongtheotherentitiesthatisnotexpressedinthemodel.Redundantrelationshipsoccurwhentherearemultiple
relationship paths between related entities. The main concern with redundant relationships is that they remain
consistent across the model.
K e y T e r ms
completeness constraint, 153 extended entity relationship partial completeness, 153
design trap, 162 model (EERM), 148 specialization, 154
disjoint subtype (nonoverlapping fan trap, 162 specialization hierarchy, 149
subtype), 151 generalization, 154 subtype discriminator, 151
EER diagram (EERD), 148 inheritance, 150 surrogate key, 158
entity cluster, 154 natural key (natural identifier), 156 time-variant data, 161
entity subtype, 148 overlapping subtype, 152 total completeness, 153
entity supertype, 148

## Page 196

166 CHAPTER 5
O n l i n e C o n t e n t
AnswerstoselectedReviewQuestionsandProblemsforthischapterarecontainedinthePremiumWebsitefor
thisbook.
R e v ie w Q u e st i o ns
1. What is an entity supertype, and why is it used?
2. What kinds of data would you store in an entity subtype?
3. What is a specialization hierarchy?
4. What is a subtype discriminator? Give an example of its use.
5. What is an overlapping subtype? Give an example.
6. What is the difference between partial completeness and total completeness?
For questions 7–9, refer to Figure Q5.7.
FIGURE The PRODUCT data model
Q5.7
7. List all of the attributes of a movie.
8. According to the data model, is it required that every entity instance in the PRODUCT table be associated with
an entity instance in the CD table? Why, or why not?
9. IsitpossibleforabooktoappearintheBOOKtablewithoutappearinginthePRODUCTtable?Why,orwhynot?
10. What is an entity cluster, and what advantages are derived from its use?
11. Whatprimarykeycharacteristicsareconsidereddesirable?Explainwhyeachcharacteristicisconsidereddesirable.
12. Under what circumstances are composite primary keys appropriate?
13. What is a surrogate primary key, and when would you use one?
14. Whenimplementinga1:1relationship,whereshouldyouplacetheforeignkeyifonesideismandatoryandone
side is optional? Should the foreign key be mandatory or optional?

## Page 197

ADVANCED DATA MODELING 167
15. What are time-variant data, and how would you deal with such data from a database design point of view?
16. What is the most common design trap, and how does it occur?
P r o b le m s
1. Giventhefollowingbusinessscenario,createaCrow’sFootERDusingaspecializationhierarchyifappropriate.
Two-BitDrillingCompanykeepsinformationonemployeesandtheirinsurancedependents.Eachemployeehas
anemployeenumber,name,dateofhire,andtitle.Ifanemployeeisaninspector,thenthedateofcertification
and the renewal date for that certification should also be recorded in the system. For all employees, the Social
Securitynumberanddependentnamesshouldbekept.Alldependentsmustbeassociatedwithoneandonlyone
employee. Some employees will not have dependents, while others will have many dependents.
2. Giventhefollowingbusinessscenario,createaCrow’sFootERDusingaspecializationhierarchyifappropriate.
Tiny Hospital keeps information on patients and hospital rooms. The system assigns each patient a patient ID
number. In addition, the patient’s name and date of birth are recorded. Some patients are resident patients (they
spendatleastonenightinthehospital)andothersareoutpatients(theyaretreatedandreleased).Residentpatients
areassignedtoaroom.Eachroomisidentifiedbyaroomnumber.Thesystemalsostorestheroomtype(private
orsemiprivate)androomfee.Overtime,eachroomwillhavemanypatientswhostayinit.Eachresidentpatientwill
stay in only one room.Every room must have had a patient, and every resident patient must have a room.
3. Giventhefollowingbusinessscenario,createaCrow’sFootERDusingaspecializationhierarchyifappropriate.
Granite Sales Company keeps information on employees and the departments that they work in. For each
department,thedepartmentname,internalmailboxnumber,andofficephoneextensionarekept.Adepartment
canhavemanyassignedemployees,andeachemployeeisassignedtoonlyonedepartment.Employeescanbe
salariedemployees,hourlyemployees,orcontractemployees.Allemployeesareassignedanemployeenumber.
Thisiskeptalongwiththeemployee’snameandaddress.Forhourlyemployees,hourlywageandtargetweekly
work hours are stored (e.g., the company may target 40 hours/week for some, 32 hours/week for others, and
20hours/weekforothers).Somesalariedemployeesaresalespeoplewhocanearnacommissioninadditionto
theirbasesalary.Forallsalariedemployees,theyearlysalaryamountisrecordedinthesystem.Forsalespeople,
their commission percentage on sales and commission percentage on profit are stored in the system. For
example, John is a salesperson with a base salary of $50,000 per year plus 2% commission on the sales price
for all sales he makes, plus another 5% of the profit on each of those sales. For contract employees, the
beginning date and end date of their contract are stored along with the billing rate for their hours.
4. InChapter4,yousawthecreationoftheTinyCollegedatabasedesign.Thatdesignreflectedsuchbusinessrules
as “a professor may advise many students” and “a professor may chair one department.” Modify the design
shown in Figure 4.36 to include these business rules:
(cid:2) An employee could be staff or a professor or an administrator.
(cid:2) A professor may also be an administrator.
(cid:2) Staff employees have a work level classification, such as Level I and Level II.
(cid:2) Only professors can chair a department. A department is chaired by only one professor.
(cid:2) Onlyprofessorscanserveasthedeanofacollege.Eachoftheuniversity’scollegesisservedbyonedean.
(cid:2) A professor can teach many classes.
(cid:2) Administrators have a position title.
Giventhatinformation,createthecompleteERDcontainingallprimarykeys,foreignkeys,andmainattributes.
5. TinyCollegewantstokeeptrackofthehistoryofalladministrativeappointments(dateofappointmentanddate
oftermination).(Hint:Time-variantdataareatwork.)TheTinyCollegechancellormaywanttoknowhowmany
deans worked in the College of Business between January 1, 1960, and January 1, 2010, or who the dean of
theCollegeofEducationwasin1990.Giventhatinformation,createthecompleteERDcontainingallprimary
keys, foreign keys, and main attributes.

