BEGIN TRANSACTION;
CREATE TABLE "weather" (
	`Id`	INTEGER NOT NULL,
	`city`	TEXT,
	PRIMARY KEY(Id)
);
INSERT INTO `weather` VALUES (1,NULL);
COMMIT;
