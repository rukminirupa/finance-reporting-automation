INSERT INTO transactions (account_id, transaction_date, debit, credit, balance)
VALUES
(101, '2024-01-01', 500.00, 0.00, 1500.00),
(101, '2024-01-05', 0.00, 200.00, 1700.00),
(102, '2024-01-03', 1000.00, 0.00, 3000.00),
(102, '2024-01-07', 0.00, 500.00, 3500.00),
(103, '2024-01-04', 0.00, 0.00, 2500.00),     -- invalid: both debit & credit zero
(104, '2024-01-06', 700.00, 300.00, 2000.00), -- invalid: both debit & credit non-zero
(105, '2024-01-08', 0.00, 400.00, -100.00);   -- invalid: negative balance