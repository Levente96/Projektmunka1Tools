DELIMITER $
DROP FUNCTION IF EXISTS OrderPrice$

DELIMITER $
CREATE PROCEDURE OrderPrice(
	IN OrderId INT
)
BEGIN
	DECLARE result INT;
    DECLARE cart_id INT;
    
    SELECT orders.CART_ID INTO cart_id FROM orders WHERE orders.ORDER_ID = OrderId;
    
	SELECT SUM(modell.MODELL_PRICE*shopping_cart.QUANTITY)
    INTO result
    FROM modell
    INNER JOIN shopping_cart ON (modell.MODELL_ID = shopping_cart.MODELL_ID)
    WHERE shopping_cart.CART_ID = cart_id;
    
    UPDATE orders 
	SET orders.ORDER_PRICE = result
	WHERE orders.ORDER_ID = OrderId;
END$

DELIMITER ;
CALL OrderPrice(1);