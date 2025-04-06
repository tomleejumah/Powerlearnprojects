SELECT * FROM expenses
WHERE description LIKE '%food%'
  AND amount > 50
  AND (category = 'Food' OR category = 'Travel')
ORDER BY amount DESC;
