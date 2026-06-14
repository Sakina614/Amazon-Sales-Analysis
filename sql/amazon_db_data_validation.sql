
-- DATA VALIDATION 
-- Any data where order was returned but payment status not updated 
SELECT o.order_status,
       p.payment_status,
       COUNT(*)
FROM orders o
JOIN payments p
ON o.order_id = p.order_id
GROUP BY o.order_status, p.payment_status
ORDER BY o.order_status;

UPDATE payments p
SET payment_status = 'Refunded'
FROM orders o
WHERE p.order_id = o.order_id
AND o.order_status = 'Returned';

--Cancelled orders still shipped
SELECT
    o.order_id,
    o.order_status,
    s.delivery_status,
    s.shipping_date
FROM orders o
JOIN shipping s
    ON o.order_id = s.order_id
WHERE o.order_status = 'Cancelled'
  AND s.delivery_status IN ('Shipped', 'Delivered', 'In Transit');

--Inventory products missing from products table
SELECT
    i.inventory_id,
    i.product_id,
    i.stock_remaining,
    i.ware_house_id,
    i.restock_date
FROM inventory i
LEFT JOIN products p
    ON i.product_id = p.product_id
WHERE p.product_id IS NULL;

-- NO DATA DISCREPENCIES FOUND 
