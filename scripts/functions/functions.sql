DELIMITER $
DROP FUNCTION IF EXISTS OrderPrice$

DELIMITER $
CREATE PROCEDURE OrderPrice(
	IN OrderId INT
)
BEGIN
	DECLARE weight_sum INT;
    DECLARE cart_id INT;
    DECLARE plastic_type INT;
    DECLARE order_prio INT;
    DECLARE licenses INT;
    DECLARE plastic_price INT DEFAULT 1;

    -- get cart_id
    SELECT orders.CART_ID INTO cart_id FROM orders WHERE orders.ORDER_ID = OrderId;
    -- get order_priority
    SELECT orders.ORDER_PRIORITY INTO order_prio FROM orders WHERE orders.ORDER_ID = OrderId;
    
    -- get how much plastic is needed
	SELECT SUM(modell.PLASTIC_REQUIRED*shopping_cart.QUANTITY)
    INTO weight_sum
    FROM modell
    INNER JOIN shopping_cart ON (modell.MODELL_ID = shopping_cart.MODELL_ID)
    WHERE shopping_cart.CART_ID = cart_id;

    -- get license fees
    SELECT SUM(modell.LICENSE_FEE*shopping_cart.QUANTITY)
    INTO licenses
    FROM modell
    INNER JOIN shopping_cart ON (modell.MODELL_ID = shopping_cart.MODELL_ID)
    WHERE shopping_cart.CART_ID = cart_id;

    -- select plastic price
    IF plastic_type = 1 THEN 
        SET plastic_price = 9;
    END IF;
    IF plastic_type = 2 THEN 
        SET plastic_price = 11;
    END IF;
    IF plastic_type = 3 THEN 
        SET plastic_price = 12;
    END IF;
    
    UPDATE orders 
	SET orders.ORDER_PRICE = licenses + (order_prio*300) + (weight_sum * plastic_price);
	WHERE orders.ORDER_ID = OrderId;
END$

DELIMITER ;
CALL OrderPrice(1);