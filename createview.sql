--学号,姓名,课程号,课程名,成绩,等级
CREATE VIEW Tscore AS
SELECT s1.s_id,s1.s_name,student_course.c_id,student_course.c_name,s1.s_score,s1.s_char
FROM student_course,(SELECT student_student.s_id s_id,
student_student.s_name s_name,
student_score.c_id_id c_id,
student_score.s_score s_score,
student_score.s_char s_char
FROM student_student,student_score
WHERE student_student.s_id = student_score.s_id_id) s1
WHERE s1.c_id = student_course.c_id

--学号,姓名,考试号,考试名,考试时间,考场
CREATE VIEW Texam AS
SELECT
s1.s_id s_id,
student_student.s_name s_name,
s1.e_id e_id,
s1.e_name e_name,
s1.e_time e_time,
s1.e_pos e_pos
FROM
student_student,(SELECT 
student_studentexam.s_id_id s_id,student_studentexam.e_id_id e_id,
student_exam.e_name e_name,
student_exam.e_time e_time,
student_exam.e_pos e_pos
FROM student_studentexam,student_exam
WHERE student_studentexam.e_id_id = student_exam.e_id) s1
WHERE student_student.s_id = s1.s_id
