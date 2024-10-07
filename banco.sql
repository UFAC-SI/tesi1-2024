BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "cliente" (
	"id"	INTEGER,
	"nome"	VARCHAR(100) NOT NULL,
	"cpf"	VARCHAR(11) NOT NULL,
	"email"	VARCHAR(60) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "banco" (
	"id"	INTEGER,
	"numero"	INTEGER NOT NULL,
	"nome"	VARCHAR(60),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "conta" (
	"id"	INTEGER,
	"cliente_fk"	INTEGER NOT NULL,
	"saldo"	REAL NOT NULL,
	"status"	INTEGER NOT NULL,
	"numero"	INTEGER NOT NULL,
	"banco_fk"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	CONSTRAINT "banco_fk" FOREIGN KEY("banco_fk") REFERENCES "banco"("id"),
	CONSTRAINT "cliente_fk" FOREIGN KEY("cliente_fk") REFERENCES "cliente"("id")
);
INSERT INTO "cliente" VALUES (1,'Manoel','99999999999','manoel@ufac.br');
INSERT INTO "cliente" VALUES (3,'Júnior','11111111111','junior@ufac.br');
INSERT INTO "cliente" VALUES (4,'Limeira','00000000000','limeira@ufac.br');
INSERT INTO "banco" VALUES (1,1,'Caixa');
INSERT INTO "conta" VALUES (1,4,100.0,1,123,1);
COMMIT;
