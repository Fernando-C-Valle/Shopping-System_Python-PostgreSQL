
CREATE DATABASE yourdatabase;

CREATE TABLE clients(
	client_id BIGSERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	user_name VARCHAR(255) NOT NULL,
	age INT NOT NULL ,
	registered TIMESTAMP DEFAULT NOW()
);

CREATE TABLE items(
	item_id BIGSERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	price DECIMAL(7,2) NOT NULL,
	quantity INTEGER NOT NULL
);

CREATE TABLE orders(
	order_id BIGSERIAL NOT NULL PRIMARY KEY,
	clientID INTEGER,
	FOREIGN KEY(clientID)
		REFERENCES clients(client_id)
		ON DELETE CASCADE,
	itemID INTEGER,	
	FOREIGN KEY(itemID)
		REFERENCES items(item_id)
		ON DELETE CASCADE,
	quantity INTEGER NOT NULL,
	ordered_at TIMESTAMP DEFAULT NOW()
);


SELECT clients.name AS Client, client_id, items.name As Product, items.price AS Price, items.item_id, ordered_at
FROM items
INNER JOIN orders
	ON items.item_id = orders.itemID
INNER JOIN clients
 	ON clients.client_id = orders.clientID;


CREATE TABLE fulfilled_orders(
	fulfilled_order_id BIGSERIAL NOT NULL PRIMARY KEY,
	clientID INTEGER,
	FOREIGN KEY(clientID)
		REFERENCES clients(client_id)
		ON DELETE CASCADE,
	itemID INTEGER,	
	FOREIGN KEY(itemID)
		REFERENCES items(item_id)
		ON DELETE CASCADE,
	quantity INTEGER NOT NULL,
	fulfilled_at TIMESTAMP DEFAULT NOW()
);


SELECT clients.client_id, clients.name, items.item_id, items.name, fulfilled_at
FROM clients
INNER JOIN fulfilled_orders
	ON clients.client_id = fulfilled_orders.clientID
INNER JOIN items
	ON items.item_id = fulfilled_orders.itemID;

