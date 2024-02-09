**BAGIT Catalog Digitization**
A catalogue is the best option if we want a thorough explanation of our company's goods and services. It is a very helpful advertising tool that has a lot of potential to encourage our clients to buy products or hire services.Still, some businesses use hardcopy catalogues as part of their strategy, and they continue to yield positive outcomes. However, the scope of this kind of publication will constantly be expanded by developing a digital catalogue.

**Scope** :- The scope of this project is to digitize catalogs using text,image and audio interfaces , while also accomplishing the mechanism for measuring the throughput of digitization.
Functionalities :- The project is divided into eight different core functionalities each of which is a potential module. 

**Module 1**

**Text**

- Catalog digitisation in the form of text is achieved in this module . It receives the input from the user in text from and saves them in the database and digitizes the catalog with the use of parameters like SKU id,product name,brand,colour ,price,etc.,

**Module 2**

**Text Indic**
- Catalog digitization in the form of indic languages text is achieved in this module . It receives the input from the user in their respective indic languaes as text from and saves them in the database and digitizes the catalog with the use of parameters like SKU id,product name,brand,colour ,price,etc., 

**Module 3**

**Voice**
- Catalog digitization in the form of voice(audio) is achieved in this module . It receives the input from the user in the audio format and converts it as text from suing Speech-To-Text and saves them in the database and digitizes the catalog with the use of parameters like SKU id,product name,brand,colour ,price,etc., 

**Module 4**

**Voice Indic**
- Catalog digitization in the form of indic languages of voice(audio) is achieved in this module . It receives the input from the user in their respective indic languaes as audio(voice) from & converts it to text suing Speech-To-Text and saves them in the database and digitizes the catalog with the use of parameters like SKU id,product name,brand,colour ,price,etc., 

**Module 5**

**Image**
- Catalog digitization in the form of images is achieved in this module . It receives the input from the user in the image format and converts it to text form using Optical Character Recognition(OCR) saves them in the database and digitizes the catalog with the use of parameters like SKU id,product name,brand,colour ,price,etc., 

**Module 6**

**Combination of all 3**
- Catalog digitization in the form of combination of all three (image , voice and text) is achieved in this module . For example ,It receives the input from the user  for product image & anme in image format , description in voice format and price in text fromat and saves them in the database and digitizes the catalog with the use of parameters like SKU id,product name,brand,colour ,price,etc., 

**Module 7** –Here we can view the catalog from a lis of previously created files & see the results of digitilization of our catalog.

**Module 8** – The mechanism of throughput digitization can be done by finding out the active users %. Active usrs are the people who visit the website and digitize the catalog . While total users are the toal no of people who have visited the project . (Active users/total users)*100 will give you the active users%

**Dependencies** :- the 7th and 8th module are interdependent on the first 6 modules . While the first 6 modules are interdependent on each other

**Feasibilty** :- while the first 6 modules are independent of each other , the 7th and 8th module depnds on the first 6 modules. 

**Prioritize** :- we should priortize in making the fisrt 6 modules in the order of 1-3-5-2-4-6 . Because first we should accompish main interfaces then we can make them into inidc and combination of all three
Inputs & Outputs :- While the Module 1&2 gets the input in text format , module 3 &4 freceives it in audio format(mp3/4) , module 5 take it up in image format(jpeg/png) , module 6 takes it up in combination of all 3 (image , audio and text) , but the output of all the three turns out to be in text format

**Tech evaluation**:-
Each module’s behavior is unique as it receives request from user it accepst the request and implements the module behavior withotu any error. The modules are error free dut to consistent naming conventions and documented interfaces which provides clear understanding of how each modules work  

**Reusability** – All Modules are independently deployable units for algorithms it can be reused without the worry of identifying which additional modules might be necessary.

**Extensibility**:- the project has a built in ability which enables it to add differentiating feature and extend it modular fashion

**Scalability** – You can type in the values in the respective fields of each module and the moudlar system allows you to effectivley implement and adapt tot eh changing needs of each individualproducts for selling

**Security** – The retail data are encrypted with aes 256 standard encryption algorithm which encrypts your datas with a key.the key is md5 hashed(since key input size is 128 bits ) . So the odules deliver transactional guarantee s for the retail sellers who are digitizing their catalog of products in retail industry

Customization deployment for the proposed solution of catalogue digitization is done using a 
Live Web App

Programming Language – **Python 2.7.18**

Database – **Google Firebase 10.7.1**

**The eight test cases** required for the catalog digitisation are as follows : 

Text digitization
Text indic digitization
Voice digitization
Voice indic mode digitization
Image mode digitization
Combination of all three(Image,text & voice) mode digitisation
View digitised catalogs
Mechanism to measure throughput of digitisation 

The first 6 test cases can be evaluated by the Program gathering data from user and saving it
successfully in the database. Test case no.7 is assessed using hoow it can retrieve data from
Database and show it to the user . 
Test case no.8 is evaluated using how it can measure the
**throughput of digitization by figuring out the total time taken for digitizing the total number of products.**   

![Screenshot] cat-digi-modular-arch.png

![Screenshot] cd_logo.png


