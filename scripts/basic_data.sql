-- PLASTIC
INSERT INTO `projektmunka`.`plastic` (`PLASTIC_NAME`, `MELTING_POINT`) VALUES ('PLA', '185');
INSERT INTO `projektmunka`.`plastic` (`PLASTIC_NAME`, `MELTING_POINT`) VALUES ('ABS', '210');
INSERT INTO `projektmunka`.`plastic` (`PLASTIC_NAME`, `MELTING_POINT`) VALUES ('PETG', '205');

-- Manufacturer
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('1', 'Prusa', '8');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('2', 'Prusa', '9');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('3', 'Prusa', '8.6');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('1', 'Sunlu', '5.9');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('3', 'Sunlu', '7.2');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('1', 'Gemibird', '7');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('2', 'Gemibird', '8.3');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('3', 'Gemibird', '9.1');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('1', 'Filamentum', '11.4');
INSERT INTO `projektmunka`.`manufacturer` (`PLASTIC_TYPE`, `MANUFACTURER_NAME`, `PRICE_PER_G`) VALUES ('2', 'Filamentum', '13.7');

-- Stock
INSERT INTO `projektmunka`.`stock` (`PLASTIC_TYPE`, `MANUFACTURER`, `STOCK_IN_G`) VALUES ('1', '4', '5000');
INSERT INTO `projektmunka`.`stock` (`PLASTIC_TYPE`, `MANUFACTURER`, `STOCK_IN_G`) VALUES ('2', '7', '2000');
INSERT INTO `projektmunka`.`stock` (`PLASTIC_TYPE`, `MANUFACTURER`, `STOCK_IN_G`) VALUES ('3', '3', '1500');

-- Maintainers
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Ralph Serrano', '150000','0');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Mohammed Cain', '148000','29500');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Jade Spencer', '162000','0');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Javon Riggs', '152000','12900');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Isabella Mcknight','147500', '0');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Rene Byrd','149800', '0');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Larry Hart','147050', '16600');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Nasir Manning','151000', '0');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Brylee Cantrell', '156000', '0');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Jayda Fernandez', '151500', '0');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Makaila Wolf', '149000', '0');
INSERT INTO `projektmunka`.`maintainer` (`MAINTAINER_NAME`, `SALARY`, `EXPENSES`) VALUES ('Dixie Schneider', '139500', '0');