# Inova CNJ Backend - 2021

## TEAM 42 - Specification

Design of a rest api with methods that meet the demands of the challenge CNJ innovates based mainly on AI.

## DB

The data files provided by the challenge were transformed into a Postgresql relational database, as it is the most used in Brazilian courts. Data import scripts were developed in python and php. For greater performance, indexes were created based on the filters performed by the application. With the focus of the work on time analysis of movements and bottlenecks, a script was developed to prepare time data in parallel. With these adjustments, the mathematical functions for the calculations used in the application became more efficient. Finally, a database dump was generated and made available at the root of the backend project.

## Backend

Made in python, the backend uses statistical techniques and manipulation of Dataframes to generate data that will be sent to the frontend and then be viewed by the user. The code structure facilitates the addition of new methods and statistical reports, changes in the complexities of the query filters, and a simple coupling in existing data systems.
