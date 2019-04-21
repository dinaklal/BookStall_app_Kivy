-- Exported from QuickDBD: https://www.quickdatatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE `user` (
    `userid` int  NOT NULL ,
    `user` string  NOT NULL ,
    `password` string  NOT NULL ,
    `access` int  NOT NULL ,
    PRIMARY KEY (
        `userid`
    )
);

CREATE TABLE `items` (
    `itemid` int  NOT NULL ,
    `item` string  NOT NULL ,
    `description` string  NOT NULL ,
    `categoryid` int  NOT NULL ,
    `gstClass_id` int  NOT NULL ,
    `addedby` int  NOT NULL ,
    `price` float  NOT NULL ,
    `quantity` int  NOT NULL ,
    PRIMARY KEY (
        `itemid`
    )
);

CREATE TABLE `gst` (
    `gstclass_id` int  NOT NULL ,
    `gstclass` string  NOT NULL ,
    `CGST` float  NOT NULL ,
    `SGST` float  NOT NULL ,
    `datetimeupdated` datetime  NOT NULL ,
    PRIMARY KEY (
        `gstclass_id`
    )
);

CREATE TABLE `sales` (
    `saleid` int  NOT NULL ,
    `itemid` int  NOT NULL ,
    `item` string  NOT NULL ,
    `billid` int  NOT NULL ,
    `when` datetime  NOT NULL ,
    `comments` string  NOT NULL ,
    `userid` int  NOT NULL ,
    `quantity` int  NOT NULL ,
    PRIMARY KEY (
        `saleid`
    )
);

CREATE TABLE `bill` (
    `billid` int  NOT NULL ,
    `name` string  NOT NULL ,
    `place` string  NOT NULL ,
    `phone` string  NOT NULL ,
    `total` float  NOT NULL ,
    `CGST_tot` float  NOT NULL ,
    `SGST_totfloat` float  NOT NULL ,
    PRIMARY KEY (
        `billid`
    )
);

CREATE TABLE `category` (
    `categoryid` int  NOT NULL ,
    `category` string  NOT NULL ,
    PRIMARY KEY (
        `categoryid`
    )
);

ALTER TABLE `user` ADD CONSTRAINT `fk_user_userid` FOREIGN KEY(`userid`)
REFERENCES `items` (`addedby`);

ALTER TABLE `items` ADD CONSTRAINT `fk_items_categoryid` FOREIGN KEY(`categoryid`)
REFERENCES `category` (`categoryid`);

ALTER TABLE `items` ADD CONSTRAINT `fk_items_gstClass_id` FOREIGN KEY(`gstClass_id`)
REFERENCES `gst` (`gstclass_id`);

ALTER TABLE `sales` ADD CONSTRAINT `fk_sales_itemid` FOREIGN KEY(`itemid`)
REFERENCES `items` (`itemid`);

ALTER TABLE `bill` ADD CONSTRAINT `fk_bill_billid` FOREIGN KEY(`billid`)
REFERENCES `sales` (`billid`);

CREATE INDEX `idx_user_user`
ON `user` (`user`);

