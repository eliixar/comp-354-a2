
INSERT INTO restaurants (name, description) VALUES
('Dominos', 'Fresh pizza'),
('Good Burger', 'Burgers, fries and shakes'),
('Yum Sushi', 'Rolls and Japanese favourites');

INSERT INTO menu_items (restaurant_id, name, description, price, category) VALUES
(1, 'Cheese Pizza', 'Mozzarella and tomato sauce, per slice', 5.50, 'Pizza'),
(1, 'Pepperoni Pizza', 'Mozzarella and pepperoni, per slice', 6.00, 'Pizza'),
(1, 'Garlic Bread', 'Toasted with garlic butter', 4.50, 'Sides'),
(1, 'House Salad', 'Mixed greens and vegetables', 6.50, 'Sides'),
(1, 'Soft Drink', '355 ml can', 2.00, 'Drinks');

INSERT INTO menu_items (restaurant_id, name, description, price, category) VALUES
(2, 'Cheeseburger', 'Beef patty with cheese', 10.00, 'Burgers'),
(2, 'Veggie Burger', 'Plant-based patty', 8.00, 'Burgers'),
(2, 'Fries', 'Crispy and salted', 4.00, 'Sides'),
(2, 'Onion Rings', 'Golden fried rings', 6.00, 'Sides'),
(2, 'Milkshake', 'Chocolate or vanilla', 5.00, 'Drinks');

INSERT INTO menu_items (restaurant_id, name, description, price, category) VALUES
(3, 'Salmon Roll', '8 pieces', 9.00, 'Rolls'),
(3, 'Cucumber Roll', '8 pieces', 6.00, 'Rolls'),
(3, 'Veggie Roll', '8 pieces', 7.00, 'Rolls'),
(3, 'Miso Soup', 'Tofu and seaweed', 3.00, 'Sides'),
(3, 'Green Tea', 'Hot or iced', 2.00, 'Drinks');
