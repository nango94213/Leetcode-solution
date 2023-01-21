<h2><a href="https://leetcode.com/problems/compute-the-rank-as-a-percentage/">2346. Compute the Rank as a Percentage</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Students</code></p>

<pre>+---------------+------+
| Column Name   | Type |
+---------------+------+
| student_id    | int  |
| department_id | int  |
| mark          | int  |
+---------------+------+
student_id is the primary key of this table.
Each row of this table indicates a student's ID, the ID of the department in which the student enrolled, and their mark in the exam.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query that reports the rank of each student in their department as a percentage, where the rank as a percentage is computed using the following formula: <code>(student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_the_department - 1)</code>. The <code>percentage</code> should be <strong>rounded to 2 decimal places</strong>. <code>student_rank_in_the_department</code> is determined by <strong>descending</strong><b> </b><code>mark</code>, such that the student with the highest <code>mark</code> is <code>rank 1</code>. If two students get the same mark, they also get the same rank.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
Students table:
+------------+---------------+------+
| student_id | department_id | mark |
+------------+---------------+------+
| 2          | 2             | 650  |
| 8          | 2             | 650  |
| 7          | 1             | 920  |
| 1          | 1             | 610  |
| 3          | 1             | 530  |
+------------+---------------+------+
<strong>Output:</strong> 
+------------+---------------+------------+
| student_id | department_id | percentage |
+------------+---------------+------------+
| 7          | 1             | 0.0        |
| 1          | 1             | 50.0       |
| 3          | 1             | 100.0      |
| 2          | 2             | 0.0        |
| 8          | 2             | 0.0        |
+------------+---------------+------------+
<strong>Explanation:</strong> 
For Department 1:
 - Student 7: percentage = (1 - 1) * 100 / (3 - 1) = 0.0
 - Student 1: percentage = (2 - 1) * 100 / (3 - 1) = 50.0
 - Student 3: percentage = (3 - 1) * 100 / (3 - 1) = 100.0
For Department 2:
 - Student 2: percentage = (1 - 1) * 100 / (2 - 1) = 0.0
 - Student 8: percentage = (1 - 1) * 100 / (2 - 1) = 0.0
</pre>
</div>