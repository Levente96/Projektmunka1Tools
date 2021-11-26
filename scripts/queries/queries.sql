-- drága rendelés ingyenes modellekből
SELECT modell.MODELL_NAME, modell.MODELL_ID, 3d_printer.PRINTER_NAME
FROM modell
INNER JOIN shopping_cart ON (modell.MODELL_ID = shopping_cart.MODELL_ID)
INNER JOIN orders ON (orders.CART_ID = shopping_cart.CART_ID)
INNER JOIN 3d_printer ON (3d_printer.PRINTER_ID = orders.PRINTER_ID)
WHERE orders.ORDER_PRICE > (SELECT AVG(orders.ORDER_PRICE) from orders) AND modell.LICENSE_FEE = 0;

-- felügyelők alatt termelt bevétel átlagos rendelésekből
SELECT maintainer.MAINTAINER_NAME, SUM(orders.ORDER_PRICE)
FROM maintainer
INNER JOIN 3d_printer ON (3d_printer.MAINTAINER_ID = maintainer.MAINTAINER_ID)
INNER JOIN orders on (orders.PRINTER_ID = 3d_printer.PRINTER_ID)
WHERE orders.ORDER_PRIORITY = 1
GROUP BY maintainer.MAINTAINER_ID ORDER BY SUM(orders.ORDER_PRICE) DESC