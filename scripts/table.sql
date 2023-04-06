-- Table: public.test1

DROP TABLE IF EXISTS public.test1;

CREATE TABLE IF NOT EXISTS public."test1"
(
    id character varying COLLATE pg_catalog."default",
    "Gender" character varying COLLATE pg_catalog."default",
    "Age" character varying COLLATE pg_catalog."default",
    "Driving_License" character varying COLLATE pg_catalog."default",
    "Region_Code" character varying COLLATE pg_catalog."default",
    "Previously_Insured" character varying COLLATE pg_catalog."default",
    "Vehicle_Age" character varying COLLATE pg_catalog."default",
    "Vehicle_Damage" character varying COLLATE pg_catalog."default",
    "Annual_Premium" character varying COLLATE pg_catalog."default",
    "Policy_Sales_Channel" character varying COLLATE pg_catalog."default",
    "Vintage" character varying COLLATE pg_catalog."default"
);

TABLESPACE pg_default;

select * from public."test1";
	
COPY public.test1 FROM 'C:\Program Files\test.csv' DELIMITER ',' CSV HEADER;
