CREATE DATABASE master_pol;
use master_pol;

CREATE TABLE `partners` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`partner_type_id` INTEGER NOT NULL,
	`partner_name` VARCHAR(255) NOT NULL,
	`first_name_director` VARCHAR(50) NOT NULL,
	`last_name_director` VARCHAR(50) NOT NULL,
	`middle_name_director` VARCHAR(255),
	`email_partner` VARCHAR(100) NOT NULL,
	`phone_partner` VARCHAR(15) NOT NULL,
	`address` VARCHAR(255) NOT NULL,
	`INN` VARCHAR(10) NOT NULL,
	`rating` INTEGER NOT NULL,
	`logo` LONGBLOB,
	PRIMARY KEY(`id`)
);


CREATE TABLE `partners_type` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(255),
	PRIMARY KEY(`id`)
);


CREATE TABLE `products` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`article` VARCHAR(10) NOT NULL,
	`name` VARCHAR(100) NOT NULL,
	`product_type_id` INTEGER NOT NULL,
	`description` VARCHAR(255),
	`picture` LONGBLOB,
	`min_price_partners` DECIMAL(10,2) NOT NULL,
	`cert_quality` LONGBLOB,
	`standard_number` VARCHAR(255),
	`selfcost` DECIMAL(10,2),
	`length` DECIMAL(10,2),
	`width` DECIMAL(10,2),
	`height` DECIMAL(10,2),
	`weight_no_package` DECIMAL(10,2),
	`weight_with_package` DECIMAL(10,2),
	`time_to_create_min` INTEGER,
	`workshop_number` INTEGER,
	`people_count_production` INTEGER,
	`product_current_stock` INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY(`id`)
);


CREATE TABLE `products_types` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(70) NOT NULL,
	`coefficent` DECIMAL(3,2) NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `product_partners` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`product_id` INTEGER NOT NULL,
	`partner_id` INTEGER NOT NULL,
	`amount` INTEGER NOT NULL,
	`sale_date` DATE NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `employees` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`employee_type_id` INTEGER NOT NULL,
	`first_name` VARCHAR(50) NOT NULL,
	`last_name` VARCHAR(50) NOT NULL,
	`middle_name` VARCHAR(60) NULL,
	`birth_date` DATE NOT NULL,
	`passport_data` VARCHAR(11) NOT NULL,
	`bank_details` VARCHAR(100) NOT NULL,
	`has_family` BOOLEAN,
	`health_status` VARCHAR(25),
	PRIMARY KEY(`id`)
);


CREATE TABLE `employees_types` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(50) NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `users` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`username` VARCHAR(30) NOT NULL,
	`password` VARCHAR(80) NOT NULL,
	`employee_id` INTEGER NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `materials` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`material_type_id` INTEGER NOT NULL,
	`supplier_id` INTEGER NOT NULL,
	`name` VARCHAR(60) NOT NULL,
	`package_quantity` INTEGER NOT NULL,
	`unit` VARCHAR(20) NOT NULL,
	`cost` DECIMAL(8,2) NOT NULL,
	`image` LONGBLOB,
	`min_stock` INTEGER,
	`material_current_stock` INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY(`id`)
);


CREATE TABLE `materials_type` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(50) NOT NULL,
	`defect_percent` DECIMAL(10,2) NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `products_recipes` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`product_id` INTEGER NOT NULL,
	`material_id` INTEGER NOT NULL,
	`material_count` INTEGER NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `partners_rating_history` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`partner_id` INTEGER NOT NULL,
	`new_rating` INTEGER NOT NULL,
	`changed` DATETIME NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `orders` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`partner_id` INTEGER NOT NULL,
	`manager_id` INTEGER NOT NULL,
	`total_price` DECIMAL(10,2) NOT NULL,
	`order_payment` DECIMAL(10,2) NOT NULL DEFAULT 0,
	`created` DATETIME NOT NULL,
	`status` ENUM('created', 'waiting prepayment', 'prepayment received', 'completed', 'canceled', 'ready for shipment', 'pending', 'in production') NOT NULL,
	`prepayment_date` DATETIME,
	`payment_date` DATETIME,
	PRIMARY KEY(`id`)
);


CREATE TABLE `products_orders` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`order_id` INTEGER NOT NULL,
	`product_id` INTEGER NOT NULL,
	`quantity` INTEGER NOT NULL,
	`agreed_price_per` DECIMAL(8,2),
	`production_date` DATE,
	PRIMARY KEY(`id`)
);


CREATE TABLE `suppliers` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(50) NOT NULL,
	`INN` VARCHAR(10) NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `materials_supply_history` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`material_id` INTEGER NOT NULL,
	`supplier_id` INTEGER NOT NULL,
	`quantity` INTEGER NOT NULL,
	`delivery_date` DATE NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `materials_movement` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`material_id` INTEGER NOT NULL,
	`amount` INTEGER NOT NULL,
	`movement_type` ENUM('incoming', 'reserve', 'write off') NOT NULL DEFAULT 'incoming',
	`movement_date` DATETIME NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `employees_access` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`employee_id` INTEGER NOT NULL,
	`door_id` INTEGER NOT NULL,
	`access_date` DATETIME NOT NULL,
	PRIMARY KEY(`id`)
);


ALTER TABLE `partners`
ADD FOREIGN KEY(`partner_type_id`) REFERENCES `partners_type`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `products`
ADD FOREIGN KEY(`product_type_id`) REFERENCES `products_types`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `product_partners`
ADD FOREIGN KEY(`product_id`) REFERENCES `products`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `product_partners`
ADD FOREIGN KEY(`partner_id`) REFERENCES `partners`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `employees`
ADD FOREIGN KEY(`employee_type_id`) REFERENCES `employees_types`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `users`
ADD FOREIGN KEY(`employee_id`) REFERENCES `employees`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `materials`
ADD FOREIGN KEY(`material_type_id`) REFERENCES `materials_type`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `products_recipes`
ADD FOREIGN KEY(`product_id`) REFERENCES `products`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `products_recipes`
ADD FOREIGN KEY(`material_id`) REFERENCES `materials`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `partners_rating_history`
ADD FOREIGN KEY(`partner_id`) REFERENCES `partners`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `orders`
ADD FOREIGN KEY(`partner_id`) REFERENCES `partners`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `orders`
ADD FOREIGN KEY(`manager_id`) REFERENCES `employees`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `products_orders`
ADD FOREIGN KEY(`order_id`) REFERENCES `orders`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `products_orders`
ADD FOREIGN KEY(`product_id`) REFERENCES `products`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `materials`
ADD FOREIGN KEY(`supplier_id`) REFERENCES `suppliers`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `materials_supply_history`
ADD FOREIGN KEY(`material_id`) REFERENCES `materials`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `materials_supply_history`
ADD FOREIGN KEY(`supplier_id`) REFERENCES `suppliers`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `materials_movement`
ADD FOREIGN KEY(`material_id`) REFERENCES `materials`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;
ALTER TABLE `employees_access`
ADD FOREIGN KEY(`employee_id`) REFERENCES `employees`(`id`)
ON UPDATE NO ACTION ON DELETE CASCADE;

INSERT INTO materials_type (name, defect_percent) VALUES
('Тип материала 1', 0.001),
('Тип материала 2', 0.0095),
('Тип материала 3', 0.0028),
('Тип материала 4', 0.0055),
('Тип материала 5', 0.0034);

INSERT INTO products_types (name, coefficent) VALUES
('Ламинат', 2.35),
('Массивная доска', 5.15),
('Паркетная доска', 4.34),
('Пробковое покрытие', 1.5);

INSERT INTO partners_type (name) VALUES
('ЗАО'),
('ООО'),
('ПАО'),
('ОАО');


INSERT INTO partners (partner_type_id, partner_name, first_name_director, last_name_director, middle_name_director, email_partner, phone_partner, address, INN, rating) VALUES
(1, 'База Строитель', 'Александра', 'Иванова', 'Ивановна', 'aleksandraivanova@ml.ru', '4931234567', '652050, Кемеровская область, город Юрга, ул. Лесная, 15', '2222455179', 7),
(2, 'Паркет 29', 'Василий', 'Петров', 'Петрович', 'vppetrov@vl.ru', '9871235678', '164500, Архангельская область, город Северодвинск, ул. Строителей, 18', '3333888520', 7),
(3, 'Стройсервис', 'Андрей', 'Соловьев', 'Николаевич', 'ansolovev@st.ru', '8122233200', '188910, Ленинградская область, город Приморск, ул. Парковая, 21', '4440391035', 7),
(4, 'Ремонт и отделка', 'Екатерина', 'Воробьева', 'Валерьевна', 'ekaterina.vorobeva@ml.ru', '4442223311', '143960, Московская область, город Реутов, ул. Свободы, 51', '1111520857', 5),
(1, 'МонтажПро', 'Степан', 'Степанов', 'Сергеевич', 'stepanov@stepan.ru', '9128883333', '309500, Белгородская область, город Старый Оскол, ул. Рабочая, 122', '5552431140', 10);

INSERT INTO products (article, name, product_type_id, min_price_partners) VALUES
('8758385', 'Паркетная доска Ясень темный однополосная 14 мм', 3, 4456.90),
('8858958', 'Инженерная доска Дуб Французская елка однополосная 12 мм', 3, 7330.99),
('7750282', 'Ламинат Дуб дымчато-белый 33 класс 12 мм', 1, 1799.33),
('7028748', 'Ламинат Дуб серый 32 класс 8 мм с фаской', 1, 3890.41),
('5012543', 'Пробковое напольное клеевое покрытие 32 класс 4 мм', 4, 5450.59);

INSERT INTO product_partners (product_id, partner_id, amount, sale_date) VALUES
(1, 1, 15500, '2023-03-23'),
(3, 1, 12350, '2023-12-18'),
(4, 1, 37400, '2024-06-07'),
(2, 2, 35000, '2022-12-02'),
(5, 2, 1250, '2023-05-17'),
(3, 2, 1000, '2024-06-07'),
(1, 2, 7550, '2024-07-01'),
(1, 3, 7250, '2023-01-22'),
(2, 3, 2500, '2024-07-05'),
(4, 4, 59050, '2023-03-20'),
(3, 4, 37200, '2024-03-12'),
(5, 4, 4500, '2024-05-14'),
(3, 5, 50000, '2023-09-19'),
(4, 5, 670000, '2023-11-10'),
(1, 5, 35000, '2024-04-15'),
(2, 5, 25000, '2024-06-12');

-- === 1. Типы сотрудников ===
INSERT INTO employees_types (name)
VALUES 
('Менеджер'),
('Бухгалтер'),
('Программист'),
('Охранник'),
('Уборщик');

-- === 2. Сотрудники ===
INSERT INTO employees (
    employee_type_id, first_name, last_name, middle_name, birth_date,
    passport_data, bank_details, has_family, health_status
)
VALUES
-- Менеджеры
(1, 'Иван', 'Петров', 'Сергеевич', '1988-03-15', '40051234567', '123456789', TRUE, 'Хорошее'),
(1, 'Мария', 'Сидорова', 'Игоревна', '1990-11-02', '40057891234', '987654321', FALSE, 'Отличное'),

-- Программист
(3, 'Андрей', 'Кузнецов', 'Алексеевич', '1995-07-21', '40101234567', '111122223333', TRUE, 'Хорошее'),

-- Бухгалтер
(2, 'Елена', 'Морозова', 'Павловна', '1982-05-08', '40104561234', '444455556666', TRUE, 'Удовлетворительное'),

-- Охранник
(4, 'Сергей', 'Волков', 'Владимирович', '1979-09-10', '40205678901', '555566667777', FALSE, 'Хорошее'),

-- Уборщик
(5, 'Наталья', 'Орлова', 'Геннадьевна', '1975-12-25', '40307891234', '888899990000', TRUE, 'Хорошее');

-- === 3. Пользователи ===
-- Пользователи, связанные с менеджерами
INSERT INTO users (username, password, employee_id)
VALUES
('ivan', 'test', 1),
('manager_maria', 'hashed_password_456', 2);


CREATE VIEW show_partners
AS
SELECT p.id, pt.name AS type_name, p.partner_name, p.first_name_director, p.last_name_director, p.middle_name_director, p.phone_partner, p.rating
FROM partners p JOIN partners_type pt
ON
p.partner_type_id = pt.id;


DELIMITER //
CREATE PROCEDURE add_parther (IN p_partner_type_id INT, IN p_partner_name VARCHAR(255),
IN p_first_name_director VARCHAR(50), IN p_last_name_director VARCHAR(50), IN p_middle_name_director VARCHAR(255),
IN p_email_partner VARCHAR(100), IN p_phone_partner VARCHAR(15), IN p_address VARCHAR(255), IN p_INN VARCHAR(10), IN p_rating INT)

BEGIN
    INSERT INTO partners (
        partner_type_id,
        partner_name,
        first_name_director,
        last_name_director,
        middle_name_director,
        email_partner,
        phone_partner,
        address,
        INN,
        rating
    ) VALUES (
        p_partner_type_id,
        p_partner_name,
        p_first_name_director,
        p_last_name_director,
        p_middle_name_director,
        p_email_partner,
        p_phone_partner,
        p_address,
        p_INN,
        p_rating
    );
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE upd_partner (IN p_partner_type_id INT, IN p_id INT, IN p_partner_name VARCHAR(255),
IN p_first_name_director VARCHAR(50), IN p_last_name_director VARCHAR(50), IN p_middle_name_director VARCHAR(255),
IN p_email_partner VARCHAR(100), IN p_phone_partner VARCHAR(15), IN p_address VARCHAR(255), IN p_INN VARCHAR(10), IN p_rating INT)

BEGIN
    UPDATE partners
    SET
        partner_type_id = p_partner_type_id,
        partner_name = p_partner_name,
        first_name_director = p_first_name_director,
        last_name_director = p_last_name_director,
        middle_name_director = p_middle_name_director,
        email_partner = p_email_partner,
        phone_partner = p_phone_partner,
        address = p_address,
        INN = p_INN,
        rating = p_rating
    WHERE id = p_id;

END //

DELIMITER ;


DELIMITER //

CREATE FUNCTION get_disc(partner_id INT)
RETURNS INT
BEGIN

    DECLARE total_amount INT;

    SELECT SUM(amount) INTO total_amount
    FROM product_partners
    WHERE partner_id = partner_id;

    IF total_amount >= 300000 THEN RETURN 15;
    ELSEIF total_amount >= 50000 THEN RETURN 10;
    ELSEIF total_amount >= 10000 THEN RETURN 5;
    ELSE RETURN 0;
    END IF;

END //

DELIMITER ;



DELIMITER //

CREATE PROCEDURE partner_history(IN p_partner_id INT)
BEGIN
    SELECT
        pr.name AS product_name,
        pp.amount AS quantity,
        pp.sale_date AS sale_date
    FROM product_partners pp JOIN products pr
    ON
    pp.product_id = pr.id
    WHERE pp.partner_id = p_partner_id
    ORDER BY pp.sale_date DESC;
END//

DELIMITER ;
