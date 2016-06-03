INSERT INTO departments
VALUES
	(1, "Algebra"),
	(2, "Computer Informatics"),
	(3, "Geometry"),
	(4, "Mathematical Analysis"),
	(5, "Numerical Methods and Algorithms"),
	(6, "Probability, Operations Research and Statistics");
	
INSERT INTO subjects 
VALUES (1, "Lineal Algebra", 1),
		(2, "Algebra2", 1),
		(3, "Introduction of Programming", 2),
		(4, "Object-oriented Programming", 2),
		(5, "Data Structures", 2),
		(6, "Analitic Geometry", 3),
		(7, "Descriptive Geometry", 3),
		(8, "Differential and Integral Calculus 1", 4),
		(9, "Differential and Integral Calculus 2", 4),
		(10, "Numerical Methods", 5),
		(11, "Algorithms", 5),
		(12, "Statistics", 6),
		(13, "Operations search", 6);

INSERT INTO students 
VALUES 
		(1, "Ivan", 1, "redovno"),
		(2, "Gosho", 1, "zadochno"),
		(3, "Anton", 2, "redovno"),
		(4, "Maria", 2, "zadochno"),
		(5, "Ivo", 2, "redovno");

INSERT INTO grade_subj
VALUES
		(1, 1, 4),
		(1, 2, 4),
		(1, 3, 5),
		(1, 4, 5),
		(2, 1, 4),
		(2, 2, 3),
		(2, 3, 6),
		(2, 4, 5),
		(3, 1, 4),
		(3, 2, NULL),
		(3, 3, 4);
		
INSERT INTO Specialties
	VALUES
	(1, "Мathematics",4),
	(2, "Applied Mathematics ",4),
	(3, "Mathematics and Informatics",4),
	(4, "Informatics",4),
	(5, "Computer Science",4),
	(6, "Software Engineering",4),
	(7, "Information System",4),
	(8, "Statistics",4);
	
INSERT INTO subj_prof
	VALUES
	(1,1),
	(2,1),
	(2,2),
	(3,4),
	(4,6),
	(3,3);

INSERT INTO subj_specialty 
VALUES 
		(1, 5),
		(1, 6),
		(2, 1),
		(3, 5),
		(3, 6),
		(4, 6),
		(4, 5);

INSERT INTO professors
VALUES
		(1, "Ivanov", "iv@abv.bg", 1),
		(2, "Dimitrov", "dimitrov@abv.bg", 1),
		(3, "Danchev", "dan@abv.bg", 2),
		(4, "Petkov", "petkov@abv.bg", 2),
		(5, "Gochev", "gocharche@hriska.com", 2);