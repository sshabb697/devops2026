-- Campus Cafe — database seed (tier 2)
-- Safe to re-run on a fresh database.

CREATE TABLE IF NOT EXISTS menu_items (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  category VARCHAR(50) NOT NULL,
  price DECIMAL(6,2) NOT NULL,
  description VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS orders (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  item_id INT UNSIGNED NOT NULL,
  student_name VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  CONSTRAINT fk_orders_item FOREIGN KEY (item_id) REFERENCES menu_items(id)
);

INSERT INTO menu_items (name, category, price, description) VALUES
  ('Filter Coffee', 'Drinks', 25.00, 'South Indian decoction with hot milk'),
  ('Masala Chai', 'Drinks', 20.00, 'Spiced tea, campus favourite'),
  ('Idli Sambar', 'Breakfast', 40.00, 'Steamed rice cakes with sambar'),
  ('Veg Sandwich', 'Snacks', 45.00, 'Grilled with mint chutney'),
  ('Samosa (2 pcs)', 'Snacks', 30.00, 'Potato filling, served hot'),
  ('Veg Fried Rice', 'Meals', 80.00, 'Wok-tossed rice with mixed veg'),
  ('Curd Rice', 'Meals', 50.00, 'Comfort food with pickle'),
  ('Gulab Jamun', 'Dessert', 35.00, 'Two pieces in sugar syrup');
