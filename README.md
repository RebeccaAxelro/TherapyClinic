- Normal form: My tables are 4th normal form, since:
  1) In first normal form:
     a) each cell in singled valued
     b) entries in a column are same type
     c) rows uniquely identified - each table has a unique ID
  2) In second normal form:
     a) all attributes dependent on the key - they're seperated out, so all attributes in the table depend on that ID in the table.
  3) In third normal form:
     a) all fields can be determined only by the key in the table and no other column
  4) In forth normal form:
     a) no multi-valued dependencies
     	--  For a single value A , there are not mulitple values of B
	    ex: Every table, is unique in their value becuase there are table to split them up. You will only see a unique client in client table,
	    a unique treamtment in treatment table, etc.
	-- But this may not be true for the appointment table since there could be many appointmentIDs with the same clientID, therapistID, etc.
	   But I decided to keep it this way becuase when updating appointment, your not changing the therapist or client.
	   You would just be updating the time or duration, etc. So I didnt see a point in splitting it up.

- See updated ER diagram: https://docs.google.com/document/d/10MBc59WyDk7OWTJHBzHqpW8b4fbZrbyAl4wETjOfj3E/edit?usp=sharing